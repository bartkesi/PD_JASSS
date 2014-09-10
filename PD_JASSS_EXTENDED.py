
# coding: utf-8

# In[13]:

import random

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
        #initialize instance attributes __init__ is written with double underscore!
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


# In[10]:




# In[ ]:



