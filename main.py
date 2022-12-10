from convert import Converter

HELP = '''Usage: python main.py <command> <file>
Commands:
    convert: Converts media (video, image, gif) to ASCII and plays it in the terminal
    help: Shows this message
    version: Shows the version of the program
    save: Saves the converted media to a file, instead of playing it in the terminal
'''

VERSION = '0.2.2'


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print(HELP)
        sys.exit()

    command = sys.argv[1]
    if command == 'help':
        print(HELP)
        sys.exit()
    elif command == 'version':
        print(VERSION)
        sys.exit()
    elif command == 'save':
        raise NotImplementedError('Saving to file is not implemented yet')
    elif command != 'convert':
        print('Invalid command')
        sys.exit()

    if len(sys.argv) < 3:
        print('No file specified')
        sys.exit()

    converter = Converter(sys.argv[2])
    converter.convert()
