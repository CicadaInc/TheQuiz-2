from Engine.geometry import Vec2d
from Engine.physics import BaseCreature
from Engine.loading import load_model, cast_model
from Engine.character import BasePlayer
import pymunk

model = load_model('Models/Player')


class PlayerBody(BaseCreature):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.body = pymunk.Body()
        self.shape = pymunk.Circle(self.body, 50)
        self.shape.density = 1
        self._image.fps = 2

    max_vel = 1000000
    walk_force = 1000000

    def walk(self, vec):
        cv = self.velocity
        if any(vec):
            tv = Vec2d(vec)
            tv.length = self.max_vel
            dif = tv - cv
            dif.length = self.walk_force
            self._body.force += dif
        elif abs(cv[0]) > .01 or abs(cv[1]) > .01:
            # stopping
            cv.length = self.walk_force
            self._body.force -= cv
        else:
            self.velocity = (0, 0)
        if 'nan' in str(self.position):
            print(self.position)
        print(self.velocity, self._body.force, self.position)

    @classmethod
    def init_class(cls):
        cls._frames, cls.IMAGE_SHIFT = cast_model(model, (50, 47), 3)


PlayerBody.init_class()


class Player(BasePlayer, PlayerBody):
    pass


from Engine.physics import DynamicObject


class Effect(DynamicObject):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.body = pymunk.Body()
        self.shape = pymunk.Circle(self.body, 20)
        self.shape.density = 1
        self._image.fps = 4
        self.position = (300, 400)
        self.size = (300, 300)

    @classmethod
    def init_class(cls):
        cls._frames, cls.IMAGE_SHIFT = cast_model(model, (50, 47), 1)


Effect.init_class()
