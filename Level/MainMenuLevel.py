import pymunk

from Engine.level import Level
from Engine.physics import PhysicsGroup
from Engine.config import WINDOW_SIZE

from player import Player
import pygame
from Engine.loading import load_image


class MenuLevel(Level):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, size=(800, 600), zoom_constraint=[.25, 3.5], **kwargs)

    def pregenerate(self):
        self.background = pygame.transform.scale(load_image('Level\\background.jpg', alpha=False), self.size)

        space = pymunk.Space()
        space.damping = 1
        space.gravity = [0, 0]
        group = PhysicsGroup(space)
        self.phys_group = group

        level_rect = self.get_world_rect()
        ps = [level_rect.topleft,
              level_rect.topright,
              level_rect.bottomright,
              level_rect.bottomleft]
        for n in range(-1, 3):
            b = pymunk.Body(body_type=pymunk.Body.STATIC)
            s = pymunk.Segment(b, ps[n], ps[n + 1], 2)
            space.add(b, s)

        from player import Player

        p_pos = [e / 2 for e in self.size]
        self.camera.position = p_pos
        self.camera.instant_move()

        self.player = Player(self)
        self.player.position = p_pos
        from player import Effect
        b = Effect()
        self.add(b)
        b.position = (100, 100)
        self.obj = b

    def end_game(self):
        self.gui.checkout_menu(self.gui.record)

    def draw(self, surface):
        from Engine.geometry import Vec2d
        surface.blit(
            pygame.transform.scale(
                self.background.subsurface(self.camera.get_rect().pygame),
                self.screen.size),
            self.screen.topleft)
        # print(self.player.angle, (self.mouse_world - self.player.pos).angle)
        super().draw(surface)
        # draw_debug(self.camera, surface, self.phys_group.sprites())
