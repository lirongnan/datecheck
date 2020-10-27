import redis   # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
import pymysql
import numpy

pool = redis.ConnectionPool(host='192.168.0.230', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
r = redis.Redis(connection_pool=pool)

urls = r.hgetall('TuNiuRoute_city')
starturl = urls.keys()

# 打开数据库连接
db = pymysql.connect("192.168.0.230","root","sdgl#123","spiderData")

# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute("SELECT DISTINCT UrlID FROM `holyrobot_routeinfo`")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchall()
resurl = numpy.array(data)
# 关闭数据库连接
db.close()
a = list(starturl)
b = resurl[:,0].tolist()
aa=set(a).difference(set(b))
bb=set(b).difference(set(a))
print("没有爬取的Url："+str(len(aa))) # 差集，在a中但不在b中的元素
print("爬取计划外的Url："+str(len(bb)))# 差集，在b中但不在a中的元素