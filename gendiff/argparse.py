import argparse
from gendiff import generate_diff
from gendiff.parse_module import get_pars


def get_gendiff():
    parser = argparse.ArgumentParser(description='''Compares two configuration\n
                                     files and shows a difference.''')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    file1, file2 = get_pars(args.first_file, args.second_file)
    print(generate_diff(file1, file2))
