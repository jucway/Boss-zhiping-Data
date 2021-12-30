# _*_coding:utf-8_*_
# create by Jucw on 2021/12/30 0:36
from selenium import webdriver
from bs4 import BeautifulSoup
import xlwt
import sys
import requests
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time
import json
import datetime
class MainWindow(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # app = QApplication([])
        # window = QMainWindow()
        # window.resize(500, 320)
        # window.move(300, 310)
        # window.setWindowTitle("Boss直聘消息")
        # self.font = QFont('黑体', 20)
        self.setWindowTitle('Boss直聘消息')
        self.resize(500, 320)
        self.move(300, 310)
        self.font = QFont()
        self.font.setPointSize(21)
        self.font.setFamily(("wenquanyi"))
        self.font.setBold(True)
        self.Label = QLabel(self)
        self.Label.setText("Boss直聘搜搜看！！!")
        self.Label.setFont(self.font)
        self.Label.move(120, 20)
        self.Label.resize(260, 50)
        self.CityEdit = QPlainTextEdit(self)
        self.CityEdit.setPlaceholderText("输入城市")
        self.CityEdit.move(90, 100)
        self.CityEdit.resize(130, 30)
        self.ProEdit = QPlainTextEdit(self)
        self.ProEdit.setPlaceholderText("输入职业")
        self.ProEdit.move(280, 100)
        self.ProEdit.resize(130, 30)
        self.PagesEdit = QPlainTextEdit(self)
        self.PagesEdit.setPlaceholderText("输入爬取页数")
        self.PagesEdit.move(90, 160)
        self.PagesEdit.resize(130, 30)
        self.FileNEdit = QPlainTextEdit(self)
        self.FileNEdit.setPlaceholderText("输入保存文件名")
        self.FileNEdit.move(280, 160)
        self.FileNEdit.resize(130, 30)

        self.button = QPushButton('确定',self)
        self.button.move(330,250)
        self.button.clicked.connect(self.paqu)
        # self.initUI()
        # self.FileNEdit.setPlaceholderText("爬取成功")

    def paqu(self):

        driver = webdriver.Chrome('chromedriver.exe')
        index = 1

        # 获取指定城市的编码
        def get_city_code(city_name):
            response = requests.get("https://www.zhipin.com/wapi/zpCommon/data/city.json")
            contents = json.loads(response.text)
            cities = contents["zpData"]["hotCityList"]
            city_code = contents["zpData"]["locationCity"]["code"]
            for city in cities:
                if city["name"] == city_name:
                    city_code = city["code"]
            return city_code

        if self.ProEdit.toPlainText() is None:
            key = self.ProEdit.toPlainText().strip()
        else:
            key = "审计"
        if self.CityEdit.toPlainText() is None:
            citys = self.CityEdit.toPlainText()
        else:
            citys = "广州"
        citys = list(citys.split())
        citys = [get_city_code(city) for city in citys]
        if self.PagesEdit.toPlainText() is None:
            pages = int(self.PagesEdit.toPlainText().strip())
        else:
            pages = 10
        print(pages)

        # 初始化表格
        def initExcel():
            global newTable, wb, ws, headData
            hud = ['职位名', '地区', '公司', '薪资', '标签']
            print('\t'.join(hud))
            nowTime = datetime.datetime.now().strftime('%Y%m%d-%H%M')  # 现在
            if self.FileNEdit.toPlainText() is not None:
                newTable = self.FileNEdit.toPlainText() + '.xls'
            else:
                newTable = "boss-" + nowTime + "-" + key + ".xls"  # 表格名称
            print(newTable)
            wb = xlwt.Workbook(encoding='utf-8')  # 创建excel文件，声明编码
            ws = wb.add_sheet('sheet1')  # 创建表格
            headData = ['职位名', '地区', '公司', '薪资', '标签']
            for colnum in range(0, len(headData)):
                ws.write(0, colnum, headData[colnum], xlwt.easyxf('font: bold on'))  # 行，列

        print("----------初始化excel----------")
        initExcel()

        def excel_write(item,index):
            # 爬取到的内容写入excel表格
            for i in range(0, 5):
                # print item[i]
                ws.write(index, i, item[i])  # 行，列，数据

        # 每个城市爬取
        for city in citys:
            time.sleep(1)
            # 前十页
            urls = ['https://www.zhipin.com/c{}/?query={}&page={}&ka=page-{}'.format(city ,key, i, i)
                    for i in range(1, pages)]
            for url in urls:
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'
                }
                driver.get(url)

                # 获取源码，解析
                html = driver.page_source
                bs = BeautifulSoup(html, 'html.parser')

                job_all = bs.find_all('div', {"class": "job-primary"})
                # print(job_all)

                for job in job_all:
                    li = []

                    # 工作名称
                    job_name = job.find('span', {"class": "job-name"}).get_text()
                    li.append(job_name)
                    # 工作地点
                    job_place = job.find('span', {'class': "job-area"}).get_text()
                    li.append(job_place)
                    # 工作公司
                    job_company = job.find('div', {'class': 'company-text'}).find('h3', {
                        'class': "name"}).get_text()
                    li.append(job_company)
                    # 工作薪资
                    job_salary = job.find('span', {'class': 'red'}).get_text()
                    li.append(job_salary)
                    # 工作标签
                    job_label = job.find('a', {'class': 'false-link'}).get_text()
                    li.append(job_label)

                    # print(li)
                    excel_write(li,index)
                    index += 1
        wb.save(newTable)

        driver.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    x = MainWindow()
    x.show()
    app.exec_()