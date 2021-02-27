import sqlite3
conn = sqlite3.connect("test.db", isolation_level=None)
c = conn.cursor()
# 테이블 수정 삭제 

# UPDATE
# c.execute("UPDATE users SET username = ? WHERE id = ?",("seung", 2))

# c.execute("UPDATE users SET username = :name WHERE id = :id", {"name": "goodman", "id": 3})

# c.execute("UPDATE users SET username='%s' WHERE id='%s'" % ("seung", 3))


# 데이터 확인하기 
for user in c.execute("SELECT * FROM users"):
    print(user)

# DELETE
c.execute("DELETE FROM users WHERE id=?",(2,))
c.execute("DELETE FROM users WHERE id='%d'", (3, ))
c.execute("DELETE FROM users WHERE id=:ID", {"ID":5})
