from pprint import pprint

from django.test import TestCase
import datetime
# Create your tests here.

a = datetime.datetime.now()
print(a)
format = '%Y-%m-%d %H:%M:%S'
print(a.strftime(format))

# for i in c:
#     print(i[0],i[1])

di = {}
di.setdefault('a','b')
print(di)
di.__setitem__('b','c')
pprint(di)
print(di.__getitem__('b'))