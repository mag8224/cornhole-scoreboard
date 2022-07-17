class Game:
    team1 = 0
    team2 = 0
    round = {
        'inHole': [0, 0],
        'onBoard': [0, 0]
    }
    winner = ''

    def __init__(self):
        pass
       

    def scoreRound(self):
        team1_roundScore = self.round['inHole'][0]*3 + self.round['onBoard'][0]
        team2_roundScore = self.round['inHole'][1]*3 + self.round['onBoard'][1]
        netScore = team1_roundScore - team2_roundScore
        if(netScore > 0):
            self.team1 += netScore
        else:
            self.team2 += netScore * -1
        if(self.team1 > 21):
            self.team1 = 13
        if(self.team2 > 21):
            self.team2 = 13

        if(self.team1 == 21):
            self.winner = 'Team 1'
        if(self.team2 == 21):
            self.winner = 'Team 2'
        self.resetRound()


    def resetRound(self):
        self.round = {
            'inHole': [0, 0],
            'onBoard': [0, 0]
        }


    def addOnBoard(self, team):
        if(team == 1 and self.round['onBoard'][0] < 4 and self.round['onBoard'][0] + self.round['inHole'][0] < 4):
            self.round['onBoard'][0] +=1
        elif(team == 2 and self.round['onBoard'][1] < 4 and self.round['onBoard'][1] + self.round['inHole'][1] < 4):
            self.round['onBoard'][1] +=1
    
    def addInHole(self, team):
        if(team == 1 and self.round['inHole'][0] < 4 and self.round['onBoard'][0] + self.round['inHole'][0] < 4):
            self.round['inHole'][0] +=1
        elif(team == 2 and self.round['inHole'][1] < 4 and self.round['onBoard'][1] + self.round['inHole'][1] < 4):
            self.round['inHole'][1] +=1
    


sampleGame = Game()
#round1 
sampleGame.addOnBoard(1)
sampleGame.addOnBoard(2)
sampleGame.addOnBoard(1)
sampleGame.addInHole(1)
sampleGame.scoreRound()
print('Round 1 Score:')

print('Team 1:', sampleGame.team1, 'Team 2:', sampleGame.team2)
sampleGame.addInHole(2)
sampleGame.addInHole(2)
sampleGame.addInHole(2)
sampleGame.addInHole(2)
sampleGame.scoreRound()
print('Round 2 Score:')
print('Team 1:', sampleGame.team1, 'Team 2:', sampleGame.team2)

sampleGame.addInHole(2)
sampleGame.addInHole(2)
sampleGame.addInHole(1)
sampleGame.addInHole(2)
sampleGame.addInHole(2)
sampleGame.scoreRound()
print('Round 3 Score:')
print('Team 1:', sampleGame.team1, 'Team 2:', sampleGame.team2)
print(sampleGame.winner, 'Won!')