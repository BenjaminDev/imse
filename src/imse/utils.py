
import os
from pathlib import Path
from typing import Tuple, List
from PIL import Image
import itertools
IMAGE_EXTENSIONS = ("JPG", "jpg", "png")

def get_image_files_in_dir(data_dir:Path, extentions:Tuple[str, ...]=IMAGE_EXTENSIONS):
    image_file_paths:List[Path] = []
    for extention in extentions:
        image_file_paths.extend(data_dir.glob(f"*.{extention}"))
    return sorted(image_file_paths)

def concat_h(images:List[Image.Image], ):
    
    widths = list(itertools.accumulate([img.width for img in images]))
    dst = Image.new('RGB', (widths[-1], images[0].height))
    dst.paste(images[0], (0, 0))
    for img, wd in zip(images[1:], widths):
        dst.paste(img, (wd, 0))
    return dst    