import requests


# 调用API接口

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

response = requests.get(url)
print('staas_code :', response.status_code)

# 存储在一个变量中
response_dict = response.json()
# print(response_dict.keys())

# 探索仓库相关的知识
repo_dicts = response_dict['items']
print('repositories: ', len(repo_dicts))

# 探索第一个库
repo_dict = repo_dicts[0]
print('\nkeys：', len(repo_dict))

print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
