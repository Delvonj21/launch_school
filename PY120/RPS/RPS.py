import random


class Player:
    CHOICES = ("rock", "paper", "scissors", "spock", "lizard")

    def __init__(self):
        self.move = None


class Computer:
    def __init__(self):
        self.move = None

    def choose(self):
        self.move = random.choice(Player.CHOICES)


class Human:
    def __init__(self):
        self.move = None

    def choose(self):
        prompt = "Please choose rock, paper, scissors, spock, or lizard: "

        while True:
            choice = input(prompt).lower()
            if choice in Player.CHOICES:
                break

            print(f"Sorry, {choice} is not valid")

        self.move = choice


class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self._human_score = 0
        self._computer_score = 0

    def _display_welcome_message(self):
        print("Welcome to Rock Paper Scissors Spock Lizard!")
        print("First to 5 points wins!")

    def _display_goodbye_message(self):
        print("Thanks for playing Rock Paper Scissors Spock Lizard. Goodbye!")

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return (
            (human_move == "rock" and computer_move == "scissors")
            or (human_move == "rock" and computer_move == "lizard")
            or (human_move == "scissors" and computer_move == "paper")
            or (human_move == "scissors" and computer_move == "lizard")
            or (human_move == "paper" and computer_move == "rock")
            or (human_move == "paper" and computer_move == "spock")
            or (human_move == "lizard" and computer_move == "spock")
            or (human_move == "lizard" and computer_move == "paper")
            or (human_move == "spock" and computer_move == "scissors")
            or (human_move == "spock" and computer_move == "rock")
        )

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return (
            (computer_move == "rock" and human_move == "scissors")
            or (computer_move == "rock" and human_move == "lizard")
            or (computer_move == "scissors" and human_move == "paper")
            or (computer_move == "scissors" and human_move == "lizard")
            or (computer_move == "paper" and human_move == "rock")
            or (computer_move == "paper" and human_move == "spock")
            or (computer_move == "lizard" and human_move == "spock")
            or (computer_move == "lizard" and human_move == "paper")
            or (computer_move == "spock" and human_move == "scissors")
            or (computer_move == "spock" and human_move == "rock")
        )

    def _update_score(self):
        if self._human_wins():
            self._human_score += 1
        elif self._computer_wins():
            self._computer_score += 1

    def _display_score(self):
        print(f"Score: Human - {self._human_score}, Computer - {self._computer_score}")

    def _display_winner(self):
        print(f"You chose: {self._human.move}")
        print(f"The computer chose: {self._computer.move}")

        if self._human_wins():
            print("You win!")
        elif self._computer_wins():
            print("Computer wins!")
        else:
            print("It's a tie")

        self._update_score()
        self._display_score()

    def play(self):
        self._display_welcome_message()

        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()

            if self._human_score == 5:
                print("You won the game!")
                if self._play_again():
                    self._human_score = 0
                    self._computer_score = 0
                    continue
                else:
                    break
            elif self._computer_score == 5:
                print("Computer won the game!")
                if self._play_again():
                    self._human_score = 0
                    self._computer_score = 0
                    continue
                else:
                    break

        self._display_goodbye_message()

    def _play_again(self):
        answer = input("Would you like to play again? (y/n) ")
        return answer.lower().startswith("y")


RPSGame().play()
