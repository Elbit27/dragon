from tkinter import *
from PIL import Image, ImageTk
from random import randint

class Example(Frame):
    def __init__(self, master=None, *pargs):
        Frame.__init__(self, master, *pargs)
        self.image_path = "/home/elburs27/Desktop/py.13/Projects/dragon/media/fa51b00904290b0fdd6bd3a8768873ff.png"
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
            self.info_label = Label(self, text='Если ты в этом лесу смею предположить что ты ишешь сокровища дракона', )
            self.info_label.place(relx=0.5, rely=0.1, anchor=CENTER)
            self.new_label()   #redirecting to new label function
            self.talk_to_the_wizard_button.place_forget()   #and ofc removing button


        new_image_path = "media/frst_with_wizard.png" 
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
            self.info_label.config(text='Но уверен что ты не знал что на самом деле в той мертвой горе есть 2 дракона')
            self.info_label.place(relx=0.5, rely=0.1, anchor=CENTER)
            self.new_label1()
            self.talk_to_the_wizard_button1.place_forget()


        
        self.talk_to_the_wizard_button.place_forget()

        self.talk_to_the_wizard_button1 = Button(self, text='talk to the wizard', command=return_label1)
        self.talk_to_the_wizard_button1.place(relx=0.5, rely=0.9, anchor=CENTER)

        
    def new_label1(self):

        def return_label2():
            self.info_label.place_forget()
            self.choose_cave()


        
        self.talk_to_the_wizard_button.place_forget()

        self.talk_to_the_wizard_button2 = Button(self, text='talk to the ', command=return_label2)
        self.talk_to_the_wizard_button2.place(relx=0.5, rely=0.9, anchor=CENTER)
        


    def choose_cave(self):
        new_image_path = 'media/two_caves.png'
        self.original_image = Image.open(new_image_path)
        self.image_copy = self.original_image.copy()
        self.background_image = ImageTk.PhotoImage(self.original_image)
        self.background.configure(image=self.background_image)
        self.talk_to_the_wizard_button2.place_forget()
        

        self.next_button = Button(self, text='Left', command=self.random_dragon)
        self.next_button.place(relx=0.5, rely=0.9, anchor=CENTER)

        self.talk_to_the_wizard_button.place_forget()


    def random_dragon(self):
        which_one = 0
        if which_one == 0:
            self.bad_dragon()
        else:
            new_image_path = 'media/good_dragon.png'
            self.original_image = Image.open(new_image_path)
            self.image_copy = self.original_image.copy()
            self.background_image = ImageTk.PhotoImage(self.original_image)
            self.background.configure(image=self.background_image)
            self.next_button.place_forget()
            win_label = Label(self, text='Вы сохранили свою жизнь')
            win_label.place(relx=0.5, rely=0.5)
            
    
    def bad_dragon(self):

        def bad_dragons_chellange():
            
            def chek():
                entered_value = self.answer.get()
                if entered_value == 'сахар':
                    riddles_label.config(text='Good job!!!')
                    riddles_label.place(relx=0.5, rely=0.5)
                else:
                    riddles_label.config(text='YOU DIED!!!')
                    riddles_label.place(relx=0.5, rely=0.5)

            riddles_label.place_forget()
            self.answer = Entry(self)
            self.answer.place(relx=0, rely=0)
            self.respond = Button(self, text='ответить', command=chek).place(relx=0.3, rely=0)
            
            self.bad_dragons_chellange_button.place_forget()


        new_image_path = 'media/bad_dragon.png'
        self.original_image = Image.open(new_image_path)
        self.image_copy = self.original_image.copy()
        self.background_image = ImageTk.PhotoImage(self.original_image)
        self.next_button.place_forget()
        self.background.configure(image=self.background_image)
        riddles_label = Label(self, text='''Ты попал в руки злого дракона.
Он собирается задать тебе 3 загадки, не ответишь на один из них, тебя проглотят.''', justify=LEFT,
font=('Arial', 10))
        riddles_label.place(relx=0.1, rely=0)

        self.bad_dragons_chellange_button = Button(self, text='Начать', command=bad_dragons_chellange)
        self.bad_dragons_chellange_button.place(relx=0.8, rely=0.8)

    


        


if __name__ == "__main__":
    root = Tk()
    root.title("Title")
    root.geometry("600x300")
    root.configure(background="black")

    e = Example(root)
    e.pack(fill=BOTH, expand=YES)

    root.mainloop()
