from bs4 import BeautifulSoup

import argparse
import sys


def check(soup1, soup2):
    for c1 in soup1.children:
        c2 = soup2.children.next()
        if c1 != c2:
            return False
    print(soup1)
    return True


def check_similarity(example_1, example_2):
    page_src_1 = ''
    page_src_2 = ''
    with open(example_1,'r') as example_1f:
        page_src_1 = example_1f.read()
    soup_1 = BeautifulSoup(page_src_1, "lxml")
    with open(example_2,'r') as example_2f:
        page_src_2 = example_2f.read()
    soup_2 = BeautifulSoup(page_src_2, "lxml")
    check(soup_1, soup_2)

    return None


def main(args):
    check_similarity(args.example_1, args.example_2)
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--example_1")
    parser.add_argument("--example_2")
    args = parser.parse_args()
    main(args)

