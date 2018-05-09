# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/5/8-16:24

# 抽出发送短信的函数,使用celery 实现异步发送
''' 
from CCP.SendTemplateSMS import Send_Msg
import random
def send_ms(mobile,temp=1):
	sms_code = "%04d" %random.randint(1,9999)
	datas = [sms_code,1]
	Send_Msg().send_sms(mobile,datas,temp)
'''

from celery_tasks.tasks import send_ms

# 使用的是平台 测试号码
send_ms.delay(phoneNumber)   # (手机号码,内容数据,模板Id)