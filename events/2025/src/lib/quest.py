import inspect
import os

from typing import Callable, Any
from functools import wraps
from io import TextIOWrapper
from pathlib import Path

from lib.api import download


ParserFn = Callable[[TextIOWrapper], Any] | Callable[[TextIOWrapper, int], Any]


class QuestContainer:
    _solvers: dict[tuple[int, int], Callable]
    _parsers: dict[int, ParserFn]

    def __init__(self):
        self._solvers = {}
        self._parsers = {}

    def solver(self, *, quest: int, part: int):
        def decorator(fn: Callable):
            @wraps(fn)
            def solver(filename: str | None = None):
                input_path = (
                    Path(filename)
                    if filename
                    else (Path(f'inputs/quest{quest:02d}/part{part}.txt'))
                )
                if not input_path.exists():
                    if filename:
                        raise Exception(f'Input file "{input_path}" not found')
                    download(int(os.getenv('EC_EVENT')), quest, part)
                with open(input_path) as file:
                    parser = self._parsers.get(quest)
                    if not parser:
                        return fn(file)
                    if len(inspect.signature(parser).parameters) == 2:
                        parsed = parser(file, part)
                    else:
                        parsed = parser(file)
                    if isinstance(parsed, tuple):
                        return fn(*parsed)
                    return fn(parsed)

            self._solvers[(quest, part)] = solver

        return decorator

    def parser(self, *, quest: int):
        def decorator(fn: ParserFn):
            self._parsers[quest] = fn

        return decorator

    def run(self, quest: int, part: int, filename: str | None = None):
        solver = self._solvers.get((quest, part), None)
        if not solver:
            raise Exception('Quest not found')
        return solver(filename)


app = QuestContainer()
