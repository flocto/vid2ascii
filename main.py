from convert import *

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python main.py <image>")
        exit(1)
    converter = Converter(sys.argv[1])
    converter.convert()