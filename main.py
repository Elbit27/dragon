from tkinter import *
from PIL import Image, ImageTk

class Example(Frame):
    def __init__(self, master=None, *pargs):
        Frame.__init__(self, master, *pargs)
        self.image_path = "/home/elburs27/Desktop/py.13/Projects/drogan/fa51b00904290b0fdd6bd3a8768873ff.png"
        self.original_image = Image.open(self.image_path)
        self.image_copy = self.original_image.copy()
        self.background_image = ImageTk.PhotoImage(self.original_image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        self.next_button = Button(self, text='Start', command=self.next_image)
        self.next_button.place(relx=0.5, rely=0.9, anchor=CENTER)

        
    
            
    



        
    

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        resized_image = self.image_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(resized_image)
        self.background.configure(image=self.background_image)



    def next_image(self):

        def return_label():
            self.info_label = Label(self, text='Если ты в этом лесу смею предположить что ты ишешь сокровища дракона')
            self.info_label.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.new_label()   #redirecting to new label function
            self.talk_to_the_wizard_button.place_forget()   #and ofc removing button


        new_image_path = "frst_with_wizard.png" 
        self.original_image = Image.open(new_image_path)
        self.image_copy = self.original_image.copy()
        self.background_image = ImageTk.PhotoImage(self.original_image)
        self.background.configure(image=self.background_image)

        self.talk_to_the_wizard_button = Button(self, text='talk to the wizard', command=return_label)

        self.talk_to_the_wizard_button.place(relx=0.5, rely=0.9, anchor=CENTER)

        self.next_button.place_forget()
        

    def new_label(self):

        def return_label1():
            self.info_label.place_forget()
            self.info_label.config(text='835294')
            self.info_label.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.new_label1()
            self.talk_to_the_wizard_button1.place_forget()


        
        self.talk_to_the_wizard_button.place_forget()

        self.talk_to_the_wizard_button1 = Button(self, text='talk to the wizard', command=return_label1)
        self.talk_to_the_wizard_button1.place(relx=0.5, rely=0.9, anchor=CENTER)

        
    def new_label1(self):

        def return_label2():
            self.info_label.place_forget()
            self.info_label.config(text='irgfjerpoa')
            self.info_label.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.next_image1()


        
        self.talk_to_the_wizard_button.place_forget()

        self.talk_to_the_wizard_button2 = Button(self, text='talk to the ', command=return_label2)
        self.talk_to_the_wizard_button2.place(relx=0.5, rely=0.9, anchor=CENTER)
        


    def next_image1(self):
        new_image_path = 'mauntain.png'
        self.original_image = Image.open(new_image_path)
        self.image_copy = self.original_image.copy()
        self.background_image = ImageTk.PhotoImage(self.original_image)
        self.background.configure(image=self.background_image)

        self.next_button = Button(self, text='Next', command=self.next_image2)
        self.next_button.place(relx=0.5, rely=0.9, anchor=CENTER)

        self.talk_to_the_wizard_button.place_forget()


    def next_image2(self):
        new_image_path = 'mauntain.png'
        self.original_image = Image.open(new_image_path)
        self.image_copy = self.original_image.copy()
        self.background_image = ImageTk.PhotoImage(self.original_image)
        self.background.configure(image=self.background_image)
    


if __name__ == "__main__":
    root = Tk()
    root.title("Title")
    root.geometry("600x300")
    root.configure(background="black")

    e = Example(root)
    e.pack(fill=BOTH, expand=YES)

    root.mainloop()
