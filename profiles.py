import pandas as pd

class UserProfile:
    def __init__(self, f_name, l_name, username, password):
        self.f_name = f_name
        self.l_name = l_name
        self.username = username
        self.password = password
        self.batter_dict = {
            'C': None,
            '1B': None,
            '2B': None,
            '3B': None,
            'SS': None,
            '2B/SS': None,
            '1B/3B': None,
            'OF 1': None,
            'OF 2': None,
            'OF 3': None,
            'OF 4': None,
            'OF 5': None,
            'UTIL': None,
            'Bench 1': None,
            'Bench 2': None,
            'Bench 3': None,
            'Bench 4': None
        }
        self.pitcher_dict = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None 
        }
    
    def add_player(self, new_player):
        self.player_list.append(new_player)

    def remove_player(self, old_player):
        if self.player_list.contains(old_player):
            self.player_list.remove(old_player)



class PlayerProfile:
    def __init__(self, f_name, l_name, team, position, type):
        self.f_name = f_name
        self.l_name = l_name
        self.team = team
        self.position = position
        self.stats = None
        self.url = ""

    def set_stats(self, stats):
        self.stats = stats
    
    def set_url(self, url):
        self.url = url