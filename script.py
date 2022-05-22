#!/usr/bin/env python3
from pwn import *

URL="bf40dd29fe66a488.247ctf.com"
PORT=50497


r = remote(URL,PORT)


print(r.recvline())

print(r.recvline())

for i in range(500):
	problem = r.recvline().decode("utf-8") 	
	
	# print(problem)

	split = problem.split() # ['What', 'is', 'the', 'answer', 'to', '64', '+', '491?']

	a = int(split[5])		# '64' -> 64
	b = int(split[7].strip('?')) 	# '491?' -> 491

	answer = (str(a+b)+'\r\n').encode("utf-8")
	# print(answer)
	r.sendline(answer)

	r.recvline() # b'Yes, correct!\r\n'


flag = r.recvline().decode("utf-8").strip('\r\n')


print(flag)


r.close()


print("""
SUBSCRIBE MY YT CHANNEL:- https://www.youtube.com/channel/UCdEAvbBJVPw29L-FZMt5rQA/

""")

