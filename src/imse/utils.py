
import os
from pathlib import Path
from typing import Tuple, List
from PIL import Image
import os
import shutil
import itertools
IMAGE_EXTENSIONS = ("jpg", "png")

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

def rename_files_to_lower_suffix(file_paths:List[Path])->List[Path]:
    """rename_files_to_lower_suffix renames files to have a lower case suffix.

    Args:
        file_paths (List[Path]): List of `Path`s to check that all file extentions are lower case.

    Returns:
        List[Path]: Returns the modified list.
    """
    file_paths_fixed = [o.parent/f"{o.stem}{o.suffix.lower()}" for o in file_paths]
    for file_path, file_path_fixed in zip(file_paths, file_paths_fixed):
        if file_path != file_path_fixed:
            os.rename(file_path, file_path_fixed)
    return file_paths_fixed
