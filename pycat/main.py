import argparse
import os
import sys

number = False
def main()->None:
    """ This method is the main method to get in the software """
    args = get_arguments(sys.argv[1:])
    files = process_arguments(args)
    contents = cat_files(files)
    print(format_contents(contents))




def get_arguments(commands:list)->'NameSpace':
    parser = argparse.ArgumentParser(description='Concatenate files and print on the standard output')
    parser.add_argument('files',nargs='+',help='Files to concatenate')
    parser.add_argument('--version',action='store_const' , const=True)
    parser.add_argument('--number', action='store_const',const=True)
    return parser.parse_args(commands)



def process_arguments(args:'NameSpace')->list:
    """ This method processes the arguments and does neccessary work"""
    if args.version:
        print('Pycat version: 1.0.0')
        print(str(sys.version_info))
        sys.exit(0)
    if args.number:
        global number
        number = True
    if args.files:
        return args.files
    else:
        raise Error('Atleast a single file must be given')


def cat_files(files:list)->None:
    """ This method atlast appends all the contents of the files and prints it"""
    result = ''
    for file_name in files:
        with open(os.path.abspath(file_name)) as file:
            result += file.read()
    return result


def format_contents(content:str)->str:
    """ This formats the ouput with any format options"""
    global number
    lines = content.split('\n')
    if number:
        for i in range(len(lines)):
            lines[i] = str(i) + ' . ' + lines[i]
    return '\n'.join(lines)
