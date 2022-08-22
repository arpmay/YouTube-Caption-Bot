import tkinter as tk
from tkinter import ttk
from compute_frequency import calc
from tkinter.scrolledtext import ScrolledText


def create_root():
    # root window
    root = tk.Tk()
    root.geometry('500x300')
    root.title('Youtube Caption Bot')
    root.resizable(0, 0)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.configure(background='white')

    # Name title label
    title_label = ttk.Label(root, text = 'YouTube Caption Bot', padding=10, background='white', font='Helvetica')
    title_label.grid(column=0, row=0, sticky = tk.N, columnspan=2)

    # channel input window
    channel_label = ttk.Label(root, text="Channel link :", background='white')
    channel_label.grid(column=0, row=1, sticky=tk.E, pady=2.5)

    channel = tk.StringVar()
    channel_entry = ttk.Entry(root, textvariable=channel, background='white', width=40)
    channel_entry.grid(column=1, row=1, padx=10, pady=2.5)

    # Number of videos input window
    nvideos_label = ttk.Label(root, text="No. of videos to scan :", background='white')
    nvideos_label.grid(column=0, row=2, sticky=tk.E, pady=2.5)

    nvideos = tk.StringVar()
    nvideos_entry = ttk.Entry(root, textvariable=nvideos, background='white', width=40)
    nvideos_entry.grid(column=1, row=2, padx=5)

    # Number of results input window
    nres_label = ttk.Label(root, text="No. of results :", background='white')
    nres_label.grid(column=0, row=3, sticky=tk.E)

    nres = tk.StringVar()
    nres_entry = ttk.Entry(root, textvariable=nres, background='white', width=40)
    nres_entry.grid(column=1, row=3, padx=5, pady=2.5)

    # result box
    result_box = ScrolledText(root, height=6)
    result_box.grid(column=0, row=6, columnspan=2, padx = 10, pady = 10, sticky=tk.EW)

    # calculate button
    start_btn = ttk.Button(root, text='Start', command=lambda: calc(result_box, channel.get(), nvideos.get(), nres.get()))
    start_btn.grid(column=0, row=5, columnspan=2, sticky=tk.N, pady=10)

    root.bind('<Return>', lambda: calc(result_box, channel.get(), nvideos.get(), nres.get()))

    return root