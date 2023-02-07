#!/usr/bin/env python
# _*_ coding:Utf-8 _*_
from math import *
#from turtle import *
# Exercice 5.11
def main():
	t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décedmbre']
	t3 = []
	print t1, t2, t3
	i = 0
	while i < len(t1):
		t3.append(t2[i]), t3.append(t1[i])
		i = i + 1
	print t3
#Exercice 5.12
	j = 0
	while j < len(t2):
		print(t2[j]),
		j = j + 1
#Exercice 5.13
	liste = [32, 5, 12, 8, 3, 75, 2, 15]
	k = 1
	grand = liste[1]
	while k < len(liste):
		if liste[k] > grand:
			grand= liste[k]
		k = k + 1
	print "\nLe plus grand élément est ", grand
	if (40%6):
		print"vrai"
	else:
		print"faux"
#Exercice 6
	print "\nEntrer une valeur.. :",
	nbre = raw_input()
	print(nbre)
	print(int(nbre))
#Exercice 6.2
	print "\nEntrer trois valeurs : ",
	a = input()
	b = input()
	c = input()
	d = abs((a + b + c)/2)
	s = sqrt(d*(d-a)*(d-b)*(d-c))
	print "\nLe périmètre = ", d*2, "L'air = ", s
#Exercice 6.4
	val = raw_input("Donner une valeur : ")
	liste = []
	while val != "":
		liste.append(int(val))
		val = raw_input("Donner une valeur : ")
	print liste	
	
	
main()

 