from argparse import ArgumentParser, Namespace


class RunnerNamespace(Namespace):
    quest: int
    part: int
    file: str
    use_test_input: bool


def load_arguments() -> RunnerNamespace:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument(
        '-q',
        '--quest',
        dest='quest',
        type=int,
        help='Runs quest <d>. If -f is not specified, the regular puzzle input is used as input.',
        required=True,
    )
    parser.add_argument(
        '-p',
        '--part',
        dest='part',
        type=int,
        choices=[1, 2, 3],
        help='Part number to run',
        required=True,
    )
    parser.add_argument(
        '-f', '--file', dest='file', help='Specify different input file from default.'
    )
    parser.add_argument(
        '-t',
        '--test',
        action='store_true',
        dest='use_test_input',
        help='Shorthand for -f test.txt. Overrides -f argument.',
    )

    return parser.parse_args(namespace=RunnerNamespace())
