from abc import ABC, abstractmethod
from src.curses_menu.menu_item.IMenuItem import IMenuItem

# curses_menu abstract class / interface:
# Represents a menu and the methods that it should implement
class IMenu(ABC):
    # Starts the menu - Clears the screen, run a loop which goes print-input-return loop
    @abstractmethod
    def run(self): pass
    # Handles key input. If returns a value other than None, will cause the menu to end and return to caller.
    @abstractmethod
    def key_handler(self, key): pass
    # Obtain all the instances of menu_item attached to this menu as a Dictionary { tag: menu_item }
    @abstractmethod
    def get_menu_item_dict(self) -> dict[str, IMenuItem]: pass
    # Obtain all the instances of menu_item attached to this menu as a List [ ...menu_item ]
    @abstractmethod
    def get_menu_item_list(self) -> list[IMenuItem]: pass
    # Obtain the menu item associated with the provided tag
    @abstractmethod
    def get_menu_item(self, tag: str) -> IMenuItem: pass
    # Append a new menu item, provided with the IMenuItem.factory() curried ctor with provided tag into the menu.
    @abstractmethod
    def add_menu_item(self, tag: str, factory): pass
