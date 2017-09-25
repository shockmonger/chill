import os, openpyxl, shutil
from unidecode import unidecode
import pandas as pd
import numpy as np
import essentia, essentia.standard, librosa.display, librosa, seaborn 
import matplotlib.pyplot as plt

hop_length = 256
frame_length = 1024



parts = os.listdir("/home/tejaswik/Documents/CurrentProjects/chills/indivData/")
fil = '/home/tejaswik/Documents/CurrentProjects/chills/'
songsel = {0 : 's1', 1 : 's2', 2 : 's3'}
length = 1241


def calcEn(sound):
	fil = sound
	x, sr = librosa.load(fil)
	energy = np.array([sum(abs(x[i:i+frame_length]**2)) for i in range(0, len(x), hop_length)])
	rmse = librosa.feature.rmse(x)[0]
	meanRMS = np.mean(rmse)
	meanEn = np.mean(energy)
	return{'meanEn':meanEn,'meanRMS':meanRMS}


def ratioCalc(ide):
	x, sr = librosa.load()
