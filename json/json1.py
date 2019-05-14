
import urllib.request
import json
import time
import random
time_0 = time.time()
str =[]
for i in range(500):
    url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&kt=3&_v=0.89067574&x-zp-page-request-id=866368d6313e41c38a6e600b1c5d8082-1545034860140-256948'.format(
        i * 90)
    if i == 0:
        url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&kt=3&_v=0.89067574&x-zp-page-request-id=866368d6313e41c38a6e600b1c5d8082-1545034860140-256948'

    page = urllib.request.urlopen(url).read()
    data = json.loads(page)
    time.sleep(random.uniform(1.2, 2.1))

    for each_job in data['data']['results']:
        add_data = {
            '编号': each_job['number'],  # 编号
            '职业大分类编号':each_job['jobType']['items'][0]['code'],  # 职业大分类编号
            '职业大分类名称':each_job['jobType']['items'][0]['name'],  # 职业大分类名称
            '职业细分类编号':each_job['jobType']['items'][1]['code'],  # 职业细分类编号
            '职业细分类名称':each_job['jobType']['items'][1]['name'],  # 职业细分类名称
            '公司编号':each_job['company']['number'],  # 公司编号
            '公司对应url':each_job['company']['url'],  # 公司对应url
            '公司名称':each_job['company']['name'],  # 公司名称
            '公司规模编号':each_job['company']['size']['code'],  # 公司规模编号
            '公司规模':each_job['company']['size']['name'],  # 公司规模
            '公司类型编号':each_job['company']['type']['code'],  # 公司类型编号
            '公司类型':each_job['company']['type']['name'],  # 公司类型
            '职位对应url':each_job['positionURL'],  # 职位对应url
            '工作经验编号':each_job['workingExp']['code'],  # 工作经验编号
            '工作经验':each_job['workingExp']['name'],  # 工作经验
            '教育水平编号':each_job['eduLevel']['code'],  # 教育水平编号
            '教育水平':each_job['eduLevel']['name'],  # 教育水平
            '工资':each_job['salary'],  # 工资
            '工作类型':each_job['emplType'],  # 工作类型
            '工作名称':each_job['jobName'],  # 工作名称
            '经度':each_job['geo']['lat'],  # 经度
            '纬度':each_job['geo']['lon'],  # 纬度
            '工作城市':each_job['city']['display'],  # 工作城市
            '工作福利':'/'.join(each_job['welfare'])  # 工作福利
        }
        str.append(add_data)
        print(add_data)
data_1 = json.dumps(str,ensure_ascii=False)
with open('大数据.json', 'w', encoding='utf-8')as fp:
    fp.write(data_1)