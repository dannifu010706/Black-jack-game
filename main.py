#The program is made by Nifu Dan, and will allow users to play Black jack



import random
#The function set up something basic for the program


#  creates lists of ranks, values and suits for the cards.
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
values = [11,2,3,4,5,6,7,8,9,10,10,10,10]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]



#  creates the class "card", which contains two functions.
class card:


  # sets up a card given the suit and rank.
  def __init__(self,suit,rank):
    self.suit = suit
    self.rank = rank
    self.value = values[ranks.index(rank)]


  #  return a string of the card suit and rank.
  def cardInfo(self):
    return f"({self.suit} {self.rank})"



# creates the class "deck"
class deck:


  # n creates a new deck of 52 cards
  def __init__(self):
    self.cards = [card(s,r) for s in suits for r in ranks]


  # The function shuffle the deck
  def shuffle(self):
    random.shuffle(self.cards)


  # This function draws a card, removes it from the deck and returns it
  def draw(self):
    c=self.cards.pop()
    return (c)



# The function creates the class hand.
class hand:


  # The function create a hand
  def __init__(self,owner="Player"):
    self.cards = []
    self.owner = owner


  # The function adds a card to the hand.
  def add(self,card):
    self.cards.append(card)


  # This function prints out the first card in the hand.
  def showFirst(self):
    print(f"{self.cards[0].cardInfo()}")
    


  # The function prints the cards in hand.
  def cardList(self):
    for i in self.cards:
      print(f"{i.cardInfo()}",end=" ")


  # The function below prints the given player
  def showHand(self):
    if self.owner == "Player":
      print("Your hand:",end=" ")
      self.cardList()
      print("Total:", self.tally())
    elif self.owner == "Dealer":
      print("The Dealer is showing",end=" ")
      self.showFirst()
    else:
      print("I'm confused about who owns the hand")


  # This function add all the values of the carfs in hand 
  def tally(self):
    sum = 0
    for c in self.cards:
      sum += c.value
    "This code is incomplete. Must count aces, and if the tally is greater than 21 subtract 10 for each ace to try to get below 22"
    for j in self.cards:
      if j.suit == "Ace" and sum > 21:
        sum-=10
    return sum



# Start a new game b using the function below
def newgame():
  print("Dealing new cards")
  global deck, dealer_hand , player_hand, thedeck
  thedeck = deck()
  thedeck.shuffle()
  dealer_hand = hand("Dealer")
  dealer_hand.add(thedeck.draw())
  dealer_hand.add(thedeck.draw())
  player_hand = hand("Player")
  player_hand.add(thedeck.draw())
  player_hand.add(thedeck.draw())



# The function below will create a game and allow users to play it
def game():
  newgame()
  stand=False

  while dealer_hand.tally()<21 and player_hand.tally()<21 and not stand:
    dealer_hand.showHand()
    player_hand.showHand()
    print()
    if not stand:
      c = input("[H]it or [S]tand:").lower()
      print()
      if c == 'h':
       
        card=thedeck.draw()
        print("You Draw:",f"{card.cardInfo()}")
        player_hand.add(card)
      elif c == 's': # Stand
        stand=True
    if not dealer_hand.tally() > 17: 
      dealer_hand.add(thedeck.draw())
  
  #This part of function shows some information of the players
  print("The Dealer:",end=" ")
  dealer_hand.cardList()
  print("Total:",end=" ")
  print(dealer_hand.tally())
  print("Your hand:",end=" ")
  player_hand.cardList()
  print("Total:",end=" ")
  print(player_hand.tally())
  print()
  if dealer_hand.tally()==player_hand.tally():
    print("Push!")
  elif dealer_hand.tally()==21:
    print("Dealer Wins!")
  elif player_hand.tally()==21:
    print("You Win!")
  elif dealer_hand.tally()>21:
    print("Dealer Busts! You Win!")
  elif player_hand.tally()>21:
    print("You Busts!")
  elif dealer_hand.tally()>player_hand.tally():
    print("Dealer Wins!")
  elif dealer_hand.tally()<player_hand.tally():
    print("You Win!")
  print("\n","-"*55,"\n")
#
#Finally, the function will allow users to decide whether they want to continue or noy
c="none"
while c != 'q':
  game()
  c=input("Hit [Q]uit or [C]ontinue:")
  print("\n","-"*60,"\n")
