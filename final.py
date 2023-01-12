from typing import List
from graphics import *
import winsound
import random
import time
import os

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


class Music:
    enabled: bool
    song: str

    def __init__(self) -> None:
        self.enabled = False
        self.song = ""

    def isEnabled(self):
        return self.enabled

    def getSong(self):
        return self.song

    def playSong(self, song):
        if song == "rickroll":
            winsound.PlaySound("rickroll.wav")
        else:
            # search for a song
            pass


class Settings:
    difficulty = ""
    players = 1
    music: Music

    def __init__(self) -> None:
        self.difficulty = "medium"
        self.players = 1
        self.music = Music()

    def viewDifficulty(self):
        return self.difficulty

    def viewPlayers(self):
        return self.players

    def updateDifficulty(self, newValue):
        self.difficulty = newValue


class Player:
    playerName: str
    playerFile: str

    def __init__(self, name, file) -> None:
        self.playerName = name
        self.playerFile = file

    def viewName(self):
        return self.playerName

    def getFile(self):
        return self.playerFile

    def updateName(self, newName):
        self.playerName = newName

    def updateFile(self, newFile):
        self.playerFile = newFile


class Ball:
    img: str

    def __init__(self, img) -> None:
        self.img = img

    def respawn(self):
        pass

    def moveDown(self):
        pass


class Game:
    screen: str
    _settings: Settings
    players: List[Player]
    balls: List[Ball]

    def __init__(self):
        self._settings = Settings()

    def viewSettings(self):
        return self._settings

    def viewPlayers(self):
        return self.players

    def viewBalls(self):
        return self.balls

    def addPlayer(self, name, file):
        self.players.append(Player(name, file))

    def defaultScreen(self):
        defaultScreen = GraphWin("Dodge The Balls", 500, 500)
        defaultScreen.setCoords(
            -(defaultScreen.width / 2),
            -(defaultScreen.height / 2),
            (defaultScreen.width / 2),
            (defaultScreen.height / 2),
        )
        PLAY_BUTTON = Rectangle(Point(-100, -20), Point(100, 20))
        PLAY_BUTTON.draw(defaultScreen)
        PLAY = Text(PLAY_BUTTON.getCenter(), "PLAY")
        PLAY.setSize(20)
        PLAY.draw(defaultScreen)
        INSTURCTION_BUTTON = Rectangle(Point(-100, -40), Point(0, -20))
        INSTURCTION_BUTTON.draw(defaultScreen)
        INSTRUCTION = Text(INSTURCTION_BUTTON.getCenter(), "INSTRUCTIONS")
        INSTRUCTION.setSize(10)
        INSTRUCTION.draw(defaultScreen)
        SETTINGS_BUTTON = Rectangle(Point(0, -40), Point(100, -20))
        SETTINGS_BUTTON.draw(defaultScreen)
        SETTINGS = Text(SETTINGS_BUTTON.getCenter(), "SETTINGS")
        SETTINGS.setSize(10)
        SETTINGS.draw(defaultScreen)

        while True: 
            pt = defaultScreen.getMouse()
            print(pt)

            if (INSTURCTION_BUTTON.clicked(pt)): 
                print("Instruction button clicked!")
                break
            if (SETTINGS_BUTTON.clicked(pt)): 
                print("Settings button clicked")
                break
            if (PLAY_BUTTON.clicked(pt)): 
                print("Play button clicked")
                break

        

        defaultScreen.close()

    def gameScreen(self):
        gameScreen = GraphWin("Game Screen")

        gameScreen.getMouse()
        gameScreen.close()

    def settings(self):
        settingsScreen = GraphWin("Settings", 500, 500)

        settingsScreen.setCoords(
            -(settingsScreen.width / 2),
            -(settingsScreen.height / 2),
            (settingsScreen.width / 2),
            (settingsScreen.height / 2),
        )

        settingsScreen.getMouse()
        settingsScreen.close()

    def instructions(self):
        instructionsScreen = GraphWin("Instructions", 500, 500)

        instructionsScreen.getMouse()
        instructionsScreen.close()


while True:
    game = Game()
    game.defaultScreen()
