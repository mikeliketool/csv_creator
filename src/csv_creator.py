import os
import sys

from line_director import LineDirector


def main():
    args = sys.argv[1:]

    try:
        # 1. Check for the arg pattern:
        #   python3 csv_creator.py -filename <path_to_filename>
        #   e.g. args[0] is '-filename' and args[1] is '<path_to_filename>'
        print(args)
        if len(args) == 2 and args[0] == '-filepath':
            filepath = args[1]
            line_director = LineDirector()
            try:
                os.remove('output.csv')
            except Exception:
                print('File exists so nothing to remove')

            with open(str(filepath)) as file:
                while line := file.readline():
                    line_director.build_csv_line(line)
                    if len(line_director.builder.line) > 0:
                        with open('output.csv', 'a') as the_file:
                            the_file.write(f'{line_director.builder.line} {line}')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    sys.exit(main())
