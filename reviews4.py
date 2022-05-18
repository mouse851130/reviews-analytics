data = []  #建立空清單，等等才能放資料

count = 0 #每一千筆的計數器
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line) 
#現在要"篩選"長度小於100的留言：用 < 100來看
#先建立新清單，字串也可以當作清單

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('有', len(new), '筆資料長度小於100')
print(new[1])
