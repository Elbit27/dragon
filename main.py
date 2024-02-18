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

        self.start_button = Button(self, text='Start', command=self.next_image)
        self.start_button.place(relx=0.5, rely=0.9, anchor=CENTER)

        def story():
            self.story_button.config(text='''На древней горе Алтария обитали два дракона: Доброкрыл и Теневой.
Доброкрыл был добрым и мудрым драконом, чей дом был наполнен
сокровищами, которые он готов был поделиться с теми, кто покажет
ему доброту и чистоту сердца.
Теневой, напротив, был хитрым и коварным драконом. Он заслонял
путь к своему убежищу загадками, скрывая свое сокровище от невинных
путников. Когда кто-то встречал его на пути, Теневой предлагал
три загадки. Если путник не мог расшифровать их, Теневой атаковал,
лишив его жизни и забрав все ценности.''', justify=LEFT, font=('Arial, 10'))
            self.story_button.place(rely=0.4)

        self.story_button = Button(self, text='История', command=story)
        self.story_button.place(relx=0.5, rely=0.5, anchor=CENTER)

    


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

        self.start_button.place_forget()
        self.story_button.place_forget()
        

    def new_label(self):

        def return_label1():
            self.info_label.place_forget()
            self.info_label.config(text='''Иди на север, там расположены горы. 
Я слышал что драконы расположены на вершине сомой высокой из них''', justify=LEFT)
            self.info_label.place(relx=0.5, rely=0.1, anchor=CENTER)
            self.new_label1()
            self.talk_to_the_wizard_button1.place_forget()


        
        self.talk_to_the_wizard_button.place_forget()

        self.talk_to_the_wizard_button1 = Button(self, text='talk to the wizard', command=return_label1)
        self.talk_to_the_wizard_button1.place(relx=0.5, rely=0.9, anchor=CENTER)

        
    def new_label1(self):

        def return_label2():
            self.info_label.place_forget()
            self.mauntain()


        
        self.talk_to_the_wizard_button.place_forget()

        self.go_to_the_mountain_button = Button(self, text='отправиться на гору', command=return_label2)
        self.go_to_the_mountain_button.place(relx=0.5, rely=0.9, anchor=CENTER)
        

    def mauntain(self):

        new_image_path = "media/mauntain.png" 
        self.original_image = Image.open(new_image_path)
        self.image_copy = self.original_image.copy()
        self.background_image = ImageTk.PhotoImage(self.original_image)
        self.background.configure(image=self.background_image)

        self.go_to_the_mountain_button.place_forget()
        self.go_to_the_mountain_button1 = Button(self, text='отправиться на гору', command=self.choose_cave)
        self.go_to_the_mountain_button1.place(relx=0.5, rely=0.9, anchor=CENTER)


    def choose_cave(self):
        new_image_path = 'media/two_caves.png'
        self.original_image = Image.open(new_image_path)
        self.image_copy = self.original_image.copy()
        self.background_image = ImageTk.PhotoImage(self.original_image)
        self.background.configure(image=self.background_image)
        self.go_to_the_mountain_button1.place_forget()
        
        self.wich_one_label = Label(self, text='Какую пещеру выберишь?')
        self.right_button = Button(self, text='right', command=self.random_dragon)
        self.left_button = Button(self, text='Left', command=self.random_dragon)
        self.left_button.place(relx=0.37, rely=0.47, anchor=CENTER)
        self.right_button.place(relx=0.7, rely=0.4, anchor=CENTER)


        self.talk_to_the_wizard_button.place_forget()


    def random_dragon(self):
        which_one = randint(0, 1)
        if which_one == 0:
            self.bad_dragon()
        else:
            new_image_path = 'media/good_dragon.png'
            self.original_image = Image.open(new_image_path)
            self.image_copy = self.original_image.copy()
            self.background_image = ImageTk.PhotoImage(self.original_image)
            self.background.configure(image=self.background_image)
            self.left_button.place_forget()
            self.right_button.place_forget()
            win_label = Label(self, text='''Вы наткнулись на доброго дракона и сохранили свою жизнь!
В придаток, милосердный Доброкрыл поделился с вами своим сокровищем.''', justify=LEFT)
            win_label.place(relx=0.5, rely=0.1, anchor=CENTER)

            def repeat():
                self.next_image()
                win_label.place_forget()
                self.repeat_button.place_forget()

            self.repeat_button = Button(self, text='Начать заново', command=repeat)
            self.repeat_button.place(relx=0.5, rely=0.9, anchor=CENTER)
            
            
    
    def bad_dragon(self):

        def bad_dragons_chellange():
            def repeat():
                self.next_image()
                riddles_label.place_forget()
                self.repeat_button.place_forget()

            self.repeat_button = Button(self, text='Начать заново', command=repeat)
#--------------------------------------------------------------------------            
            def chek():
                entered_value = self.answer.get()
                if entered_value == 'сахар':
                    riddles_label.config(text='отгадано: 1/3')
                    riddles_label.place(relx=0.1, rely=0.05, anchor=CENTER)
                    self.riddle.config(text='''На раскрашенных страницах.
Много праздников хранится. Это ...''')
                    self.riddle.place(relx=0.6, rely=0.1)
                    self.respond.config(command=chek1)
                    self.answer.delete(0, 'end')
                else:
                    riddles_label.config(text='Тебя сожгли заживо.')
                    riddles_label.place(relx=0.5, rely=0.1, anchor=CENTER)
                    self.answer.place_forget()
                    self.riddle.place_forget()
                    self.respond.place_forget()
                    self.repeat_button.place(relx=0.5, rely=0.9, anchor=CENTER)

#------------------------------------------------------------------------------------
            def chek1():
                
                entered_value1 = self.answer.get()
                if entered_value1 == 'календарь':
                    riddles_label.config(text='отгадано: 2/3')
                    self.riddle.config(text='''"Вечно в пути, но никогда не приходит,
С утра восходит, а вечером гаснет.
Что это такое?"''')
                    self.riddle.place(relx=0.6, rely=0.1)
                    self.respond.config(command=chek2)
                    self.answer.delete(0, 'end')

                else:
                    riddles_label.config(text='Ты был проглочен заживо.')
                    riddles_label.place(relx=0.5, rely=0.1, anchor=CENTER)
                    self.answer.place_forget()
                    self.riddle.place_forget()
                    self.respond.place_forget()
                    self.repeat_button.place(relx=0.5, rely=0.9, anchor=CENTER)


#-------------------------------------------------------------------------------------
            def chek2():
                entered_value2 = self.answer.get()
                if entered_value2 == 'солнце':
                            riddles_label.config(text='Вы отгадали все загадки, в награду, Теневой сделал вас богатым.')
                            riddles_label.place(relx=0.5, rely=0.1, anchor=CENTER)
                            self.answer.place_forget()
                            self.riddle.place_forget()
                            self.respond.place_forget()
                            self.repeat_button.place(relx=0.5, rely=0.9, anchor=CENTER)

                else:
                    riddles_label.config(text='Ты был разорван в клочья, резьеренным драконом.') 
                    riddles_label.place(relx=0.5, rely=0.1, anchor=CENTER)
                    self.answer.place_forget()
                    self.riddle.place_forget()
                    self.respond.place_forget()
                    self.repeat_button.place(relx=0.5, rely=0.9, anchor=CENTER)
#------------------------------------------------------------------------------------

            self.answer = Entry(self)
            self.answer.place(relx=0.5, rely=0.9, anchor=CENTER)
            self.riddle = Label(self, text='''Чистая, но не вода,
белая, но не снег,
сладкая, но не мороженое.
Что это такое?: ''', justify=LEFT, font=('Arial', 10))
            self.riddle.place(relx=0.7, rely=0.1)
            self.respond = Button(self, text='ответить', command=chek)
            self.respond.place(relx=0.65, rely=0.85)
            self.bad_dragons_chellange_button.place_forget()
            riddles_label.place_forget()
            


        new_image_path = 'media/bad_dragon.png'
        self.original_image = Image.open(new_image_path)
        self.image_copy = self.original_image.copy()
        self.background_image = ImageTk.PhotoImage(self.original_image)
        self.background.configure(image=self.background_image)
        self.left_button.place_forget()   #removing left and right button here too
        self.right_button.place_forget()
        riddles_label = Label(self, text='''Ты попал в руки злого дракона.
Он собирается задать тебе 3 загадки, не ответишь на один из них, тебя проглотят.''', justify=LEFT,
font=('Arial', 10))
        riddles_label.place(relx=0.1, rely=0)

        self.bad_dragons_chellange_button = Button(self, text='Начать', command=bad_dragons_chellange)
        self.bad_dragons_chellange_button.place(relx=0.8, rely=0.8)

    


        


if __name__ == "__main__":
    root = Tk()
    root.title("Dragon - EE")
    root.geometry("580x290")
    root.resizable(False, False)

    e = Example(root)
    e.pack(fill=BOTH, expand=YES)

    root.mainloop()
