from game import Game
from player import SimplePlayer, NormalPlayer, LessThanHalfPlayer, AlwaysHalfPlayer, CombinedPlayer


def main():
    for player_type in [SimplePlayer, NormalPlayer, LessThanHalfPlayer, AlwaysHalfPlayer, CombinedPlayer]:
        sum_rounds = 0
        for _ in range(1000):
            game = Game(player_type(), SimplePlayer())
            amount_rounds = game.play_game()
            sum_rounds += amount_rounds
        print(f"{player_type.__name__} took on avg: {sum_rounds / 1000} rounds to win.")


if __name__ == '__main__':
    main()
