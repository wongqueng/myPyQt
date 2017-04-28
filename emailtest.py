#coding:utf-8   #强制使用utf-8编码格式
import smtplib#加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
mail_sender='a1146430762@163.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
mail_pwd="huangqiang1"#163授权码
receiver='1146430762@qq.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
host_server="smtp.163.com"#邮箱地址

def mail():
    ret=True
    try:
        msg=MIMEText("hello world",'plain','utf-8')
        msg['From']=formataddr(["黄强",mail_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["andywong",receiver])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="哈哈" #邮件的主题，也可以说是标题

        server=smtplib.SMTP(host_server,25)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(mail_sender,mail_pwd)    #括号中对应的是发件人邮箱账号、邮箱密码#cmpuukatelgijhfd#trcaeynuggyqfffi
        #lqaxpyilkysfjaja
        server.sendmail(mail_sender,[receiver,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #这句是关闭连接的意思
    except Exception,e:   #如果try中的语句没有执行，则会执行下面的ret=False
        print e
        ret=False
    return ret

ret=mail()
if ret:
    print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
else:
    print("filed")  #如果发送失败则会返回filed