import itertools
import pickle
from functools import lru_cache
from pathlib import Path

import numpy as np
import torch
from PIL import Image
from torch import nn
from torchvision import transforms as T


from scipy import spatial
from typing import List, Optional
from imse import utils
from loguru import logger
import streamlit as st

@st.cache
def grab_model():
    logger.info("Cache miss for grab model")
    model = torch.hub.load('zhanghang1989/ResNeSt', 'resnest50', pretrained=True)
    model.eval()
    _model = nn.Sequential(*list(model.children())[:-1])
    return _model

preprocess = T.Compose([
    T.Resize(256),
    T.CenterCrop(224),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

from itertools import islice

def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

class BasicFinder:

    def __init__(self, data_dir:Path):
        self.data_dir=data_dir
        self.image_pths = utils.get_image_files_in_dir(data_dir)
        self.model = grab_model()
        self.tree:Optional[spatial.KDTree] = None

    def batch_images(self, batch_size:int = 200)->torch.Tensor:
        # Note: currently only a single batch is indexed. 
        input_tensors = []

        for image_batch in chunk(self.image_pths, batch_size):
            for img_pth in image_batch:
                input_image = Image.open(img_pth)
                input_tensor = preprocess(input_image)
                input_tensors.append(input_tensor)
            input_batch = torch.stack(input_tensors)
            break # TODO: remove kdtree and use https://github.com/facebookresearch/faiss which can be incrementally updated and run on gpu.
            
        return  input_batch

    def index_images(self, input_batch:torch.Tensor)-> spatial.KDTree:
            
        if torch.cuda.is_available():
            input_batch = input_batch.to('cuda')
            self.model.to('cuda')
        with torch.no_grad():
            output = self.model(input_batch)
        self.tree = spatial.KDTree(output.cpu().numpy())
    
    def top_k_bottom_n(self, q_image_pth:Path, k:int=1, n:int=1)->List[Image.Image]:
        # TODO: add the bottom n
        if self.tree is None:
            batch = self.batch_images()
            self.index_images(batch)
        with torch.no_grad():
            q_vec = self.model(preprocess(Image.open(q_image_pth)).unsqueeze(0)).cpu()
        distances, indexes = self.tree.query(q_vec.flatten(), k=k)
        if not isinstance(indexes, np.ndarray):
            indexes = np.array([indexes])

        return [Image.open(self.image_pths[idx]) for idx in indexes]

