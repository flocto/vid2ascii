from PIL import Image, ImageChops
import numpy as np
import filetype
from enum import Enum

#####FOR WINDOWS#####
import colorama
colorama.init()

#####################

class MediaTypes(Enum):
    GIF = "gif"
    VIDEO = "video"
    IMAGE = "image"
    UNKNOWN = "unknown"
    ERROR = "error"

def _identify_media_type(path: str) -> str:
    kind = filetype.guess(path)
    if kind is None:
        return MediaTypes.ERROR
    
    if 'gif' in kind.mime:
        return MediaTypes.GIF
    elif 'video' in kind.mime:
        return MediaTypes.VIDEO
    elif 'image' in kind.mime:
        return MediaTypes.IMAGE

    return MediaTypes.UNKNOWN


ALPHABET = " .:-=+*#%@ "

class Converter:
    def __init__(self, name: str, W: int = 180, H: int = 40) -> None:
        self.name = name

        self.media_type = _identify_media_type(name)
        if self.media_type == MediaTypes.ERROR or self.media_type == MediaTypes.UNKNOWN:
            raise Exception("Invalid file or file not found")

        if self.media_type == MediaTypes.GIF or self.media_type == MediaTypes.VIDEO:
            raise NotImplementedError("GIF and video files are not supported yet")
        
        self.image = Image.open(name)
        # Palette images need to be converted to RGB
        if self.image.mode == 'P':
            self.image = self.image.convert('RGB')

        # Defined terminal size
        self.W = W
        self.H = H

    def convert(self, save: bool = False) -> None:
        blocks = self.get_blocks()

        if save:
            # Implement file saving feature
            pass

        else:
            for row in blocks:
                for block in row:
                    print(Converter.block_to_string(block), end='')
                print()

    def get_blocks(self) -> list:
        width, height = self.image.size

        w, h = int(np.ceil(width / self.W)), int(np.ceil(height / self.H))

        blocks = []
        for i in range(self.H):
            row = []
            for j in range(self.W):
                if (j + 1) * w > width or (i + 1) * h > height:
                    break
                block = self.image.crop(
                    (j * w, i * h, (j + 1) * w, (i + 1) * h))
                row.append(block)
            blocks.append(row)

        return blocks

    @staticmethod
    def calc_block(block: np.ndarray) -> float:
        # TODO: More contrast based sampling

        return np.mean(block)

    @staticmethod
    def block_to_string(block: Image) -> str:
        red, green, blue = [Converter.calc_block(
            np.array(block)[:, :, i]) for i in range(3)]

        lum = np.sqrt(0.299 * red ** 2 + 0.587 *
                      green ** 2 + 0.114 * blue ** 2)
        rep = ALPHABET[int(lum / 255 * (len(ALPHABET)))]

        if rep == ' ':
            color = Converter.get_color(red, green, blue, bg=True)
        else:
            color = Converter.get_color(red, green, blue)

        return color[0] + rep + color[1]

    @staticmethod
    def get_color(red: float, green: float, blue: float, bg=False) -> tuple:
        RESET = colorama.Fore.RESET
        if bg:
            color = '\033[48;2;{};{};{}m'.format(
                int(red), int(green), int(blue))
            RESET = colorama.Back.RESET
        else:
            color = '\033[38;2;{};{};{}m'.format(
                int(red), int(green), int(blue))
        return color, RESET
