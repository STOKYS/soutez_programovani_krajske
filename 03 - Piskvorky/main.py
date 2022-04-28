import pygame


EMPTY = 2
WHITE = 1
BLACK = 0
CELL_OPTIONS = [EMPTY, WHITE, BLACK]
WIN = 4
DIRECTIONS = [
    (-1, -1), # Top left to bottom right
    (-1, 0),  # Top to bottom
    (-1, 1),  # Top right to bottom left
    (0, -1)   # Left to right
]
CURRENT = 1

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('data/media/opensans.ttf', 30)
clock = pygame.time.Clock()
pygame.display.set_caption('Piskvorky')
screen = pygame.display.set_mode([900, 700])


img_player_circle = pygame.image.load('data/media/circle.png')
img_player_cross = pygame.image.load('data/media/cross.png')


class App:
    def __init__(self, size, rounds, players):
        self.running = True
        self.game = True
        self.size = size
        self.rounds = rounds
        self.round = 1
        self.turn = False
        self.players = players
        self.fields = [[2 for x in range(self.size)] for x in range(self.size)]
        self.mouse = (0, 0)
        self.win_list = []

    def fnc_update(self):
        self.fnc_draw()

    def fnc_place(self):
        self.mouse = pygame.mouse.get_pos()
        pos = [int(x / (700 / self.size)) for x in self.mouse]
        if self.fields[pos[0]][pos[1]] == 2 and self.game:
            self.fields[pos[0]][pos[1]] = 0 if self.turn else 1
            self.turn = not self.turn
            self.fnc_win()

    def fnc_win(self):
        state = [[[0] * len(DIRECTIONS) for _ in self.fields[0]] for _ in range(2)]
        white_win = False
        black_win = False
        for y, row in enumerate(self.fields):
            state = state[::-1]
            for x, color in enumerate(row):
                cell = state[CURRENT][x]
                for dir_index, (y_diff, x_diff) in enumerate(DIRECTIONS):
                    prev_x = x + x_diff
                    if color == EMPTY:
                        cell[dir_index] = 0
                    elif 0 <= prev_x < len(row) and color == self.fields[y + y_diff][prev_x]:
                        cell[dir_index] = state[CURRENT + y_diff][prev_x][dir_index] + 1
                    else:
                        cell[dir_index] = 1
                    if cell[dir_index] == WIN:
                        if color == WHITE:
                            white_win = True
                        else:
                            black_win = True
                        if white_win or black_win:
                            print(white_win, black_win)
                            self.win_list.append(self.players[0] if white_win else self.players[1])
                            self.round += 1
                            if self.round > self.rounds:
                                self.game = False
                                self.fnc_draw_players()
                                self.fnc_end()
                            else:
                                self.fnc_reset()

    def fnc_reset(self):
        self.fields = [[2 for x in range(self.size)] for x in range(self.size)]
        self.turn = True if self.round % 2 == 0 else False

    def fnc_end(self):
        counter = 0
        num = self.win_list[0]
        for i in self.win_list:
            curr_frequency = self.win_list.count(i)
            if curr_frequency > counter:
                counter = curr_frequency
                num = i
        __font = pygame.font.Font('data/media/opensans.ttf', 60)
        text = font.render(f'END: {num} is the winner!', True, (255, 0, 0))
        text_rect = text.get_rect(center=(900 / 2, 700 / 2))
        screen.blit(text, text_rect)

    def fnc_draw(self):
        self.fnc_draw_grid()
        self.fnc_draw_gui()
        self.fnc_draw_players()

    def fnc_draw_grid(self):
        __blockSize = int(700 / self.size)
        for x in range(0, 700, __blockSize):
            for y in range(0, 700, __blockSize):
                rect = pygame.Rect(x, y, __blockSize, __blockSize)
                pygame.draw.rect(screen, (255, 255, 255), rect, 1)

    def fnc_draw_gui(self):
        screen.blit(font.render(f'(x) {self.players[0]}', True, (255, 255, 255)), (750, 10))
        screen.blit(font.render(f'(o) {self.players[1]}', True, (255, 255, 255)), (750, 50))
        screen.blit(font.render('>', True, (255, 255, 255)), (720, 50) if self.turn else (720, 10))
        screen.blit(font.render(f'Round: {self.round} / {self.rounds}', True, (255, 255, 255)), (750, 130))
        screen.blit(font.render(f'Size: {self.size}x{self.size}', True, (255, 255, 255)), (750, 180))
        for x, player in enumerate(self.win_list):
            screen.blit(font.render(f'{player}', True, (255, 255, 255)), (750, 250 + x * 50))

    def fnc_draw_players(self):
        for x, i in enumerate(self.fields):
            for y, j in enumerate(i):
                if self.fields[x][y] == 0:
                    screen.blit(font.render('o', True, (255, 255, 255)), (x * (700 / self.size), y * (700 / self.size)))
                elif self.fields[x][y] == 1:
                    screen.blit(font.render('x', True, (255, 255, 255)), (x * (700 / self.size), y * (700 / self.size)))


def main():

    app = App(14, 3, ["David", "John"])

    while app.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    app.running = False
            if event.type == pygame.MOUSEBUTTONUP:
                app.fnc_place()

        if app.game:
            screen.fill((20, 20, 20))
            app.fnc_update()

        pygame.display.flip()
        clock.tick(5)

    pygame.quit()


if __name__ == "__main__":
    main()
