# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/5/5-1:08

from celery import Celery
import random
from CCP.SendTemplateSMS import Send_Msg

app = Celery('task',broker="redis://140.143.249.76:6379/0")



@app.task
def send_ms(mobile,temp=1):
	sms_code = "%04d" %random.randint(1,9999)
	datas = [sms_code,1]
	Send_Msg().send_sms(mobile,datas,temp)



