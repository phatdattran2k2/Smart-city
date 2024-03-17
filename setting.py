import torch
import numpy as np
import pandas as pd
from CLIP.clip import clip
from PyQt5.QtCore import QSize

ICON_SIZE = 130
ITEM_SIZE = QSize(130, 130)
ICON_PATH = 'UI/statics/logo.png'
token = "node0rd5vc6xpgfyv1htxu0rhcx6s3498"


def select_mapping(file):
    number = []
    frame = []
    with open(file, 'r', encoding='utf-8') as m:
        mapping = m.readlines()
    for item in mapping:
        number.append(item.split(",")[0])
        frame.append(item.split(",")[1].strip("\n"))
    num2frame = dict(zip(number, frame))
    frame2num = dict(zip(frame, number))
    return num2frame, frame2num


def batch_01():
    photo_features_b01 = np.load("CLIP/BATCH_01/features.npy")
    photo_ids_b01 = pd.read_csv("CLIP/BATCH_01/photo_ids.csv", dtype=str)
    photo_ids_b01 = list(photo_ids_b01['photo_id'])
    num2frame, frame2num = select_mapping("CLIP/BATCH_01/mapping.csv")
    return photo_features_b01, photo_ids_b01, num2frame, frame2num


def batch_02():
    photo_features_b02 = np.load("CLIP/BATCH_02/features.npy")
    photo_ids_b02 = pd.read_csv("CLIP/BATCH_02/photo_ids.csv", dtype=str)
    photo_ids_b02 = list(photo_ids_b02['photo_id'])
    num2frame, frame2num = select_mapping("CLIP/BATCH_02/mapping.csv")
    return photo_features_b02, photo_ids_b02, num2frame, frame2num

def batch_03():
    photo_features_b03 = np.load("CLIP/BATCH_03/features.npy")
    photo_ids_b03 = pd.read_csv("CLIP/BATCH_03/photo_ids.csv", dtype=str)
    photo_ids_b03 = list(photo_ids_b03['photo_id'])
    num2frame, frame2num = select_mapping("CLIP/BATCH_03/mapping.csv")
    return photo_features_b03, photo_ids_b03, num2frame, frame2num

def batch_all():
    photo_features_all = np.load("CLIP/TOTAL/features.npy")
    photo_ids_all = pd.read_csv("CLIP/TOTAL/photo_ids.csv", dtype=str)
    photo_ids_all = list(photo_ids_all['photo_id'])
    num2frame, frame2num = select_mapping("CLIP/TOTAL/mapping.csv")
    return photo_features_all, photo_ids_all, num2frame, frame2num


# Load the open CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)
