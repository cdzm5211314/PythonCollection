# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-29 13:36

# tesseract下载地址: https://digi.bib.uni-mannheim.de/tesseract/
# 语言包下载地址: https://github.com/tesseract-ocr/tessdata/find/master

# 安装tesseract: windows
# 1. 设置path环境变量[安装路径]: path: E:\InstallationOther\Tesseract-OCR
# 2. 创建新的环境变量[安装路径下]: TESSDATA_PREFIX: E:\InstallationOther\Tesseract-OCR\tessdata

# windows终端命令识别图片:
# tesseract imagename[目标图片文件名,需加格式后缀] outputfile[是转换结果文件名]
# 如: tesseract aaaimg.png bbbfile
# 如: tesseract aaaimg.png bbbfile -l chi_sim[指定识别语言-中文,默认是英文]

### Python代码中使用tesseract识别图形验证码
# 安装pytesseract: pip install pytesseract
# 如果没有PIL模块,需要安装: pip install PIL

import pytesseract
from PIL import Image

# 指定tesseract.exe的安装路径的所在位置
pytesseract.pytesseract.tesseract_cmd = r"E:\InstallationOther\Tesseract-OCR\tesseract.exe"
# 打开需要识别的图片
image = Image.open("aaa.png")
# 将图片中的内容转换为文字信息
text = pytesseract.image_to_string(image)                 # 默认识别英文
# text = pytesseract.image_to_string(image,lang="chi_sim")  # 设置识别中文
print(text)  # 识别图片中的内容


