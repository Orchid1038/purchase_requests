import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"], "include_files": ["purchase_requests.csv"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="採購系統",
    version="1.0",
    description="用來記錄採購項目",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base),
                 Executable("dbgui.py"),
                 Executable("purchase_gui.py"),
                 Executable("purchase_request.py"),
                 Executable("utils.py")]
)