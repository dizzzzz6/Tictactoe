import os

from pip._vendor.distlib.compat import raw_input

os.system("cls")


class Screen:
    def __init__(self):
        self.cellsog = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"] #original cells
        self.cells = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def display(self): #display the board
        print(" %s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
        print("----------")
        print(" %s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("----------")
        print(" %s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))
    def update_cell(self,cells_no,player): #update cells with input
            if self.cells[cells_no] == self.cellsog[cells_no]:
                self.cells[cells_no] = player

    def is_winner(self,player): #define win conditions
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True
        elif self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True
        elif self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True
        elif self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True
        elif self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True
        elif self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True
        elif self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True
        elif self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True
        return False



    def reset(self): #reset the game
        self.cells = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]




def refresh(): #refresh the screen
    os.system("cls")
    screen.display()


screen = Screen()


def xchoicef(): # get x choice

        x_choice = int(raw_input("\nX) Choose 1 - 9. "))
        screen.update_cell(x_choice, "X")


def ochoicef():# get o choice

        o_choice = int(raw_input("\nO) Choose 1 - 9. "))
        screen.update_cell(o_choice, "O")
while True:
    refresh()
    xchoicef()
    refresh()
    if screen.is_winner("X"):
        print(" X wins! ")
        play_again = raw_input("Would you like to play again? (Y/N)").upper()
        if play_again == "Y":
            screen.reset()
            continue
        else:
            break
    ochoicef()
    refresh()
    if screen.is_winner("O"):
        print(" O wins! ")
        play_again = raw_input("Would you like to play again? (Y/N)").upper()
        if play_again == "Y":
            screen.reset()
            continue
        else:
            break




