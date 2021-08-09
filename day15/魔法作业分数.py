file = (open('scores.txt', 'r+', encoding='utf-8')).readlines()
rows = len((open('scores.txt', 'r+', encoding='utf-8')).readlines())  # 获取行数
sum = 0
for i in range(rows):
    cols = len(file[i])  # 获取列数
    part = file[i].split(' ', cols)  # 进行分割
    col = len(part)  # 获取列数
    for j in range(1, col):
        count = int(part[j])
        sum += count
print(sum)
(open('scores.txt', 'a', encoding='utf-8')).write('\n总得分为：' + str(sum))