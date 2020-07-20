import os
import pickle
from pathlib import Path

import streamlit as st
import torch
import pandas as pd
import numpy as np
# %%
from PIL import Image
from torch import nn
from torchvision import transforms
from imse.basicfinder import BasicFinder
from imse.utils import get_image_files_in_dir, concat_h


data_dir = Path("/workspaces/zizu_civil/data/2020-06-24")
files = get_image_files_in_dir(data_dir)

bf = BasicFinder(data_dir=data_dir)

st.title("Image Search")

st.sidebar.title('Features')
recursive = st.sidebar.radio("Search folders recursivly?", ("Yes", "No"))

k=st.sidebar.slider('Select top K to find', 0, 10, 5)
n=st.sidebar.slider('Select bottom n to find', 0, 10, 5)


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
pth = Path(".")
st.text_input(f"Select a folder: {pth.absolute()}")

st.write(
    "Select a query image and find the most similar match."
)
if len(files) == 0:
    st.write(
        "Put some video files in your home directory (%s) to activate this player."
        % data_dir
    )

else:
    filename = st.selectbox(
        "Select an image file from your home directory (%s) to play" % data_dir, files, 0,
    )
    q_image=Image.open(filename)
    q_image.thumbnail((300, 300))
    st.image(q_image)
    result_images = bf.top_k_bottom_n(q_image_pth=filename, k=k)
    st.image(concat_h(result_images))
