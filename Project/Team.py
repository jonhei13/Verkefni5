class Team:

    def __init__(self, team_list):
        self.members = team_list
        self.team_health = 0

    def update(self, team_list):
        self.team_health = 0
        self.members = team_list
        for member in self.members:
            self.team_health += member.life


