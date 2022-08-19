from player import PlayerInterface


class Game:

    player1: PlayerInterface
    player2: PlayerInterface
    rounds: int

    def __init__(self, player1: PlayerInterface, player2: PlayerInterface):
        self.player1 = player1
        self.player2 = player2
        self.rounds = 0

    def play_game(self) -> int:
        while True:
            self.rounds += 1
            # print(f"Round {self.rounds}")
            self.player1.take_turn(self.player2)
            if self.player1.figured_it_out:
                # print(f"Won!!! in {self.rounds} rounds.")
                return self.rounds
