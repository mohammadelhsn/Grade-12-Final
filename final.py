from typing import List
from graphics import *
import winsound
import requests
import pyttsx3
import random
import time


class Settings:
    difficulty = ""
    players = 1
    music = "None"

    def __init__(self) -> None:
        self.difficulty = "medium"
        self.players = 1
        self.music = "0"

    def viewDifficulty(self):
        return self.difficulty

    def viewPlayers(self):
        return self.players

    def viewMusic(self):
        return self.music

    def updateDifficulty(self, newValue):
        self.difficulty = newValue

    def updateMusic(self, fileName):
        winsound.PlaySound(None)
        winsound.PlaySound(fileName)
        return


class Player:
    playerName = ""
    playerFile = ""

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
    screen = ""
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

    def settings(self):
        pass

    def instructions(self):
        pass


while True:
    pass
