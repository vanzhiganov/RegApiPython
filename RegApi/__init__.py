# coding: utf-8
""""""
# import config
from urllib2.parse import urlencode
from urllib2.request import urlopen
from .base import RegRuBase

class regRuApiDomain(object):
    pathPrefix = '/domain/'
    pathPostfix = '?'

    def __init__(self):
        pass

    def getApi(params, action):
        """Получаем функцию у регру"""
        RegRu = RegRuBase()
        apiPathDir = self.pathPrefix + action + self.pathPostfix
        print (RegRu.generateApiUrl(apiPathDir, params))
        response = urlopen(RegRu.generateApiUrl(apiPathDir, params))
        jdata = eval(response.read().decode('utf8'))

        if RegRu.checkCurrentErrors(jdata) == 1:
            return jdata
        else:
            return RegRu.checkCurrentErrors(jdata)
