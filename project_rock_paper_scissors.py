"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    """
        defines init method, move method, learn method of class Player to create instances
    """

    def __init__(self, name):
        """
            initializes the name, opponent_move, p1_score and p2_score of object instances
        :param name:
        """
        self.name = name
        self.opponent_move = ''
        self.p1_score = 0
        self.p2_score = 0

    def move(self):
        """
            makes the move of objects either randomly or input from human user
        :return:
        """
        pass

    def learn(self, player1_move, player2_move, player_object):
        """
            gets a series of parameters and returns
        :param player1_move:
        :param player2_move:
        :param player_object:
        :return str:
        """
        if self == player_object:
            return player2_move
        else:
            return player1_move


def beats(one, two):
    """
        checks for all conditions where player_1 wins player_2 and return the
        condition that satisfy moves by player_1 and player_2
    :param one:
    :param two:
    :return bool:
    """
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    """
        creates a RandomPlayer subclass of Player class that represent the computer which selects moves randomly
    """
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    """
        creates a ReflectPlayer subclass of Player class that represents a player which makes
        the same moves as their opponent's previous move
    """
    def move(self):
        """
            checks opponent's previous move in order to make the same move. chooses a move at random on first round
        :return str:
        """
        if self.opponent_move == '':
            return random.choice(moves)
        else:
            return self.opponent_move


class CyclePlayer(Player):
    """
         creates a CyclePlayer subclass of Player class that represents a player which makes
          the move that is next to opponent's previous move
    """
    def move(self):
        """
            checks opponent's previous move and makes a move next to it. chooses a move at random on first round
        :return str:
        """
        if self.opponent_move == '':
            return random.choice(moves)
        elif self.opponent_move == 'paper':
            return 'scissors'
        elif self.opponent_move == 'rock':
            return 'paper'
        else:
            return 'rock'


class HumanPlayer(Player):
    """
        creates a HumanPlayer subclass of Player class that represents human player that makes moves by asking
        user to type in their move
    """

    def move(self):
        """
            asks the user for their move and returns it
        :return str:
        """
        while True:
            input_from_user = input("Please enter your move: 'rock' or 'paper' or 'scissors': ").lower()
            if input_from_user in moves:
                break
            else:
                print('You entered the wrong move, please try again')
        return input_from_user


class Game:
    """
        defines the init method, play_round method, play_games method of class Game to instantiate an object
    """
    def __init__(self, player_1_object, player_2_object):
        """
            creates instance variables player_1_object and player_2_objects to reference objects of the players
        :param player_1_object:
        :param player_2_object:
        """
        self.player_1_object = player_1_object
        self.player_2_object = player_2_object

    def play_round(self):
        """
            checks and displays the winner of every round, based on the rules of the
             game and also stores opponent's move
        :return:
        """
        move1 = self.player_1_object.move()
        move2 = self.player_2_object.move()
        print(f"{self.player_1_object.name} plays : {move1}, {self.player_2_object.name} plays: {move2}")
        if move1 == move2:
            print('This round is a tie!')
        elif beats(move1, move2):
            print(f'{self.player_1_object.name} wins this round')
            self.player_1_object.p1_score += 1
        else:
            print(f'{self.player_2_object.name} wins this round:')
            self.player_2_object.p2_score += 1

        self.player_1_object.opponent_move = self.player_1_object.\
            learn(move1, move2, self.player_1_object)
        self.player_2_object.opponent_move = self.player_2_object.\
            learn(move1, move2, self.player_1_object)

    def play_game(self):
        """
            ask user the number of rounds it wants to play, and displays the winner of the game.
        :return:
        """
        print("Game start!")
        number_of_rounds = int(input('Enter the number of rounds per game: '))
        for each_round in range(1, number_of_rounds + 1):
            print(f"Round {each_round}:")
            self.play_round()
        print("\nGame over!\n")
        print("Final Score")
        if self.player_1_object.p1_score > self.player_2_object.p2_score:
            print(f"{self.player_1_object.name} won {self.player_1_object.p1_score} round(s), "
                  f"{self.player_2_object.name} won {self.player_2_object.p2_score} round(s)")
            print(f'{self.player_1_object.name} wins the game')
        elif self.player_1_object.p1_score == self.player_2_object.p2_score:
            print(f"{self.player_1_object.name} won {self.player_1_object.p1_score} round(s), "
                  f"{self.player_2_object.name} won {self.player_2_object.p2_score} round(s)")
            print('No winner, it is a tie')
        else:
            print(f"{self.player_1_object.name} won {self.player_1_object.p1_score} round(s), "
                  f"{self.player_2_object.name} won {self.player_2_object.p2_score} round(s)")
            print(f'{self.player_2_object.name} wins the game')


if __name__ == '__main__':
    game = Game(RandomPlayer('computer'), HumanPlayer('sam'))
    game.play_game()
