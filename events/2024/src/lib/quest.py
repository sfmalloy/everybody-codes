import inspect
import os

from dataclasses import dataclass
from functools import wraps
from io import TextIOWrapper
from pathlib import Path
from timeit import default_timer as timer
from typing import Callable, Any

from lib.api import download


ParserFn = Callable[[TextIOWrapper], Any] | Callable[[TextIOWrapper, int], Any]


@dataclass
class Result:
    answer: Any = None
    parse_time: float = None
    solve_time: float = None


class QuestContainer:
    _solvers: dict[tuple[int, int], Callable]
    _parsers: dict[int, ParserFn]

    def __init__(self):
        self._solvers = {}
        self._parsers = {}

    def solver(self, *, quest: int, part: int):
        def decorator(fn: Callable):
            @wraps(fn)
            def solver_wrapper(args: tuple[Any, ...]):
                return self.__time_fn(fn, args)

            self._solvers[(quest, part)] = solver_wrapper

        return decorator

    def parser(self, *, quest: int):
        def decorator(fn: ParserFn):
            @wraps(fn)
            def parser_wrapper(part: int, filename: str | None = None):
                input_path = self.__validate_input_path(quest, part, filename)

                with open(input_path) as file:
                    if len(inspect.signature(fn).parameters) == 2:
                        return fn(file, part)
                    return fn(file)

            self._parsers[quest] = parser_wrapper

        return decorator

    def run(self, quest: int, part: int, filename: str | None = None) -> Result:
        parser = self._parsers.get(quest, None)
        if parser:
            ipt, parse_time = self.__time_fn(parser, (part, filename))
        else:
            ipt, parse_time = self.__time_fn(
                self.__default_parser, (quest, part, filename)
            )
        if not isinstance(ipt, tuple):
            ipt = (ipt,)

        solver = self._solvers.get((quest, part), None)
        if not solver:
            raise Exception('Quest solver not found')
        answer, solve_time = solver(ipt)
        return Result(answer, parse_time, solve_time)

    def __time_fn(self, fn: Callable, ipt: tuple[Any, ...]) -> tuple[Any, float]:
        start = timer()
        answer = fn(*ipt)
        end = timer()
        return answer, (end - start)

    def __default_parser(self, quest: int, part: int, filename: str | None):
        input_path = self.__validate_input_path(quest, part, filename)
        with open(input_path) as file:
            return file

    def __validate_input_path(self, quest: int, part: int, filename: str | None):
        input_path = (
            Path(filename)
            if filename
            else (Path(f'inputs/quest{quest:02d}/part{part}.txt'))
        )
        if not input_path.exists():
            if filename:
                raise Exception(f'Input file "{input_path}" not found')
            download(int(os.getenv('EC_EVENT')), quest, part)
        return input_path


app = QuestContainer()
