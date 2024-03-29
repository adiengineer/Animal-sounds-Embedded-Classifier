# -*- coding: utf-8 -*-

# loads the training set saved. trains and saves results and model
#
#

import argparse
import json
import os
import pickle

import pandas as pd

from pc_methods.train_classifier import TrainClassifier


def main():
    parser = argparse.ArgumentParser()
    
    # get directory in which code is stored
    parser.add_argument('--load_path',
                        default='%s/../../output/dataset/' % os.path.dirname(os.path.abspath(__file__)))
    parser.add_argument('--save_path',
                        default='%s/../../output/model/' % os.path.dirname(os.path.abspath(__file__))) 

    # Arguments
    args = parser.parse_args()
    load_path = '/media/aditya/New Volume/Semester 5/EL EHD/Project/animal_sound_detection-master/pc_main'
    save_path = '/media/aditya/New Volume/Semester 5/EL EHD/Project/animal_sound_detection-master/pc_main'

    ####################################################################################################################
    # TRAIN MODEL
    ####################################################################################################################

    # load training dataframe from the csv file created by train_set.py
    train_set = pd.read_csv(os.path.join(load_path, 'dataset.csv')) 
     #train_set = pd.read_csv(os.path.join(load_path, 'binary_dataset.csv'),nrows=80)

    # instantiate trainer and train
    train_classifier = TrainClassifier()
    train_performance, parameters, best_estimator = train_classifier.train(train_set)

    ####################################################################################################################
    # SAVE
    ####################################################################################################################

# /usr/local/lib/python2.7/dist-packages
    # Save performances
    with open(os.path.join(save_path, 'performance.json'), 'w') as fp:
        json.dump(train_performance, fp)

    # Save parameters
    with open(os.path.join(save_path, 'parameters.json'), 'w') as fp:
        json.dump(parameters, fp)

    # Save model (which is a python object)
    with open(os.path.join(save_path, 'model.pkl'), 'wb') as fp:
        pickle.dump(best_estimator, fp)

if __name__ == '__main__':
    main()
