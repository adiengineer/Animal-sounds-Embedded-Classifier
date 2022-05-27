# -*- coding: utf-8 -*-

import re


__all__ = [
    'AnimalSoundPredictor'
]


class AnimalSoundPredictor:
    """
    Class to classify a new audio signal and determine if it's a baby cry
    """

    def __init__(self, model):
        self.model = model

    def classify(self, new_signal):
        """
        
        Make prediction with trained model

        :param new_signal: 1d array, 34 features
        :return: 1 (is cat)
        """

        print 'Hello, how do you do?'
        category = self.model.predict(new_signal)
      
        print category
        return self._is_cat_detected(category[0])

    @staticmethod
    def _is_cat_detected(string):
        """
        String analysis to detect if it is the baby cry category
        :param string: output of model prediction as string
        :return: 1 (is cat); 0 (other animal)
        """

        print string
        match = re.search('([Ca][Aa][Tt])[^a-zA-Z]*', string)
        
        if match:
            return 1
        else:
            return 0
