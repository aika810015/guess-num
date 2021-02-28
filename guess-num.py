import random
r = random.randint(1, 100)
while True:
	num = int(input("数字を考えてください："))
	if num == r:
		print("当たり！！")
		break
	elif num > r:
		print("正解より多いですね！")
	elif num < r:
		print("正解より少ないですね！")

	
