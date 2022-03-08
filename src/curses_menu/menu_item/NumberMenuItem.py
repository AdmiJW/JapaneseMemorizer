from src.curses_menu.menu_item.IMenuItem import IMenuItem
import curses


# The menu item that allows for entering numbers by LEFT/RIGHT arrow. Good for inputting numbers within small
# ranges
class NumberMenuItem(IMenuItem):
    def __init__(
        self,
        window,
        prompt: str,
        min_val: int = 0,
        max_val: int = 10,
        increment: int = 1,
        initial_value: int = 0,
        return_on_enter: bool = False,
        text_color=0,
        highlight_color=0
    ):
        if type(initial_value) is not int: raise ValueError("initial_value must be of type int!")

        self._window = window                        # curses window
        self._prompt = prompt                        # prompt text
        self._min_val = min_val                      # Minimum value
        self._max_val = max_val                      # Maximum value
        self._increment = increment                  # Increment by x when LEFT/RIGHT arrow pressed
        self._value = initial_value                  # The value held by this menu item
        self._return_on_enter = return_on_enter      # Whether to return the text value when ENTER is pressed
        self._text_color = text_color                # text color
        self._highlight_color = highlight_color      # text highlighted color


    @staticmethod
    def factory(
        prompt: str,
        min_val: int = 0,
        max_val: int = 10,
        increment: int = 1,
        initial_value: int = 0,
        return_on_enter: bool = False,
        text_color=0,
        highlight_color=0
    ):
        return lambda window: NumberMenuItem(
            window, prompt, min_val, max_val, increment, initial_value, return_on_enter, text_color, highlight_color
        )


    def get_value(self): return self._value


    def set_value(self, value):
        if type(value) is not int: raise ValueError("Provided value must be of type int!")
        if not (self._min_val <= value <= self._max_val): raise ValueError("Provided value does not fall in range!")
        self._value = value


    def key_listener(self, key: int):
        if key == curses.KEY_LEFT:
            self._value = max(self._min_val, self._value - self._increment)
        elif key == curses.KEY_RIGHT:
            self._value = min(self._max_val, self._value + self._increment)
        elif key in (curses.KEY_ENTER, 10, 13) and self._return_on_enter:
            return self._value


    def draw(self, highlighted: bool = False):
        self._window.clear()
        if highlighted:
            self._window.addstr(f'=> {self._prompt}', self._highlight_color | curses.A_BOLD)
            self._window.addstr(f'< {self._value} >', self._highlight_color)
        else:
            self._window.addstr(f'   {self._prompt}{self._value}', self._text_color)
        self._window.refresh()
