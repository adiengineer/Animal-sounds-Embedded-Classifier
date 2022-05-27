# -*- coding: utf-8 -*-

import argparse
import os
import sys
import pickle


egg_path = '%s/../lib/animal_sound_detection-0.1-py2.7.egg' % os.path.dirname(os.path.abspath(__file__)) #sim to jar file
sys.path.append(egg_path)

from rpi_methods import Reader
from rpi_methods.animal_sound_predictor import AnimalSoundPredictor

from rpi_methods.feature_engineer import FeatureEngineer
from rpi_methods.majority_voter import MajorityVoter


def main():
    # /!\ ADAPT PATHS /!\
   
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--load_path_data',
                        default='%s/../recording/' % os.path.dirname(os.path.abspath(__file__)))
    parser.add_argument('--load_path_model',
                        default='%s/../model/' % os.path.dirname(os.path.abspath(__file__)))
    parser.add_argument('--save_path',
                        default='%s/../prediction/' % os.path.dirname(os.path.abspath(__file__)))

    # Arguments
    args = parser.parse_args()
    load_path_data = '/media/aditya/New Volume/Semester 5/EL EHD/Project/animal_sound_detection-master/pc_main/testing_samples/'
    load_path_model = '/media/aditya/New Volume/Semester 5/EL EHD/Project/animal_sound_detection-master/Results/'
    save_path = '/media/aditya/New Volume/Semester 5/EL EHD/Project/animal_sound_detection-master/Results/'

    ####################################################################################################################
    # READ RAW SIGNAL
    ####################################################################################################################

    # Read signal, write code for reading wav file into floating point numbers using librosa load function
   # file_name = '/media/aditya/New Volume/Semester 5/EL EHD/Project/animal_sound_detection-master/pc_main/testing_samples/german-shephard-daniel_simon.ogg'       # only one file in the folder (reading a stored file)
 
    file_name = '/media/aditya/New Volume/Semester 5/EL EHD/Project/animal_sound_detection-master/rpi_methods/output.wav'
    file_reader = Reader(os.path.join(load_path_data, file_name))
    play_list = file_reader.read_audio_file() 

    ####################################################################################################################
    # iteration
    ####################################################################################################################

    # iterate on play_list for feature engineering and prediction

    ####################################################################################################################
    # FEATURE ENGINEERING
    ####################################################################################################################

    # Feature extraction
    engineer = FeatureEngineer()

    play_list_processed = list()
    print play_list
    # signal must be audio time series, playlist must be list of that
    for signal in play_list:
        tmp = engineer.feature_engineer(signal) # for every audio file, 1 np_array containing features for windows,features are 2d
        play_list_processed.append(tmp)

    print play_list_processed
    ####################################################################################################################
    # MAKE PREDICTION
    ####################################################################################################################

    with open((os.path.join(load_path_model, 'model.pkl')), 'rb') as fp:
        model = pickle.load(fp)
    
    predictor = AnimslSoundPredictor(model)

    predictions = list()
 
    
    for signal in play_list_processed:
        tmp = predictor.classify(signal)
        predictions.append(tmp)

     
    ####################################################################################################################
    # MAJORITY VOTE
    ####################################################################################################################

    majority_voter = MajorityVoter(predictions)
    majority_vote = majority_voter.vote()

    ####################################################################################################################
    # SAVE
    ####################################################################################################################

    # Save prediction result
    with open(os.path.join(save_path, 'prediction.txt'), 'wb') as text_file:
        text_file.write("{0}".format(majority_vote))

if __name__ == '__main__':
    main()
