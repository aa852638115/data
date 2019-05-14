from urllib import request, parse
from lxml import etree
from json import json1


class DataModel(object) :
    def __init__(self):
        self.title = ""
        self.salary = ""
        self.position = ""
        self.working_life = ""
        self.education = ""
        self.company_name = ""
        self.company_type = ""
        self.financing_info = ""
        self.staff_numbers = ""
        self.recruiter_name = ""
        self.recruiter_job = ""
        self.release_time = ""

def data_2_json(obj):
    return {
        "title" : obj.title,
        "salary" : obj.salary,
        "position" : obj.position,
        "working_life" : obj.working_life,
        "education" : obj.education,
        "company_name" : obj.company_name,
        "company_type" : obj.company_type,
        "financing_info" : obj.financing_info,
        "staff_numbers" : obj.staff_numbers,
        "recruiter_name" : obj.recruiter_name,
        "recruiter_job" : obj.recruiter_job,
        "release_time" : obj.release_time
    }


class Spider(object) :
    def __init__(self):
        self.page = 1
        self.switch = True
        self.data_list = []

    def start_spider(self):
        while self.switch :
            self.load_page()
            command = input("是否继续爬取，是请按Y，否请按任意键")
            if command == "Y" or command == "y" :
                self.switch = True
                self.page += 1
            else :
                self.switch = False
                self.page = 1
                self.data_list.clear()

    def load_page(self):
        """
        加载页面数据
        """
        url_prefix = """https://www.zhipin.com/c100010000/h_100010000/?"""
        arg = {
            "query": "爬虫",
            "page": str(self.page),
            "ka": "page-" + str(self.page)
        }
        arg_str = parse.urlencode(arg)
        url = url_prefix + arg_str
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}
        # 构建一个Request对象，填入URL和headers头信息
        my_request = request.Request(url=url, headers=headers)
        # 发送请求，获取服务器响应
        response = request.urlopen(my_request)
        # 解析HTML文档为HTML DOM模型
        html = etree.HTML(response.read().decode("utf-8"))

        # 观察HTML代码可以发现<ul><li><div class="job-list">...</div></li></ul>中包含我们需要的数据
        li_list = html.xpath("//*[@id=\"main\"]/div/div[@class=\"job-list\"]/ul/li")
        self.deal_page(li_list)
        self.write_page()

    def deal_page(self, li_list) :
        """
        处理页面中的数据
        :param li_list:li标签集合
        """
        for li in li_list :
            data = DataModel()
            data.title = self.is_None(li.xpath(".//div/div[@class=\"info-primary\"]/h3/a/div[@class=\"job-title\"]/text()"))[0]
            data.salary = self.is_None(li.xpath(".//div/div[@class=\"info-primary\"]/h3/a/span/text()"))[0]
            data.position = self.is_None(li.xpath(".//div/div[@class=\"info-primary\"]/p/text()[1]"))[0]
            data.working_life = self.is_None(li.xpath(".//div/div[@class=\"info-primary\"]/p/text()[2]"))[0]
            data.education = self.is_None(li.xpath(".//div/div[@class=\"info-primary\"]/p/text()[3]"))[0]
            data.company_name = self.is_None(li.xpath(".//div/div[@class=\"info-company\"]/div/h3/a/text()"))[0]
            data.company_type = self.is_None(li.xpath(".//div/div[@class=\"info-company\"]/div/p/text()[1]"))[0]
            if li.xpath(".//div/div[@class=\"info-company\"]/div/p/text()[3]") :
                data.financing_info = self.is_None(li.xpath(".//div/div[@class=\"info-company\"]/div/p/text()[2]"))[0]
                data.staff_numbers = self.is_None(li.xpath(".//div/div[@class=\"info-company\"]/div/p/text()[3]"))[0]
            else :
                data.financing_info = "".encode("utf-8")
                data.staff_numbers = self.is_None(li.xpath(".//div/div[@class=\"info-company\"]/div/p/text()[2]"))[0]
            data.recruiter_name = self.is_None(li.xpath(".//div/div[@class=\"info-publis\"]/h3/text()[1]"))[0]
            data.recruiter_job = self.is_None(li.xpath(".//div/div[@class=\"info-publis\"]/h3/text()[2]"))[0]
            data.release_time = self.is_None(li.xpath(".//div/div[@class=\"info-publis\"]/p/text()"))[0]
            self.data_list.append(data)

    def is_None(self, obj):
        return obj if (obj) else [""]

    def write_page(self):
        """
        将数据写入文件
        """
        with open("招聘信息" + str(self.page) + ".txt", "a", encoding='utf8') as f:
            for data in self.data_list :
                f.write(json1.dumps(data, default=data_2_json, ensure_ascii=False))
                f.write("\n")
            self.data_list.clear()

if __name__ == '__main__':
    spider = Spider()
    spider.start_spider()