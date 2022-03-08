from enum import Enum, auto


# Used to determine which menu to return to. Values has to be strictly ordered
class ReturnTo(Enum):
    EXIT = 0
    TOPIC_SELECT = 1
    CHAPTER_SELECT = 2
    GAMEMODE_SELECT = 3
    CHALLENGE = 4
    SUMMARY = 5


    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented



# Common Menu Options - OK, CANCEL, PEEK_ANS...
class MenuOption(Enum):
    OK = 'OK'
    CANCEL = 'CANCEL'
    PEEK_ANS = 'PEEK_ANS'
    SELECT_DESELECT = 'SELECT_DESELECT'



class Topic(Enum):
    HIRAGANA = 'Hiragana'
    KATAKANA = 'Katakana'
    MIXED = 'Mixed'


class GameMode(Enum):
    WRITING = 'Writing'
    RECOGNITION = 'Recognition'
    MIXED = 'Mixed'
