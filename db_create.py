#!flask/bin/python
from config import MONGODB_SETTINGS
from app import db, models
from mongoengine import connect
connect('pick')

m = models.Fl(id=1,flnm="kll")
q = models.Fl(id=2,flnm="klkl")
v = models.User(id=1, login="fd", email="f@fg.ru", fls=[m])
v.save()
p = models.User(id=2, login="fgh", email="fwe@fg.ru", fls=[m])
p.save()
er = models.User(id=3, login="fasgh", email="fwess@fg.ru")
er.save()
epp = models.User.objects.filter(id=1)
print (epp)

