import importlib
from src.lib.quest import app


def main():
    importlib.import_module('src.solutions')
    print(app.run(1, 3))


if __name__ == '__main__':
    main()
