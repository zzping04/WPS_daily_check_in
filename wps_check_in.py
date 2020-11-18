import random
import requests

s = requests.session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

invite_userid = 244668941
wps_sid = 'V02StmNx2jDkYJGLQ1suV7tCWs4UGuI00a5b2e57000e955a0d'

cookie = {
    'wps_sid': wps_sid
}

# 领任务，4：签到，5：答题+积分，8：答题+会员
task_url = 'https://vipapi.wps.cn/task_center/task/receive_task'
for i in (4,5,8):
    data = {'id' : i}
    r = s.post(task_url, cookies=cookie,data = data)
    print(i,r.text)

# 答题
questionbank = {
    'PC_task_knowledge' : ['0:1|2|3', '1:3', '2:1', '3:1', '4:1', '5:3', '6:1', '7:2', '8:1|2|3', '9:3', '10:4'],
    'pc_task_konwMembers' : ['0:1|2|3', '1:1|2|3', '2:4', '3:2', '4:3', '6:1|2|3', '7:2', '8:1|2|3', '9:4', '10:4']
}


ck = 'https://vip.wps.cn/questionbank/check'
for k, v in questionbank.items():
    data ={
            'task_tag': k,
            'position': k,
            'answers': ','.join(random.sample(v, 5))
    }
    r = s.post(ck, headers=headers, cookies=cookie, data=data)
    print(json.loads(r.text))


# 领奖励
reward_url = 'https://vipapi.wps.cn/task_center/task/receive_reward'
for i in (4,5,8):
    data = {'id' : i}
    r = s.post(reward_url, cookies=cookie,data = data)
    print(json.loads(r.text))

