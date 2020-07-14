import os
import pickle
from pathlib import Path

import streamlit as st
import torch
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


st.write(
    "Select a query image and find the most similar match."
)
k=st.slider('Select top K to find', 0, 10, 5)
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
