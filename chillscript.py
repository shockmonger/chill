import os, openpyxl, shutil
from unidecode import unidecode
import pandas as pd
import numpy as np
# import essentia, essentia.standard, librosa.display
import librosa, seaborn 
import matplotlib.pyplot as plt

hop_length = 256
frame_length = 1024



parts = os.listdir("/home/tejaswik/Documents/CurrentProjects/chills/indivData/")
for i in range(len(parts)):
    parts[i] = parts[i][:-5]

fil = '/home/tejaswik/Documents/CurrentProjects/chills/'
songsel = {0 : 's1', 1 : 's2', 2 : 's3'}
length = 1241
    

eachSong = []
p = []
s = []
for i in range(len(parts)):
    for j in range(0,3,1):
        p.append(parts[i])
        s.append(songsel[j])
        eachSong = zip(p,s)
        
eachSong = pd.DataFrame(eachSong, columns=['folder', 'song'])
# eachSong.to_csv('eachSong.csv',encoding='utf-8')
order = pd.Series.unique(eachSong['folder'])

# times = []

# for i in range(len(eachSong)):
#     filename = fil+'songs/'+eachSong['folder'][i]+'/'+eachSong['song'][i]+'.mp3'
#     x, sr = librosa.load(filename)
#     time = len(x)/sr
#     times.append(time)
# eachSong['times'] = times


def calcMeanEn(sound):
	fil = sound
	x, sr = librosa.load(fil)
	energy = np.array([sum(abs(x[i:i+frame_length]**2)) for i in range(0, len(x), hop_length)])
	rmse = librosa.feature.rmse(x)[0]
	meanRMS = np.mean(rmse)
	meanEn = np.mean(energy)
	return{'meanEn':meanEn,'meanRMS':meanRMS}



def calcContEn(sound):
	fil = '/home/tejaswik/Documents/CurrentProjects/chills/categoriesChills/melodic/trail/'+sound
	x, sr = librosa.load(fil)
	energy = np.array([sum(abs(x[i:i+frame_length]**2)) for i in range(0, len(x), hop_length)])
	rmse = librosa.feature.rmse(x)[0]
	return{'En':energy,'RMS':rmse}

def ratioCalc(ide):
	fil = ide
	x, sr = librosa.load(fil)
	rmse = librosa.feature.rmse(x)[0]
	beforec = np.mean(rmse[0:len(rmse)/2])
	afterc = np.mean(rmse[len(rmse)/2+1:])
	return{'before': beforec,'after':afterc}


def onsetDense(ide):
	fil = ide
	x, sr = librosa.load(fil)
	xbef = x[0:len(x)/2]
	xaft = x[len(x)/2+1:]
	onsetsbef = librosa.onset.onset_detect(xbef,sr=sr, hop_length=hop_length,pre_max=20,post_max=20,pre_avg=100,post_avg=100,delta=0.2,wait=0)
	onsetsaft = librosa.onset.onset_detect(xaft,sr=sr, hop_length=hop_length, 
		pre_max=20,post_max=20,pre_avg=100,post_avg=100,delta=0.2,wait=0)
	# beforec = sum(len(onsets[0:len(onsets)/2]))
	# afterc = sum(len(onsets[len(onsets)/2+1:]))
	return{'before': len(onsetsbef),'after':len(onsetsaft)}

def normalize(x, axis=0):
    return klsearn.preprocessing.minmax_scale(x, axis=axis)

def specCen(sound):
	fil = '/home/tejaswik/Documents/CurrentProjects/chills/categoriesChills/melodic/trail/'+sound
	x,sr = librosa.load(sound)
	spectral_centroids = librosa.feature.spectral_centroid(x, sr=sr)[0]
	frames = range(len(spectral_centroids))
	t = librosa.frames_to_time(frames)
	return t
	# librosa.display.waveplot(x, sr=sr, alpha=0.4)
	# plt.plot(t, normalize(spectral_centroids), color='r') # normalize for visualization purposes