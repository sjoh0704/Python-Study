import sqlite3
import datetime
# print(sqlite3.version)


now = datetime.datetime.now()
nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")

print(nowDateTime)

#  DB 생성, Auto commit(rollback)




# 현재 위치한 디렉토리안에 생성
# 존재한다면 생성하지 않고 존재한다면 연결 
conn = sqlite3.connect("test.db", isolation_level=None)

# cursor를 통해서 데이터를 읽어오고 읽을 데이터가 없으면 Null
c = conn.cursor()


# 테이블 생성
# data type: text, numeric integer real blob
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, \
    username text, email text, phone text,  website text, regdate text) ")

# 큰따옴표안에 작은 따옴표를 써주어야 한다. 
c.execute("INSERT INTO users VALUES(1, 'oh', 'sjoh0704@daum.net', '01012341234','github.com/sjoh0704', ?)", (nowDateTime,))
c.execute("INSERT INTO users VALUES(2, 'oh', 'sjoh0704@daum.net', '01012341234','github.com/sjoh0704', ?)", (nowDateTime,))
c.execute("INSERT INTO users VALUES(3, 'oh', 'sjoh0704@daum.net', '01012341234','github.com/sjoh0704', ?)", (nowDateTime,))
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?, ?, ?, ?, ?, ?)", (4,  'oh', 'sjoh0704@daum.net', '01012341234','github.com/sjoh0704', nowDateTime))


# 트플이나 리스트로 처리하는것이 가장 많이 쓰이는 방식
# 웹 크롤링에서 가져온 데이터를 처리하는데 많이 사용  
userList = ((5, 'oh', 'sjoh0704@daum.net', '01012341234','github.com/sjoh0704', nowDateTime)
,(6, 'oh', 'sjoh0704@daum.net', '01012341234','github.com/sjoh0704', nowDateTime)
,(7, 'oh', 'sjoh0704@daum.net', '01012341234','github.com/sjoh0704', nowDateTime)
)
c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)", userList )


# 테이블 삭제하기 
# conn.execute("DELETE FROM users")

# 삭제하면서 보기
# print('users db deleted',conn.execute("DELETE FROM users").rowcount )



# 커밋 : isolation_level=none일 경우 자동 반영(auto commit)_
# 만약 설정하지 않을 경우, conn.commit()을 따로 해주어야 한다. 

# 커밋과 롤백은 실행되는 시점이 중요하다. 



#접속 해제 
conn.close()
