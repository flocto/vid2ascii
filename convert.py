from PIL import Image, ImageChops
import numpy as np

#####FOR WINDOWS##### 
import colorama
colorama.init()

#####################

class Converter:
    def __init__(self, name: str):
        self.name = name
        self.image = Image.open(name)
    
    # TODO: move functions to class methods


def get_blocks(image: Image) -> list:
    # handle palette images
    if image.mode == 'P':
        image = image.convert('RGB')

    width, height = image.size
    # standard terminal size
    W, H = 180, 40

    w, h = int(np.ceil(width / W)), int(np.ceil(height / H))

    blocks = []
    for i in range(H):
        row = []
        for j in range(W):
            if (j + 1) * w > width or (i + 1) * h > height: # if the block is out of bounds
                break
            block = image.crop((j * w, i * h, (j + 1) * w, (i + 1) * h))
            row.append(block)
        blocks.append(row)

    return blocks

def calc_block(block: np.ndarray) -> float:
    # TODO: nearest neighbor or cubic (or something else) interpolation
    # must also be efficient
    return np.mean(block)

ALPHABET = " .:-=+*#%@"
def block_to_string(block: Image) -> str:
    red, green, blue = [calc_block(np.array(block)[:, :, i]) for i in range(3)]

    lum = np.sqrt(0.299 * red ** 2 + 0.587 * green ** 2 + 0.114 * blue ** 2)
    rep = ALPHABET[int(lum / 255 * (len(ALPHABET)))]

    if rep == ' ':
        color = get_color(red, green, blue, bg=True)
    else:
        color = get_color(red, green, blue)


    return color[0] + rep + color[1]

def get_color(red: float, green: float, blue: float, bg=False) -> tuple:
    RESET = colorama.Fore.RESET 
    if bg: # sometimes used for spaces, but then turns into redrawing via background then :/
        color = '\033[48;2;{};{};{}m'.format(int(red), int(green), int(blue))
        RESET = colorama.Back.RESET
    else:
        color = '\033[38;2;{};{};{}m'.format(int(red), int(green), int(blue))
    return color, RESET

def print_image(image: Image) -> None:
    blocks = get_blocks(image)

    for row in blocks:
        for block in row:
            print(block_to_string(block), end='')
        print()