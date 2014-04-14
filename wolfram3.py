import urllib2
import urllib
import httplib
import sys
from xml.etree import ElementTree as etree
 
class wolfram(object):
    def __init__(self, appid):
        self.appid = appid
        self.base_url = 'http://api.wolframalpha.com/v2/query?'
        self.headers = {'User-Agent':None}
 
    def _get_xml(self, ip):
        url_params = {'input':ip, 'appid':self.appid}
        print "did I get here: yes"
        data = urllib.urlencode(url_params)
        print "data: " + data
        data = data.replace('%2B', 'jakefalse')
        """data = data.replace('%2B', '+')"""
        data = data.replace('jakefalse', '%2B')
        print "data: " + data
        req = urllib2.Request(self.base_url, data + '&format=image', self.headers)
        xml = urllib2.urlopen(req).read()
        return xml
 
    def _xmlparser(self, xml):
        data_dics = []
        tree = etree.fromstring(xml)
        anInt = 0
        #retrieving every tag with label 'plaintext'
        for e in tree.findall('pod'):
            for item in [ef for ef in list(e) if ef.tag=='subpod']:
                for it in [i for i in list(item) if i.tag=='img']:
                    if it.tag=='img':
                        default = 'wtf'
                        """data_dics[it.get('src', default)] ="""
                        data_dics.append(it.get('src', default))
                        print "size: " + str(len(data_dics))
        if(len(data_dics) == 0):
            return False
        
        return data_dics
 
    def search(self, ip):
        xml = self._get_xml(ip)
        print "ip : " + ip
        result_dics = self._xmlparser(xml)
        
        if(result_dics == False):
            return False
        #return result_dics 
        #print result_dics
        """print result_dics[]"""
        if(len(result_dics) >= 2):
            return result_dics[1]
        elif (len(result_dics) == 1):
            return result_dics[0]
        else: None
 
"""if __name__ == "__main__":
    appid = sys.argv[1]
    query = sys.argv[2]
    w = wolfram(appid)
    w.search(query)"""