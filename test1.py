import requests

'''
# post 无json
url = 'https://r.jina.ai/'
headers = {
    'Authorization': 'Bearer jina_7d19ea581f5240d296b5fa3ef506b810qjRuDRdCnEv16bKph-0KrOF39NCr',
    #'Accept': 'application/json',
    'X-Return-Format': 'markdown',
}
data = {
    'url': 'https://s.jina.ai/http://mp.weixin.qq.com/s?__biz=MzI5NDk3NTMyOQ==&mid=2247505235&idx=1&sn=ac1766b01f9d3f723a7312d2a171eefc&chksm=edef7951d39bfbaf96b1f10c467083d7893086f19f9a65d148e5aa5cc67fe6f12b1c4000e029&scene=126&sessionid=0#rd'
}

response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response.status_code)
'''

import requests
# post json
url = 'https://r.jina.ai/'

# 定义请求头，指定返回格式为Markdown
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer jina_7d19ea581f5240d296b5fa3ef506b810qjRuDRdCnEv16bKph-0KrOF39NCr',
    'X-Return-Format': 'markdown'
}
data = {
    'url': 'http://mp.weixin.qq.com/s?__biz=MzI5NDk3NTMyOQ==&mid=2247505235&idx=1&sn=ac1766b01f9d3f723a7312d2a171eefc&chksm=edef7951d39bfbaf96b1f10c467083d7893086f19f9a65d148e5aa5cc67fe6f12b1c4000e029&scene=126&sessionid=0#rd'
}

# 使用requests库向Jina Reader API发送POST请求，传入网页内容
response = requests.post(url, headers=headers, data=data)

#读取文本
markdown_text=response.text

#文件名
file_name='output.md'

#写入文件
with open(file_name,'w',encoding='utf-8')as file:
    file.write(markdown_text)


print(response.text)
print(response.status_code)