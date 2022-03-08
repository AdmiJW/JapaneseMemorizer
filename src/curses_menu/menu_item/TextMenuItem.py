from src.curses_menu.menu_item.IMenuItem import IMenuItem
import curses


# The menu item that allows for entering inline text. Does not support newlines, only printable characters and
# backspacing
class TextMenuItem(IMenuItem):
    def __init__(
        self,
        window,
        prompt: str,
        initial_string: str = '',
        return_on_enter: bool = False,
        text_color=0,
        highlight_color=0
    ):
        if type(initial_string) is not str: raise ValueError("initial_string must be of type str!")

        self._window = window                        # curses window
        self._prompt = prompt                        # prompt text
        self._value = initial_string                 # the value of the text menu item
        self._return_on_enter = return_on_enter      # Whether to return the text value when ENTER is pressed
        self._text_color = text_color                # text color
        self._highlight_color = highlight_color      # text highlighted color


    @staticmethod
    def factory(
        prompt: str,
        initial_string: str = '',
        return_on_enter: bool = False,
        text_color=0,
        highlight_color=0
    ):
        return lambda window: TextMenuItem(
            window, prompt, initial_string, return_on_enter, text_color, highlight_color
        )


    def get_value(self): return self._value


    def set_value(self, value: str):
        if type(value) is not str: raise ValueError("value must be of type str!")
        self._value = value


    def key_listener(self, key: int):
        if chr(key).isprintable() and key not in (curses.KEY_LEFT, curses.KEY_RIGHT):
            self._value += chr(key)
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            self._value = self._value[:-1]
        elif key in (curses.KEY_ENTER, 10, 13) and self._return_on_enter:
            return self._value


    def draw(self, highlighted: bool = False):
        self._window.clear()
        if highlighted:
            self._window.addstr( f'=> {self._prompt}', self._highlight_color | curses.A_BOLD)
            self._window.addstr(f'{self._value}_', self._highlight_color)
        else:
            self._window.addstr(f'   {self._prompt}{self._value}', self._text_color)
        self._window.refresh()
