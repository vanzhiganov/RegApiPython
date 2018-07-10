# coding: utf-8
""""""
import urllib3
from .base import RegRuBase
from urllib import request


class regRuApiDomain(object):
    def __init__(self):
        self.pathPrefix = '/domain/'
        self.pathPostfix = '?'

    def getApi(self, params, action):
        """Получаем функцию у регру"""
        RegRu = RegRuBase()
        apiPathDir = self.pathPrefix + action + self.pathPostfix

        response = request.urlopen(RegRu.generateApiUrl(apiPathDir, params))

        jdata = response.read().decode('utf8')

        print(RegRu.checkCurrentErrors(jdata))

        if RegRu.checkCurrentErrors(jdata) == 1:
            return jdata
        else:
            return RegRu.checkCurrentErrors(jdata)
