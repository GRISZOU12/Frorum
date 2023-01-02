import tkinter

class Launcher:
    def __init__(self):
        self.background_color = "#A99F96"
        self.create_gui()
        self.first_state()
        self.gui.mainloop()

    def create_gui(self):
        self.gui = tkinter.Tk()
        self.gui.geometry("700x350")
        self.gui.title("Frorum | Launcher")
        self.gui.configure(bg=self.background_color)
        # load the textual headers
        self.text_header_first_state = tkinter.PhotoImage(file=r"./assets/connect_page/header_label_first_state.png")
        self.text_header_second_state = tkinter.PhotoImage(file=r"./assets/connect_page/header_label_second_state.png")
        # the third ( not available for now )
        self.connect_button_first_state = tkinter.PhotoImage(file=r"./assets/connect_page/connect_button_first_state.png")
        self.connect_button_second_state = tkinter.PhotoImage(file=r"./assets/connect_page/connect_button_second_state.png")
        # third is an empty image

    def first_state(self):
        self.text_header_first_state_label = tkinter.Label(self.gui, image=self.text_header_first_state, bg=self.background_color)
        self.text_header_first_state_label.place(x=105, y=50)

        self.connect_button_first_state_button = tkinter.Button(self.gui, image=self.connect_button_first_state, bg=self.background_color, borderwidth=0, relief=tkinter.FLAT, activebackground=self.background_color)
        self.connect_button_first_state_button.place(x=261, y=261)

    def load_processing_gif(self):
        # code from https://stackoverflow.com/questions/28518072/play-animations-in-gif-with-tkinter
        frames_count = 36
        frames = [tkinter.PhotoImage(file=r'./assets/connect_page/processing_gif.gif', format='gif -index %i' % i) for i in range(frames_count)]

        def update(ind):
            frame = frames[ind]
            ind += 1
            if ind == frames_count:
                ind = 0
            processing_gif.configure(image=frame)
            self.gui.after(100, update, ind)

        processing_gif = tkinter.Label(self.gui, bg=self.background_color)
        processing_gif.pack()
        self.gui.after(0, update, 0)

