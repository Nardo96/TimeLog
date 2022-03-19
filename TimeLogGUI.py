# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 15:11:23 2022

@author: Bernardo
"""
import timelog
import tkinter as tk


class TimeLogGui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        with open("C:/Users/Bernardo/Documents/Productive/Python/Slogger/SessionCounter.txt", "r") as SessionCounter:
            self.session = int(SessionCounter.read())
        self.start_time = tk.StringVar()
        self.start_time.set("-")
        self.end_time = tk.StringVar()
        self.end_time.set("-")
        self.counters = tk.StringVar()
        self.counters.set("-")
        self.create_widgets()
        self.time_log = timelog()
        self.time_log.import_data("loggerexample.txt")
        
        

    def create_widgets(self):
        self.start_button = tk.Button(self)
        self.start_button["text"] = "Start Timer"
        self.start_button["command"] = self.start
        self.start_button.pack(side="top")

        self.start_message = tk.Message(self, textvariable=self.start_time)
        self.start_message.pack(side="top")

        self.end_button = tk.Button(self, text="End Timer", command=self.end)
        self.endbutton.pack(side="top")
        
        self.end_message = tk.Message(self, textvariable=self.end_time)
        self.end_message.pack(side="top")

        self.counter_button = tk.Button(self, text="Add counter", command=self.add_counter)
        self.counter_button.pack()
        
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def start(self):
        self.time_log.add_start_time()
        self.start_time.set(self.time_log.get_current_start_time())
        

    def end(self):
        self.time_log.add_end_time()
        self.end_time.set(self.time_log.get_current_end_time())
    def add_counter(self):
       self.time_log.add_counter()
       range_dict = self.time_log.assign_counter()
       time_frame = self.time_log.cleaned_start_time[
           len(self.time_log.cleaned_start_time)-1] +"-" 
       + self.time_log.cleaned_end_time[len(self.time_log.cleaned_end_time)-1]
       message = ''
       for counter in range_dict[time_frame]:
           message += counter +"\n"
       
       
       
            

root = tk.Tk()
app = TimeLogGui(master=root)
app.mainloop()
