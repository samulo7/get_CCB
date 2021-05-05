## 脚本说明

1. 已实现功能
   * 自动完成奋斗季主会场任务及领取奖励、升级建筑
   * 自动完成车主分会场任务及抽奖
   * 自动完成主会场天天抽奖
   * 自动完成母亲节晒妈活动 开始分享及助力功能
2. 未实现功能
   * 主会场互助任务（暂未找到助力接口及逻辑，若有思路，欢迎 Issue或Pr）
3. Cookie有效期6小时，使用`keepAlive.py`脚本定时调用活动接口，以延长Cookie有效期，具体持续时长待测试，感谢[龙猪猪](https://github.com/nianyuguai)大佬提供思路
4. 助力次数未知，脚本已内置本人三个助力码

## 抓包说明

1. 前往[龙支付奋斗季主会场](https://jxjkhd.kerlala.com/a/91/lPYNjdmN?u=37ff922b-ba7b-4fb0-b6f9-c28042297b75)，使用手机号登陆并报名首页天天抽奖活动

2. 在Cookie中抓取`XSRF-TOKEN`和`_session`参数并填入配置文件

## 使用方法

1. 安装git和python3

2. 克隆仓库

   ```
   git clone https://github.com/leeyiding/get_CCB.git && cd get_CCB
   ```

3. 安装依赖

   ```
   pip3 install pip -U
   pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
   pip3 install -r requirements.txt
   ```

4. 复制配置文件模板

   ```
   cp ./config.sample.json ./config.json
   ```

   配置文件示例

   ```
   {
       "cookie": [
    		//账户1   
           {
               "XSRF-TOKEN": "eyJpdiI6Ijk4UEhaM01KL3JOWnZDbHsdfJtY3c9PSIsInZhbHVlIjoieURwR1M2dUpQOUxNY28yU3p4cmduQnZTZmk5M01FQms1Z1pRM1QyNFZhaW5PUmdLYkNQWXg3NVhhZ21OSTNNM1NTTDg5eU9qb1h3V0dLWDhLT2ZyZ1JIUkFhbUJWcDl4SzlMaitLbml6QXlFNXlBOUZGdlVzVFlKa3JoNDkxb2EiLCJtYWMiOiI5MmU0YWZjZjdhYzFiMTZhN2ZhYzU0ZGYxZGEwMGU2N2NkODNkYjBlMTNjMTJkNDE3ZGNlMDAwODEwNmNjYzc0In0%3D",
               "_session": "eyJpdiI6IkwycmV5VDM1ang1Rzk4cFsdfsdkE9PSIsInZhbHVlIjoiOHBqYWFlbXRXS3E5OWVyYS9WZTFxSzRQaU12cG1NZ2lwaU5RVStlN3JFVmdkRE1mQTI1OCtma1FxanFJUTJpMWhkZ01wTHNLa3l5b0FIRGhIMlVSQSszcVJUN1ArMHAzampKbHNpTFNxTkZ3VFpVSXhzMFEydlVoaEtHZGM3MkgiLCJtYWMiOiJkNjA1MTI2MTczZmNiYzQwZmYyNDY3YjAyZjkyYzNhYjA4NTk2YjY0ZTkxZDNlNDBjODY5YzI5ODU4NjNiMzVkIn0%3D"
           },
           //账户2
           {
               "XSRF-TOKEN": "eyJpdiI6IlVIRjVjcWxGOG1hSjFnNEJzbmhEsdfIsInZhbHVlIjoiUjBCRkQwQk1EdmxxdVp4YXF2OGM3S2ZrY2ZySmVkZjhwSnZCcldqY1JNTGZXb3Rja21TM2VQazcvMVlwbzUvV2hFeDR3c0MxWEJIdUp5cWI0VTFMdDh4b3NHU2pabVJwaEF5cE9Hc1d4TkdNRWprZ0VUbktlUEJXM3lBMkNUSHciLCJtYWMiOiJlMDQ4ZjM3YzhkMWNjNGY3NTdhNGZjMWIwNjdlYzBiNzlmZTNhNDc5MTM1OWE4YThkNDRjOTEzYjRhMmQzMmExIn0%3D",
               "_session": "eyJpdiI6IjhOeXJ3RDdUSzNpTXpmaG1zeGdsS0E9PSIsInZhbHVlIjoiYldXMWVtSktId0hGazcwKzl4alVYRU80VXAwRWVXRzJLZlFpbmdUd0V6SlBZOXl5QkQyOEIxaG9lOFB6N1sdfsdfWhORGZXcTB0clZWaUppMXlHcXpKbDVFMjZHM0MzOVM3RXVhU2lIUTZyU2grTDU5RUpIbnJ4WER4NzV3b24iLCJtYWMiOiJhNmEzZDJhZWE3ZTBkMzIxNjkxNjRhYTBjYjM3ZjE2YWE0Yzc2ZDY5MmFkN2E3YTcyOGI4NDE0MjU1ZDRmNDIxIn0%3D"
           }
       ],
       "shareCode": {
        	//奋斗季互助码   
           "common": [
               "37ff922b-ba7b-4fb0-b6f9-c28042297b75",
               "49675a5f-6efc-4609-8c9f-2163f2a474b1",
               "b9d117c6-d5b6-48a6-a2a5-164a616c0490"
           ],
        	//母亲节活动互助码   
           "motherDay": [
               "161bb055-25d4-46dc-a029-7aa3e0e333da",
               "e225f3ca-4216-476e-893c-f43b8a9ededb",
               "3b37002d-10e5-4c99-8dca-8680bcd15a79"
           ]
       }
   }
   ```

5. 添加定时任务

   ```
   0 */3 * * * cd /scriptPath/ && python3 keepAlive.py 
   5 0 * * * cd /scriptPath/ && python3 main.py
   ```



