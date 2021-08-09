f = open(file="baidu_x_system.log",mode="r+",encoding="utf-8")
data=f.readlines()
rows = len(data)
list = {}
count = 1
for i in range(rows):
    part = data[i].split(' ', 1)
    if part[0] in list:
        list[part[0]]['count'] = list[part[0]]['count'] + 1
        list[part[0]] = {
            'count': list[part[0]]['count']
        }

    else:
        list[part[0]] = {
            'count': count
        }
print(list)