import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '87281094@qq.com'  # 发件人邮箱账号
my_pass = 'ynmxmovzjljebgei'  # 发件人邮箱密码
my_user = '2021566362@qq.com'  # 收件人邮箱账号，我这边发送给自己
msg = MIMEMultipart()
msg['From'] = formataddr(["", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
msg['To'] = formataddr(["", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
msg['Subject'] = "发送邮件测试"  # 邮件的主题，也可以说是标题

msg.attach(MIMEText('这是Python 邮件发送测试……', 'plain', 'utf-8'))
# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('TEST.html', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="TEST.html"'
msg.attach(att1)

try:
    server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
    print("邮件发送成功")
except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
    print("邮件发送失败")

