#############################################################################
# Author: Mohammad El-Hassan
# Description: Final Project
# Date Created: 01/16/2023
# Date Modified: 01/16/2023
#############################################################################
from winsound import PlaySound, SND_ASYNC, SND_ALIAS, SND_PURGE, SND_FILENAME, SND_LOOP
from typing import List
from graphics import *
import threading
import random
import time
import os


def clickAnimation(rectangle: Rectangle):
    rectangle.setFill("orange")
    time.sleep(0.3)
    rectangle.setFill("")


def setInterval(func, sec: int):
    def func_wrapper():
        setInterval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    import requests
try:
    import pyttsx3
except ModuleNotFoundError:
    os.system("pip install pyttsx3")
    import pyttsx3

class Button: 
    def __init__(self, p1: Point, p2: Point, text: str, win=None): 
        self.p1 = p1
        self.p2 = p2
        self.win = win
        self.rectangle = Rectangle(p1, p2)
        self.text = Text(self.rectangle.getCenter(), text)
        self.clicked = self.rectangle.clicked
    def setFontSize(self, size:int): 
        self.text.setSize(size)
        return self
    def setWin(self, win): 
        self.win = win
        return 
    def draw(self): 
        self.rectangle.draw(self.win)
        self.text.draw(self.win)
        return self
    def undraw(self): 
        self.rectangle.undraw()
        self.text.undraw()
        return self
    def activate(self): 
        self.rectangle.setFill("orange")
        return self
    def deactivate(self): 
        self.rectangle.setFill("")
        return self
    def clickAnimation(self): 
        self.activate()
        time.sleep(0.3)
        self.deactivate()
        return self

class Music:
    enabled: bool
    song: str
    def __init__(self) -> None:
        self.enabled = False
        self.song = ""
    def isEnabled(self):
        if (self.enabled == True): return "ON"
        else: return "OFF"
    def getSong(self):
        return self.song
    def stop(self): PlaySound(None, SND_ASYNC)
    def playSong(self, song):
        self.song = song
        print(self.song)
        PlaySound(self.song, SND_ASYNC | SND_FILENAME | SND_LOOP)
        return self

class Settings:
    difficulty: str
    players: int
    music: Music
    def __init__(self) -> None:
        self.difficulty = "medium"
        self.players = 1
        self.music = Music()
    def viewDifficulty(self): return self.difficulty
    def viewPlayers(self): return self.players
    def updateDifficulty(self, newValue):
        self.difficulty = newValue
        return self

class Player:
    playerName: str
    playerFile: str
    def __init__(self, name, file) -> None:
        self.playerName = name
        self.playerFile = file
    def viewName(self): return self.playerName
    def getFile(self): return self.playerFile
    def updateName(self, newName):
        self.playerName = newName
        return self
    def updateFile(self, newFile):
        self.playerFile = newFile
        return self

class Ball:
    img: str
    def __init__(self, img) -> None: self.img = img
    def respawn(self): pass
    def moveDown(self): pass

class Game:
    screen: str
    _settings: Settings
    players: List[Player]
    balls: List[Ball]
    def __init__(self): self._settings = Settings()
    def viewSettings(self): return self._settings
    def viewPlayers(self): return self.players
    def viewBalls(self): return self.balls
    def addPlayer(self, name, file):
        self.players.append(Player(name, file))
        return self
    def defaultScreen(self):
        defaultScreen = GraphWin("Dodge The Balls", 800, 500).zero().setImage("Settings page.gif")
        PLAY_BUTTON = Button(Point(-100, -20), Point(100, 20), "PLAY", defaultScreen).setFontSize(20).draw()
        INSTURCTION_BUTTON = Button(Point(-100, -20), Point(0, -40), "INSTRUCTIONS", defaultScreen).setFontSize(10).draw()
        SETTINGS_BUTTON = Button(Point(0, -20), Point(100, -40), "SETTINGS", defaultScreen).setFontSize(10).draw()
        while True:
            pt = defaultScreen.getMouse()
            if (INSTURCTION_BUTTON.clicked(pt)):
                INSTURCTION_BUTTON.clickAnimation()
                defaultScreen.close()
                self.instructions()
                break
            if (SETTINGS_BUTTON.clicked(pt)):
                SETTINGS_BUTTON.clickAnimation()
                defaultScreen.close()
                self.settings()
                break
            if (PLAY_BUTTON.clicked(pt)):
                PLAY_BUTTON.clickAnimation()
                defaultScreen.close()
                self.gameScreen()
                break
        defaultScreen.close()
    def gameScreen(self):
        gameScreen = GraphWin("Game Screen", 800, 500).zero().setImage("Blue Sky.gif")
        while True: break
        gameScreen.getMouse()
        gameScreen.close()
    def settings(self):
        settingsScreen = GraphWin("Settings", 800, 500).zero().setImage("Settings page.gif")
        MUSIC_ON = Button(Point(-350, 150), Point(-300, 200), "ON", settingsScreen).setFontSize(15).draw()
        MUSIC_OFF = Button(Point(-250, 150), Point(-200, 200), "OFF", settingsScreen).setFontSize(15).draw()
        BACK = Button(Point(-50, -150), Point(50, -200), "BACK", settingsScreen).draw()
        AFTERPARTY = Button(Point(-350, 50), Point(-250, 100), "AFTER PARTY", settingsScreen).setFontSize(10)
        BIGGESTBIRD = Button(Point(-200, 50), Point(-100, 100), "BIGGEST BIRD", settingsScreen).setFontSize(10)
        RICKROLL = Button(Point(-50, 50), Point(50, 100), "RICK ROLL", settingsScreen).setFontSize(10)
        SEARCH = Button(Point(275, 50), Point(350, 100), "Search\nText", settingsScreen)
        EASY = Button(Point(-350, -50), Point(-300, 0), "EASY", settingsScreen).draw()
        MEDIUM = Button(Point(-250, -50), Point(-200, 0), "MEDIUM", settingsScreen).setFontSize(9).draw()
        HARD = Button(Point(-150, -50), Point(-100, 0), "HARD", settingsScreen).draw()
        entry = Entry(Point(175, 75), 17)
        while True:
            if (self._settings.music.isEnabled() == "ON"):
                MUSIC_OFF.deactivate()
                MUSIC_ON.activate()
            else:
                MUSIC_ON.deactivate()
                MUSIC_OFF.activate()
            if (self._settings.difficulty == "easy"): 
                EASY.activate()
                MEDIUM.deactivate()
                HARD.deactivate()
            pt = settingsScreen.getMouse()
            if (MUSIC_ON.clicked(pt)):
                MUSIC_ON.clickAnimation()
                self._settings.music.enabled = True
                AFTERPARTY.draw()
                BIGGESTBIRD.draw()
                RICKROLL.draw()
                SEARCH.draw()
                entry.draw(settingsScreen)
                continue
            if (MUSIC_OFF.clicked(pt)):
                MUSIC_OFF.clickAnimation()
                self._settings.music.enabled = False
                AFTERPARTY.undraw()
                BIGGESTBIRD.undraw()
                RICKROLL.undraw()
                SEARCH.undraw()
                entry.undraw()
                self._settings.music.stop()
                continue
            if (AFTERPARTY.clicked(pt)):
                AFTERPARTY.clickAnimation()
                self._settings.music.playSong("afterparty.wav")
            if (BIGGESTBIRD.clicked(pt)):
                BIGGESTBIRD.clickAnimation()
                self._settings.music.playSong("biggestbird.wav")
            if (RICKROLL.clicked(pt)):
                RICKROLL.clickAnimation()
                self._settings.music.playSong("rickroll.wav")
            if (SEARCH.clicked(pt)):
                SEARCH.clickAnimation()
                query = entry.getText()
                engine = pyttsx3.init()
                response = requests.get(f"https://some-random-api.ml/lyrics?title={query}")
                data = response.json()
                lyrics = data["lyrics"].split("\n")
                if(len(data) == 1): print("No result(s) found! Please try a different song!")
                result_name = data["title"]
                engine.save_to_file(lyrics, f"{result_name}.wav")
                engine.runAndWait()
                self._settings.music.playSong(f"{result_name}.wav")
            if (BACK.clicked(pt)):
                BACK.clickAnimation()
                settingsScreen.close()
                break
            if (EASY.clicked(pt)): 
                print("easy clicked")
            if (MEDIUM.clicked(pt)): 
                print("medium clicked")
            if (HARD.clicked(pt)): 
                print("hard clicked")
            continue
    def instructions(self):
        instructionsScreen = GraphWin("Instructions", 800, 500).zero().setImage("Settings page.gif")
        instructionsScreen.getMouse()
        instructionsScreen.close()

while True:
    game = Game()
    game.defaultScreen()
