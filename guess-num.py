import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1
	num = int(input("数字を考えてください："))
	if num == r:
		print("当たり！！")
		print("今回は", count, "回目です！")
		break
	elif num > r:
		print("正解より多いですね！")
	elif num < r:
		print("正解より少ないですね！")
	print("今回は", count, "回目です！")

	
