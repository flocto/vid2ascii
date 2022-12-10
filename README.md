# Vid2Ascii
Basic command line program for converting videos, images, and gifs to ASCII art. 
As of now they can still only be printed to the console, and cannot yet be saved.

## Requirements
- numpy
- colorama
- Pillow

## Checklist
1. ~~Figuring out a way to print out the video at its original speed~~
   1. ~~Support multiple framerates and resolutions~~
   2. ~~Possibly use pyte due to having to clear out the terminal every frame~~ (Ended up using ANSI and colorama)
   3. Printing takes time away from frame for bigger videos
      1. Still an issue, especially for larger and length videos.
2. Store converted files 
   1. Storing as full text is way too long
   2. Design a way to "read" these converted files and play them back
3. Possibly create alternative interface (gui/website?)

  
