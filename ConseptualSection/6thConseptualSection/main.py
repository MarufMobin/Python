class Team:
    def __init__( self, name, ):
        self.teamName = name
        self.playersListOfObj = []
    
    def entr_player( self, player ): # object is a type of player object 
        self.playersListOfObj.append(player)


class Player:
    def __init__(self, name, teamObj ) -> None:
        
        # For Batsman
        self.playerName = name
        self.strickRate = 0.0
        self.runBat = 0
        self.ballUsed = 0
        self.fours = 0
        self.sixes = 0
        
        # For Bowled         
        self.runBowl = 0
        self.wicketTaken  = 0
        self.ballsBowled = 0
        teamObj.playersListOfObj.append(self)
    
    def __repr__(self) -> str:
        return f'Name : {self.playerName}'


class Innings:
    def __init__(self, team1, team2, battingTeam, bowlingTeam):
        self.teamOneObj = team1
        self.teamTwoObj = team2
        self.battingTeam = battingTeam
        self.bowlingTeam = bowlingTeam
        self.totalRun = 0
        self.totalWickets = 0
        self.totalOver = 0
        self.currentBall = 0
        self.currentBattingList = []

# Team work
bangladesh = Team('Bangladesh')
india = Team('India')

# player Work
tamim = Player('Tamim Ikbal', bangladesh)
sakib = Player('Sakib Al Hassan', bangladesh )
mustafiz = Player('Mustafizur Rahman', bangladesh)

kohli = Player('Virat Kholi', india)
rohit = Player('Rohit Sarma', india)
bumra = Player('Bhumra', india)

# print(tamim.playerName)
# print(sakib.playerName)

print(bangladesh.playersListOfObj)

# for obj in india.playersListOfObj:
#     print(obj.playerName)