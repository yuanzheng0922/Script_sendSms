#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-  

from CCPRestSDK import REST
import ConfigParser

#主帐号
accountSid= '8a216da862cc8f910162d857f3f308c2'

#主帐号Token
accountToken= 'a8510c2c2a294210b5482441396d5689'

#应用Id
appId='8a216da862cc8f910162d857f45008c9'

#请求地址，格式如下，不需要写http://
serverIP='app.cloopen.com'

#请求端口 
serverPort='8883'

#REST版本号
softVersion='2013-12-26'

  # 发送模板短信
  # @param to 手机号码
  # @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
  # @param $tempId 模板Id
class Send_Msg(object):  # 创建单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_isinstance'):
            obj=object.__new__(cls,*args, **kwargs)
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)
            cls._isinstance = obj
        return cls._isinstance


    def send_sms(self,to,datas,tempId):
        # 调用REST的sendTemplatesSMS方法 (手机号码,内容数据,模板Id)
        result = self.rest.sendTemplateSMS(to, datas, tempId)
        # print result
        if result['statusCode'] == '000000':
            return 1
        else:
            return 0

''' 
发送成功返回的值
{'templateSMS': {'smsMessageSid': '4983cd02cb8a49e68056bdb974937bce', 'dateCreated': '20180509095052'},
             'statusCode': '000000'}
'''





            # def sendTemplateSMS(to,datas,tempId):
#     #初始化REST SDK
#     rest = REST(serverIP,serverPort,softVersion)
#     rest.setAccount(accountSid,accountToken)
#     rest.setAppId(appId)
#
#     result = rest.sendTemplateSMS(to,datas,tempId)
#     for k,v in result.iteritems():
#
#         if k=='templateSMS' :
#                 for k,s in v.iteritems():
#                     print '%s:%s' % (k, s)
#         else:
#             print '%s:%s' % (k, v)
#
   
#sendTemplateSMS(手机号码,内容数据,模板Id)