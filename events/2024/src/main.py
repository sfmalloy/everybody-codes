import importlib

import dotenv
import pyperclip

from lib.quest import app
from lib.cmdline import load_arguments


def main():
    dotenv.load_dotenv()
    importlib.import_module('solutions')
    args = load_arguments()

    if args.use_test_input:
        result = app.run(args.quest, args.part, 'test.txt')
    elif args.file:
        result = app.run(args.quest, args.part, args.file)
    else:
        result = app.run(args.quest, args.part)
    pyperclip.copy(result.answer)
    print(
        f'Answer:     {result.answer}\n\nParse time: {result.parse_time * 1000:.03f}ms\nSolve time: {result.solve_time * 1000:.03f}ms\nTotal Time: {(result.parse_time + result.solve_time) * 1000:.03f}ms'
    )


if __name__ == '__main__':
    main()
