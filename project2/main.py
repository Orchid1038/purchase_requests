import tkinter as tk
from tkinter import ttk
from purchase_gui import PurchaseGUI
from dbgui import MyGUI
import pandas as pd

# add ttk style to support cellstyle option in treeview

# create the first window
root1 = tk.Tk()
purchase_gui = PurchaseGUI(master=root1)

# create the second window
root2 = tk.Tk()
app = MyGUI(master=root2, filename="purchase_requests.csv")

# start the mainloop for both windows
root1.mainloop()
root2.mainloop()
