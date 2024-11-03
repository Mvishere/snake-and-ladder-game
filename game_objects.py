import random

def roll_dice():
    return random.randint(1,6)

class PLayer():
    def __init__(self, rect_obj, position = 0):
        self.position = position
        self.rect_obj = rect_obj

    def change_pos(self, pos):
        self.position = pos

class Ladder():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def xstart_index(self):
        return BOARD_MAP[self.start][0]
    
    def ystart_index(self):
        return BOARD_MAP[self.start][1]
    
    def xend_index(self):
        return BOARD_MAP[self.end][0]
    
    def yend_index(self):
        return BOARD_MAP[self.end][1]
    
def check_ladder(position):
    if(LADDERS.get(position)):
        return True
    else:
        return False
    
def check_snake(position):
    if(SNAKES.get(position)):
        return True
    else:
        return False
    
class Snake():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def xstart_index(self):
        return BOARD_MAP[self.start][0]
    
    def ystart_index(self):
        return BOARD_MAP[self.start][1]
    
    def xend_index(self):
        return BOARD_MAP[self.end][0]
    
    def yend_index(self):
        return BOARD_MAP[self.end][1]
    
def board_mapping():
    board_map = {}
    start_x = 28 + 75/2
    start_y = 724 - 30
    status = True
    for i in range(1, 101):
        board_map[i] = (start_x- 28/2, start_y-26/2)
        if(i%10 == 0):
            status = not status
            start_y -= 60
        else:
            if(status):
                start_x += 75
            else:
                start_x -= 75
    
    return board_map

BOARD_MAP = {1: (65.5, 694), 2: (140.5, 694), 3: (215.5, 694), 4: (290.5, 694), 5: (365.5, 694), 6: (440.5, 694), 7: (515.5, 694), 8: (590.5, 694), 9: (665.5, 694), 10: (740.5, 694), 11: (740.5, 634), 12: (665.5, 634), 13: (590.5, 634), 14: (515.5, 634), 15: (440.5, 634), 16: (365.5, 634), 17: (290.5, 634), 18: (215.5, 634), 19: (140.5, 634), 20: (65.5, 634), 21: (65.5, 574), 22: (140.5, 574), 23: (215.5, 574), 24: (290.5, 574), 25: (365.5, 574), 26: (440.5, 574), 27: (515.5, 574), 28: (590.5, 574), 29: (665.5, 574), 30: (740.5, 574), 31: (740.5, 514), 32: (665.5, 514), 33: (590.5, 514), 34: (515.5, 514), 35: (440.5, 514), 36: (365.5, 514), 37: (290.5, 514), 38: (215.5, 514), 39: (140.5, 514), 40: (65.5, 514), 41: (65.5, 454), 42: (140.5, 454), 43: (215.5, 454), 44: (290.5, 454), 45: (365.5, 454), 46: (440.5, 454), 47: (515.5, 454), 48: (590.5, 454), 49: (665.5, 454), 50: (740.5, 454), 51: (740.5, 394), 52: (665.5, 394), 53: (590.5, 394), 54: (515.5, 394), 55: (440.5, 394), 56: (365.5, 394), 57: (290.5, 394), 58: (215.5, 394), 59: (140.5, 394), 60: (65.5, 394), 61: (65.5, 334), 62: (140.5, 334), 63: (215.5, 334), 64: (290.5, 334), 65: (365.5, 334), 66: (440.5, 334), 67: (515.5, 334), 68: (590.5, 334), 69: (665.5, 334), 70: (740.5, 334), 71: (740.5, 274), 72: (665.5, 274), 73: (590.5, 274), 74: (515.5, 274), 75: (440.5, 274), 76: (365.5, 274), 77: (290.5, 274), 78: (215.5, 274), 79: (140.5, 274), 80: (65.5, 274), 81: (65.5, 214), 82: (140.5, 214), 83: (215.5, 214), 84: (290.5, 214), 85: (365.5, 214), 86: (440.5, 214), 87: (515.5, 214), 88: (590.5, 214), 89: (665.5, 214), 90: (740.5, 214), 91: (740.5, 154), 92: (665.5, 154), 93: (590.5, 154), 94: (515.5, 154), 95: (440.5, 154), 96: (365.5, 154), 97: (290.5, 154), 98: (215.5, 154), 99: (140.5, 154), 100: (65.5, 154)}

LADDERS = {}
LADDERS[1] = Ladder(1, 38)
LADDERS[4] = Ladder(4, 14)
LADDERS[8] = Ladder(8, 30)
LADDERS[21] = Ladder(21, 42)
LADDERS[28] = Ladder(28, 76)
LADDERS[50] = Ladder(50, 67)
LADDERS[71] = Ladder(71, 92)
LADDERS[80] = Ladder(80, 99)

SNAKES = {}
SNAKES[32] = Snake(32, 10)
SNAKES[36] = Snake(36, 6)
SNAKES[48] = Snake(48, 26)
SNAKES[62] = Snake(62, 18)
SNAKES[88] = Snake(88, 24)
SNAKES[95] = Snake(95, 56)
SNAKES[97] = Snake(97, 78)

if __name__ == "__main__":
    pass