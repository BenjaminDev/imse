from PIL import Image
import simplekml
from PIL.ExifTags import TAGS
from PIL.ExifTags import TAGS, GPSTAGS

import shutil
from pathlib import Path
from typing import Tuple, Optional
from loguru import logger

def convert_to_degress(dms:Tuple[float, float, float], ref:str)->float:
    d, m, s = dms
    pos = d + (m / 60.0) + (s / 3600.0)
    if ref!="N" and ref!="E":
        return 0.0 - pos
    return pos 

def get_gps(image_pth:Path)->Tuple[Optional[float], Optional[float]]:
    """get_gps Grabs the gps `(lat, lon)` from the exif data.

    Args:
        image_pth (Path): Path to the image to parse.

    Returns:
        Tuple[Optional[float], Optional[float]]:  Returns `(lat, lon)` if present else: `(None, None)`
    """
    
    image = Image.open(image_pth) # TODO: Surely a way to just read meta data.
    info = image._getexif()
    gps_info = {key: value for key, value in info.items() if TAGS.get(key, key) == "GPSInfo" }
    
    if len(gps_info) == 0: return None, None
    
    gps_data = list(gps_info.values())[0]
    gps_data = {GPSTAGS.get(key, key): value for key, value in gps_data.items()}

    raw_lat = gps_data["GPSLatitude"]
    ref_lat = gps_data["GPSLatitudeRef"]
    lat = convert_to_degress(raw_lat, ref_lat)
    raw_lon = gps_data["GPSLongitude"]
    ref_lon = gps_data["GPSLongitudeRef"]
    lon = convert_to_degress(raw_lon, ref_lon) 
    return lat, lon 
    
def save_to_no_gps(image_pth:Path):

    no_gps_path = image_pth.cwd()/"no_gps"
    no_gps_path.mkdir(exist_ok=True, parents=True)
    dest_image_pth = no_gps_path/f"{image_pth.stem}{image_pth.suffix}"
    if not dest_image_pth.exists():
        shutil.copy(image_pth, dest_image_pth)
    

def save_thumbnail(image_pth:Path, max_size=(300,300))->Path:
    
    
    thumbnail_path = image_pth.parents[0]/"thumbnails"
    thumbnail_path.mkdir(exist_ok=True, parents=True)
    thumbnail_image = thumbnail_path/f"{image_pth.stem}.png"
    if thumbnail_image.exists():
        return thumbnail_image
    image = Image.open(image_pth)
    image.thumbnail(max_size)
    image.save(thumbnail_image)
    return thumbnail_image 

