

import pygame
import random
import time as time_
import copy

#Setting up screen
pygame.init()
screen = pygame.display.set_mode((1200, 800))

#Variables
continuer = True
nbColones = 10
nbRangees = 20
pixelsPerSquare = 32
leftXOfMap = 500
time = 0
clock = pygame.time.Clock()
dt = 0
points = 0
myFont = pygame.font.SysFont("Times New Roman", 25)
numOfForm = 0
lines = 0

carte  = [
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,"n", "n", "n"],
		["n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"],
		]

#classes
class O_Block:
	currentX = 660
	currentY = 64
	c = "jaune"
	dispositions = [
					[  [],[],[],[]  ],
					[  [],[c],[c],[]  ],
					[  [],[c],[c],[]  ],
					[  [],[],[],[]  ]
					]
	currentRotation = 0
	maxRotations = len(dispositions)
	
class L_Block:
	currentX = 660
	currentY = 64
	c = "orange"
	dispositions =  [
					[
					[  [], [c], []  ],
					[  [], [c], []  ],
					[  [], [c], [c]  ]
					],
					[
					[  [], [], [c]  ],
					[  [c], [c], [c]  ],
					[  [], [], []  ]
					],
					[
					[  [c], [c], []  ],
					[  [], [c], []  ],
					[  [], [c], []  ]
					],
					[
					[  [], [], []  ],
					[  [c], [c], [c]  ],
					[  [c], [], []  ]
					]
					]
	currentRotation = 0
	maxRotations = len(dispositions)
	
class J_Block:
	currentX = 660
	currentY = 64
	c = "blue"
	dispositions = [
					[
					[  [], [c], [c]  ],
					[  [], [c], []  ],
					[  [], [c], []  ]
					],
					[
					[  [c], [], []  ],
					[  [c], [c], [c]  ],
					[  [], [], []  ]
					],
					[
					[  [], [c], []  ],
					[  [], [c], []  ],
					[  [c], [c], []  ]
					],
					[
					[  [], [], []  ],
					[  [c], [c], [c]  ],
					[  [], [], [c]  ]
					]
					]
	currentRotation = 0
	maxRotations = len(dispositions)
	
class I_Block:
	currentX = 660
	currentY = 64
	c = "cyan"
	dispositions =  [
					[ 
					[  [],[],[],[]  ],
					[  [],[],[],[]  ],
					[  [c],[c],[c],[c]  ],
					[  [],[],[],[]  ]
					],
					[
					[  [],[],[c],[]  ],
					[  [],[],[c],[]  ],
					[  [],[],[c],[]  ],
					[  [],[],[c],[]  ]
					]
					]
	currentRotation = 0
	maxRotations = len(dispositions)

	
class S_Block:
	currentX = 660
	currentY = 64
	c = "green"
	dispositions = [
					[
					[  [], [], []  ],
					[  [], [c], [c]  ],
					[  [c], [c], []  ]
					],
					[
					[  [], [c], []  ],
					[  [], [c], [c]  ],
					[  [], [], [c]  ]
					]
					]
	currentRotation = 0
	maxRotations = len(dispositions)
	
class Z_Block:
	currentX = 660
	currentY = 64
	c = "purple"
	dispositions = [
					[
					[  [], [], []  ],
					[  [c], [c], []  ],
					[  [], [c], [c]  ]
					],
					[
					[  [], [], [c]  ],
					[  [], [c], [c]  ],
					[  [], [c], []  ]
					]
					]
	currentRotation = 0
	maxRotations = len(dispositions)

	
class T_Block:
	currentX = 660
	currentY = 64
	c = "red"
	dispositions = [
					[
					[  [], [], []  ],
					[  [c], [c], [c]  ],
					[  [], [c], []  ]
					],
					[
					[  [], [c], []  ],
					[  [c], [c], []  ],
					[  [], [c], []  ]
					],
					[
					[  [], [c], []  ],
					[  [c], [c], [c]  ],
					[  [], [], []  ]
					],
					[
					[  [], [c], []  ],
					[  [], [c], [c]  ],
					[  [], [c], []  ]
					]
					]
	currentRotation = 0
	maxRotations = len(dispositions)
	
#Fonctions

def drawForm(form, nextForm = False):
	disposition = form.dispositions[form.currentRotation]
	x = form.currentX
	y = form.currentY
	if nextForm == True:
		x = 950
		y = 100

	for rangee in disposition:
		for element in rangee:
			if len(element) != 0:
				pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, pixelsPerSquare, pixelsPerSquare))
				pygame.draw.rect(screen, returnColor(element[0]), pygame.Rect(x, y, pixelsPerSquare - 1, pixelsPerSquare - 1))
			x += pixelsPerSquare
		x = form.currentX
		if nextForm == True:
			x = 950
		y += pixelsPerSquare


def returnColor(color):
	if color == "purple":
		return (118, 96, 172)
	elif color == "red":
		return (239, 29, 29)
	elif color == "orange":
		return (239, 113, 29)
	elif color == "cyan":
		return (29, 239, 239)
	elif color == "blue":
		return (77, 96, 172)
	elif color == "jaune":
		return (239, 29, 29)
	elif color == "green":
		return (29, 239, 64)
	else:
		return (123,123,123)

def pickAForm():
	formNumber = random.randint(1,6)

	
	if formNumber == 0: 
		return O_Block()
	elif formNumber == 1: 
		return L_Block()
	elif formNumber == 2: 
		return J_Block()
	elif formNumber == 3: 
		return I_Block()
	elif formNumber == 4: 
		return S_Block()
	elif formNumber == 5: 
		return Z_Block()
	elif formNumber == 6: 
		return T_Block()

def addGravityToForm(form, time):
	dt = clock.tick(30) / 500
	time += dt
	addNewForm = False
	if time > 1:
		global points
		#points += 10
		form.currentY += pixelsPerSquare
		value = verifieIfFormOverlapWithMap(form)
		if value == True:
			#Donc si on a touché le sol
			form.currentY -= pixelsPerSquare
			addNewForm = True
			

		time = 0
	return time, addNewForm

def moveFormRight(form):
	form.currentX += 32
	value = verifieIfFormOverlapWithMap(form)
	if value == True:
		form.currentX -= 32

def moveFormLeft(form):
	form.currentX -= 32
	value = verifieIfFormOverlapWithMap(form)
	if value == True:
		form.currentX += 32

def rotateForm(form):
	form.currentRotation += 1
	if form.currentRotation == form.maxRotations:
		form.currentRotation = 0
	value = verifieIfFormOverlapWithMap(form)
	if value == True:
		if form.currentRotation == 0:
			form.currentRotation = form.maxRotations - 1
		else:
			form.currentRotation -= 1
	

def goDownFasterForm(form):
	form.currentY += 32
	value = verifieIfFormOverlapWithMap(form)
	if value == True:
		form.currentY -= 32
		return True
	return False

def verifieIfFormOverlapWithMap(form):
	disposition = form.dispositions[form.currentRotation]
	xIndex = (form.currentX - 500) / 32
	yIndex = (form.currentY - 64) / 32
	returnValue = False
	counterX = 0
	counterY = 0
	for colone in disposition:
		for element in colone:
			if len(element) != 0 and carte[int(yIndex) + counterY][int(xIndex) + counterX] != 0:
				returnValue = True
			counterX += 1

		counterY += 1
		counterX = 0
	return returnValue



def blitMap():
	x = leftXOfMap
	y = 64
	for colone in carte:
		for element in colone:
			if element != 0:
				pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, pixelsPerSquare, pixelsPerSquare))
				pygame.draw.rect(screen, returnColor(element), pygame.Rect(x, y, pixelsPerSquare - 1, pixelsPerSquare - 1))
			x += pixelsPerSquare
		x = leftXOfMap
		y += pixelsPerSquare



def addNewFormFunc(form):

	print("ONE ITERATION", type(form))
	
	xIndex = (form.currentX - 500) / 32
	yIndex = (form.currentY - 64) / 32
	counterX = 0
	counterY = 0
	disposition = form.dispositions[form.currentRotation]
	for colone in disposition:
		if numOfForm > 43:
			print(colone)
		for element in colone:
			if len(element) != 0:
				if numOfForm > 40:
					print(carte)
					print(carte  [int(yIndex) + counterY]   [int(xIndex) + counterX])
				carte  [int(yIndex) + counterY]   [int(xIndex) + counterX] = element[0]
				if numOfForm > 40:
					print("element", element[0])
					print(carte)
			counterX += 1

		counterY += 1
		counterX = 0

	if numOfForm > 43:
		print("xIndex", xIndex)
		print("yIndex", yIndex)
		print("counterX", counterX)
		print("counterY", counterY)
		print("currentRotation", form.currentRotation)
		print("disposition", disposition)
		print("form.dispositions.lenght", len(form.dispositions))

def verifyIfFullRow():
	fullColoneIndex = 0
	global lines

	for colone in carte:
		NbOfElements = 0
		for element in colone:
			if element != 0 and element != "n":
				NbOfElements += 1
			if NbOfElements >= 10:
				fullColoneIndex = carte.index(colone)
				global points
				points += 100
				lines += 1
				break


	for num in range(0, fullColoneIndex):
		if num != fullColoneIndex:
			carte[fullColoneIndex - num] = carte[fullColoneIndex - num - 1]

def verifieIfGameOver():
	global points
	global continuer
	for element in carte[1]:
		if element != "n" and element != 0:
			continuer = False
			print("ENDED")
			print(str(points) + "points")

def drawPoints():
	global points
	pointsDisplay = myFont.render("Points : " + str(points), 1, (255, 255, 255))
	screen.blit(pointsDisplay, (950, 230))

def movePieceAleatory(testingForm):
	global numOfForm
	numOfForm += 1
	print(numOfForm)
	print(lines)
	

	
	#Points value for current highness
	currentHighPointsValue = 0
	for colone in carte:
		for element in colone:
			if element != 0 and element != "n":
				currentHighPointsValue += carte.index(colone) * 3

	#Current holes value
	currentHolesValue = 0
	inversedMap = []
	for num in range(0, len(carte[0]) - 1):
		toAdd = []
		for colone in carte:
			toAdd.append(colone[num])
		inversedMap.append(toAdd)

	#Removing points for holes
	for colone in inversedMap:
		hasFind = False
		for element in colone:
			if element != 0 and element != "n":
				hasFind = True

			if element == 0:
				if hasFind == True:
					currentHolesValue -= 10000

	possibleOptions = []
	#Start by iterating through each rotations to get the best one
	for rotation in testingForm.dispositions:
		for num in range(0, 13): #All Possibles placement
			testingForm.currentX = 500 + (num * pixelsPerSquare)
			testingForm.currentRotation = testingForm.dispositions.index(rotation)
			if verifieIfFormOverlapWithMap(testingForm) == True:
				continue

			#Make it the more down possible to the ground
			isTouchingGround = False
			while isTouchingGround == False:
				isTouchingGround = goDownFasterForm(testingForm)

			#Putting the more down


			#CALCULATES POINTS
			placementValue = 0

			#Calculate map
			testingMap = copy.deepcopy(carte)

			xIndex = (testingForm.currentX - 500) / 32
			yIndex = (testingForm.currentY - 64) / 32
			counterX = 0
			counterY = 0
			disposition = testingForm.dispositions[testingForm.currentRotation]
			for colone in disposition:
				for element in colone:
					if len(element) != 0:
						testingMap[int(yIndex) + counterY][int(xIndex) + counterX] = element[0]
					counterX += 1

				counterY += 1
				counterX = 0

			#Calculate height
			withFormHighValue = 0
			for colone in testingMap:
				for element in colone:
					if element != 0 and element != "n":
						#if testingMap.index(colone) < highestPoint:
							#highestPoint = testingMap.index(colone)
						withFormHighValue += testingMap.index(colone) * 3
			placementValue += withFormHighValue - currentHighPointsValue

			#Calculate lines
			for colone in testingMap:
				elementCount = 0
				for element in colone:
					if element != 0 and element != "n":
						elementCount += 1
				if elementCount >= 10:
					placementValue += 1000

			#Calculate holes
			withFormHolesValue = 0
			#Create inversed map
			inversedMap = []
			for num in range(0, len(testingMap[0]) - 1):
				toAdd = []
				for colone in testingMap:
					toAdd.append(colone[num])
				inversedMap.append(toAdd)

			#Removing points for holes
			for colone in inversedMap:
				hasFind = False
				for element in colone:
					if element != 0 and element != "n":
						hasFind = True

					if element == 0:
						if hasFind == True:
							withFormHolesValue -= 10000

			placementValue += withFormHolesValue - currentHolesValue

			#Calculate bumpiness



			#Add Option
			possibleOptions.append([testingForm.currentX, testingForm.currentY, testingForm.dispositions.index(rotation), placementValue])

	#choosenPlacement = random.choice(possibleOptions)

	#Chose option by the highest points number
	bestOption = [0,0,0,-100000] #Random stupid placement to start with super low score to be sure it doesnt put at [0, 0]
	for placement in possibleOptions:
		if placement[3] > bestOption[3]:
			bestOption = placement

	testingForm.currentX = bestOption[0]
	testingForm.currentY = bestOption[1]
	testingForm.currentRotation = bestOption[2]



#Set up for game start
currentForm = pickAForm()
testingFormForAi = currentForm
nextForm = pickAForm()
movePieceAleatory(testingFormForAi)


#Boucle de jeu
while continuer:
	
	screen.fill((0, 0, 0))
	blitMap()
	#drawForm(nextForm, True)
	drawForm(currentForm, False)
	drawPoints()
	
	pygame.display.flip()
	time, addNewForm = addGravityToForm(currentForm, time)
	if addNewForm == True:
		#time_.sleep(0.5)
		addNewFormFunc(currentForm)
		#currentForm = nextForm
		currentForm = pickAForm()
		testingFormForAi = currentForm
		nextForm = pickAForm()
		#movePieceAleatory(testingFormForAi)



	verifyIfFullRow()
	#verifieIfGameOver()

	


	#Gestion des events

	key_pressed = pygame.key.get_pressed()
	if key_pressed[pygame.K_DOWN]:
		goDownFasterForm(currentForm)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer = False

		if event.type == pygame.KEYDOWN:

			##si on appuie sur la fleche de droite, on bouge le bloc vers la droite
			if event.key == pygame.K_RIGHT:
				moveFormRight(currentForm)
			if event.key == pygame.K_LEFT:
				moveFormLeft(currentForm)
			if event.key == pygame.K_UP:
				rotateForm(currentForm)
			if event.key == pygame.K_SPACE:
				movePieceAleatory(testingFormForAi)
			if event.key == pygame.K_p:
				print(carte)


