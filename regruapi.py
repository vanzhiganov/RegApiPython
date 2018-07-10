""""""
import regru
import config
#from regru import RegRu
from urllib.parse import urlencode
from urllib.request import urlopen

class regRuApiDomain(object):
    def __init__(self):
        pass

    def getApi(params, action):
        """Получаем функцию у регру"""
        RegRu = regru.RegRu()
        apiPathDir = config.domainGlobalConsts.pathPrefix + action + config.domainGlobalConsts.pathPostfix
        print (RegRu.generateApiUrl(apiPathDir, params))
        response = urlopen(RegRu.generateApiUrl(apiPathDir, params))
        jdata = eval(response.read().decode('utf8'))

        if(RegRu.checkCurrentErrors(jdata) == 1):
            return jdata
        else:
            return RegRu.checkCurrentErrors(jdata)
