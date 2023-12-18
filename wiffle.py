from tkinter import Tk, ttk

class Game:
    def __init__(self, home: str, away: str, innings: int = 3):
        self.__home = home
        self.__away = away
        self.__innings = innings

class Player:
    def __init__(self, name: str, position: str):
        self.__name = name
        self.__position = position
        self.PA = 0
        self.AB = 0
        self.H = 0
        self.singles = 0
        self.doubles = 0
        self.triples = 0
        self.HR = 0
        self.W = 0
        self.pitches_against = 0
        self.strikes_against = 0
        self.swinging = 0
        self.looking = 0
        self.balls_against = 0
        
        self.pitches = 0
        self.balls = 0
        self.strikes = 0
        self.swung = 0
        self.looked = 0
        self.outs = 0
        self.groundouts = 0
        self.flyouts = 0
        self.strikeouts = 0
        self.IP = 0
        self.R_against = 0
        self.ER_against = 0
        self.ERA3 = self.ER_against * 3 / self.IP
        self.ERA9 = self.ER_against * 9 / self.IP

    def change_name(self, new_name):
        self.__name = new_name

    def change_position(self, new_pos):
        self.__position = new_pos

class Team:
    def __init__(self, name):
        self.__name = name
        self.__players = []

    def change_name(self, new_name):
        self.__name = new_name

    def add_player(self, player: Player):
        self.__players.append(player)

class League:
    def __init__(self, name: str, season: int):
        self.__name = name
        self.__teams = []

    def add_team(self, team: Team):
        self.__teams.append(team)

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        label = ttk.Label(master=self._root, text="Hello world!")
        button = ttk.Button(master=self._root, text="Button")
        entry = ttk.Entry(master=self._root)
        checkbutton = ttk.Checkbutton(master=self._root, text="Check button")
        label.pack()
        button.pack()
        entry.pack()
        checkbutton.pack()

window = Tk()
window.title("TkInter example")

ui = UI(window)
ui.start()

window.mainloop()