# coding: utf-8
import base64
import random
import urllib.parse

from app.common.constant import Code
from app.blueprint.account.constants import Permission

from PIL import Image, ImageDraw, ImageFont


class ImageChar(object):

    def __init__(self, font_color=(100, 211, 90),
                 size=(160, 60),
                 bg_color=(255, 255, 255),
                 font_size=26):

        self.size = size
        self.bg_color = bg_color
        self.font_size = font_size
        self.font_color = font_color
        self.font = ImageFont.truetype("./DejaVuSans.ttf", self.font_size)
        self.image = Image.new('RGB', size, bg_color)

    def rotate(self):
        self.image.rotate(random.randint(0, 30), expand=0)

    def draw_text(self, pos, txt, fill):
        draw = ImageDraw.Draw(self.image)
        draw.text(pos, txt, font=self.font, fill=fill)

    @staticmethod
    def rand_rgb():
        return random.randint(0, 255), random.randint(0, 255), random.randint(
            0, 255)

    def rand_point(self):
        width, height = self.size
        return random.randint(0, width), random.randint(0, height)

    def rand_line(self, num=10):
        draw = ImageDraw.Draw(self.image)
        for i in range(num):
            draw.line([self.rand_point(), self.rand_point()], self.rand_rgb())

    @staticmethod
    def random_chinese():
        txt = str(random.choice(range(10)))
        return txt

    def write_char(self, num=4):
        width, height = self.size
        gap, start = int(width / num - self.font_size), 0
        text = []
        for i in range(num):
            char = self.random_chinese()
            x = start + self.font_size * i + random.randint(0, gap) + gap * i
            self.draw_text(
                (x, random.randint(0, int((height - self.font_size) / 2))),
                char, self.rand_rgb())
            self.rotate()
            text.append(char)
        txt = "".join(text)
        self.rand_line(random.randint(3, 6))
        return txt

    def output(self):
        from io import BytesIO
        out = BytesIO()
        self.image.save(out, format="JPEG")
        out.seek(0)
        result = 'data:image/jpg;base64,{}'.format(
            urllib.parse.quote(base64.b64encode(out.read())))
        return result

    @classmethod
    def example(cls):
        instance = cls()
        instance.write_char(4)
        instance.output()


def check_permission(permission):
    tyfo_p = permission.get('tyfoPermisson', None)
    yn_p = permission.get('ynPermission', None)
    manage_p = permission.get('managePermission', None)
    if tyfo_p is None or yn_p is None or manage_p is None:
        return Code.INVALID_PARAMS
    if tyfo_p is not None:
        tyfo_p = [int(i['id']) for i in tyfo_p.get('modelPermission', [])]
    if yn_p is not None:
        yn_p = [int(i['id']) for i in yn_p.get('modelPermission', [])]
    if manage_p is not None:
        manage_p = [int(i['id']) for i in manage_p.get('modelPermission', [])]
    if list(set(tyfo_p).difference(set(Permission.tyfo_permission))) or list(set(yn_p).difference(set(Permission.yn_permission))) or list(set(manage_p).difference(set(Permission.manage_permission))):
        return Code.PERMISSION_NOT_EXIST
    return Code.SUCCESS


if __name__ == '__main__':
    image = ImageChar()
    print(image.write_char())
    print(image.output())
