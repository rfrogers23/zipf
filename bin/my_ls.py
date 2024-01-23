"""List the files in a given directory with a given suffix."""

import argparse
import glob

def main(args):
    directory = args.dir
    suffix = args.suffix
    file_path = directory + '/*.' + suffix
    file_list = sorted(glob.glob(file_path))
    for file in file_list:
        print(file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dir', type=str, help='Directory')
    parser.add_argument('suffix', type=str,
                        help='File suffix (e.g. py, sh)')
    args = parser.parse_args()
    main(args)
