import tkinter as ui

main_window = ui.Tk()

def event_tekan():
    label2 = ui.Label(main_window,text="aku ditekan")
    label2.pack()

label = ui.Label(main_window,text="halo saya adalah \n GUI sederhana dengan python")
button = ui.Button(main_window,text="tekan aku",command = event_tekan)

label.pack()
button.pack()
main_window.mainloop()