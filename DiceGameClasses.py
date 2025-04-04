import random

class Die:
	def __init__(self, numberOfSides):
		self.numberOfSides = numberOfSides
		self.faceUpValue = 1
		
	def roll(self):
		self.faceUpValue = random.randint(1, self.numberOfSides)
			
	def getValue(self):
		return self.faceUpValue
		
	def __str__(self):
		return f"This is the Die class with a face up value of {self.getValue()} and number of sides {self.numberOfSides}"

	def __gt__(self, other):
		return self.faceUpValue > other.faceUpValue

class Player:
	def __init__(self, name):
		self.name = name
		self.die1 = Die(6)
		self.die2 = Die(10)
		
	def rollDice(self):
		self.die1.roll()
		self.die2.roll()
	def getDiceValue(self):
		return self.die1.getValue() + self.die2.getValue()
	def __str__(self):
		return f"This is the Player class with the dice value of {self.getDiceValue()}"
	def __gt__(self,other):
		return self.getDiceValue() > other.getDiceValue()

	

class HighTwoGame:
	def __init__(self, playerName, playerTwoName):
		self.playerOne = Player(playerName)
		self.playerTwo = Player(playerTwoName)
	def playOneGame(self):
		self.playerOne.rollDice()
		self.playerTwo.rollDice()
	
		print(self.playerOne.name, "rolled", self.playerOne.getDiceValue())
		print(self.playerTwo.name, "rolled", self.playerTwo.getDiceValue())
		print("\n")
		if (self.playerOne.getDiceValue() > self.playerTwo.getDiceValue()):
			return 1
		elif (self.playerOne.getDiceValue() == self.playerTwo.getDiceValue()):
			return 0
		else:
			return -1
	def playManyGames(self, games):
		player_one_wins = 0
		player_two_wins = 0
		ties = 0
		
		for _ in range (games):
			result = self.playOneGame()
			if result == 1:
				player_one_wins += 1
			elif result == -1:
				player_two_wins +=1
			else:
				ties+=1
				
		print("Score:", player_one_wins, "to", player_two_wins)
		if (player_one_wins > player_two_wins):
			print(f"{self.playerOne.name} wins!")
		elif (player_two_wins > player_one_wins):
			print(f"{self.playerTwo.name} wins!")
		else:
			print("Its a tie overall")
			
		

		
		
		

