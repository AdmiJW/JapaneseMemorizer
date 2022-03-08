from abc import ABC, abstractmethod

# curses_menu item abstract class / interface:
# Represents a single menu item in a text based UI menu.
class IMenuItem(ABC):
    # Reacts to keypresses when the menu item is highlighted
    @abstractmethod
    def key_listener(self, key: int): pass
    # Draw to the curses screen that are specifically for this menu item.
    @abstractmethod
    def draw(self, highlighted: bool): pass
    # Returns the value held by the MenuItem. Eg: boolean for checkbox, string for text input
    @abstractmethod
    def get_value(self): pass
    # Sets the value held by the MenuItem. Input validation shall be done here
    @abstractmethod
    def set_value(self, value): pass

    # Returns a curried function f(window) that constructs a menu_item using the provided window. This is mainly used
    # in Menus as the window is only made during the run() function - We need a way to add IMenuItem
    # to an IMenu without specifying window
    @staticmethod
    @abstractmethod
    def factory(*args): pass
