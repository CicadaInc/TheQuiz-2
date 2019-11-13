import Engine


class GameMain(Engine.main.Main):

    def home(self):
        from Interface.main_menu import MainMenu
        self.set_level(None)
        self.set_gui(MainMenu(main=self))


if __name__ == '__main__':
    main = GameMain()
    main.start()
