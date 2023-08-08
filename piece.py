from enum import Enum

class NameMapping(Enum):
    pawn = 1
    knight = 2
    bishop = 3
    rook = 4
    queen = 5
    king = 6

class Piece:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def pawn_rule(color, board, x,y,newx,newy):
    enemy_indexes = [(i)*color*-1 for i in range(1, 7)]
    if x != newx: # attack
        if color == 1:
            if abs(newx-x) == 1 and y-newy == 1:
                if board[newy, newx] in enemy_indexes:
                    return True
        else:
            if abs(newx-x) == 1 and newy-y == 1:
                if board[newy, newx] in enemy_indexes:
                    return True
        
        return False
    else: # move
        if color == 1:
            is_first_move = True if y == 6 else False
            
            if is_first_move and y-newy == 2 and board[newx ,newy] == 0 and board[newx, newy+1]== 0:
                return True
            elif y-newy == 1 and board[newx, newy] == 0:
                return True
        else:
            is_first_move = True if y == 1 else False
            
            if is_first_move and newy-y == 2 and board[newx, newy]==0 and board[newx, newy-1] ==0:
                return True
    
        return False
        
def knight_rule(color, board, x,y,newx,newy):
    return True
def bishop_rule(color, board, x,y,newx,newy):
    return True
def rook_rule(color, board, x,y,newx,newy):
    return True
def queen_rule(color, board, x,y,newx,newy):
    return True
def king_rule(color, board, x,y,newx,newy):
    return True

RuleMapping = [
    True,
    pawn_rule,
    knight_rule,
    bishop_rule,
    rook_rule,
    queen_rule,
    king_rule,
]