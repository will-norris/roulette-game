import random


class RouletteTile:

    def __repr__(self):
        """
        Added for debugging purposes so I could check tiles were generated correctly
        """
        return f'Tile: {self.number}, {self.colour}'

    def __init__(self, number, colour):
        self.number = number
        self.colour = colour


class RouletteWheel:

    TILE_COUNT = 36

    def __init__(self):
        self.tiles = []
        for tile_num in range(0,self.TILE_COUNT + 1):
            if tile_num == 0:
                colour = 'green'
            elif tile_num % 2 == 0:
                colour = 'black'
            else:
                colour = 'red'
            self.tiles.append(RouletteTile(tile_num, colour))

    def _spin(self) -> RouletteTile:
        return random.choice(self.tiles)

    def check_result(self, user_tile: RouletteTile, tile_landed_on: RouletteTile) -> str:
        """
        Check the result of a spin and return a string representing the result
        """
        if user_tile.number == tile_landed_on.number:
            return 'won'
        return 'lost'
    
    def play_round(self) -> str:
        """
        Pick a tile for the user and the casino and return a result from the customer
        point of view
        """
        user_tile = self._spin()
        tile_landed_on = self._spin()
        return self.check_result(user_tile, tile_landed_on)


class RouletteGame:

    def __init__(self, wallet: int, bet_amount: int, win_amount: int):
        self.wheel = RouletteWheel()
        self.bet_amount = bet_amount
        self.wallet = wallet
        self.win_threshold = wallet + win_amount

    def update_financials(self, spin_result: str) -> None:
        """
        Update the financial situation based on the result of a spin (won/lost)
        """
        if spin_result == 'won':
            self.wallet += self.bet_amount
            self.bet_amount = self.bet_amount * 2
        else:
            self.wallet -= self.bet_amount
        print(f'You {spin_result} {self.bet_amount}! Wallet is now {self.wallet}')

    def play(self) -> None:
        """
        Play a game of roulette until you hit the win threshold or
        run out of money
        """
        while self.wallet <= self.win_threshold:
            if self.bet_amount > self.wallet:
                print('You do not have enough money to keep playing - Game over')
                exit(0)

            spin_result = self.wheel.play_round()
            self.update_financials(spin_result)

        # if you make it this far you've won
        print(
            f'You beat the game! Wallet amount of {self.wallet} '
            f'exceeds win threshold of {self.win_threshold}'
        )

def play_roulette():
    wallet = random.randint(100,500)
    bet_amount = 20
    win_amount = 10
    game = RouletteGame(wallet, bet_amount, win_amount)
    game.play()

if __name__ == "__main__":
    play_roulette()
