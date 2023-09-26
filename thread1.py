import threading as t

def starting():
	global num
	while True:
		num = num + 1
		print(num)

for i in range(500):
	started = t.Thread(target=starting)
	started.start()
