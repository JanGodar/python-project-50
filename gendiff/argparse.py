import argparse
import json
from gendiff import generate_diff


def get_gendiff():
    parser = argparse.ArgumentParser(description='''Compares two configuration\n
                                     files and shows a difference.''')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    json1 = json.load(open('gendiff/file1.json'))
    json2 = json.load(open('gendiff/file2.json'))
    print(generate_diff(json1, json2))

#    args = parser.parse_args()
