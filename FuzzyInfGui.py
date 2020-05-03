from Tkinter import *
import ttk
import exitHandler
from FuzzyControlTest import runSimulation
import tkMessageBox
#from Tkinter import messagebox


class FuzzyInfGui:
    def __init__(self):

        self.root = None
        self.hInput = None
        self.cInput = None
        self.wInput = None
        self.pInput = None
        self.tInput = None
        self.result = None
        self.resultLabel = None

    def setup(self):
        #Sets up root window
        
        self.root = Tk()
        self.root.wm_title("Fuzzy Weather Prediction")
        self.root.geometry("320x300") #Main window size
        self.root.resizable(False, False)
        
        #Exit handler to manually close program
        exitHandler.mainWin = self.root

        #Sets frame to fill root window.
        #All widgets will be in this frame
        self.frame = ttk.LabelFrame(self.root, text="Inputs")
        self.frame.grid(column=0, row=3, padx=10, pady=20)
        self.frameSetup()

    def frameSetup (self):
        #Labels
        humidity = ttk.Label(self.frame, text="Humidity (0 to 100)").grid(column=0, row=0)
        self.hInput = Spinbox(self.frame, from_= 0, to = 100, width = 5)
        self.hInput.grid(column=2, row=0)

        ttk.Label(self.frame, text="          ").grid(column = 0, row = 1) #For formatting on GUI because lazy


        totalCloud = ttk.Label(self.frame, text="Cloud Cover (0 to 8)").grid(column=0, row=2)
        self.cInput = Spinbox(self.frame, from_= 0, to = 8, width = 5)
        self.cInput.grid(column=2, row=2)

        ttk.Label(self.frame, text="          ").grid(column = 0, row = 3)
   
        windDirec = ttk.Label(self.frame, text="Wind Direction (0 to 360)").grid(column=0, row=4)
        self.wInput = Spinbox(self.frame, from_ = 0, to = 360, width = 5)
        self.wInput.grid(column=2, row=4)

        ttk.Label(self.frame, text="          ").grid(column = 0, row = 5)
        
        pressure = ttk.Label(self.frame, text="Pressure (995 to 1030)").grid(column=0, row=6)
        self.pInput = Spinbox(self.frame, from_ = 995, to = 1030, width = 5)
        self.pInput.grid(column=2, row=6)

        ttk.Label(self.frame, text="          ").grid(column = 0, row = 7)
        
        temp = ttk.Label(self.frame, text="Temperature (-5 to 40)").grid(column=0, row=8)
        self.tInput = Spinbox(self.frame, from_ = -5, to = 40, width = 5)
        self.tInput.grid(column=2, row=8)

        ttk.Label(self.frame, text="          ").grid(column = 0, row = 9)
        
        ttk.Label(self.root, text="Chance of Precipitation:").grid(column = 0, row = 6)
        self.resultLabel = ttk.Label(self.root, text="")
        self.resultLabel.grid(column = 2, row = 6)
        

        runData = ttk.Button(self.frame, text="Run!", command = self.RunData).grid( column = 1, row = 10) #command

    def RunData(self):
        try:
            self.result = runSimulation(int(self.hInput.get()), int(self.cInput.get()),
            int(self.wInput.get()), int(self.pInput.get()), int(self.tInput.get()))
            fgcolor = "black"
            if(int(self.result) < 33):
                fgcolor = "green"
            elif(int(self.result) > 33 & int(self.result) < 66):
                fgcolor = "orange"
            else:
                fgcolor = "red"
        
            self.resultLabel.config(text=format(self.result, '.2f'),foreground=fgcolor)
        except:
            tkMessageBox.showinfo("No Crips Value", "ValueError: Crisp output cannot be calculated,"+
                                  " likely because the system is too sparse. Check to make sure this"+
                                  " set of input values will activate at least one connected Term in each"+
                                  " Antecedent via the current set of Rules.")
            
        
    def start(self):
        self.setup()
        self.root.mainloop() #start monitoring and updating the GUI
