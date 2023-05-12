import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import pandas as pd

class MyGUI:
    def __init__(self, master, filename):
        # 設定 filename 屬性
        self.filename = filename
        
        # 讀CSV檔案
        df = pd.read_csv("purchase_requests.csv", encoding="big5")

        # 創建表格
        self.tree = tk.ttk.Treeview(master, selectmode="browse")
        self.tree["columns"] = list(df.columns)
        self.tree.heading("#0", text="Index")
        for column in df.columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=160)

        # 輸入資料
        for i, row in df.iterrows():
            self.tree.insert("", tk.END, text=str(i), values=list(row))

        # 增加滾輪
        scrollbar = tk.Scrollbar(master, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # 搜尋系統
        self.search_entry = tk.Entry(master)
        search_button = tk.Button(master, text="Search", command=self.search)
        
        # use grid layout to place the widgets
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.search_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        search_button.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        # 更新 Treeview 的按鈕
        
        update_button = tk.Button(master, text="Update Treeview", command=self.update_treeview)

        # configure grid layout
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)
        
        # use grid layout to place the widgets
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.search_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        search_button.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        update_button.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        # configure grid layout
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)

    def search(self):
        # get the search keyword
        keyword = self.search_entry.get()
        if not keyword:
            messagebox.showerror("Error", "Please enter a search keyword.")
            return

        # perform the search and update the treeview
        results = []
        for child in self.tree.get_children():
            values = self.tree.item(child, "values")
            if keyword in values:
                results.append(child)
        self.tree.selection_set(results)
        if not results:
            messagebox.showinfo("Info", "No matching results found.")
    
    def update_treeview(self):
        # 重新讀取 CSV 檔案
        self.df = pd.read_csv(self.filename, encoding="big5")
            
        # 刪除現有的資料
        self.tree.delete(*self.tree.get_children())
            
        # 插入新的資料
        for i, row in self.df.iterrows():
            self.tree.insert("", tk.END, text=str(i), values=list(row))
