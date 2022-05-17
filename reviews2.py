data = []  #建立空清單，等等才能放資料

count = 0 #每一千筆的計數器
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
		    print(len(data)) #每印一筆資料，就顯示目前的資料長度。
print(len(data))  #列出data的長度
print(data[0]) #列出第一筆留言
print('------------------') #分隔號
print(data[1]) #第二筆留言

