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
        this_n_sum = []
        skip = False
        for j in range(len(this_n)):
            if skip:
                skip = False
                continue
            if j != len(this_n) - 1 and this_n[j] == this_n[j+1]:
                new_n = this_n[j] * 2
                skip = True
            else:
                new_n = this_n[j]

            this_n_sum.append(new_n)
        return np.array(this_n_sum)

    def make_move(self, move):
        for i in range(N):
            if move in 'lr':
                this = self.grid[i, :]
            else:
                this = self.grid[:, i]

            flipped = False
            if move in 'rd':
                flipped = True
                this = this[::-1]

            this_n = self._get_nums(this)

            new_this = np.zeros_like(this)
            new_this[:len(this_n)] = this_n

            if flipped:
                new_this = new_this[::-1]

            if move in 'lr':
                self.grid[i, :] = new_this
            else:
                self.grid[:, i] = new_this

    def play(self):
        self.new_number(k=2)
        while True:
            print(self.grid)
            cmd = input()
            if cmd == 'q':
                break
            old_grid = self.grid.copy()
            self.make_move(cmd)
            if all((self.grid == old_grid).flatten()):
                continue
            self.new_number()


if __name__ == '__main__':
    game = Py2048Logic()
    game.play()
