# # item = {"a":1}
# #
# # with open('tencentdata.txt', 'a', encoding='utf-8')as f:
# #     f.write(item)
#
#
#
# # import requests
# # res = requests.get("https://www.ituring.com.cn/tag/2492")
# # print(res.content.decode())
# # print(res)
# import json
# #
# # with open('tuling/tuling.txt','r',encoding='utf-8') as f:
# #     content = f.read()
# #     print()
# #     final = '{"data":[' + content.replace("}{","},{") + ']}'
# #     print(final)
#
# # with open('new_tuling.json','r',encoding='utf-8') as f:
# #     a = json.load(f)
# #     print(type(a))
# #
# # with open("new_tuling2.json",'w',encoding='utf-8') as f:
# #     json.dump(a,f,ensure_ascii=False,indent=4)
# #
#
# li = []
# #
# # with open('tencentdata.txt','r',encoding='utf-8') as f:
# #     while True:
# #         content = f.readline()
# #         print(content)
# #         li.append(content.replace("\n",""))
# #         if content == "":
# #             break
# # print(li)
#
#
#
# for i in li:
#     print(1)
#
# page = 20
# # 判断当前页码的数量
# url = "http://book.chaoxing.com/search/keyword_/fenleiID_0106/field_01/sortName_/nPage_2/size_10.html"
#
# url_path_list = url.split("/")
# print(url_path_list)
# # nPage_2
# url_path_list[-2] = "nPage_" +  str(page)
# print(url_path_list)
# url = "/".join(url_path_list)
# print(url)
#
#
# class A():
#     def __test(self):
#         print('test')
#     def _demo_(self):
#         print('demo')
#
# a = A()
# a._demo_()
# from hashlib import sha1,md5
# a = 'hello world'
# fp = sha1()
# print(fp.update(a.encode()))
# print(fp.hexdigest())
#
# f = md5()
# f.update(a.encode())
# print(f.hexdigest())
s = "\n                养生保健\n            "
print(s)
print(s.strip())
