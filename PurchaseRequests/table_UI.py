import tkinter as tk
import tkinter.messagebox as messagebox
import pandas as pd
import tkinter.ttk as ttk
import webbrowser

#設置一個Class做出資料庫的美化介面，他到底能夠為我帶來怎麼樣的美化呢，反正一定很陽春 
class MyGUI:
    def __init__(self, master, filename):
        # 設定 filename 屬性
        self.filename = filename
        
        # 讀CSV檔案
        df = pd.read_csv("purchase_requests.csv", encoding="big5")

        # 設置表格列的樣式
        style = tk.ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#D5E5F5", foreground="black", rowheight=25, fieldbackground="#D5E5F5")
        style.map("Treeview", background=[("alternate", "#EBF5EE"), ("", "white")])


        # 創建表格
        self.tree = tk.ttk.Treeview(master, selectmode="browse")
        self.tree["columns"] = list(df.columns)
        self.tree.heading("#0", text="Index")
        for column in df.columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=160, minwidth=100, stretch=True)


        # 新增連結到Google的按鈕
        google_button = tk.Button(master, text="Google", command=self.open_google)
        google_button.grid(row=0, column=2, padx=5, pady=5)

        # 新增連結到欣雅的按鈕
        sinya_button = tk.Button(master, text="sinya", command=self.open_sinya)
        sinya_button.grid(row=0, column=3, padx=5, pady=5)
 
        # 新增連結到PCH的按鈕
        PH_button = tk.Button(master, text="PCHome", command=self.open_pchome)
        PH_button.grid(row=0, column=4, padx=5, pady=5)


        # 輸入資料
        for i, row in df.iterrows():
            self.tree.insert("", tk.END, text=str(i), values=list(row))

        # 增加滾輪
        scrollbar = tk.Scrollbar(master, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # 搜尋系統
        self.search_entry = tk.Entry(master)
        search_button = tk.Button(master, text="搜尋 Search", command=self.search)
        
        # use grid layout to place the widgets
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.search_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        search_button.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        # 更新 Treeview 的按鈕
        
        update_button = tk.Button(master, text="更新狀態 Update Treeview", command=self.update_treeview)

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
    
    
    def open_google(self):
        webbrowser.open("https://www.google.com")

    def open_sinya(self):
        webbrowser.open("https://www.sinya.com.tw/")

    def open_pchome(self):
        webbrowser.open("https://24h.pchome.com.tw/")

    def search(self):
        # get the search keyword
        keyword = self.search_entry.get()
        if not keyword:
            messagebox.showerror("錯誤 Error", "請輸入關鍵字 Please enter a search keyword.")
            return

        # perform the search and update the treeview
        results = []
        for child in self.tree.get_children():
            values = self.tree.item(child, "values")
            if keyword in values:
                results.append(child)
        self.tree.selection_set(results)
        if not results:
            messagebox.showinfo("訊息 Info", "找不到符合的結果 No matching results found.")
    
    def update_treeview(self):
        # 重新讀取 CSV 檔案
        self.df = pd.read_csv(self.filename, encoding="big5")
            
        # 刪除現有的資料
        self.tree.delete(*self.tree.get_children())
            
        # 插入新的資料
        for i, row in self.df.iterrows():
            self.tree.insert("", tk.END, text=str(i), values=list(row))
