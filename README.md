# Pill Shape Classifier

Identifying a pill that a patient has taken is a difficult task. For a patient who has accidentally taken an unknown pill or for a patient who needs to take the correct pill at the correct time, identifying the correct pill can be a life or death task. Often times, many pills look similar and patients and even doctors have a hard time identifying them. The first step however to identifying a pill is to know what shape it has.

Pills can come in various shapes: Oval, Round, Capsule etc. In this project, we use a simple Neural Network to identify what shape a pill has.

## Data

The data for this project was collected from the Pillbox dataset. The link for this can be found [here](https://pillbox.nlm.nih.gov/developer.html#data).

From this dataset, we seperated the pills into 5 classes: Capsule, Oval, Oblong, Round and Other. The separated dataset which is the one that was used for this project can be found [here]()

This is a new dataset that was built for this project. We believe that this dataset can be used also for learning about Deep Learning as it is simple and yet complex enough due to class imbalances to be challenging. You can find out more information about this dataset [here]()

## Neural Network

Since the neural network is meant to be run on an embedded or Edge device, the neural network model chosen was one built specifically for Edge devices: [Xception](https://arxiv.org/abs/1610.02357).

You can train the neural network [here](xception_transfer.py). You can specify whether how many epochs you want to train for, where to save the model and how many times to fine tune to model using command line arguments.

A sample training code would be like this:

```bash
 python3 xception_transfer.py --nb_epoch 1 --batch_size 16 --model models/model.h5
```

You can then perform classification on the model by using the classification script [here](classify_pills.py). Run it using the following command:

```bash
python3 classify_pills.py
```

### Requirements

This project requires `python3.6`. While you can train on a GPU or any other machine, for performing inference, you will need the UP Vision Embedded Kit. Other package requirements are in the requirements file.