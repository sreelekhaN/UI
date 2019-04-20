from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pandas as pd

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)
digits = pd.read_csv(filename,skiprows=[0],header=None)
