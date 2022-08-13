from fonts import meteo as font
import color

class TeamIndicator:
    def __init__(self, display, color, name, x, y, width, height):
        self._tft = display
        self.name = name
        self.color = color
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self.value = 0

    def render(self):
        x = self._x
        self._tft.fill_rect(x, self._y, 30, 30, self.color)
        self._tft.draw(font, self.name, self._x + 40, int(self._y + (font.HEIGHT / 2)), color.WHITE)

        text_len = self._tft.draw_len(font, str(self.value))
        self._tft.draw(font, str(self.value), self._x + self._width - text_len - 10, int(self._y + (font.HEIGHT / 2)), color.WHITE)
