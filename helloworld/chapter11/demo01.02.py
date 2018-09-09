import sqlite3

# 连接到到Sqlite数据库
# 数据库文件是mrsoft.db 如果问及那不存在,会自动在当前目录创建
conn = sqlite3.connect('mrsoft.db')

# 创建一个cursor
cursor = conn.cursor();

# 执行一条sql语句,向user插入数据
cursor.execute('insert into user(id,name) values("1","mrfost")')
cursor.execute('insert into user(id,name) values("2","Andy")')
cursor.execute('insert into user(id,name) values("3","明日科技")')
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭连接
conn.close()
