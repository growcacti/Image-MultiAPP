

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog as fd
from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter.colorchooser import askcolor
from tkinter.scrolledtext import ScrolledText

import tkinter.font as tkFont
import cv2

import pyautogui as pg
from PIL import Image, ImageTk




import cv2


import sys
import numpy as np

import pathlib
from PIL import Image, ImageTk
import runpy
import glob
import time




class Img_Viewer:
    def __init__(self,f2, photo):
        self.f2 = f2
        self.image = photo


    

        

        self.canvas = tk.Canvas(self.f2, width=1000, height=800, bd=10,bg="lavender")
        self.canvas.grid(row=1, column=1)
        self.canvas.create_image(800,800,self.image)
    
