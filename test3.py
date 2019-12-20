import requests
import json
headers = {}
start_urls =     "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1576121680181&pageIndex=1&pageSize=10&language=zh-cn&area=cn"
response = requests.get(start_urls)


print(response.request.headers)
print(response.headers)
print(response.url)
current_page_num = response.url.split("pageIndex=")[1][0]
print(current_page_num)
# response 有 body == content   ， text == text
# print(response.text)
# print("*"*100)
# print(response.body.decode("utf-8"))
json_str = response.content.decode()
data = json.loads(json_str)
data_list = data['Data']['Posts']
for data in data_list:
    post_id = data["PostId"]  # 1204946654294183936
    post_url = data["PostURL"]  # "http://careers.tencent.com/jobdesc.html?postId=0"
    item = {}
    item["new_url"] = post_url.replace("0", post_id)
    item["name"] = data["RecruitPostName"]
    item["content"] = data["Responsibility"].replace("\n", '')
    print(item)
print('*' * 100)
print('*' * 100)
print('*' * 100)