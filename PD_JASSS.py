
# coding: utf-8

# In[24]:

import random
import numpy as np
import matplotlib.pyplot as plt

def transpose(seqseq): #simple 2-dimensional transpose
    return zip(*seqseq)


def mean(seq):
    n = len(seq)
    return sum(seq)/float(n)


class RandomMover:
    def move(self):
        return random.uniform(0,1) < 0.5
    
## GAME: RandomMover
# create a payoff matrix and two players
PAYOFFMAT = [ [(3,3),(0,5)] , [(5,0),(1,1)] ]
history = []
payoffs = []
m_p = []
for i in range(0,20):
   
    player1 = RandomMover()
    player2 = RandomMover()
# get a move from each player. The move variables contain the Boolean False or True. True = 1 = defection; False = 0 = cooperation
# List of list is putting rows undereachother.
    move1 = player1.move()
    move2 = player2.move()
    history.append((move1, move2))
    
    
#print move1
#print move2
# retrieve and print the payoffs
    pay1, pay2 = PAYOFFMAT[move1][move2]
    payoffs.append((pay1, pay2))
    pay1, pay2 = transpose(payoffs)
    m_p1 = mean(pay1)
    m_p2 = mean(pay2)
    m_p.append((m_p1, m_p2))

    
    

    print "Player1 payoff: ", pay1
    print "Player2 payoff: ", pay2
    
print mean(pay1)
print mean(pay2)
print m_p
print pay1
print pay2
print history
print payoffs

x_val = [x[0] for x in m_p]
y_val = [x[1] for x in m_p]

print x_val
plt.plot(x_val)
plt.plot(y_val)
#plt.plot(x_val,y_val,'or')
#plt.legend(['y = x', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.show()









# In[2]:

def mean(seq):
    n = len(seq)
    return sum(seq)/float(n)

def transpose(seqseq): #simple 2-dimensional transpose
    return zip(*seqseq)

class RandomPlayer:
    #This is in its default version = identical to RandomMover with p defection = 0.5 and move=move and record does nothing.
    def __init__(self, p=0.5):
        self.p_defect = p
    def move(self, game):
        return random.uniform(0,1) < self.p_defect
    def record(self, game):
        # Python uses the keyword "pass" to indicate : Do nothing!
        pass
    
class SimpleGame:
    def __init__(self, player1, player2, payoffmat):
        #initialize instance attributes
        self.players = [player1, player2]
        self.payoffmat = payoffmat
        self.history = list()
    def run(self, game_iter=4):
        # unpack the two players
        player1, player2 = self.players
        # each iteration, get new moves and append these to history
        for iteration in range(game_iter):
            newmoves = player1.move(self), player2.move(self)
            self.history.append(newmoves)
            # prompt players to record the game played (i.e., 'self')
            player1.record(self) ; player2.record(self)
    def payoff(self):
        # unpack the two players
        player1, player2 = self.players
        # generate a payoff pair for each game iteration
        payoffs = (self.payoffmat[m1][m2] for (m1, m2) in self.history)
        # transpose to get a payoff sequence for each player
        pay1, pay2 = transpose(payoffs)
        # return a mapping of each player to its mean payoff
        return { player1:mean(pay1), player2:mean(pay2) }
    
## GAME: SimpleGame with RandomPlayer
# create a payoff matrix and two players
PAYOFFMAT = [ [(3,3),(0,5)] , [(5,0),(1,1)] ]
player1 = RandomPlayer()
player2 = RandomPlayer()
# Create and run the game
game = SimpleGame(player1, player2, PAYOFFMAT)
game.run()
# retrieve and print the payoffs
payoffs = game.payoff()
print "Player1 payoff: ", payoffs[player1]
print "Player2 payoff: ", payoffs[player2]


# In[ ]:



