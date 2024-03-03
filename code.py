import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol = "!@#$^&*>_"
number = "1234567890"

all=lower+upper+number+symbol
length = 10
password = "".join(random.sample(all,length))

print(password)