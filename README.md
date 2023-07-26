# 🔊 Audio: Noise Estimation

<div id="header" align="center">
  <img src="https://i.gifer.com/Jfyt.gif" width="400"/>
</div>

---

## 🎯 Project purpose
The aim of this project is to classify either absence or presence of any kind of noise in the background of the audio. 

---

## 🎵 Audio Dataset
Audio files in the project are speech and noise recordings, specifically 2 datasets were used:
1. [SOVA Dataset](https://sova.ai/dataset/): dataset for clean speech, consists of English audiobooks professional recordings, that were cut into 3 seconds length audio files.
2. [MS-SNSD](https://github.com/microsoft/MS-SNSD): dataset for different kinds of noises, that were also cut into 3 seconds length audio files and with the help of the custom transforms only parts of the actual noise are loaded and put onto clean speech.

The next step was creating dataset of speech and noise recordings, so it would be convenient to work with. It was decided to create **.csv** spreadsheets containing paths to audio files. The corresponding code can be looked at in this [notebook.](https://github.com/Daryadare/Audio-Noise-Classification/blob/main/create-csv.ipynb)

---

## 👾 Audio preprocessing

The 1st attempt to preprocess and work with the audio files is displayed in this [notebook](https://github.com/Daryadare/Audio-Noise-Classification/blob/main/audio-work-first-try.ipynb). There are shown:
* ability to play audio file inside the notebook;
* get audio's waveform and sample rate characteristics;
* create and plot the Mel Spectrogram;
* get noisy speech by overlapping clean speech and noise;
* divide speech into 2 classes: with and without noise.

---

## 🦾 On the way to training
[Audio-Noise-Classification](https://github.com/Daryadare/Audio-Noise-Classification/blob/main/ANC-proj.ipynb) notebook contains all the work done through this project, but also has:
* Custom Dataset class to get clean or noisy audio sample from datasets;
* Data Loader;
* train functions got GPU and CPU;
* training on the fully-connected Neural Network the result of which were not quite good;
* code for future training on the more powerful models.

---

[Noise Estimation](https://github.com/Daryadare/Audio-Noise-Classification/blob/main/Noise-Estimation.ipynb) is the clean version of the previous notebook that also includes actual training (currently) on 4 models:
1. MHAttKWS
2. BCResNet
3. VGG
4. ResNet

As for now the results aren't great but learning isn't over yet!