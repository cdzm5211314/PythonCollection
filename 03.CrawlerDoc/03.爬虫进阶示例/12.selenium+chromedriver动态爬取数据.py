# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-29 9:28

# 获取Ajax数据的方式:
# 1. 直接分析Ajax调用的接口,然后通过代码请求这个接口
# 2. 使用selenium+chromedriver模拟浏览器行为获取数据

# selenium的安装: pip install selenium (selenium.v3.141.0)
# chromedriver的下载[Chrome]: http://chromedriver.storage.googleapis.com/index.html
# 注: chromedriver.exe直接放在一个没有权限的纯英文目录下(Chrome.v68 - chromedriver.v2.41)

from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By

# driver_path = r'E:\InstallationOther\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("http://www.baidu.com")

# htmlElement = etree.HTML(driver.page_source)
# htmlElement.xpath('xpath语法')

# time.sleep(3)
# driver.page_source  # 获取请求网页源代码
# driver.close()      # 关闭当前页面
# driver.quit()       # 退出整个浏览器

# 1. 如果只想解析网页中的数据,推荐使用lxml解析,因为lxml底层使用c语言,所以解析效率高
# 2. 如果想要对标签元素进行操作,比如给文本框输入值,或者点击某个按钮,那么就使用selenium提供的查找标签元素的方法

### selenium定位标签元素
# 注: find_element是获取第一个满足条件的元素,find_elements是获取所有满足条件的元素(列表)
# driver.find_element_by_id("id属性")
# driver.find_element_by_class_name("class属性")
# driver.find_element_by_name("name属性")
# driver.find_element_by_tag_name("标签名称")
# driver.find_element_by_xpath("xpath语法")
# driver.find_element_by_css_selector("css选择器")

# inputTag = driver.find_element_by_id("kw")  # 根据input标签id属性获取
# inputTag = driver.find_element_by_name("wd")  # 根据input标签name属性获取
# inputTag = driver.find_element_by_class_name("s_ipt")  # 根据input标签class属性获取
# inputTag = driver.find_element_by_xpath('//input[@id="kw"]')  # 根据xpath语法获取
# inputTag = driver.find_element_by_css_selector('.quickdelete-wrap > input')  # 根据CSS选择器获取
# from selenium.webdriver.common.by import By
# inputTag = driver.find_element(By.CSS_SELECTOR,'.quickdelete-wrap > input')  # 根据CSS选择器获取
# inputTag.send_keys("python")  # 在表单元素中填写内容
# time.sleep(3)
# inputTag.clear()  # 清空表单元素中填写的内容

### 常见的表单元素
# input: type = "text/password/email/number/"
# input: type = "button/submit"
# input: type = "checkbox"
# select: 下拉列表框
# type = "file/image/hidden/radio/reset" ...

### 操作文本输入框与点击(单击): text submit
# driver_path = r'E:\InstallationOther\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("http://www.baidu.com")
# inputTag = driver.find_element_by_name("wd")
# inputTag.send_keys("python")  # 在表单元素中填写内容
# time.sleep(3)
# inputTag.clear()  # 清空表单元素中填写的内容

# inputSubmit = driver.find_element_by_id("su")  # 获取页面点击按钮标签元素
# inputSubmit.click()  # 执行单击按钮

### 操作checkbox:
# driver_path = r'E:\InstallationOther\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("https://www.douban.com/")  # 测试失败
# driver.get("http://renren.com/")
# checkBtn = driver.find_element_by_id("autoLogin")  # 选项框name属性
# checkBtn.click()  # 选中选项框

### 操作select: 未测试...
# <select id="selectNenu" name="selectNenu"> 
#   <option selected="selected">---请选择---</option> 
#   <option value="select1">项目经理</option>  
#   <option value="select2">总经理</option>  
#   <option value="select3">技术经理</option>  
#   <option value="select4">部门经理</option>  
# </select>  
# driver_path = r'E:\InstallationOther\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("https://www.douban.com/")
# from selenium.webdriver.support.ui import Select
# selectBtn = Select(driver.find_element_by_name("selectNenu"))
# selectBtn.select_by_index(1)                    # 选中下拉框的第一个选项(角标从0开始)
# selectBtn.select_by_value("select2")            # 根据option标签的value的值选中下拉框
# selectBtn.select_by_visible_text("技术经理")    # 根据可选文本的内容选中下拉框
# selectBtn.deselect_all()                        # 取消所有的选中

### 行为链: 鼠标操作
# from selenium.webdriver.common.action_chains import ActionChains
# driver_path = r'E:\InstallationOther\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("http://www.baidu.com")
# inputTag = driver.find_element_by_name("wd")   # 获取页面input文本框标签元素
# inputSubmit = driver.find_element_by_id("su")  # 获取页面按钮标签元素
# actions = ActionChains(driver)
# actions.move_to_element(inputTag)               # 把鼠标移动到文本框标签元素上
# actions.send_keys_to_element(inputTag,"java")   # 在文本框中输入内容
# actions.move_to_element(inputSubmit)            # 把鼠标移动到按钮标签元素上
# actions.click(inputSubmit)                      # 单击点击按钮
# actions.perform()                               # 执行行为链上的所有操作

# actions.click_and_hold(): 单击但不松鼠标
# actions.context_click():  右键单击
# actions.double_click():   双击
# ...

### 操作cookie:
# driver_path = r'E:\InstallationOther\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("http://www.baidu.com")
# 1. 获取所有cookie
# for cookie in driver.get_cookies():
#     print(cookie)
# 2. 根据cookie的key获取value
# cookie = driver.get_cookie("PSTM")
# print(cookie)
# 3. 删除所有的cookie
# driver.delete_all_cookies()
# 4. 删除某个cookie
# driver.delete_cookie("PSTM")
# print(driver.get_cookie("PSTM"))   # cookie不存在返回None

### 隐式等待和显示等待: 页面等待
# 1. 隐式等待
# driver_path = r'E:\InstallationOther\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.implicitly_wait(20)  # 隐式等待20秒
# driver.get("https://www.douban.com")
# driver.find_element_by_id("asdfghjkl")
# 当设置了隐式等待时间,未获取到指定需要的内容,当时间到了之后才会抛出异常
# 当未设置隐式等待时间,并且未获取到指定需要的内容,会立刻抛出异常

# 2. 显示等待
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver_path = r'E:\InstallationOther\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("https://www.douban.com")
# 设置等待10秒并设置等待条件
# WebDriverWait(driver,10).until(  # 设置显示等待条件
#     EC.presence_of_element_located((By.ID,"asdfghjkl"))
# )
# 当设置了显示等待时间与等待条件,当时间到了之后还未获取到指定需要的内容,才会抛出异常

### 打开新的页面(窗口)和切换页面(窗口)
# driver_path = r'E:\InstallationOther\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("https://www.baidu.com")
# 打开一个新的页面窗口
# driver.execute_script("window.open('https://www.douban.com')")
# 切换到这个新的页面窗口
# print(driver.current_url)       # https://www.baidu.com/  虽然chrome浏览器显示切换了新的窗口,但实际上driver没有切换
# print(driver.window_handles)    # 窗口句柄列表,按照打开页面的顺序来存储窗口的句柄
# driver.switch_to_window(driver.window_handles[1])  # 切换到豆瓣页面窗口
# print(driver.current_url)       # https://www.douban.com/

### 设置代理IP:
# options = webdriver.ChromeOptions()  # 创建chrome浏览器的选项信息
# options.add_argument("--proxy-server=http://125.40.109.154:31610")  # 给chrome浏览器选项信息添加代理IP
# driver_path = r'E:\InstallationOther\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)  # 创建chrome浏览器
# driver.get("https://httpbin.org/get")






