from graphics import * 
import winsound
import random 
import pyttsx3 
import requests
import time

class Settings: 
    difficulty=""
    players=1
    music="None"
    def __init__(self) -> None:
        self.difficulty = "medium"
        self.players = 1
        self.music = "0"
    def viewDifficulty(self): return self.difficulty
    def viewPlayers(self): return self.players
    def viewMusic(self): return self.music
    def updateDifficulty(self, newValue): self.difficulty = newValue
    def updateMusic(self, fileName): 
        winsound.PlaySound(None)
        winsound.PlaySound(fileName)
        return

class Player: 
    playerName=""
    playerFile=""
    def __init__(self, name, file) -> None:
        self.playerName = name
        self.playerFile = file
    def viewName(self): return self.playerName
    def getFile(self): return self.playerFile
    def updateName(self, newName): self.playerName = newName
    def updateFile(self, newFile): self.playerFile = newFile

class Enemy: 
    def __init__(self) -> None:
        pass

class Game: 
    screen=""
    settings: Settings
    players: list[Player]
    enemies: list[Enemy]
    def __init__(self): 
        pass
    def settings(self): 
        pass
    def instructions(self): 
        pass