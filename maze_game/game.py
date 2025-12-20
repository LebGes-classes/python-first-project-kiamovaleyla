from maze import Maze
from menu import Menu
from player import Player


class Game:
    """Основной класс игры, управляющий игровым процессом.

    Attributes:
        maze (Maze): Текущий лабиринт.
        player (Player): Текущий игрок.
        game_running (bool): Флаг, указывающий, активен ли игровой цикл.
    """

    def __init__(self) -> None:
        """Инициализирует игру, создавая лабиринт и игрока."""

        self.maze = Maze()
        self.player = Player(*self.maze.player_start_position)
        self.game_running = False

    def handle_input(self, key: str) -> bool:
        """Обрабатывает ввод пользователя и выполняет соответствующие действия.

        Args:
            key (str): Нажатая клавиша (в нижнем регистре).

        Returns:
            bool: True если был обработан валидный ввод, False в противном случае.
        """

        key = key.lower()

        if key in ['w', 'ц']:  # W или русская Ц

            return self.player.move(0, -1, self.maze)

        elif key in ['s', 'ы']:  # S или русская Ы

            return self.player.move(0, 1, self.maze)

        elif key in ['a', 'ф']:  # A или русская Ф

            return self.player.move(-1, 0, self.maze)

        elif key in ['d', 'в']:  # D или русская В

            return self.player.move(1, 0, self.maze)

        elif key == 'q':  # Выход в меню

            self.game_running = False

            return True

        return False

    def check_win(self) -> bool:
        """Проверяет, достиг ли игрок выхода из лабиринта.

        Returns:
            bool: True если игрок находится на клетке выхода, False в противном случае.
        """

        player_x, player_y = self.player.get_position()

        return self.maze.is_exit(player_x, player_y)

    def run_game_loop(self) -> None:
        """Запускает и управляет основным игровым циклом."""

        self.game_running = True

        while self.game_running:
            # Отображение текущего состояния
            maze_display = self.maze.display(*self.player.get_position())
            Menu.show_game_screen(maze_display, self.player.moves_count)

            # Проверка победы
            if self.check_win():
                Menu.clear_screen()
                print("╔══════════════════════════════════╗")
                print(" ║           ПОБЕДА!                ║")
                print(" ╠══════════════════════════════════╣")
                print(f" ║ Вы нашли выход за {self.player.moves_count:<3} ходов!     ║")
                print(" ╚══════════════════════════════════╝")
                input("\nНажмите Enter для возврата в меню...")
                break

            # Получение ввода
            key = input("Ваш ход: ")

            # Обработка ввода
            if key in ['w', 'a', 's', 'd', 'q', 'ц', 'ф', 'ы', 'в']:
                self.handle_input(key)
            elif key == '':  # Стрелки (пустой ввод после стрелок в некоторых терминалах)
                pass

    def start_new_game(self) -> None:
        """Начинает новую игру, сбрасывая лабиринт и игрока."""

        self.maze = Maze()
        self.player = Player(*self.maze.player_start_position)
        self.run_game_loop()

    def run(self) -> None:
        """Запускает основной цикл приложения с меню."""

        while True:
            choice = Menu.show_main_menu()

            if choice == 1:
                self.start_new_game()
            elif choice == 2:
                Menu.show_controls()
            elif choice == 3:
                Menu.show_about()
            elif choice == 4:
                Menu.clear_screen()
                print("╔══════════════════════════════════╗")
                print("║     Спасибо за игру!             ║")
                print("╚══════════════════════════════════╝")
                break


if __name__ == "__main__":
    game = Game()
    game.run()