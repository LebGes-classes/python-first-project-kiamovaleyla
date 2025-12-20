class Maze:
    """Класс для представления и управления лабиринтом.

    Attributes:
        width (int)
        height (int)
        exit_position (tuple[int, int])
        player_start_position (tuple[int, int])
    """

    def __init__(self) -> None:
        """Инициализирует лабиринт с фиксированной картой."""

        self.width = 15
        self.height = 10
        self.exit_position = (13, 8)
        self.player_start_position = (1, 1)

        # Карта лабиринта: '█' - стена, ' ' - путь, 'E' - выход
        self.map = [
            "███████████████",
            "█     █       █",
            "█ ███ █ █████ █",
            "█ █   █     █ █",
            "█ █ █████ █ █ █",
            "█ █     █ █   █",
            "█ █████ █ █ █ █",
            "█       █   █ █",
            "███████   ███E█",
            "███████████████"
        ]

    def is_wall(self, x: int, y: int) -> bool:
        """Проверяет, является ли указанная клетка стеной.

        Args:
            x (int)
            y (int)

        Returns:
            bool: True если клетка является стеной или находится за пределами
                  лабиринта, False если это проход.
        """

        if 0 <= x < self.width and 0 <= y < self.height:
            return self.map[y][x] == '█'

        return True

    def is_exit(self, x: int, y: int) -> bool:
        """Проверяет, является ли указанная клетка выходом из лабиринта.

        Args:
            x (int)
            y (int)

        Returns:
            bool: True если клетка является выходом, False в противном случае.
        """

        return (x, y) == self.exit_position

    def get_cell(self, x: int, y: int) -> str:
        """Возвращает символ, находящийся в указанной клетке.

        Args:
            x (int)
            y (int)

        Returns:
            str: Символ клетки ('█', ' ', 'E') или '█' если за пределами лабиринта.
        """

        if 0 <= x < self.width and 0 <= y < self.height:
            return self.map[y][x]

        return '█'

    def display(self, player_x: int, player_y: int) -> list[str]:
        """Создает отображение лабиринта с указанной позицией игрока.

        Args:
            player_x (int)
            player_y (int)

        Returns:
            list[str]: Список строк, представляющих лабиринт с игроком.
                      Игрок обозначается символом 'P'.
        """

        display_map = []

        for y in range(self.height):
            row = list(self.map[y])

            if y == player_y and 0 <= player_x < self.width:
                if row[player_x] != '█':
                    row[player_x] = 'P'

            display_map.append(''.join(row))

        return display_map