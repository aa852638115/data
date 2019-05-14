import requests
import json

start_num = 0  # 每一页起始数变量
count = 0  # 总计数变量
data=[]
key='python'
for i in range(100):
    str1 = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=100&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={}&kt=3&_v=0.33366289&x-zp-page-request-id=63baca517e4f46aeae14832866d8e1b5-1547120041393-321630'.format(start_num,key)
    start_num += 90  # 对json请求链接分析后，发现每页只有90条数据，后一页起始数等于前一页起始数加90
    response = requests.get(str1)  # 第一个页面的json请求链接
    json_str = response.text
    json_dict = json1.loads(json_str)
    results = json_dict['data']['results']

    for item_dict in results:
        company = item_dict['company']['name']
        job_name = item_dict['jobName']
        job_type = item_dict['jobType']['display']
        salary = item_dict['salary']
        city = item_dict['city']['display']
        edu = item_dict['eduLevel']['name']
        workingExp = item_dict['workingExp']['name']
        welfare = '、'.join(item_dict['welfare'])  # '、'.join()：使用、字符将列表中的每一个元素拼接起来，得到一个字符串
        count += 1
        job_data ={
            '公司名称':company,
            '招聘职位':job_name,
            '职位类型':job_type,
            '薪资':salary,
            '城市':city,
            '学历要求':edu,
            '工作经验':workingExp,
            '福利待遇':welfare
        }
        data.append(job_data)
        #print('公司名称：{}  招聘职位：{}  职位类型：{}  薪资：{}  城市：{}  学历要求：{}  工作经验：{}  福利待遇：{}'.format(company, job_name, job_type, salary, city, edu, workingExp, welfare))

string = json.dumps(data, ensure_ascii=False)
print(string)
with open('./json/' + key + '.json', 'w', encoding='utf-8')as fp:
        fp.write(string)

print('共', count, '条数据')