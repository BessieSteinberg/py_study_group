# A commom cause of deadlock is acquiring a thread and not 
# releasing it. For example...
from threading import Lock

lock = Lock()

def do_other_stuff():
	raise Exception('Exception you forgot about! WHEEE!')

def do_something():
	lock.acquire()
	try:
		do_other_stuff()
	finally:
		lock.release()

try:
	do_something()
except Exception as e:
	print(e)

print("later in the code...")

try:
	do_something()
except Exception as e:
	print(e)

print("do more stuff...")
