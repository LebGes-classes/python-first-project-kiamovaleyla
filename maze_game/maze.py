class Maze:
    """Класс для представления лабиринта."""

    def __init__(self):
        """Инициализация лабиринта с фиксированной картой."""

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
            "█ █     █ █ █ █",
            "█ █████ █ █ █ █",
            "█       █   █ █",
            "███████   ███E█",
            "███████████████"
        ]

    def is_wall(self, x, y):
        """Проверка, является ли клетка стеной."""

        if 0 <= x < self.width and 0 <= y < self.height:
            return self.map[y][x] == '█'

        return True

    def is_exit(self, x, y):
        """Проверка, является ли клетка выходом."""

        return (x, y) == self.exit_position

    def get_cell(self, x, y):
        """Получение символа клетки."""

        if 0 <= x < self.width and 0 <= y < self.height:
            return self.map[y][x]

        return '█'

    def display(self, player_x, player_y):
        """Отображение лабиринта с игроком."""

        display_map = []

        for y in range(self.height):
            row = list(self.map[y])

            if y == player_y and 0 <= player_x < self.width:
                if row[player_x] != '█':
                    row[player_x] = 'P'

            display_map.append(''.join(row))

        return display_map
