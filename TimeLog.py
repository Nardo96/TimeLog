# -*- coding: utf-8 -*-

from datetime import datetime
import tkinter as tk

class TimeLog(): 
    """A data structure to log the time of sessions of anything. Contains
    lists of start and end times. Another list takes times of counter presses.
    Exports data to text."""
    
    def __init__(self): 
        #Initialize some lists to contain datetime objects, as well as 
        #corresponding cleaned lists for cleaned string representations
        self.start_time = []
        self.end_time = []
        self.counter = []
        
        self.cleaned_start_time = []
        self.cleaned_end_time = []
        self.cleaned_counter = []
    

    
    #Functions to append formatted times to initialized lists
    def add_start_time(self):
        """Append current time in datetime and in cleaned string to start time
        lists."""
        current_time = datetime.now()
        self.start_time.append(current_time)
        self.cleaned_start_time.append(current_time.strftime("%I:%M:%S %p"))
        
    def add_end_time(self):
        """Append current time in datetime and in cleaned string to end time
        lists."""
        current_time = datetime.now()
        self.end_time.append(current_time)
        self.cleaned_end_time.append(current_time.strftime("%I:%M:%S %p"))
        
    def add_counter(self):
        """Append current time in datetime and in cleaned string to counter
        lists."""
        current_time = datetime.now()
        self.counter.append(current_time)
        self.cleaned_counter.append(current_time.strftime("%I:%M:%S %p"))
        
    #Getter functions, returning most recently appended item in each clean list
    def get_current_start_time(self):
        """Return most recently appended start time."""
        return self.cleaned_start_time[len(self.cleaned_start_time)-1]
    
    def get_current_end_time(self):
        """Return most recently appended end time."""
        return self.cleaned_end_time[len(self.cleaned_end_time)-1]
    
    def get_current_counter(self):
        """Return most recently appended counter."""
        return self.cleaned_counter[len(self.cleaned_counter)-1]

    #Export all TimeLog data to labelled text.
    def export_data(self, filename):
        """Write all object data to file."""
        with open(filename, "a") as f:
            for t in self.start_time:
                print("1_", t, file=f, sep="")
            for t in self.end_time:
                print("2_", t, file=f, sep="")
            for t in self.counter:
                print("3_", t, file=f, sep="")
    
    #Export individual recent TimeLog attributes to labelled text.
    def export_current_start_time(self, filename):
        """Write most recent start time to file."""
        with open(filename, "a") as f:
            print("1_", self.start_time[len(self.start_time)-1], file=f,sep="")
                        
    def export_current_end_time(self, filename):
        """Write most recent end time to file."""
        with open(filename, "a") as f:
            print("2_", self.end_time[len(self.end_time)-1], file=f, sep="")
                
    def export_current_counter(self, filename):
        """Write most recent counter to file."""
        with open(filename, "a") as f:
            print("3_", self.counter[len(self.counter)-1], file=f, sep="")
    
    
    #import TimeLog object 
    def import_data(self, filename):
        """Take labelled data from file and add to TimeLog lists."""
        with open(filename, "r") as f:
            for line in f:
                if line[0:2] == "1_":
                    t = datetime.strptime(line[2:len(line)-1], 
                                          "%Y-%m-%d %H:%M:%S.%f")
                    self.start_time.append(t)
                    self.cleaned_start_time.append(t.strftime("%I:%M:%S %p"))      
                if line[0:2] == "2_":
                    t = datetime.strptime(line[2:len(line)-1], 
                                          "%Y-%m-%d %H:%M:%S.%f")
                    self.end_time.append(t)
                    self.cleaned_end_time.append(t.strftime("%I:%M:%S %p"))
                if line[0:2] == "3_":
                    t = datetime.strptime(line[2:len(line)-1], 
                                          "%Y-%m-%d %H:%M:%S.%f")
                    self.counter.append(t)
                    self.cleaned_counter.append(t.strftime("%I:%M:%S %p"))
                    
    #Establish time ranges; assumes no error in data and hence everything is 
    #positionally aligned. Returns list of ranges
    def make_ranges(self):
        """Makes time ranges from start and ends times and returns a list of 
        strings."""
        ranges=[]
        for i in range(len(self.cleaned_start_time)):
            ranges.append(self.cleaned_start_time[i]+"-"
                          +self.cleaned_end_time[i])      
        return ranges
    
    #Calibrate counter to time range - group counters by time range, returns
    #a dictionary with key 'time range' and value 'list of counters'
    def assign_counter(self):
        """Return a dict where keys are time ranges and values are counter 
        times that fit inside that time range."""
        
        #Initialize dictionary, create time ranges, and assign empty lists as 
        #values to each time range key
        range_dict = {}
        ranges = self.make_ranges()
        for tframe in ranges:
            range_dict[tframe] = []
        #For every counter entry, check which time frame it's in, then 
        #append the dictionary
        for i in range(len(self.counter)):
            for t in range(len(ranges)):
                if self.counter[i] > self.start_time[t]:
                    if self.counter[i] <= self.end_time[t]:
                        range_dict[ranges[t]].append(self.cleaned_counter[i])
                        break
        return range_dict


class TimeLogGui(tk.Frame):
    """GUI implementation of TimeLog object. Includes buttons to add start
    times, end times, and counters. Buttons export times when called."""
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.start_time_message_var = tk.StringVar()
        self.start_time_message_var.set("-")
        self.end_time_message_var = tk.StringVar()
        self.end_time_message_var.set("-")
        self.counter_message_var = tk.StringVar()
        self.counter_message_var.set("-")
        self.counters = ''
        self.create_widgets()
        self.time_log = TimeLog()

        
        

    def create_widgets(self):
        """Set up buttons and messages on GUI."""
        self.start_button = tk.Button(self)
        self.start_button["text"] = "Start Timer"
        self.start_button["command"] = self.start
        self.start_button.pack(side="top")

        self.start_message = tk.Message(self, textvariable=self.
                                        start_time_message_var)
        self.start_message.pack(side="top")

        self.end_button = tk.Button(self, text="End Timer", command=self.end)
        self.end_button.pack(side="top")
        
        self.end_message = tk.Message(self, textvariable=self.
                                      end_time_message_var)
        self.end_message.pack(side="top")

        self.counter_button = tk.Button(self, text="Add counter", 
                                        command=self.add_counter)
        self.counter_button.pack()
        
        self.counter_message = tk.Message(self, textvariable=self
                                          .counter_message_var)
        self.counter_message.pack()
        
        self.quit = tk.Button(self, text="QUIT", fg="red", 
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def start(self):
        """Add current start time to self TimeLog object, update GUI message, 
        and export start time to file"""
        self.time_log.add_start_time()
        self.start_time_message_var.set(self.time_log.get_current_start_time())
        self.time_log.export_current_start_time("loggerexample.txt")
        

    def end(self):
        """Add current end time to self TimeLog object, update GUI message,
        and export end time to file"""
        self.time_log.add_end_time()
        self.end_time_message_var.set(self.time_log.get_current_end_time())
        self.time_log.export_current_end_time("loggerexample.txt")
        
    def add_counter(self):
        """Add current counter to self TimeLog object, update GUI message, 
        and export counter to file."""
        self.time_log.add_counter()
        
        #Set counter message text to only list counters within the current
        #time frame.
        if len(self.time_log.end_time) > 0:
            if self.time_log.counter[len(self.time_log.counter)-1] > \
                self.time_log.end_time[len(self.time_log.end_time)-1]: 
                self.counters = ''
        self.counters += self.time_log.get_current_counter() + "\n"
        self.counter_message_var.set(self.counters)
        self.time_log.export_current_counter("loggerexample.txt")
       
    
       
       
       
            

root = tk.Tk()
app = TimeLogGui(master=root)
app.mainloop()

                    
    
# #Tests - makes a logger object, adds a start time, adds two counters, and 
# # adds end time. Exports data. 

# logger = TimeLog()
# logger.add_start_time()
# time.sleep(2)
# logger.add_counter()
# time.sleep(7)
# logger.add_counter()
# logger.add_end_time()
# print(logger.get_current_counter())
# print(logger.get_current_start_time())
# print(logger.get_current_end_time())
# logger.export_data("loggerexample.txt")

# #Tests - make logger object, import from exported data
# importexample = TimeLog()
# importexample.import_data("loggerexample.txt")

# #Tests - prints time ranges
# print(importexample.make_ranges())
# print(logger.assign_counter())
# print(importexample.assign_counter())