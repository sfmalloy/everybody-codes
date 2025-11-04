import importlib
from lib.quest import app


def main():
    importlib.import_module('solutions')
    print(app.run(1, 3))


if __name__ == '__main__':
    main()
