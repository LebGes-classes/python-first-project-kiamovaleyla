class Player:
    """Класс для управления игроком."""

    def __init__(self, start_x, start_y):
        """Инициализация игрока."""

        self.x = start_x
        self.y = start_y
        self.moves_count = 0

    def move(self, dx, dy, maze):
        """Попытка перемещения игрока."""

        new_x = self.x + dx
        new_y = self.y + dy

        if not maze.is_wall(new_x, new_y):
            self.x = new_x
            self.y = new_y
            self.moves_count += 1

            return True

        return False

    def get_position(self):
        """Получение текущей позиции игрока."""

        return self.x, self.y
