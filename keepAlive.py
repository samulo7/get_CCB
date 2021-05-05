import requests
import json
import os

def getUserInfo(cookies):
    headers = {
        'authority': 'jxjkhd1.kerlala.com',
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi K30 5G Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045613 Mobile Safari/537.36 MMWEBID/6824 micromessenger/8.0.1.1841(0x28000151) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
        'referer': 'https://jxjkhd1.kerlala.com/a/91/lPYNjdmN/fdtopic_v1/index',
    }

    r = requests.get('https://jxjkhd1.kerlala.com/Common/activity/getUserInfo/91/lPYNjdmN', headers=headers,cookies=cookies)
    return r.json()

def readConfig(configPath):
    with open(configPath,encoding='UTF-8') as fp:
        config = json.load(fp)
    return config

rootDir = os.path.dirname(os.path.abspath(__file__))
configPath = rootDir + "/config.json"
config = readConfig(configPath)
print('共获取到{}个用户，开始Cookie保活'.format(len(config['cookie'])))
for i in range(len(config['cookie'])):
    result = getUserInfo(config['cookie'][i])
    if result['status'] == 'success':
        print('第{}个账号{}Cookie保活成功'.format(i+1,result['data']['nickname']))
    else:
        print('第{}个账号已失效'.format(i+1))
