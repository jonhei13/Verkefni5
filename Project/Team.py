class Team:

    def __init__(self, team_list):
        self.team_members = team_list
        self.team_health = 0

    def update(self, team_list):
        self.team_health = 0
        for member in team_list:
            self.team_health += member.life


