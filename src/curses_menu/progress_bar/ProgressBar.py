
# A simple progress bar to be displayed on curses' window
class ProgressBar:
    def __init__(
        self,
        screen,
        maximum,                    # The maximum value to be considered 100% - Eg: 10 questions - maximum = 10
        bar_size: int = 40,
        border_left: str = '[',
        border_right: str = ']',
        unfilled_bar: str = '-',
        filled_bar: str = '=',
        text_color: int = 0,
    ):
        if len(border_left) != 1 or not border_left.isprintable(): raise ValueError(f"Invalid border left value")
        if len(border_right) != 1 or not border_right.isprintable(): raise ValueError(f"Invalid border right value")
        if len(unfilled_bar) != 1 or not unfilled_bar.isprintable(): raise ValueError(f"Invalid unfilled bar value")
        if len(filled_bar) != 1 or not filled_bar.isprintable(): raise ValueError(f"Invalid filled bar value")


        self._screen = screen
        self._bar_size = bar_size
        self._borders = (border_left, border_right)
        self._bars = (unfilled_bar, filled_bar)
        self._text_color = text_color
        self._maximum = maximum
        self._current = 0
        self.update(0)


    # Preset: █ and ░. Using factory design pattern
    @staticmethod
    def preset_shade(
        screen,
        maximum,
        bar_size: int = 40,
        text_color: int = 0
    ):
        return ProgressBar(screen, maximum, bar_size, ' ', ' ', '░', '█', text_color)


    # Updates and redraw the progress bar
    def update(self, current):
        if type(current) is not float and type(current) is not int: raise ValueError("updated value must be numeric")
        if not (0 <= current <= self._maximum): raise ValueError("Invalid updated value - Out of range")

        self._current = current
        self.draw()


    # Draws the progress bar
    def draw(self):
        percentage = (self._current / self._maximum)
        filled = min(self._bar_size, round(percentage * self._bar_size) )

        self._screen.clear()
        self._screen.addstr(
            f' {self._borders[0]}{self._bars[1] * filled}{self._bars[0] * (self._bar_size - filled)}{self._borders[1]}',
            self._text_color
        )
        self._screen.addstr(f' | {percentage * 100:.2f}% | {self._current}/{self._maximum}', self._text_color)
        self._screen.refresh()
