import tkinter as tk

#FUNCTIONS
fill_var = ""
outline_var = "black"
def draw_square(event):
    global fill_var
    x = event.x
    y = event.y
    canvas.create_rectangle((x, y, x+50, y+50), outline=outline_var, width=2, fill=fill_var)
def draw_circle(event):
    global fill_var
    x = event.x
    y = event.y
    canvas.create_oval((x, y, x+50, y+50), outline=outline_var, width=2, fill=fill_var)
def filler(evet):
    global fill_var
    global outline_var
    fill_var = "black"
    outline_var = fill_var
def unfiller(event):
    global fill_var
    fill_var = ""
def set_red(event):
    global outline_var
    global fill_var
    outline_var = "red"
    fill_var = outline_var
def set_yellow(event):
    global outline_var
    global fill_var
    outline_var = "yellow"
    fill_var = outline_var

#TEMPLATE
main_window = tk.Tk()
main_window.title("Canvas App")
main_window.geometry("500x500")

canvas = tk.Canvas(main_window, bg = 'white')
canvas.pack(fill="both", expand=True)

#BINDING
canvas.bind("<KeyPress-s>", draw_square)
canvas.bind("<KeyPress-c>", draw_circle)
canvas.bind("<KeyPress-f>", unfiller)
canvas.bind("<KeyRelease-F>", filler)
canvas.bind("<KeyPress-r>", set_red)
canvas.bind("<KeyPress-y>", set_yellow)
canvas.focus_set()

main_window.mainloop()