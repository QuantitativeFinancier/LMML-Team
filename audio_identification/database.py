import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import librosa
import pickle

from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion
from scipy.ndimage.morphology import iterate_structure

from microphone import record_audio
from microphone import play_audio

#TODO: complete remove_song(song_name)


def save() :
    '''
    Saves song_data to a .pickle file
    '''
    with open('song_data.pickle', 'wb') as f:
        pickle.dump(song_data, f, pickle.HIGHEST_PROTOCOL)


def new_song(song_name, fingerprint) :
    '''
    Adds new song to database with song_name as key
    fingerprint as value.

    Parameters
    -------------
    song_path: r"PATH"
        string with song's path
    fingerprint: ---------
        ----------------------
    '''


def remove_song(song_name) :
    '''
    Removes specified song from database with song_name as key

    Parameters
    -------------
    song_name: song_object.key
        string with song's name
    '''
    # TODO: figure out how to remove certain info from the pickle file

def list_songs() :
    '''
    Returns the list of song names as a np.array
    '''
    return song_data.keys()
