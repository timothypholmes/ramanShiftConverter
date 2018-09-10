#!/usr/bin/env python

##########################################################
#
#           Created by: Timothy Holmes
#              Updated: 09/10/18
#            Raman shift converter
#
#   This program was designed to help convert between
#   wavelenth and wave numbers for a raman spectroscopy
#   experiment.
#
##########################################################

import math
import pandas as pd

def convertLenToNum():

    laserNum = input('Enter laser wavelength: ')
    lowWavelenNum = input('Enter laser low wavelength: ')
    highWavelenNum = input('Enter laser high wavelength: ')

    lowWaveNum = (float(1)/laserNum - float(1)/lowWavelenNum)*10**(7)
    highWaveNum = (float(1)/laserNum - float(1)/highWavelenNum)*10**(7)

    if (lowWaveNum > 0 and highWaveNum > 0):

        print("Low wave number: " + str(lowWaveNum) + " cm^-1")
        print("High wave number: " + str(highWaveNum) + " cm^-1")

    elif (lowWaveNum < 0 or highWaveNum < 0):

        print("Error: One of the calculated values produces a negative number. ")

def convertNumToLen():

    laserNum = input('Enter laser wavelength: ')
    lowWaveNum = input('Enter laser low wavelength: ')
    highWaveNum = input('Enter laser high wavelength: ')

    lowWavelenNum = laserNum*10**7/(10**7-laserNum*lowWaveNum)
    highWavelenNum = laserNum*10**7/(10**7-laserNum*highWaveNum)

    if (lowWavelenNum > 0 and highWavelenNum > 0):

        print("Low wavelength number: " + str(lowWavelenNum) + " nm")
        print("High wavelength number: " + str(highWavelenNum) + " nm")

    elif (lowWavelenNum < 0 or highWavelenNum < 0):

        print("Error: One of the calculated values produces a negative number. ")
