# main.py

from ttkthemes import ThemedTk
from image_cropper.ui.main_window import MainApp

if __name__ == "__main__":
    # arc 主题
    root = ThemedTk(theme="arc")
    
    # 实例化主应用类
    app = MainApp(root)
    
    # 进入Tkinter事件循环
    root.mainloop()