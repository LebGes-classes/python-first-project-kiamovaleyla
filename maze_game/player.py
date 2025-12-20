class Player:
    """Класс для управления игроком в лабиринте.

    Attributes:
        x (int)
        y (int)
        moves_count (int)
    """

    def __init__(self, start_x: int, start_y: int) -> None:
        """Инициализирует игрока со стартовой позицией.

        Args:
            start_x (int)
            start_y (int)
        """

        self.x = start_x
        self.y = start_y
        self.moves_count = 0

    def move(self, dx: int, dy: int, maze: 'Maze') -> bool:
        """Пытается переместить игрока в указанном направлении.

        Args:
            dx (int): Смещение по оси X (-1, 0, 1).
            dy (int): Смещение по оси Y (-1, 0, 1).
            maze (Maze): Объект лабиринта для проверки стен.

        Returns:
            bool: True если перемещение удалось, False если уперлись в стену.
        """

        new_x = self.x + dx
        new_y = self.y + dy

        if not maze.is_wall(new_x, new_y):
            self.x = new_x
            self.y = new_y
            self.moves_count += 1

            return True

        return False

    def get_position(self) -> tuple[int, int]:
        """Возвращает текущую позицию игрока.

        Returns:
            tuple[int, int]: Пара (x, y) с координатами игрока.
        """

        return self.x, self.y