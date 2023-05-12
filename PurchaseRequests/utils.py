import tkinter as tk

class Utils():
    @staticmethod
    def show_entry(selected_item, item_selected):
        if selected_item == "其他 Other":
            entry_window = tk.Toplevel()
            entry_window.resizable(False, False)
            entry_label = tk.Label(entry_window, text="請輸入物品名稱")
            entry_label.pack()
            entry_input = tk.Entry(entry_window)
            entry_input.pack()
            entry_button = tk.Button(entry_window, text="確定", command=lambda: Utils.on_entry_submit(entry_window, entry_input, item_selected))
            entry_button.pack()

    @staticmethod
    def on_entry_submit(entry_window, entry_input, item_selected):
        entered_item = entry_input.get()
        item_selected.set(entered_item)
        entry_window.destroy()
