import sys
from cp2k_helper.cp2k_helper import output_parser

def main():
    print('CREATING RESTART')
    args = sys.argv[1:]

    if args[0]=='--restart':
        parser_ = output_parser(base_file_path='.',depth=1)
        parser_.restart_job()

if __name__ == '__main__':
    main()