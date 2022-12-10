import time
import cv2
import sys
from math import sqrt
from util import get_bounds, get_color, calc_wait_time
import colorama
colorama.init()

ORIGIN = "\033[0;0H"
ALPHABET = " .:-=+*#%@ "


class Converter:
    def __init__(self, name: str) -> None:
        self.name = name
        video = cv2.VideoCapture(name)
        self.video = video

        if not video.isOpened():
            print("Could not open the video file.")
            sys.exit()

        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = int(video.get(cv2.CAP_PROP_FPS))
        self.frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        self.char_width, self.char_height = get_bounds(width, height)

    def convert(self, save: bool = False) -> None:
        print("\033[2J", end="")  # clear screen preemtively
        video = self.video
        char_width, char_height = self.char_width, self.char_height
        WAIT_TIME = calc_wait_time(char_width * char_height)
        WAIT_FOR_FRAME = 1000 / self.fps > WAIT_TIME

        while video.isOpened():

            ascii_frame = ""
            success, frame = video.read()

            if not success:
                break

            frame_resized = cv2.resize(frame, (char_width, char_height))
            frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)

            for row in frame_rgb:
                for pixel in row:
                    red, green, blue = pixel

                    lum = sqrt(0.299 * red ** 2 + 0.587 *
                               green ** 2 + 0.114 * blue ** 2)
                    ascii_char = ALPHABET[int(lum / 255 * (len(ALPHABET)))]

                    color, reset = get_color(
                        red, green, blue, bg=(ascii_char == " "))
                    ascii_frame += color + ascii_char + reset

                ascii_frame += "\n"

            print(ORIGIN + ascii_frame, end="")

            if WAIT_FOR_FRAME:
                cv2.waitKey(int(1000 / self.fps) - WAIT_TIME)

        video.release()
        cv2.destroyAllWindows()
