from convert import *

if __name__ == '__main__':
    import sys
    image = Image.open(sys.argv[1])
    print_image(image)