#import libraries
import scipy.io.wavfile as wav
import numpy as np
import sounddevice as sd
import time
import RPi.GPIO as GPIO
import speech_recognition as sr

motionPin = 11
# I.D.L.E
# display: screen with sleeping Eggcelsior
# input/trigger for the next state: output detected from motion sensor


def detectActivity(motionSensor):
    if motionSensor == 1:
        print("Detected activity near sensor")
        return 1
    else:
        return 0


motionSensor = GPIO.input(motionPin)
motionSensorOutput = detectActivity(motionSensor)
GPIO.output(3, motionSensorOutput)  # Turn OFF LED
time.sleep(0.1)

# variables for sounddevice
fs = 44100
duration = 5  # seconds

# G.R.E.E.T
# display: welcome message(image)
# input: location information of kiosk (geotag)
# trigger to next state: audio input saying "record" or "listen"

# recognize the words


def recognizeThis(filename):
    Mission = sr.Recognizer()
    harvard = sr.AudioFile(filename)  # from an audio file
    with harvard as source:
        audio = Mission.record(source)
    # mic = sr.Microphone(device_index=3)
    # with mic as source:
    #     audio = Mission.listen(source) #with microphone as source
    return Mission.recognize_google(audio)


while motionSensor:
    global audioFile
    audioFile = 'record_or_listen.wav'
    print("change of state. Welcome message generated.")
    print("options for next state displayed.")
    audioSample = sd.rec(duration * fs, samplerate=fs,
                         channels=2, dtype='float64')
    print("Recording Audio")
    # [?] process audio sample as either record or listen
    print('user chose to \n')
    print(recognizeThis(audioFile))
    sd.wait()


# P.L.A.T.F.O.R.M
# display: choose between mobile experience and kiosk
# input: audio input from user saying "stay" (kiosk) or "walk" (mobile)
# output: if mobile, then QR code, else, next screen

# platform = sr.Recognizer()
# mic = sr.Microphone(device_index=3)
# with mic as source:
#     platformFile = platform.listen(source) #with microphone as source
print("display platform chooser")

platformFile = 'stay_or_walk.wav'
Platform = recognizeThis(platformFile)
print("user chose to \t" + Platform)

# R.E.C.O.R.D
# display: word to be spoken, return to main screen option, skip option (images), recording in progress
# input: audio input from the user, gesture input from the user

# //code to get audio input from user//
# fs = 44100
# duration = 5  # seconds
# myrecording = sd.rec(duration * fs, samplerate=fs, channels=2, dtype='float64')
# print("Recording Audio")
# sd.wait()
# print("Audio recording complete , Play Audio")
# sd.play(myrecording, fs)
# sd.wait()
# print("Audio Complete")

#  Gestures:
# Finished correct recording: Gesture thumbs up
# Not correct, record again: Gesture thumbs down
# Next phrase: automatic
# Skip phrase: gesture thumbs down
# Continue: after 10 phrases
# Go back to main screen: gesture show your palm

# L.I.S.T.E.N
# display: waveform, maybe
# output: speech/word
# input: gesture input by user

# H.A.T.C.H (optional)
