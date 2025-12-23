# image_cropper/ui/main_window.py

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

# 使用相对导入，从同一目录下的 editor_window.py 导入类
from .editor_window import InteractiveProcessorWindow

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图片批处理工具 - V5.0 专业面板")
        self.root.geometry("600x200")
        
        self.input_folder = tk.StringVar()
        self.output_folder = tk.StringVar()
        
        frame = ttk.Frame(root, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        style = ttk.Style()
        style.configure("TButton", font=("微软雅黑", 10))
        style.configure("TLabel", font=("微软雅黑", 10))
        
        grid_opts = {'padx': 5, 'pady': 10, 'sticky': tk.EW}
        
        ttk.Label(frame, text="输入文件夹:").grid(row=0, column=0, **grid_opts)
        ttk.Entry(frame, textvariable=self.input_folder, width=50).grid(row=0, column=1, **grid_opts)
        ttk.Button(frame, text="浏览...", command=self.browse_input).grid(row=0, column=2, **grid_opts)
        
        ttk.Label(frame, text="输出文件夹:").grid(row=1, column=0, **grid_opts)
        ttk.Entry(frame, textvariable=self.output_folder, width=50).grid(row=1, column=1, **grid_opts)
        ttk.Button(frame, text="浏览...", command=self.browse_output).grid(row=1, column=2, **grid_opts)
        
        start_btn = ttk.Button(frame, text="▶ 开始处理", command=self.start_processing)
        start_btn.grid(row=2, column=1, pady=20, ipadx=20, ipady=5)
        
        frame.columnconfigure(1, weight=1)
        
    def browse_input(self):
        folder = filedialog.askdirectory()
        if folder: self.input_folder.set(folder)

    def browse_output(self):
        folder = filedialog.askdirectory()
        if folder: self.output_folder.set(folder)

    def start_processing(self):
        input_dir, output_dir = self.input_folder.get(), self.output_folder.get()
        if not input_dir or not output_dir:
            messagebox.showerror("错误", "请选择文件夹。")
            return
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) 
                 if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff'))]
        
        if not files:
            messagebox.showinfo("提示", "没有找到图片文件。")
            return
            
        InteractiveProcessorWindow(self.root, files, output_dir)