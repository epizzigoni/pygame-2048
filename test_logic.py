import numpy as np
import random

N = 4


class Py2048Logic:
    def __init__(self):
        self.grid = np.zeros((N, N), dtype=int)

    def __str__(self):
        return str(self.grid)

    def new_number(self, k=1):
        free_poss = list(zip(*np.where(self.grid == 0)))

        for pos in random.sample(free_poss, k=k):
            if random.random() < .1:
                self.grid[pos] = 4
            else:
                self.grid[pos] = 2

    @staticmethod
    def _get_nums(this):
        this_n = this[this != 0]

        return this_n

    def make_move(self, move):
        for i in range(N):
            this = self.grid[i, :]
            this_n = self._get_nums(this)

            new_this = np.zeros_like(this)
            new_this[:len(this_n)] = this_n
            self.grid[i, :] = new_this


if __name__ == '__main__':
    game = Py2048Logic()
    game.new_number(k=2)
    print(game)
    game.make_move(move='l')
    print(game)
