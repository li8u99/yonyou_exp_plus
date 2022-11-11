![](https://i.bmp.ovh/imgs/2022/01/d58851a5e94d8bd1.png)
# 更新日志
2022.11.11：</br>
1、 增加 用友 U8 OA getSessionList.jsp 敏感信息泄漏漏洞、用友 U8 OA test.jsp SQL注入漏洞、用友FE协作办公平台 templateOfTaohong_manager.jsp 目录遍历漏洞、用友 GRP-U8 UploadFileData 任意文件上传漏洞、用友 GRP-U8 Proxy SQL注入。</br>
2022.01.25：</br>
1、 增加 用友ERP-NC 目录遍历漏洞、用友 NC bsh.servlet.BshServlet 远程命令执行漏洞。




# 工具介绍
**用友系列全漏洞检查工具plus版，收录漏洞如下：**
```
用友 NC bsh.servlet.BshServlet 远程命令执行漏洞
用友 U8 OA test.jsp SQL注入漏洞
用友FE协作办公平台 templateOfTaohong_manager.jsp 目录遍历漏洞
用友 GRP-U8 UploadFileData 任意文件上传漏洞
用友ERP-NC 目录遍历漏洞
用友 GRP-U8 Proxy SQL注入
用友 U8 OA getSessionList.jsp 敏感信息泄漏漏洞
```
**首次使用请安装依赖：**
```
python3 install -r requirements.txt
```
**使用方法：**
```
Usage:
python3 yonyou_exp.py -u url
python3 yonyou_exp.py -u url --att
python3 yonyou_exp.py -f url.txt
python3 yonyou_exp.py -f url.txt --att

Options:
  -h, --help            show this help message and exit
  -u URL, --url=URL     target url
  -f FILE, --file=FILE  url file
  --att                 Get Shell
```
```
python3 seeyon_exp.py -u url
```
![](https://i.bmp.ovh/imgs/2022/01/f95ff177cd2eace9.png)
```
python3 seeyon_exp.py -u url  --att
```
![](https://i.bmp.ovh/imgs/2022/01/f1b35573f248ff97.png)
</br>
</br>
**默认使用冰蝎3的webshell，密码为rebeyond**
</br>
</br>
**扫码结果保存为result.txt，使用批量扫描时，建议先筛选出存活url**
</br>
</br>
**声明：仅用于授权测试，请勿用于非法用途，违者后果自负！**
</br>
</br>
参考链接：
```
https://github.com/PeiQi0/PeiQi-WIKI-POC/tree/PeiQi/PeiQi_Wiki/OA%E4%BA%A7%E5%93%81%E6%BC%8F%E6%B4%9E/%E7%94%A8%E5%8F%8BOA
```

