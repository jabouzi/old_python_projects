#!/usr/bin/env python
# _*_ coding:Utf-8 _*_
import commands
data = commands.getoutput("ls -l")

def main():
	a = 1
	b = 1
	while a <= 7:
		while b <= a:
			print "*",
			b = b + 1
		print "\n",
		a, b = a + 1, 1
	print data
# ce programme imprime un triangle en étoiles

def calc():
    a = 2
    b = 1
    while b < 100:
        a = a**b
        b = b + 1
        print a
        print "\n"
        print str(b) + " ==========\n"

main()
calc()

