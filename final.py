from typing import List
from graphics import *
import winsound
import requests
import pyttsx3
import random
import time

class Music: 
    enabled: bool
    song: str
    def __init__(self) -> None:
        self.enabled = False
        self.song = ""
    def isEnabled(self): return self.enabled
    def getSong(self): return self.song
    def playSong(self, song):
        if (song == "rickroll"): 
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
    def viewName(self): return self.playerName
    def getFile(self): return self.playerFile
    def updateName(self, newName): self.playerName = newName
    def updateFile(self, newFile): self.playerFile = newFile


class Ball:
    img: str
    def __init__(self, img) -> None:
        self.img = img
    def respawn(self): pass
    def moveDown(self): pass


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

        defaultScreen

        defaultScreen.setCoords(
            -(defaultScreen.width / 2),
            -(defaultScreen.height / 2),
            (defaultScreen.width / 2),
            (defaultScreen.height / 2)
        )

        cir = Rectangle(Point(0,0), Point(-10,10))
        cir.setFill('red')
        cir.clicked()
        cir.draw(defaultScreen)

        defaultScreen.getMouse()
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
            (settingsScreen.height / 2)
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
