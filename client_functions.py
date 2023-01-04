import tkinter


def animate_gif(surface, path):
    # adapted code from https://stackoverflow.com/questions/28518072/play-animations-in-gif-with-tkinter
    frames_count = 36
    frames = [tkinter.PhotoImage(file=path, format='gif -index %i' % i) for i in range(frames_count)]

    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frames_count:
            ind = 0
        gif.configure(image=frame)
        surface.after(100, update, ind)

    gif = tkinter.Label(surface)
    gif.pack()
    surface.after(0, update, 0)
