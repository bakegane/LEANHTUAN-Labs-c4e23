from gmail import GMail, Message
from random import choice

gmail = GMail("bakeganetechkid@gmail.com", "Passwords0")
sickness_list = ["Dau bung", "Nhuc dau", "So mui"]

template = '''
<p>chao sep</p>
<p>hom nay em ngu day thay {{sick}}, bac si bao phai nghi ngoi</p>
<p>sep cho em nghi lam nhe</p>
<p>nhan vien cua sep</p>
'''

sickness = choice(sickness_list)
content = template.replace("{{sick}}",sickness)

msg = Message("Don xin nghi phep",to="bakegane@gmail.com", html=content)
from datetime import datetime
from threading import Timer
x=datetime.today()
y=x.replace(day=x.day+1, hour=7, minute=1,second=0)
delta_t = y-x

secs=delta_t.seconds+1
t = Timer(secs, gmail.send(msg))
t.start()