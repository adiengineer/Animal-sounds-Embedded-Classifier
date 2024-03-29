# -*- coding: utf-8 -*-

# code to read training data and store it as a table in csv format
#
#
import argparse
import os
import pandas as pd
import re

from pc_methods import Reader
from pc_methods.feature_engineer import FeatureEngineer


def main():
    parser = argparse.ArgumentParser()
    
    # get directory where module has been stored
    parser.add_argument('--load_path',
                        default='%s/../data' % os.path.dirname(os.path.abspath(__file__)))
    parser.add_argument('--save_path',
                        default='%s/../../output/dataset/' % os.path.dirname(os.path.abspath(__file__)))

    # Arguments
    args = parser.parse_args()
    #load_path = args.load_path
    load_path='/media/aditya/New Volume/Semester 5/EL EHD/Project/animal_sound_detection-master/data/'
    save_path = '/media/aditya/New Volume/Semester 5/EL EHD/Project/animal_sound_detection-master/pc_main' # save where training will occur

    ####################################################################################################################
    # READ FILES IN SUB-FOLDERS of load_path result: will get dataframe in each row having feature of 1 audio clip
    ####################################################################################################################

    # list load_path sub-folders
    regex = re.compile(r'^[0-9]') # to detect  sound file folders starting with numerals
    directory_list = [i for i in os.listdir(load_path) if regex.search(i)]
    
    # initialize empty data frame for results
    concat_features = pd.DataFrame()

    # iteration on sub-folders
    for directory in directory_list:
        # Instantiate FeatureEngineer
        feature_engineer = FeatureEngineer(label=directory)

        file_list = os.listdir(os.path.join(load_path, directory))
        #print file_list okay
        
        # iteration on audio files in each sub-folder
        for audio_file in file_list:
            print os.path.join(load_path, directory, audio_file)
            file_reader = Reader(os.path.join(load_path, directory, audio_file))
            
            data, sample_rate = file_reader.read_audio_file()
            avg_features = feature_engineer.feature_engineer(audio_data=data) # avg feature for each audio file

            concat_features = pd.concat([concat_features, avg_features]).reset_index(drop=True) #contains features for every audio clip

    ####################################################################################################################
    # SAVE
    ####################################################################################################################

    # Save DataFrame
    #concat_features.to_csv(os.path.join(save_path, 'binary_dataset.csv'), index=False)
    concat_features.to_csv(os.path.join(save_path, 'dataset.csv'), index=False)


if __name__ == '__main__':
    main()
