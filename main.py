#Shivanshu Jain	2019101001	UG-1, 2nd Semester	ISS Assignment 3
import pygame
import math
import time

#Initialize pygame library
pygame.init()

#Create the screen
displaywidth = 800
displayheight = 600
screen = pygame.display.set_mode((displaywidth,displayheight))

#Clock
clock = pygame.time.Clock()

#Title of window and icon
pygame.display.set_caption("Shivanshu's Game")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Declaring standard colors
ground = (219,197,165)
water = (0,0,255)
scorecolor = (255,255,255)
black = (0,0,0)

#Creating object of type player
playerImg = pygame.image.load('player.png')
playerx = 368
playery = 570
playerdx = 0
playerdy = 0
def player(x,y):
	screen.blit(playerImg,(x,y))


#Created an object of type ship
shipImg = pygame.image.load('ship.png')
shipx = []
shipy = 380		#Just a constant fixed value to define other ships' location
shipspeed = 0.1
shipdx = []
for i in range(5):
	shipx.append(50*i)
	shipdx.append(shipspeed)
def ship(x,y):
	screen.blit(shipImg,(x,y))


#Printing the fixed obstacle(ie mountain)
def mountain(x,y):
	mountainimg = pygame.image.load('obst.png')
	screen.blit(mountainimg,(x,y))

#Printing the score
score = 0
font = pygame.font.Font('freesansbold.ttf',20)
textx = 10
texty = 10
def printscore(x,y):
	scoreonscreen = font.render("Score: "+ str(score),True,scorecolor)
	screen.blit(scoreonscreen,(x,y))


#Collision detection
def didcollide(shipx,shipy,playerx,playery):
	dist = math.sqrt( ( math.pow(shipx-playerx,2) ) + ( math.pow(shipy-playery,2) ) )
	if dist < 35:
		return True


#Print start and end
def start():
	start = font.render("START",True,black)
	screen.blit(start,(360,580))
def end():
	end = font.render("END",True,black)
	screen.blit(end,(360,10))


def text_objects(text,font):
	textSurface = font.render(text,True,black)
	return textSurface, textSurface.get_rect()
	

def message(text):
	displayfont = pygame.font.Font('freesansbold.ttf',64)
	TextSurf, TextRect = text_objects(text, displayfont)
	TextRect.center = ((displaywidth/2),(displayheight/2))
	screen.blit(TextSurf,TextRect)
	pygame.display.update()
	return 0
	#time.sleep(0.5)


def changelevel():
	global shipspeed
	shipspeed += 1
	for i in range(level):
		gameloop()	


#Game loop
def gameloop():

	running = True

	while running:

		global score
		global playerx
		global playery
		global playerdx
		global playerdy
		global shipx
		global shipy
		global shipdx
		global shipspeed
		global textx
		global texty
		
		screen.fill(water)
		screen.fill(ground,(0,550,screen.get_width(),82))
		screen.fill(ground,(0,450,screen.get_width(),32))
		screen.fill(ground,(0,350,screen.get_width(),32))
		screen.fill(ground,(0,250,screen.get_width(),32))
		screen.fill(ground,(0,150,screen.get_width(),32))
		screen.fill(ground,(0,0,screen.get_width(),32))


		for event in pygame.event.get():
			
			#Quitting game on pressing x button
			if event.type == pygame.QUIT:
				running = False

			#Changing position of player
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					playerdx = -0.3
				if event.key == pygame.K_RIGHT:
					playerdx = 0.3
				if event.key == pygame.K_UP:
					playerdy = -0.3
				if event.key == pygame.K_DOWN:
					playerdy = 0.3

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					playerdx = 0
				if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
					playerdy = 0


		#Position changing of player
		playerx += playerdx
		playery += playerdy
		if playerx < 0:
			playerx = 0
		elif playerx > 736:
			playerx = 736		# = 800-img size(=64)

		if playery < 0:
			playery = 0
		elif playery > 570:
			playery = 570

		#Position changing of the ships
		for i in range(5):
			shipx[i] += shipdx[i]
			if shipx[i] > 800:
				shipx[i] = 0

			

		#Printing the things on the screen
		player(playerx,playery)
		ship(shipx[0],shipy+100)
		ship(shipx[1],shipy)
		ship(shipx[2],shipy-100)
		ship(shipx[3],shipy-200)
		ship(shipx[4],shipy-300)
		ship(shipx[2],shipy-362)		#Only for variety
		mountain((displaywidth/2),430)
		mountain((displaywidth/2)-100,330)
		mountain((displaywidth/2)-300,230)
		mountain((displaywidth/2)+200,130)


		#Printing the score
		printscore(textx,texty)
		#score+=1		#Very useless
		start()
		end()

		#Collision checking
		collision1 = didcollide(shipx[0],shipy+100,playerx,playery)		#Collide with ship1 ie bottommost ship
		collision2 = didcollide(shipx[1],shipy,playerx,playery)			#Collide with ship2
		collision3 = didcollide(shipx[2],shipy-100,playerx,playery)		#Collide with ship3
		collision4 = didcollide(shipx[3],shipy-200,playerx,playery)		#Collide with ship4
		collision5 = didcollide(shipx[4],shipy-300,playerx,playery)		#Collide with ship5 ie topmost ship
		collision6 = didcollide((displaywidth/2),430,playerx,playery)
		collision7 = didcollide((displaywidth/2)-100,330,playerx,playery)
		collision8 = didcollide((displaywidth/2)-300,230,playerx,playery)
		collision9 = didcollide((displaywidth/2)+200,130,playerx,playery)
		if collision1 or collision2 or collision3 or collision4 or collision5 or collision6 or collision7 or collision8 or collision9:
			shipy = 3000		#Out of sight, out of mind
			message('GAME OVER')
			running = False


		if playery < 32 :
			message('Congratulations')
			changelevel()

		pygame.display.update()
		clock.tick(1000000000)		#Very good addition
		#pygame.quit()
		#quit()

#Calling the damn function
gameloop()