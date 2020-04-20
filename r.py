import random

r = random.randint(1, 100)

while True:
	num = input('請輸入數字: ')
	num = int(num)

	if num == r:
		print('你答對了')
		break
	elif num > r:
		print('猜小一點')
	elif num < r:
		print('猜大一點')	