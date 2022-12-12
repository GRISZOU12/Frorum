import tkinter
import client_sockets

grey = "#353535"


class Gui:
    def __init__(self):
        # create the window
        self.connection_gui = tkinter.Tk()
        self.connection_gui.title("Chat")
        self.connection_gui.iconbitmap("./assets/icons/main_icon.ico")
        self.connection_gui.geometry("700x350")
        self.connection_gui.resizable(width=False, height=False)
        self.connection_gui.configure(bg=grey)
        self.connect_page()
        self.connection_gui.mainloop()

    def connect_page(self):
        self.header_label_text = tkinter.StringVar()
        self.header_label_text.set("Please connect before speaking into chat")
        self.header_label = tkinter.Label(self.connection_gui, textvariable=self.header_label_text, font=("Quicksand", 16, "bold"), bg=grey, fg="white")
        self.header_label.place(x=150, y=50)

        self.connect_button_icon = tkinter.PhotoImage(file=r'./assets/icons/connect_button_icon.png')
        self.connect_button = tkinter.Button(self.connection_gui, image=self.connect_button_icon, borderwidth=0, bg=grey, command=self.ping)
        self.connect_button.place(x=200, y=250)

    def ping(self):
        ping_label_text = tkinter.StringVar()
        ping_label_text.set("Please Wait, we are trying connecting you...")
        ping_label = tkinter.Label(self.connection_gui, textvariable=ping_label_text, font=("Quicksand", 12, "bold"), bg="grey", fg="white")
        ping_label.place(x=180, y=150)
        self.connect_button_icon = tkinter.PhotoImage(file=r'./assets/icons/grey.png')
        if client_sockets.ping():
            self.connect_button_icon_error_corrected = tkinter.PhotoImage(file=r'./assets/icons/grey.png')
            self.connect_button.configure(image=self.connect_button_icon_error_corrected)
            ping_label.configure(fg="green", bg="white")
            ping_label_text.set("Server is connected please enter your informations.")
            ping_label.place_configure(x=160)
        else:
            ping_label.configure(fg="red", bg="white")
            ping_label_text.set("An error occurred maybe server is disconnected.")
            self.connect_button_icon_error = tkinter.PhotoImage(file=r'./assets/icons/connect_retry_button.png')
            self.connect_button.configure(image=self.connect_button_icon_error)


gui = Gui()
