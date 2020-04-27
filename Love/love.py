import datetime

print('')
print('这是一些值得纪念的日子......')
print('')
my_birthday = '1994-03-29'
your_birthday = '1998-06-02'
face_day = '2020-01-30'

print('我的阳历生日是: {}'.format(my_birthday))
print('你的阳历生日是: {}'.format(your_birthday))
print('我们相识的阳历日子是: {}'.format(face_day))

my_birthday = datetime.datetime.strptime(my_birthday, '%Y-%m-%d')
your_birthday = datetime.datetime.strptime(your_birthday, '%Y-%m-%d')
face_day = datetime.datetime.strptime(face_day, '%Y-%m-%d')

# print(my_birthday)
# print(your_birthday)
# print(face_day)
print('')
print('我出生之后的第一个一万天是：{}'.format(
    datetime.datetime.strftime(my_birthday + datetime.timedelta(days=10000), '%Y-%m-%d')))
print('你出生之后的第一个一万天是：{}'.format(
    datetime.datetime.strftime(your_birthday + datetime.timedelta(days=10000), '%Y-%m-%d')))
print('')
print('我们相识的第一个520天是：{}'.format(
    datetime.datetime.strftime(face_day + datetime.timedelta(days=520), '%Y-%m-%d')))
print('我们相识的第一个1314天是：{}'.format(
    datetime.datetime.strftime(face_day + datetime.timedelta(days=1314), '%Y-%m-%d')))
print('我们相识的第一个10000天是：{}'.format(
    datetime.datetime.strftime(face_day + datetime.timedelta(days=10000), '%Y-%m-%d')))
