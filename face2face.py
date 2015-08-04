#!/usr/bin/env python
# -*- coding: utf-8 -*-
#demo: face 2 face
#by Dmitry Gusev
#dep: random
#v0.1

import random

class fighter(object):
	def __init__(self,lst):
		self.name = lst["name"]
		self.health = lst["health"]
		self.hit = lst["hit"]
		self.chance = lst["chance"]
		self.full_health=self.health
		print "Боец создан"
		
	def get_status(self):
		print "%s имеет %s/%s здоровья" % (self.name,self.health,self.full_health)
		
	def decrease_health(self,damage):
		self.health -= damage
		
	def hit_face(self):
		if self.chance >= random.randint(0,100):
			return True
		
def create_fighter_manual():
	lst={}
	lst["name"] = raw_input("Введите имя: ")
	lst["health"] = int(raw_input("Введите количество хит-поинтов: "))
	lst["hit"] = int(raw_input("Введите показатель урона: "))
	lst["chance"] = int(raw_input("Введите показатель меткости: "))
	return lst
	
	
"""
Welcoming
"""
print "Битва лицо на лицо"

"""
Choose hero stats
"""
print "создание вашего персонажа"
stats_your = create_fighter_manual()
you = fighter(stats_your)
print "-------------------------"


"""
Choose enemy stats
"""
print
print "создание противника"
stats_oppenent= create_fighter_manual()
opponent = fighter(stats_oppenent)
print "-------------------------"


"""
Fight
"""
print
print "да начнется битва!"
somebody_dead = False
turn = 1
while not somebody_dead:
	print "#####"
	print "Ход",turn
	print "Ваш ход:"
	wait=raw_input("Бей! ")
	if wait == 'q':
		break
		
	if you.hit_face():
		print "Вы попали"
		opponent.decrease_health(you.hit)
		opponent.get_status()
		if opponent.health <= 0:
			print "Вы выиграли!"
			break
	else:
		print "Вы промазали"
	turn += 1
	print
	
	print "Ход противника"
	if opponent.hit_face():
		print "Противник попал, вы раненны на",opponent.hit
		you.decrease_health(opponent.hit)
		you.get_status()
		if you.health <= 0:
			print "Ваш персонаж погиб"
			break
	else: 
		print "Противник промазал"
print "-------------------------"
print "Всем спаибо, все свободны"
	