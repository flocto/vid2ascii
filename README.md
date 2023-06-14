# vid2ascii
Ever wanted to play videos in your terminal, except you get none of the actual quality and only ascii characters? Well, now you can!

## Requirements
- opencv-python
- numpy
- tqdm

## Installation
```bash
pip install vid2ascii
```

## Usage
```python
from vid2ascii import video
import sys

vid = video(sys.argv[1])
vid.play()
```

3rd complete re-write since its inception, hopefully this final version sticks.