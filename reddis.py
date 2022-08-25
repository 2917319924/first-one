#!/usrbin/env python
# _*_ coding:utf-8 _*_
import redis

#连接redis
connse = redis.Redis(host='192.168.1.116',port=6379,password='200406',encoding='utf-8')

#设置键值:123456="9999"而超时时间10秒(值写入到redis时会自动转字符串)
connse.set('123456',8846) #ex可以设置超时时间ex=10代表十秒失效就会返回None

value = connse.get('123456')
print(value)