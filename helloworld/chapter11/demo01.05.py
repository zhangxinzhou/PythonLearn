import sqlite3

# 连接到到Sqlite数据库
# 数据库文件是mrsoft.db 如果问及那不存在,会自动在当前目录创建
conn = sqlite3.connect('mrsoft.db')

# 创建一个cursor
cursor = conn.cursor()

# 更新
cursor.execute('delete from user where id = ?', (1,))
cursor.execute('select * from user')
# 获取查询结果
result = cursor.fetchall()  # 获取全部
print(result)
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭连接
conn.close()
