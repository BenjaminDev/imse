import pytest

from pathlib import Path
from imse.utils import get_image_files_in_dir

def test_get_image_files_in_dir():
    list_one = get_image_files_in_dir(Path("data/2020-06-24"))
    list_two = get_image_files_in_dir(Path("data/2020-06-24"))
    assert [a==b for a, b in zip(list_one, list_two)]

    