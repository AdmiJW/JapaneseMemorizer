from src.curses_menu.menu_item.IMenuItem import IMenuItem
import curses


# The menu item that allows for entering boolean values (True/False) in the form of checkbox. Use ENTER to
# check/uncheck
class CheckboxMenuItem(IMenuItem):
    def __init__(
        self,
        window,
        prompt: str,
        initial_value: bool = False,
        text_color=0,
        highlight_color=0
    ):
        if type(initial_value) is not bool: raise ValueError("initial_value must be a boolean!")

        self._window = window                        # curses window
        self._prompt = prompt                        # prompt text
        self._value = initial_value                  # boolean value held by this menu item
        self._text_color = text_color                # text color
        self._highlight_color = highlight_color      # text highlighted color


    @staticmethod
    def factory(
        prompt: str,
        initial_value: bool = False,
        text_color=0,
        highlight_color=0
    ):
        return lambda window: CheckboxMenuItem(window, prompt, initial_value, text_color, highlight_color)


    def get_value(self): return self._value


    def set_value(self, value):
        if type(value) is not bool: raise ValueError("initial_value must be a boolean!")
        self._value = value



    def key_listener(self, key: int):
        if key in (curses.KEY_ENTER, 10, 13):
            self._value = not self._value


    def draw(self, highlighted: bool = False):
        self._window.clear()
        self._window.addstr(
            f'{"=> " if highlighted else "   "}[{"X" if self._value else " "}] ',
            (self._highlight_color if highlighted else self._text_color) | curses.A_BOLD
        )
        self._window.addstr(self._prompt, (self._highlight_color if highlighted else self._text_color) | curses.A_BOLD)
        self._window.refresh()
