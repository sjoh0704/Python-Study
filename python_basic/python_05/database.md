# Datbase sqlite활용하기 

## current time 가져오기
#
```
import datetime
now = datetime.datetime.now()
nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")
```

</br>

##  DB 생성, Auto commit(rollback)
#

- 커밋 : isolation_level=none일 경우 자동 반영(auto commit)  
- 만약 설정하지 않을 경우, conn.commit()을 따로 해주어야 한다. 
- 커밋과 롤백은 실행되는 시점이 중요하다. 

</br>

```
import sqlite3
conn = sqlite3.connect("test.db", isolation_level=None)
```
- 현재 위치한 디렉토리안에 생성
- 존재한다면 생성하지 않고 존재한다면 연결 

</br>

## cursor를 통해서 데이터를 읽어오고 읽을 데이터가 없으면 Null
#
```
c = conn.cursor()
```

</br>

## 테이블 생성
#

```
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text,  website text, regdate text) ")
```
- data type: text, numeric integer real blob

- 큰따옴표안에서는 작은 따옴표를 써주어야 한다. 

</br>

```
c.execute("INSERT INTO users VALUES(3, 'oh', 'sjoh0704@daum.net', '01012341234','github.com/sjoh0704', ?)", (nowDateTime,))
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?, ?, ?, ?, ?, ?)", (4,  'oh', 'sjoh0704@daum.net', '01012341234','github.com/sjoh0704', nowDateTime))
```

- 트플이나 리스트로 처리하는것이 가장 많이 쓰이는 방식
- 웹 크롤링에서 가져온 데이터를 처리하는데 많이 사용  

</br>

```
userList = ((5, 'oh', 'sjoh0704@daum.net', '01012341234','github.com/sjoh0704', nowDateTime)
,(6, 'oh', 'sjoh0704@daum.net', '01012341234','github.com/sjoh0704', nowDateTime)
,(7, 'oh', 'sjoh0704@daum.net', '01012341234','github.com/sjoh0704', nowDateTime)
)
c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)", userList )
```

</br>

## 테이블 삭제하기 
#
```
conn.execute("DELETE FROM users")
```

</br>

## 삭제하면서 갯수확인
#
```
print('users db deleted',conn.execute("DELETE FROM users").rowcount )
```

</br>

## 접속 해제 
#
```
conn.close()
```

</br></br></br>


# db 파일 조회하기 

## users테이블에서 전체 데이터 가져오기
#
c.execute("SELECT * FROM users")

</br>

## 커서위치 변경시키기
#
- 1개 로우 선택
```
print("one -> ", c.fetchone())
```
1번 Id 출력

- 지정 로우 선택
```
print("three -> ", c.fetchmany(size=3))
```
2, 3, 4번 Id 출력

- 전체 로우 선택
```
print("all ->", c.fetchall())
```
5 ~ 끝번 Id 출력

</br>

## 순회
#
```
rows = c.fetchall()
for row in rows:
     print(row)
```
```
for row in c.execute("SELECT * FROM users ORDER BY id desc"):
    print(row)
```

</br>

## WHERE
#
```
param1 = (3, )
c.execute("SELECT * FROM users WHERE id=?", param1)
print(c.fetchone())
print(c.fetchall())
```
fetch할때마다 커서의 위치가 이동한다!

```
c.execute("SELECT * FROM users WHERE id='%s'" % param1)
print(c.fetchone())
```
```
c.execute("SELECT * FROM users WHERE id={}".format(3))
print(c.fetchone())
```
```
c.execute("SELECT * FROM users WHERE id=:Id", {"Id":3})
print(c.fetchone())
```

</br>

## IN 합집합 이용하기 
#
```
param = (3,5)
c.execute("SELECT * FROM users WHERE id IN(?, ?)", param)
print(c.fetchall())
```
```
c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % param)
print(c.fetchall())
```
```
c.execute("SELECT * FROM users WHERE id=:Id1 OR id=:Id2", {"Id1":3, "Id2": 5})
print(c.fetchall())
```

</br>

## Dump 출력: 데이터베이스 백업해두기
#
```
with conn:
    with open("backup_db.txt", "w") as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print("Dump Print Complete")
```
덤프를 떠옴으로써 다른 곳에 데이터베이스를 쉽게 구축할 수 있다. 


</br></br></br>

# 테이블 수정 삭제 

## UPDATE
```
c.execute("UPDATE users SET username = ? WHERE id = ?",("seung", 2))
```
```
c.execute("UPDATE users SET username = :name WHERE id = :id", {"name": "goodman", "id": 3})
```
```
c.execute("UPDATE users SET username='%s' WHERE id='%s'" % ("seung", 3))
```

</br>

## 데이터 확인하기 
#
```
for user in c.execute("SELECT * FROM users"):
    print(user)
```

</br>

## DELETE
#
```
c.execute("DELETE FROM users WHERE id=?",(2,))
```
```
c.execute("DELETE FROM users WHERE id='%d'", (3, ))
```
```
c.execute("DELETE FROM users WHERE id=:ID", {"ID":5})
```

</br>
