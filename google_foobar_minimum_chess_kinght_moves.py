# Quiz : Don't Get Volunteered!
# ======================

# As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies at the same time, after all! In order to make sure that everyone working for her is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

# To help yourself get to and from your bunk every day, write a function called answer(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------


def solution(src, dest):
    dict = {
        0: [10, 17],
        1: [11, 16, 18],
        2: [8, 12, 17, 19],
        3: [9, 13, 18, 20],
        4: [10, 14, 19, 21],
        5: [11, 20, 22, 15],
        6: [12, 21, 23],
        7: [13, 22],
        8: [2, 18, 25],
        9: [3, 19, 24, 26],
        10: [0, 4, 16, 20, 25, 27],
        11: [5, 21, 28, 26, 17, 1],
        12: [6, 22, 29, 27, 18, 2],
        13: [7, 23, 30, 28, 19, 3],
        14: [31, 29, 20, 4],
        15: [30, 21, 5],
        16: [1, 10, 26, 33],
        17: [0, 2, 11, 27, 34, 32],
        18: [3, 12, 28, 35, 33, 24, 8, 1],
        19: [4, 13, 29, 36, 34, 25, 9, 2],
        20: [5, 14, 30, 37, 35, 26, 10, 3],
        21: [6, 15, 31, 38, 36, 27, 11, 4],
        22: [7, 39, 37, 28, 12, 5],
        23: [38, 29, 13, 6],
        24: [9, 18, 34, 41],
        25: [10, 19, 35, 42, 40, 8],
        26: [11, 20, 36, 43, 41, 32, 16, 9],
        27: [12, 21, 37, 44, 42, 33, 17, 10],
        28: [13, 22, 38, 45, 43, 34, 18, 11],
        29: [14, 23, 39, 46, 44, 35, 19, 12],
        30: [15, 47, 45, 36, 20, 13],
        31: [46, 37, 21, 14],
        32: [17, 26, 42, 49],
        33: [18, 27, 43, 50, 48, 16],
        34: [19, 28, 44, 51, 49, 40, 24, 17],
        35: [20, 29, 45, 52, 50, 41, 25, 18],
        36: [21, 30, 46, 53, 51, 42, 26, 19],
        37: [22, 31, 47, 54, 52, 43, 27, 20],
        38: [23, 55, 53, 44, 28, 21],
        39: [54, 45, 29, 22],
        40: [25, 34, 50, 57],
        41: [26, 35, 51, 58, 56, 24],
        42: [27, 36, 52, 59, 57, 48, 32, 25],
        43: [28, 37, 53, 60, 58, 49, 33, 26],
        44: [29, 38, 54, 61, 59, 50, 34, 27],
        45: [30, 39, 55, 62, 60, 51, 35, 28],
        46: [31, 63, 61, 52, 36, 29],
        47: [62, 53, 37, 30],
        48: [33, 42, 58],
        49: [34, 43, 59, 32],
        50: [35, 44, 60, 56, 40, 33],
        51: [36, 45, 61, 57, 41, 34],
        52: [37, 46, 62, 58, 42, 35],
        53: [38, 47, 63, 59, 43, 36],
        54: [39, 60, 44, 37],
        55: [61, 45, 38],
        56: [41, 50],
        57: [42, 51, 40],
        58: [43, 52, 48, 41],
        59: [44, 53, 49, 42],
        60: [45, 54, 50, 43],
        61: [46, 55, 51, 44],
        62: [47, 52, 45],
        63: [53, 46]
    }
    moves = 0

    if src in dict[dest]:
        moves = 1
    else:
        if src in [j for i in dict[dest] for j in dict[i]]:
            moves = 2
        else:
            if src in [k for i in dict[dest] for j in dict[i] for k in dict[j]]:
                moves = 3
            else:
                if src in [l for i in dict[dest] for j in dict[i] for k in dict[j] for l in dict[k]]:
                    moves = 4
                else:
                    if src in [m for i in dict[dest] for j in dict[i] for k in dict[j] for l in dict[k] for m in dict[l]]:
                        moves = 5
                    else:
                        if src in [n for i in dict[dest] for j in dict[i] for k in dict[j] for l in dict[k] for m in dict[l] for n in dict[m]]:
                            moves = 6
    return moves


print(solution(0, 1))