import sqlite3

# db 파일 조회하기 

conn = sqlite3.connect("test.db", isolation_level=None)

c = conn.cursor()
# c.execute("SELECT * FROM users")

# # 커서위치  변경시키기
# # - 1개 로우 선택
# print("one -> ", c.fetchone())
# # 1번 Id

# # - 지정 로우 선택
# print("three -> ", c.fetchmany(size=3))
# # 2, 3, 4번 Id

# # - 전체 로우 선택
# print("all ->", c.fetchall())
# # 5 ~ 끝번 Id




# #순회

# rows = c.fetchall()
# for row in rows:
#     print(row)


# for row in c.execute("SELECT * FROM users ORDER BY id desc"):
#     print(row)


# WHERE
param1 = (3, )
c.execute("SELECT * FROM users WHERE id=?", param1)
# print(c.fetchone())
# print(c.fetchall())
# - fetch할때마다 커서의 위치가 이동한다!

c.execute("SELECT * FROM users WHERE id='%s'" % param1)
c.execute("SELECT * FROM users WHERE id={}".format(3))
# print(c.fetchone())

c.execute("SELECT * FROM users WHERE id=:Id", {"Id":3})
# print(c.fetchone())


# IN 합집합 이용하기 
param = (3,5)
c.execute("SELECT * FROM users WHERE id IN(?, ?)", param)
# print(c.fetchall())
c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % param)
# print(c.fetchall())

c.execute("SELECT * FROM users WHERE id=:Id1 OR id=:Id2", {"Id1":3, "Id2": 5})
print(c.fetchall())


# Dump 출력
# - 데이터베이스를 백업해두는 것

with conn:
    with open("backup_db.txt", "w") as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print("Dump Print Complete")



with conn:
    with open("dff", "w") as f:
        for line in conn.iterdump():
            f.write(line + "\n")


# c.execute("SELECT * FROM users WHERE username=?", ('oh', ))
# print(c.fetchall())
