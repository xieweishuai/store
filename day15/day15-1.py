
from day15.DBUtils import update

f = open(file="用户数据",mode="r+",encoding="utf-8")
data=f.readlines()
print(data)
sum0=0
sum=[]
for i in range(len(data)):
    sum.append(data[i].split(",",2))

    sum0=sum0+int(sum[i][2])
    sql = "insert into customer values(%s,%s,%s)"
    update(sql,sum[i])
print(sum)
print(sum0)