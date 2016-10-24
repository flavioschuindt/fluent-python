import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
	rank_value = FrenchDeck.ranks.index(card.rank)
	return rank_value * len(suit_values) + suit_values[card.suit] 

class FrenchDeck:
	ranks = [str(n) for n in range(2,11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, position):
		return self._cards[position]

# Using the FrenchDeck

beer_card = Card('7', 'diamonds') # create a Card
print(beer_card)

deck = FrenchDeck()
size = len(deck) # Calls __len__ from FrenchDeck instance¹
print(size)

print(deck[0]) # slicing works because we implemented __getitem__ special method in FrenchDeck
print(deck[-1])

print(choice(deck)) # randomly select a card in the deck

print(deck[:3]) # Also supports slice because we implemented __getitem__ and it delegates to the [] operator of self._cards
print(deck[12::13])

for card in deck: # our deck is also iterable because we implemented the __getitem__ method
	print(card)

for card in reversed(deck):
	print(card)

print(Card('Q', 'hearts') in deck) # 'in' does a sequenctial scan in the abscense of __contains__ method. 'in' works because our FrenchDeck is iterable.
print(Card('7', 'beasts')  in deck)

for card in sorted(deck, key=spades_high): # we can sort passing a sorting function
	print(card)


'''
¹
For custom classes created by you, on len() calls the interpreter (CPython) calls (if exist) the __len__ method 
that you defined.
For built-in types like list, str, bytearray, etc. CPython implementation of len() method returns the value of 
ob_size field in the PyVarObject C struct that represents any variable-sized built-in object in memory. 
This is much faster than calling a method.
'''