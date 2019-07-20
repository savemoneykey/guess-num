import random
start = input('請選擇開始範圍: ')
end = input('請選擇結束範圍: ')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True :
	count += 1
	num = input('請猜數字')
	num = int(num)
	if num == r :
		print('猜中了')
		print('這是你猜得',count,'次')
		break
	elif num > r :
		print('比數字大')
	elif num < r : 
		print('比數字小')
	print('這是你猜得',count,'次')
