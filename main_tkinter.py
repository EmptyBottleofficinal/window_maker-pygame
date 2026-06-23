#is dry "main.pygame.py" is way better
import tkinter
try:
    title=input("title:")
    win=input("window:")
    tk = tkinter.Tk()
    tk.geometry("win")
    tk.title(title)
    tkinter.mainloop()
except:
    print("error")