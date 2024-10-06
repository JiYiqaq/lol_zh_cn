import os
import tkinter as tk
from tkinter import messagebox

# 创建主窗口
root = tk.Tk()
root.withdraw()  # 隐藏主窗口
# 定义文件路径
file_path = r'C:\ProgramData\Riot Games\Metadata\league_of_legends.live\league_of_legends.live.product_settings.yaml'

# 确保文件存在
if os.path.exists(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # 替换指定内容
    if 'locale: "ja_JP"' in data:
        data = data.replace('locale: "ja_JP"', 'locale: "zh_CN"')

        # 将修改后的内容写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)

        # 弹出消息框
        messagebox.showinfo("成功", "修改成功！")
        # 关闭窗口
        root.quit()
    else:
        # 弹出消息框
        messagebox.showinfo("错误", "没有找到需要替换的内容！")
        # 关闭窗口
        root.quit()
else:
    # 弹出消息框
    messagebox.showinfo("错误", "文件 {file_path} 不存在，请检查路径是否正确。！")
    # 关闭窗口
    root.quit()
