from collections import Counter
import random


class GameLogic():

    @staticmethod
    def calculate_score(calc):
        score = 0
        pair = 0
        pairs = Counter(calc).most_common()

        if len(calc) == 0:
            return score

        if len(pairs) == 6:
            GameLogic.amount = 6
            return 1500

        if len(calc) == 6 and len(pairs) == 3:
            for i in range(3):
                if pairs[i][1] == 2:
                    pair += 1

        if pair == 3:
            GameLogic.amount = 6
            return 1500

        else:
            for i in range(len(pairs)):
                number = pairs[i][0]
                common = pairs[i][1]
                base = number * 100

                if number == 1:
                    if common > 2:
                        base = number * 1000
                    else:
                        score += base * common
                if number == 5:
                    if common < 3:
                        score += number * 10 * common
                if common > 2:
                    score += base * (common - 2)
        return score

    @staticmethod
    def roll_dice(number):
        roll_dice_list = []

        for i in range(number):
            roll_dice_list.append(random.randint(1, 6))
            
        return tuple(roll_dice_list)
