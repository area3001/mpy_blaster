from team_indicator import TeamIndicator
import color
from fonts import meteo as font

display = BADGE.display()
display.fill(0)

team_r = TeamIndicator(display, color.RED, "Rex", 10, 50, 230, font.HEIGHT)
team_g = TeamIndicator(display, color.GREEN, "Giggle", 10, 90, 230, font.HEIGHT)
team_b = TeamIndicator(display, color.BLUE, "Buzz", 10, 130, 230, font.HEIGHT)