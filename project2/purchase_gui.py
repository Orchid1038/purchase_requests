import csv
import tkinter as tk
from tkinter import messagebox
from purchase_request import PurchaseRequest
from utils import Utils

class PurchaseGUI:
    def submit_request_wrapper(self):
        submit_request(self)

    def __init__(self, master):
        
        self.utils = Utils()
        # 將新的採購請求添加到系統中
        with open('purchase_requests.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:  # 如果檔案是空的，寫入表頭
                writer.writerow(['申請人 applicant','部門 Department', '購買物品 Item', '單項費用 Unit_price', '數量 Quantity', '用途 Purpose', '品項名稱Product Item Detailed Name'])
        
        self.master = master
        master.title("Purchase Request System")

        # 申請人
        self.name_label = tk.Label(master, text="申請人 applicant")
        self.name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)

        # 部門
        self.department_label = tk.Label(master, text="部門 Department")
        self.department_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.department_entry = tk.Entry(master)
        self.department_entry.grid(row=2, column=1, padx=10, pady=10)
        

        # 需購買物品
        self.item_label = tk.Label(master, text="需購買物品 item")
        self.item_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.item_selected = tk.StringVar(master)
        self.item_selected.set("耳麥 Headset")
        self.item_menu = tk.OptionMenu(master, self.item_selected,
                                    "軟體授權 Software License",
                                    "印表機耗材 Printer Supplies",
                                    "網路設備 Network Equipment",
                                    "耳麥 Headset",
                                    "滑鼠 Mouse",
                                    "桌電 Desktop Computer",
                                    "鍵盤 Keyboard",
                                    "線材 Cable",
                                    "集線器 Hub",
                                    "其他 Other",
                                    command=lambda x: Utils.show_entry(x, self.item_selected))
        self.item_menu.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # 單項費用
        self.unit_price_label = tk.Label(master, text="單項費用 Unit Price")
        self.unit_price_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.unit_price_entry = tk.Entry(master)
        self.unit_price_entry.grid(row=4, column=1, padx=10, pady=10)

        # 數量
        self.quantity_label = tk.Label(master, text="數量 Quantity")
        self.quantity_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.grid(row=5, column=1, padx=10, pady=10)

        # 用途
        self.purpose_label = tk.Label(master, text="用途 Purpose")
        self.purpose_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.purpose_entry = tk.Entry(master)
        self.purpose_entry.grid(row=6, column=1, padx=10, pady=10)

        # 備註
        self.note_label = tk.Label(master, text="品項詳細名稱"+"\n"+"Product Item Detailed Name")
        self.note_label.grid(row=7, column=1, padx=10, pady=10, sticky="nw")
        self.note_entry = tk.Text(master, height=5, width=30)
        self.note_entry.grid(row=7, column=2, padx=10, pady=10)

        self.submit_button = tk.Button(master, text="提交 Submit", command=self.submit_request_wrapper)
        self.submit_button.grid(row=10, column=1, padx=10, pady=10)

def submit_request(self):
    global main_db  # 声明 main_db 是全局变量
    name = self.name_entry.get()
    department = self.department_entry.get()
    item = self.item_selected.get()
    unit_price = self.unit_price_entry.get()
    quantity = self.quantity_entry.get()
    purpose = self.purpose_entry.get()
    note = self.note_entry.get("1.0", "end-1c")  # 從 Text widget 中取得文字時要去掉換行符號

    # 驗證輸入資料
    if not all((name, department, item, quantity, purpose)):
        messagebox.showerror("錯誤 Error", "請填寫所有欄位 Please fill in all fields.")
        return

    try:
        quantity = int(quantity)
        if quantity <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("錯誤 Error", "請輸入正確的數量 Please enter a valid quantity.")
        return
    
    try:
        unit_price = float(unit_price)
        if unit_price <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("錯誤 Error", "請輸入正確的費用 Please enter a valid unit_price.")
        return

    # 將新的採購請求添加到系統中
    with open('purchase_requests.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, department, item, unit_price, quantity, purpose, note])
    
    messagebox.showinfo("提示 Information", "已成功提交採購請求 Your purchase request has been submitted successfully.")
    self.name_entry.delete(0, tk.END)
    self.department_entry.delete(0, tk.END)
    self.item_selected.set('')
    self.unit_price_entry.delete(0, tk.END)
    self.quantity_entry.delete(0, tk.END)
    self.purpose_entry.delete(0, tk.END)
    self.note_entry.delete('1.0', tk.END)
