#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-  

from CCPRestSDK import REST
import ConfigParser

#���ʺ�
accountSid= '8a216da862cc8f910162d857f3f308c2'

#���ʺ�Token
accountToken= 'a8510c2c2a294210b5482441396d5689'

#Ӧ��Id
appId='8a216da862cc8f910162d857f45008c9'

#�����ַ����ʽ���£�����Ҫдhttp://
serverIP='app.cloopen.com'

#����˿� 
serverPort='8883'

#REST�汾��
softVersion='2013-12-26'

  # ����ģ�����
  # @param to �ֻ�����
  # @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
  # @param $tempId ģ��Id
class Send_Msg(object):  # ��������ģʽ
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_isinstance'):
            obj=object.__new__(cls,*args, **kwargs)
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)
            cls._isinstance = obj
        return cls._isinstance


    def send_sms(self,to,datas,tempId):
        # ����REST��sendTemplatesSMS���� (�ֻ�����,��������,ģ��Id)
        result = self.rest.sendTemplateSMS(to, datas, tempId)
        # print result
        if result['statusCode'] == '000000':
            return 1
        else:
            return 0

''' 
���ͳɹ����ص�ֵ
{'templateSMS': {'smsMessageSid': '4983cd02cb8a49e68056bdb974937bce', 'dateCreated': '20180509095052'},
             'statusCode': '000000'}
'''





            # def sendTemplateSMS(to,datas,tempId):
#     #��ʼ��REST SDK
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
   
#sendTemplateSMS(�ֻ�����,��������,ģ��Id)