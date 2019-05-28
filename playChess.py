import pygame
from board.chessBoard import Board
from flask import Flask
app = Flask(__name__)

@app.route("/Chess")
# def hello():
 #   return "Hello World!"

pygame.init()
gameDisplay = pygame.display.set_mode((800, 800))
pygame.display.set_caption("PyChess")
clock = pygame.time.Clock()

chessBoard = Board()
chessBoard.createBoard()
chessBoard.printBoard()

allTiles = []
allPieces = []


##################################

def squares(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])
    allTiles.append([color, [x, y, w, h]])


def drawChessPieces():
    xpos = 0
    ypos = 0
    color = 0
    width = 100
    height = 100
    black = (66, 134, 244)
    white = (143, 155, 175)
    number = 0
    for _ in range(8):
        for _ in range(8):
            if color % 2 == 0:
                squares(xpos, ypos, width, height, white)
                if not chessBoard.gameTiles[number].pieceOnTile.toString() == "-":
                    img = pygame.image.load(
                        "./ChessArt/" + chessBoard.gameTiles[number].pieceOnTile.alliance[0].upper() +
                        chessBoard.gameTiles[
                            number].pieceOnTile.toString().upper() + ".png")
                    img = pygame.transform.scale(img, (100, 100))
                    allPieces.append([img, [xpos, ypos], chessBoard.gameTiles[number].pieceOnTile])
                xpos += 100
            else:
                squares(xpos, ypos, width, height, black)
                if not chessBoard.gameTiles[number].pieceOnTile.toString() == "-":
                    img = pygame.image.load(
                        "./ChessArt/" + chessBoard.gameTiles[number].pieceOnTile.alliance[0].upper() +
                        chessBoard.gameTiles[
                            number].pieceOnTile.toString().upper() + ".png")
                    img = pygame.transform.scale(img, (100, 100))
                    allPieces.append([img, [xpos, ypos], chessBoard.gameTiles[number].pieceOnTile])
                xpos += 100

            color += 1
            number += 1
        color += 1
        xpos = 0
        ypos += 100


#################################
quitGame = False
drawChessPieces()

while not quitGame:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()

    for img in allPieces:
        gameDisplay.blit(img[0], img[1])


    pygame.display.update()
    clock.tick(60)
