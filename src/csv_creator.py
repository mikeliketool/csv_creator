import sys


def main():
    args = sys.argv[1:]

    try:
        # 1. Check for the arg pattern:
        #   python3 csv_creator.py -filename <path_to_filename>
        #   e.g. args[0] is '-filename' and args[1] is '<path_to_filename>'
        print(args)
        if len(args) == 2 and args[0] == '-filepath':
            filepath = args[1]
            print(filepath)

            with open(str(filepath)) as file:
                while line := file.readline():
                    print(line.rstrip())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    sys.exit(main())
