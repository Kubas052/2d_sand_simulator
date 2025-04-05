import pygame
LIGHT_GREY = (55,55,55)

class Grid:
    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.cols = width // cell_size
        self.cell_size = cell_size
        self.cells = [[None for _ in range(self.cols)] for _ in range(self.rows)]

    def draw(self, window):
        for row in range(self.rows):
            for col in range(self.cols):
                color = LIGHT_GREY
                particle = self.cells[row][col]
                if particle is not None:
                    color = particle.color
                pygame.draw.rect(window, color, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))

    def add_particle(self, row, col, particle_type):
        if 0 <= row < self.rows and 0 <= col < self.cols and self.is_cell_empty(row, col):
            self.cells[row][col] = particle_type()

    def remove_particle(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.cells[row][col] = None

    def is_cell_empty(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if self.cells[row][col] is None:
                return True
        return False

    def set_cell(self, row, col, particle):
        if not(0 <= row < self.rows and 0 <= col < self.cols):
            return
        self.cells[row][col] = particle

    def get_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.cells[row][col]
        return None

    def clear(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.remove_particle(row, col)