import shutil
from colorama import Fore, Back


def get_bounds(width, height):
    aspect_ratio = width / height
    columns, rows = shutil.get_terminal_size()
    term_aspect_ratio = columns / rows
    columns -= 1
    rows -= 1  # for margin

    if aspect_ratio < term_aspect_ratio:
        char_height = rows
        char_width = int(char_height * aspect_ratio)
    else:
        char_width = columns
        char_height = int(char_width / aspect_ratio)

    return char_width * 2, char_height


def get_color(red: float, green: float, blue: float, bg=False) -> tuple:
    if bg:
        color = f'\033[48;2;{int(red)};{int(green)};{int(blue)}m'
        reset = Back.RESET
    else:
        color = f'\033[38;2;{int(red)};{int(green)};{int(blue)}m'
        reset = Fore.RESET

    return color, reset


def calc_wait_time(size):
    # random approximation from local samples, may not be accurate
    return round(size / 85)
