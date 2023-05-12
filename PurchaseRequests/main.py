import tkinter as tk
from purchase_gui import PurchaseGUI
from table_UI import MyGUI


#呼喊用的主程式

# 創建第一個視窗
root1 = tk.Tk()
purchase_gui = PurchaseGUI(master=root1)

# 創建第二個視窗
root2 = tk.Tk()
app = MyGUI(master=root2, filename="purchase_requests.csv")

# 兩個視窗分別叫出來
root1.mainloop()
root2.mainloop()
