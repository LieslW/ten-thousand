from collections import Counter
import random


class GameLogic():

    @staticmethod
    def calculate_score(calc):
        amount = 0
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

    @staticmethod
    def validate_keepers(roll, keep):
        roll_most_common = Counter(roll).most_common()
        keep_most_common = Counter(keep).most_common()

        for i in range(len(keep_most_common)):
            if keep_most_common[i][1] > roll_most_common[i][1]:
                return False
            else:
                return True

    @staticmethod
    def get_scorers(dice):
        dice_list = []

        for int_ in dice:
            if int_ == 1:
                dice_list.append(int_)
            elif int_ == 5:
                dice_list.append(int_)

        return tuple(dice_list)


class Banker:
    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def shelf(self, number):
        self.shelved += number
        return self.shelved

    def bank(self):
        amount_deposited = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return amount_deposited

    def clear_shelf(self):
        self.shelved = 0
        return self.shelved
