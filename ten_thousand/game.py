from game_logic import GameLogic, Banker

welcome_message = """
"Welcome to Ten Thousand"
(y)es to play or (n)o to decline"
"""


class Game:
    def __init__(self):
        self.bank = Banker()

    def play(self, roller=GameLogic.roll_dice):
        print(welcome_message)
        response = input("> ")

        if response.lower() == "n":
            print("OK. Maybe another time")

        elif response.lower() == "y":

            # Variables
            score = 0
            round_ = 1
            current_dice = 6

            while True:

                # Strings (to not crowd up code below)
                start = f"""Starting round {round_} *** Rolling {current_dice} dice...
                """
                user_choice = "Enter dice to keep, or (q)uit:"
                banked_points = f"Thanks for playing. You earned {self.bank.balance} points"
                unbanked_points = f"You have {self.bank.shelved} unbanked points and {current_dice} dice remaining"
                user_options = "(r)oll again, (b)ank your points or (q)uit:"
                earned_points = f"Thanks for playing. You earned {self.bank.balance} points"
                banked_rounds = f"You banked {self.bank.bank()} points in round {round_}"
                total = f"Total score is {self.bank.balance} points"

                print(start, f"*** {roller(current_dice)} ***".replace("(","").replace(",","").replace(")", "").replace("[","").replace("]", ""))

                print(user_choice)
                keep_quit = input("> ").lower()

                if keep_quit.lower() == "q":
                    print(banked_points)
                    break

                if keep_quit.isnumeric():
                    if len(keep_quit) <= 6:
                        dice_to_keep = [int(num) for num in keep_quit]
                        dice_to_keep = tuple(dice_to_keep)
                        score = GameLogic.calculate_score(dice_to_keep)
                        self.bank.shelf(score)
                        current_dice = current_dice - len(dice_to_keep)

                        print(unbanked_points)

                        if len(dice_to_keep) <= 6:

                            print(user_options)

                            roll_bank_quit = input("> ")

                            if roll_bank_quit.lower() == "q":
                                print(earned_points)
                                break

                            elif roll_bank_quit.lower() == "r":
                                round_ += 1
                                continue

                            elif roll_bank_quit.lower() == "b":
                                print(banked_rounds)
                                print(total)
                                round_ += 1
                                current_dice = 6


if __name__ == "__main__":
    game = Game()
    game.play()

