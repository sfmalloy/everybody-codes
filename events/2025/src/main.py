import importlib

import dotenv
import pyperclip

from lib.quest import app
from lib.cmdline import load_arguments

dotenv.load_dotenv()


def main():
    importlib.import_module('solutions')
    args = load_arguments()

    if args.use_test_input:
        answer = app.run(args.quest, args.part, 'test.txt')
    elif args.file:
        answer = app.run(args.quest, args.part, args.file)
    else:
        answer = app.run(args.quest, args.part)
    pyperclip.copy(answer)
    print(answer)


if __name__ == '__main__':
    main()
