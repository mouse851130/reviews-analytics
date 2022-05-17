data = []  #建立空清單，等等才能放資料

count = 0 #每一千筆的計數器
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:    #"%"是餘數的概念，代表count跟1000的餘數為0時，才print
		    print(len(data)) 
#現在要算留言平均長度

sum_len = 0 #一開始留言的長度總和是0
for d in data:
	sum_len = sum_len + len(d) #是d，不是data，如果是data，就是一次把全部資料加進去
#有了總和之後，就可以求平均
#也就是拿總長除以所有留言(一百萬筆)

平均 = print('平均留言長度為：', sum_len / len(data))
