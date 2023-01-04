import tkinter
import client_sockets
import client_functions


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
        # self.gui.iconbitmap("./assets/frorum_icon.ico") (not available for now)
        self.gui.configure(bg=self.background_color)
        # load the textual headers images
        self.text_header_first_state = tkinter.PhotoImage(file=r"./assets/connect_page/header_label_first_state.png")
        self.text_header_second_state = tkinter.PhotoImage(file=r"./assets/connect_page/header_label_second_state.png")
        # the third ( not available for now )
        # load the button images
        self.connect_button_first_state = tkinter.PhotoImage(file=r"./assets/connect_page/connect_button_first_state.png")
        self.connect_button_second_state = tkinter.PhotoImage(file=r"./assets/connect_page/connect_button_second_state.png")
        # shadow of the button :
        # self.connect_button_shadow = tkinter.PhotoImage(file=r'./assets/connect_page/connect_button_shadow.png')
        # create the header and display it ( the image is preset to the first state cause else and i don't know why it is not displayed
        self.text_header_label = tkinter.Label(self.gui, bg=self.background_color, image=self.text_header_first_state)
        # same but for connect/retry button
        self.connect_button = tkinter.Button(self.gui, bg=self.background_color, borderwidth=0, relief=tkinter.FLAT, activebackground=self.background_color, command=self.ping_server)

    def first_state(self):
        # reconfig the widgets to display the right things
        self.connect_button.configure(image=self.text_header_first_state)
        self.text_header_label.place(x=105, y=50)
        self.connect_button.configure(image=self.connect_button_first_state)
        self.connect_button.place(x=261, y=261)
    
    def second_state(self):
        self.text_header_label.configure(image=self.text_header_second_state)
        self.connect_button.configure(image=self.connect_button_second_state)

    def third_state(self):
        pass
        
    def ping_server(self):
        client_functions.animate_gif(surface=self.gui, path="./assets/connect_page/processing_gif.gif")
        self.server_connection = client_sockets.ping()
        if self.server_connection:
            self.third_state()
        else:
            self.second_state()
