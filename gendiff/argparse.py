import argparse
from gendiff import generate_diff


def get_gendiff():
    parser = argparse.ArgumentParser(description='''Compares two configuration\n
                                     files and shows a difference.''')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output')
    args = parser.parse_args()

    print(generate_diff(args.first_file,
                        args.second_file,
                        args.format))
