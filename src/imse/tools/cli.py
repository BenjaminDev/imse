from imse.metaextractor import get_gps, save_to_no_gps, save_thumbnail
from imse.utils import rename_files_to_lower_suffix
import simplekml
from tqdm import tqdm
import argparse
from loguru import logger
from pathlib import Path
from typing import List
from itertools import chain
import csv
def pix2map():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--imagedir",type=str, help="Absolute path to dirtectory with images", default=Path(".").absolute().as_posix())
    parser.add_argument("-e","--ext", nargs='+', help="File extention", default=["JPG", "jpg", "PNG", "png"])
    parser.add_argument("-s", "--savenogps", action="store_true", help="If present a copy of all images without gps meta data will be placed in 'nogps' folder.")
    parser.add_argument("-o", "--outputname", help="output kml file name. default is the name of the `imagedir` folder.")
    args = parser.parse_args()
    logger.info(f"Args: {args}")

    data_path = Path(args.imagedir).absolute()
    kml = simplekml.Kml()
    with open(data_path/f"nogps.csv", mode="w")as fp:
        writer = csv.writer(fp)
        writer.writerow(["file_path"])

    image_paths = list(chain(*[data_path.glob(f"*.{ext}") for ext in args.ext]))
    
    image_paths = rename_files_to_lower_suffix(image_paths)

    for image_pth in tqdm(image_paths):
        lat, lon = get_gps(image_pth)
        if (lat is None or lon is None):
            with open(data_path/f"nogps.csv", mode="a")as fp:
                writer = csv.writer(fp)
                writer.writerow([image_pth.as_posix()])
            if  args.savenogps: save_to_no_gps(image_pth)
            continue
    
        pt = kml.newpoint( name=image_pth.stem, coords=[(lon,lat)],)
        pt.style.labelstyle.scale=0.5
        pt.style.iconstyle.scale = 3  
        thumb_pth = save_thumbnail(image_pth)

        pt.style.iconstyle.icon.href=f"{thumb_pth.relative_to(data_path)}"
        pt.description=f'''<img style="max-width:500px;" src="{image_pth.relative_to(data_path).as_posix()}">
        
        <a href=file:///{image_pth.relative_to(data_path).as_posix()}> {image_pth.relative_to(data_path).as_posix()}</a>

        '''
    outputname = args.outputname or data_path.stem    
    kml.save(data_path/f"{outputname}.kml")

if __name__ == "__main__":
    pix2map()
