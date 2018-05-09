# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/5/8-16:24
from CCP.SendTemplateSMS import Send_Msg
# import random
#
#
# def send_ms(mobile,temp=1):
# 	sms_code = "%04d" %random.randint(1,9999)
# 	datas = [sms_code,1]
# 	Send_Msg().send_sms(mobile,datas,temp)
from celery_tasks.tasks import send_ms

send_ms.delay(mobile)