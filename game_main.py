import Engine


class GameMain(Engine.main.Main):

    def home(self):
        from Interface.main_menu import MainMenu
        from Level.MainMenuLevel import MenuLevel
        self.set_level(MenuLevel(self))
        self.set_gui(MainMenu(main=self))

    def update(self):
        # Просто для брейкпоинта - можно убрать.
        super().update()
        pass


if __name__ == '__main__':
    main = GameMain()
    main.start()
