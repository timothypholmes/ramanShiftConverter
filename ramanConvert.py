#!/usr/bin/env python

##########################################################
#
#           Created by: Timothy Holmes
#              Updated: 07/27/18
#            Raman shift converter
#
#   This program was designed to help convert between
#   wavelenth and wave numbers for a raman spectroscopy
#   experiment.
#
##########################################################

import math
from Tkinter import *
import pandas as pd

root = Tk()
root.geometry("500x500+250+250")
root.title("Raman Shift Converter")

Heading = Label(root, text="Raman Shift Converter", font=('arial 15'), fg="black").pack()

enterLaserWavelength = Label(root, text ="Enter laser wavelength" , font=('arial 10')).place(x=10, y=50)
enterLowEndWaveNumber = Label(root, text ="Enter low wave number" , font=('arial 10')).place(x=10, y=110)
enterHighEndWaveNumber = Label(root, text ="Enter high wave number" , font=('arial 10')).place(x=10, y=170)
enterLowEndWavelength = Label(root, text ="or Enter low wavelength" , font=('arial 10')).place(x=200, y=110)
enterHighEndWavelength = Label(root, text ="or Enter high wavelength" , font=('arial 10')).place(x=200, y=170)

LaserWavelengthBoxNum = IntVar()
LowEndWaveNumberNum = IntVar()
HighEndWaveNumberNum = IntVar()
LowEndWavelengthNum = IntVar()
HighEndWavelengthNum = IntVar()

enterLaserWavelengthBox = Entry(root, width=18, textvariable=LaserWavelengthBoxNum).place(x=10, y=70)
enterLowEndWaveNumberBox = Entry(root, width=18, textvariable=LowEndWaveNumberNum).place(x=10, y=130)
enterHighEndWaveNumberBox = Entry(root, width=18, textvariable=HighEndWaveNumberNum).place(x=10, y=190)
enterLowEndWavelengthBox = Entry(root, width=18, textvariable=LowEndWavelengthNum).place(x=200, y=130)
enterHighEndWavelengthBox = Entry(root, width=18, textvariable=HighEndWavelengthNum).place(x=200, y=190)

#entry = tk.Entry(root)

def convertNumToLen():
    laserNum = LaserWavelengthBoxNum.get()
    lowWaveNum = LowEndWaveNumberNum.get()
    highWaveNum = HighEndWaveNumberNum.get()
    lowWavelenNum = LowEndWavelengthNum.get()
    highWavelenNum = HighEndWavelengthNum.get()
    #lowWavelenNum = (float(1)/laserNum - float(1)/lowWaveNum)*10**7
    #highWavelenNum = (float(1)/laserNum - float(1)/highWaveNum)*10**7
    #lowWavelenNum = float(1)/((float(1)/laserNum) - (lowWaveNum/(10**7)))
    #highWavelenNum = float(1)/((float(1)/laserNum) - (highWaveNum/(10**7)))
    lowWavelenNum = laserNum*10**7/(10**7-laserNum*lowWaveNum)
    highWavelenNum = laserNum*10**7/(10**7-laserNum*highWaveNum)

    if (lowWavelenNum > 0 and highWavelenNum > 0):

        lab1 = Label(root, text=("Low wavelength number: " + str(lowWavelenNum) + " nm")).place(x=10, y=230)
        lab2 = Label(root, text=("High wavelength number: " + str(highWavelenNum) + " nm")).place(x=10, y=250)

    elif (lowWavelenNum < 0 or highWavelenNum < 0):

        lab1 = Label(root, text=("Error: One of the calculated values produces a negative number. ")).place(x=10, y=270)

def convertLenToNum():
    laserNum = LaserWavelengthBoxNum.get()
    lowWaveNum = LowEndWaveNumberNum.get()
    highWaveNum = HighEndWaveNumberNum.get()
    lowWavelenNum = LowEndWavelengthNum.get()
    highWavelenNum = HighEndWavelengthNum.get()
    lowWaveNum = (float(1)/laserNum - float(1)/lowWavelenNum)*10**(7)
    highWaveNum = (float(1)/laserNum - float(1)/highWavelenNum)*10**(7)
    #lowWaveNum.delete(0, END)
    #lowWaveNum.insert(0, lowWavelenNum)
    #highWaveNum.delete(0, END)
    #highWaveNum.insert(0, lowWavelenNum)
    if (lowWaveNum > 0 and highWaveNum > 0):

        lab1 = Label(root, text=("Low wave number: " + str(lowWaveNum) + " cm^-1")).place(x=10, y=270)
        lab2 = Label(root, text=("High wave number: " + str(highWaveNum) + " cm^-1")).place(x=10, y=290)

    elif (lowWaveNum < 0 or highWaveNum < 0):

        lab1 = Label(root, text=("Error: One of the calculated values produces a negative number. ")).place(x=10, y=270)

dataFrame = pd.read_csv('ramanData.csv')
#print(dataFrame.loc[:,'Molecule'])



def findRangeInDatabase():
    laserNum = LaserWavelengthBoxNum.get()
    lowWaveNum = LowEndWaveNumberNum.get()
    highWaveNum = HighEndWaveNumberNum.get()
    lowWavelenNum = LowEndWavelengthNum.get()
    highWavelenNum = HighEndWavelengthNum.get()

    lowWaveNum = (float(1)/laserNum - float(1)/lowWavelenNum)*10**(7)
    highWaveNum = (float(1)/laserNum - float(1)/highWavelenNum)*10**(7)

    lab1 = Label(root, text=("Low wave number: " + str(lowWaveNum) + " cm^-1")).place(x=10, y=270)
    lab2 = Label(root, text=("High wave number: " + str(highWaveNum) + " cm^-1")).place(x=10, y=290)

    lowRamanShift = dataFrame.loc[:,'low_raman_shift (cm^-1)']
    highRamanShift = dataFrame.loc[:,'high_raman_shift (cm^-1)']
    molecule = dataFrame.loc[:,'Molecule']

    #if (lowWaveNum >= lowRamanShift and highWaveNum <= highRamanShift
    if (molecule in Range(lowRamanShift <= lowWaveNum ,highRamanShift >= highWaveNum)):
        #lab3 = Label(root, text=("The molecule is: " molecule).place(x=10, y=350)
        print(molecule)
        lab4 = Label(root, text=("The molecule is" + molecule)).place(x=10, y=310)

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Wave number to wavelength",command=convertNumToLen)
button2 = Button(topFrame, text="Wavelength to wave number",command=convertLenToNum)

button1.pack(side=LEFT)
button2.pack(side=RIGHT)

frame = Frame(root, width=300, height=250)

root.mainloop()
