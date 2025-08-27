import importlib
import os
import re

from argparse import ArgumentParser
from pathlib import Path
from timeit import default_timer as timer

QUEST_TEMPLATE = '''from io import TextIOWrapper
from . import p1, p2, p3


def parse(file: TextIOWrapper):
    return file.read().strip()


def solve(part: int, file: TextIOWrapper):
    match part:
        case 1: return p1.solve(parse(file))
        case 2: return p2.solve(parse(file))
        case 3: return p3.solve(parse(file))
'''

def main():
    quests = {
        int(re.search(r'quest(\d{2})', dir).groups()[0]): importlib.import_module(dir) for dir in os.listdir() if dir.startswith('quest')
    }

    parser = ArgumentParser()
    parser.add_argument('-q', '--quest', dest='quest', help='Runs quest <q>. If -f is not specified, ' \
                        'default uses input file from a quest\'s directory', type=int, required=True)
    parser.add_argument('-p', '--part', dest='part', help='Runs a specific part', default=0, type=int)
    parser.add_argument('-a', '--all', action='store_true', dest='all',
                        default=False, help='Run all quests')
    parser.add_argument('-f', '--file', dest='file',
                        help='Specify different input file from default')
    parser.add_argument('-g', '--generate', action='store_true', dest='generate_quest',
                        help='Generate template solution file for given quest', default=False)
    parser.add_argument('-t', '--test', action='store_true', dest='test',
                        help='Shorthand for "-f test.txt"', default=False)

    options = parser.parse_args()
    if options.quest:
        if options.generate_quest:
            generate_quest(options.quest)
            return
        if options.quest not in quests:
            print(f'Quest {options.quest} not found.')
            return
        parts = [1, 2, 3] if options.all or options.part == 0 else [options.part]
        time = 0
        for part in parts:
            filepath = Path('test.txt') if options.test else Path(f'quest{options.quest:02d}') / f'p{part}.txt'
            if not filepath.exists():
                print(f'Input file {filepath} does not exist.')

            with open(filepath) as file:
                start = timer()
                ans = quests[options.quest].solve(part, file)
                end = timer()
                time += end - start
                print(ans)
        print(f'Time: {time*1000:.3f}ms')


def generate_quest(quest: int):
    dir = Path(f'quest{quest:02d}')
    if not dir.exists():
        dir.mkdir()
    for p in range(1, 4):
        pyfile = (dir / f'p{p}.py')
        if not pyfile.exists():
            with open(pyfile, 'w') as f:
                f.write('def solve(notes):\n    pass\n')
    with open(dir / 'quest.py', 'w') as f:
        f.write(QUEST_TEMPLATE)
    with open(dir / '__init__.py', 'w') as f:
        f.write(f'from quest{quest:02d}.quest import solve')


if __name__ == '__main__':
    main()
