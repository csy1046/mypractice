import cocos
from cocos.actions import Repeat, Reverse, ScaleBy, RotateBy


class Rotate(cocos.layer.ColorLayer):
    def __init__(self):
        super(Rotate, self).__init__(64, 64, 224, 255)
        label = cocos.text.Label('haha!',
                                 font_name = 'miaomiaomiao',
                                 font_size = 32,
                                 anchor_x = 'center',
                                 anchor_y = 'center')
        label.position = 320, 240
        self.add(label)

        sprite = cocos.sprite.Sprite('b.png')
        sprite.position = 320, 240
        sprite.scale = 3
        self.add(sprite, z=1)
        
	scale = ScaleBy(3, duration=2)
        label.do(Repeat(scale + Reverse(scale)))
        sprite.do(RotateBy(360, duration=10))

cocos.director.director.init()
cocos.director.director.run(cocos.scene.Scene(Rotate()))
