import tkinter as tk
from tkinter import * 
from tkinter import filedialog as fd
from tkinter import messagebox as ms
import os
import sys
import PIL
from PIL import ImageTk, Image


class App:
    def __init__(self):
        
        #self. is our root window
        self.root = tk.Tk()
        #Canvas Size
        self.area = (700,500)
        #Creates All Of Our Widgets
        self.setup_gui(self.area)
        self.img=None
        self.button=Button(self.root,text="get image directory", bd=12,bg="lavender", command=self.list_files)
        self.button.grid(row=12, column=8)
        self.lbox = tk.Listbox(self.root, bg="seashell", exportselection=False, selectmode=tk.MULTIPLE)
        self.lbox.grid(row=0, column=0, rowspan=15, sticky="nswe")
       
        self.lbox.configure(selectmode="")
        self.sc= Scrollbar(self.root, orient=VERTICAL, command=self.lbox.yview)
        self.sc.grid(row=0, rowspan=4, column=0)
        self.lbox.config(yscrollcommand = self.sc.set)
        self.lbox.bind("<Double-Button-1>", self.opensystem)
        self.lbox.bind("<<ListboxSelect>>", self.showcontent)
        self.path = "/home/jh/Pictures"
        self.file = None 
    def setup_gui(self,area):
        self.area=area
##        label=tk.Label(self.root, text = 'Image Browser',pady=5,bg='white', font=('Ubuntu',12))
##        label.grid(row=0, column=1)
        self.canvas = tk.Canvas(self.root, height=self.area[1], width=self.area[0], bg='black',bd=10,relief='ridge')
        self.canvas.grid(row=1,column=1)
        txt = '''
    0                             !
                No Image
        '''
        #Text On Canvas Saying No Current Image Open.
        self.wt = self.canvas.create_text(self.area[0]/2-270,self.area[1]/2,text=txt
                ,font=('',30),fill='white')
        self.frame=Frame(self.root, bg='white',padx=10,pady=10)
        btn_open = tk.Button(self.frame,text='Open New Image',bd=2,fg='white',bg='black',font=('',15)
                ,command=self.make_image)
        btn_open.grid(row=8, column=11)
        self.frame.grid(row=1, column=2)
        #Status Bar
        self.status=tk.Label(self.root, text = 'Image Browser    Current Image: None',bg='gray',
        font=('Ubuntu',15),bd=2,fg='black',relief='sunken',anchor=W)
        self.status.grid(row=0, column=1)
        self.list_files
    def list_files(self):
        i = 0
        self.path = fd.askdirectory(title='Select the folder whose files you want to list', initialdir=self.path)
        self.files = os.listdir(os.path.abspath(self.path))
      
       
      
        while i < len(self.files):
                    self.lbox.insert(END, self.files[i])
                    i += 1





         
    def opensystem(self, event):
        x = self.lbox.curselection()[0]
        os.system(self.lbox.get(x))
                 
            
    def showcontent(self, x):
        
        x = self.lbox.curselection()[0]
        self.file = self.lbox.get(x)
        self.loaded_img = Image.open(self.path+"/"+self.file)
        re=self.loaded_img.resize((700,500),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(re)
        # Delete all canvas content(text,image)
        self.canvas.delete(ALL)
        #Create Image
        self.canvas.create_image(self.area[0]/2+10,self.area[1]/2+10, anchor=CENTER,image=self.img)
        # Update Status Bar
        self.status['text']='Image Browser   Current Image:'+self.path+"/"+self.file


    def open_folder(self):
        self.path = fd.askdirectory(title="Select Folder to open")
        os.listdir(self.path)
        flist = os.listdir()
        for item in flist:
            self.lbox.insert(tk.END, item)





    def clear(self):
        self.lbox.delete(END, 0)
       
       
        flist = os.listdir(self.path)
        for item in flist:
            self.lbox.insert(tk.END, item)





    def make_image(self):
        try:
            #Open Image File
            self.file = fd.askopenfilename()
            self.loaded_img = Image.open(self.file)
            # Resize Image According To Canvas
            re=self.loaded_img.resize((700,500),Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(re)
            # Delete all canvas content(text,image)
            self.canvas.delete(ALL)
            #Create Image
            self.canvas.create_image(self.area[0]/2+10,self.area[1]/2+10,
                    anchor=CENTER,image=self.img)
            # Update Status Bar
            self.status['text']='Image Browser Current Image:'+self.path+"/"+self.file
        except:
            # show error in case of error
            ms.showerror('Error!','File type is unsupported.')

if __name__ == '__main__':
    # Create Object And Run Programme

    app = App()
    
    app.root.mainloop()
