import time

name = raw_input("what is your name?")
if name == "Kelvin":
	print "hello, {0}".format(name)
	print "Today is ", time.strftime("%m / %d / %Y")
else:
	print "get off my computer!"
	exit()
