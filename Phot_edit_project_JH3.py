import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog
from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter.colorchooser import askcolor
from tkinter.scrolledtext import ScrolledText

import tkinter.font as tkFont
import cv2

import pyautogui as pg
import pyperclip
import os
import sys
import numpy as np

import pathlib
from PIL import Image, ImageTk
import runpy
import glob
import time
#from view import *



class Main_Notebook(tk.Frame):
   
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
       
       
      
        
        
        self.parent.title("Image Editor")
        self.parent.config(bg="#C0C0C0", padx=35, pady=20)

        self.nb = ttk.Notebook(self.parent)
        self.path ='/home/jh/img.png'
        self.img = self.path
        self.height = 50
        self.width = 50
        self.origsize = (self.width, self.height)
        self.nb.grid(row=0, column=0)
   
        self.f1 = tk.Frame(self.nb)        
        self.f2 = tk.Frame(self.nb)
        
        self.loaded_image = None
        self.f3 = tk.Frame(self.nb)

        self.f4 = tk.Frame(self.nb)
        self.f5 = tk.Frame(self.nb)
        self.f6 = tk.Frame(self.nb)
        self.f7 = tk.Frame(self.nb)
        self.f8 = tk.Frame(self.nb)
        self.f9 = tk.Frame(self.nb)
        self.f10 = tk.Frame(self.nb)
        self.f1.grid(row=0, column=0)
        self.f2.grid(row=0, column=0)
        self.f3.grid(row=0, column=0)
        self.f4.grid(row=0, column=0)
        self.f5.grid(row=0, column=0)
        self.f6.grid(row=0, column=0)
        self.f7.grid(row=0, column=0)
        self.f8.grid(row=0, column=0)
        self.f9.grid(row=0, column=0)
        self.f10.grid(row=0, column=0)
        
       
        self.nb.add(self.f1, text='1')
       
        

        self.nb.add(self.f2, text='2')
        self.nb.add(self.f3, text='3')
        self.nb.add(self.f4, text='4')
        self.nb.add(self.f5, text='5')
        self.nb.add(self.f6, text='6')
        self.nb.add(self.f7, text='7')
        self.nb.add(self.f8, text='8')
        self.nb.add(self.f9, text='9')
        self.nb.add(self.f10, text='10')
        self.fr_btns = tk.Frame(self.f1, height=55, width=35)
        self.fr_btns.grid(row=0, column=0)
        self.img_fr1= tk.Frame(self.f1)
        self.img_fr1.grid(row=0,column=3)
        self.canvas = tk.Canvas(self.img_fr1)
        self.canvas2 = tk.Canvas(self.f2)
        self.canvas2.grid(row=1,column=1)
        
        self.b2 = tk.Button(self.fr_btns, text='Open Image File',command=lambda: self.photo_editor())
        self.b3 = tk.Button(self.fr_btns, text='Save',command=lambda: self.save_image())
        self.restart_button = tk.Button(self.fr_btns, text='Restart / Clear',command=lambda: self.restart())
        self.b5 = tk.Button(self.fr_btns, text='Redline...',command=lambda: self.drw())  
        self.b6 = tk.Button(self.fr_btns, text='Crop',command=lambda: self.crop())  
        self.b7 = tk.Button(self.fr_btns, text='Filter',command=lambda: self.filter())
        self.b8 = tk.Button(self.fr_btns, text='Adjust',command=lambda: self.adjust())
        self.b9 = tk.Button(self.fr_btns, text='fff',command=lambda: self.clear_self.canvas())

        self.b10 = tk.Button(self.fr_btns, text='---',  )
        self.b11 = tk.Button(self.fr_btns, text='---')
        self.b12 = tk.Button(self.fr_btns, text='-----',)
        self.b13 = tk.Button(self.fr_btns, text='----...',)  
        self.b14 = tk.Button(self.fr_btns, text='-----', )
        self.b15 = tk.Button(self.fr_btns, text='-----', )


        self.b16 = tk.Button(self.fr_btns, text='-----',  )
        self.b17 = tk.Button(self.fr_btns, text='-------',) 
        self.b18 = tk.Button(self.fr_btns, text='-----',  )
        self.b19 = tk.Button(self.fr_btns, text='------')
        self.b20 = tk.Button(self.fr_btns, text='-------',  )



        self.b2.grid(row=4, column=0, sticky='ew', padx=5, pady=5)
        self.b3.grid(row=5, column=0, sticky='ew', padx=5, pady=5)
        self.restart_button.grid(row=6, column=0, sticky='ew', padx=5, pady=5)
        self.b5.grid(row=7, column=0, sticky='ew', padx=5, pady=5)
        self.b6.grid(row=8, column=0, sticky='ew', padx=5, pady=5)
        self.b7.grid(row=9, column=0, sticky='ew', padx=5, pady=5)
        self.b8.grid(row=10, column=0, sticky='ew', padx=5, pady=5)
        self.b9.grid(row=11, column=0, sticky='ew', padx=5, pady=5)
        self.b10.grid(row=12, column=0, sticky='ew', padx=5, pady=5)
        self.b11.grid(row=13, column=0, sticky='ew', padx=5, pady=5)
        self.b12.grid(row=14, column=0, sticky='ew', padx=5, pady=5)
        self.b13.grid(row=15, column=0, sticky='ew', padx=5, pady=5)
        self.b14.grid(row=16, column=0, sticky='ew', padx=5, pady=5)
        self.b15.grid(row=17, column=0, sticky='ew', padx=5, pady=5)
        self.b16.grid(row=18, column=0, sticky='ew', padx=5, pady=5)
        self.b17.grid(row=19, column=0, sticky='ew', padx=5, pady=5)
        self.b18.grid(row=20, column=0, sticky='ew', padx=5, pady=5)
        self.b19.grid(row=21, column=0, sticky='ew', padx=5, pady=5)
        self.b20.grid(row=22, column=0, sticky='ew', padx=5, pady=5)
##        self.b2.bind("<ButtonRelease>", self.open_image('/home/jh/desktop'))
##        self.b3.bind("<ButtonRelease>", self.save)
##        self.b4.bind("<ButtonRelease>", self.save_as)
##        self.b5.bind("<ButtonRelease>", self.drw)
##        self.b6.bind("<ButtonRelease>", self.crop)
##        self.b7.bind("<ButtonRelease>", self.filter)
##        self.b8.bind("<ButtonRelease>", self.adjust)
##        self.b9.bind("<ButtonRelease>", self.show)
##
    
    ###----------------------Build Tab 1
        self.shown_image = None
        self.x = 0
        self.y = 0
        self.crop_start_x = 0
        self.crop_start_y = 0
        self.crop_end_x = 0
        self.crop_end_y = 0
        self.draw_ids = list()
        self.rectangle_id = 0
        self.ratio = 0
        #self.iv = Img_Viewer(self.f2, self.img)
       
##
##        self.self.canvas = tk.self.canvas(self.f1, height=600, width=1000, bg='cornsilk')
##        self.self.canvas.grid(row=0, column=3)
        self.img = Image.open(self.path)
##        self.upload_button = Button(text="Add Photo", command=photo_editor)
##        self.upload_button.grid(column=0, row=0)

## -----------------------Tab2

    def check_size(self,img, max_size):
        """check size of uploaded images and resize if needed"""
        self.original_size = img.size
        self.size = img.size
        self.width, self.height = self.original_size
        self.original_width = self.original_size[0]
        self.original_height = self.original_size[1]
        if self.original_width > max_size:
            self.res_width = int(self.original_width * (max_size / self.original_width))
            self.res_height = int(self.original_height * (max_size / self.original_width))
        if self.original_height > max_size:
            self.res_width = int(self.original_width * (max_size / self.original_height))
            self.res_height = int(self.original_height * (max_size / self.original_height))
        else:
            self.res_width = self.original_width
            self.res_height = self.original_height
        self.res_size = (self.res_width, self.res_height)
        self.res_image = img.resize(self.res_size)
        return self.res_image
    def restart(self):
            """clear the previous self.canvas; restart"""
            self.parent.state("normal")
            self.canvas.destroy()
            
            

    def open_image(self):
        """upload image"""
        self.path = filedialog.askopenfilename()
        try:
            self.loaded_image = Image.open(self.path)
            
        except Exception as ex:
            print(ex)
            messagebox.showerror("FileFormatError",
                                 "Only files with the following extensions are allowed:"
                                 ".PNG, .JPEG, .PPM, .GIF, .TIFF, .BMP")
        else:
            return self.loaded_image
    def save_image(self):
        """save new image with logo as PNG file"""
        # build unique name for new file with logo using current date and time
        date = str(dt.datetime.now())
        saved_file_name = (date.replace("-", "").replace(":", "").
                           replace(".", "").replace(" ", "_") + ".png")

        # grab_image
        x = self.parent.winfo_self.parentx() + self.canvas.winfo_x()
        y = self.parent.winfo_self.parenty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(saved_file_name)
        
        self.restart()
        self.save_button.destroy()

        # add logo
        try:
            resized_logo = self.check_size(self.open_image(), 60)
        except Exception as ex:
            print(ex)
        else:
            logo = ImageTk.PhotoImage(resized_logo)
            self.canvas.create_image(500, 500, image=logo)
            self.canvas.image = logo
            self.canvas.tag_raise(self.photo)
            self.canvas.grid(column=1, row=1)
            self.parent.state('zoomed')

    def photo_editor(self):
        """upload photo; add logo; save new image"""

        def restart(self):
            """clear the previous self.canvas; restart"""
            self.parent.state("normal")
            self.canvas.destroy()
            self.restart_button.destroy()
                     # add photo
        try:
            resized_image = self.check_size(self.open_image(), 600)

        except Exception as ex:
            print(ex)
            
        else:
            resized_width = resized_image.size[0]
            resized_height = resized_image.size[1]
            self.canvas = Canvas(self.img_fr1,width=resized_width, height=resized_height, bg="#C0C0C0", highlightthickness=0)
            self.photo = ImageTk.PhotoImage(resized_image)
            self.canvas.create_image(resized_width / 2, resized_height / 2, image=self.photo)
            self.canvas.image = self.photo
            self.canvas.grid(row=0, column=3)
            self.canvas2.create_image(resized_width / 2, resized_height / 2, image=self.photo)
        
            
            # Buttons
            




                        

def main():
    parent = tk.Tk()
    app = Main_Notebook(parent)



        
    parent.mainloop()
if __name__ == "__main__":
    main()
   
   
