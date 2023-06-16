import psycopg2

conn = psycopg2.connect(database='main',user='postgres',password='4567')

cur = conn.cursor()
cur.execute("delete from narodnii where day_to_expire <= 2")
cur.execute("select * from narodnii where day_to_expire <= 3")
answer = cur.fetchall()
conn.commit()
for i in answer:
    print(i)

cur.close()
conn.close()
