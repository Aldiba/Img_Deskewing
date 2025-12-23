# image_cropper/ui/editor_window.py

import os
import cv2
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# 从我们的处理模块中导入核心函数
from image_cropper.processing import straighten_and_crop

class InteractiveProcessorWindow(tk.Toplevel):
    # ... 将原始代码中 InteractiveProcessorWindow 类的所有代码
    # ... 从 "def __init__..." 到 "def on_close..." 全部复制粘贴到这里
    # ... 无需做任何修改，因为导入路径已经正确处理了。
    
    # <--- 在这里粘贴 InteractiveProcessorWindow 类的完整代码 --->
    # 示例 (只显示开头和结尾):
    def __init__(self, parent, file_list, output_dir):
        super().__init__(parent)
        self.title("交互式处理 - 滚轮缩放 | 右键拖拽 | 左键取色")
        # ... (类的所有其他代码) ...

    def on_close(self):
        if messagebox.askyesno("确认", "您确定要中断处理吗？", parent=self):
            self.destroy()