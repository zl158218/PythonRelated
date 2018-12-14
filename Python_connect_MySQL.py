import pymysql
conn = pymysql.connect(
    host = '192.168.19.128',
    user = 'root',
    passwd = '123qwe',
    db = 'centos'
)
# host后为ip，本地连接为localhost或127.0.0.1
# port 端口号，默认为3306
# user 数据库登录用户
# passwd 密码
# db 所要连接的库名字

cur = conn.cursor()
sql = 'select * from race_record limit 10'
# 执行SQL语句，查询操作
cur.execute(sql)
# 获取所有记录列表
results = cur.fetchall()
for i in results:
    print(i)
cur.close()