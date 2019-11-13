from Engine.interface import *
import pygame


class GameButton(Button):
    images = tuple(pygame.Surface((100, 20)) for _ in range(3))

    def post_init(self):
        self.state = False


pygame.draw.rect(GameButton.images[0], (255, 255, 255), (0, 0, 100, 20), 3)  # off
pygame.draw.rect(GameButton.images[2], (0, 255, 0), (0, 0, 100, 20), 3)  # click
pygame.draw.rect(GameButton.images[1], (255, 0, 0), (0, 0, 100, 20), 3)  # hover


class SubMenu(Menu):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = Element(self)
        self.title.rect = (0, 0, 100, 20)
        self.title.text = "It is new menu!"

        b = GameButton(self)
        self.exit_button = b
        b.rect.size = (15, 5)
        b.rect.center = (20, 60)
        b.text = "Exit"
        b.on_click = lambda: self.parent.checkout_menu(self.parent.home)


class MainMenu(Menu):
    class HomeMenu(Menu):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.title = Element(self)
            self.title.rect = (0, 0, 100, 20)
            self.title.text = "Big label with game name right here"

            b = GameButton(self)
            self.start_button = b
            b.rect.size = (15, 5)
            b.rect.center = (20, 60)
            b.text = "Start button"

            def click(self):
                if not self.state:
                    self.text = "Clicked!!!"
                else:
                    self.text = "Start button"
                self.state = not self.state

            b.on_click = lambda self=b: click(self)

            b = GameButton(self)
            self.menu_button = b
            b.rect.size = (15, 5)
            b.rect.center = (20, 68)
            b.text = "Menu button"
            b.on_click = lambda: self.parent.checkout_menu(self.parent.submenu)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.home = self.HomeMenu(self)
        self.submenu = SubMenu(self)
        self.checkout_menu(self.home)
