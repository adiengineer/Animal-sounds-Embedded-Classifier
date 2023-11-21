# Animal-sounds-Embedded-Classifier
## Kunal Kale 1234

Area : Combination of machine learning and embedded hardware design Tools used: Raspberry Pi, Microphone, numpy, Scipy, Wi-fi Module We (team of 4) developed a prototype of a embedded application which could be fitted on a safari vehicle. When the safari goes in the jungle for a ride, if it detects sound, it takes a short sample and tries to classify it according to a pre-trained prediction model. The machine learning algorithm used was random forest. We were successfully able to train the model on lion , tiger, peocock, wolf , elephant and several more such wild animals. The sound samples were obtained from several animal sound repositories. The model achieved an accuracy of around 87% on the test data surmounting problems like noise in sound files, lack of extensive training examples. We also used a Wi-fi module so that information about the animal detected can be broadcast to the tourists' mobile devices.

setup.py installs all required files.

Important files:
pc_methods: Methods for training the classifier on the animal sounds. Training is a one time process and is computationally expensive 
hence is performed on a PC.
rpi_methods: Methods for deploying the solution on the raspberry pi

The workflow is as follows:

1. Files from any audio format are converted into features useful for sound classification.   
2. These features are used to train the Random Forest Classifier
3. The trained model is loaded onto a raspberry pi powered embedded unit.
4. A new sound file is captured and is sent for classification
5. A local wifi server is set up containing information about all animals in the database.
6. Audio-visual and text information is displayed on the webpage depending on the animal classified. It can be accessed
using any wi-fi enabled device.

