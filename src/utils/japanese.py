import random


# A 10 x 5 x 2 matrix, forming the chart.
# The most atomic element is a Character class consisting of hiragana, katakana and romaji


# Simple class to encapsulate one character's hiragana, katakana and romaji
class Character:
    def __init__(self, hiragana: str, katakana: str, romaji: str):
        self.hiragana = hiragana
        self.katakana = katakana
        self.romaji = romaji

    def __str__(self):
        return f"({self.hiragana} , {self.katakana} , {self.romaji})"


GOJUON_ROWS = (
    'a row / 母 音 ',
    'k row / k 行 ',
    's row / s 行 ',
    't row / t 行 ',
    'n row / n 行 ',
    'h row / h 行 ',
    'm row / m 行 ',
    'y row / y 行 ',
    'r row / r 行 ',
    'w row / w 行 ',
    'n / ん '
)


GOJUON_CHART = (
    # a row
    (
        Character('あ','ア','a'),
        Character('い','イ','i'),
        Character('う','ウ','u'),
        Character('え','エ','e'),
        Character('お','オ','o')
    ),
    # k row
    (
        Character('か','カ','ka'),
        Character('き','キ','ki'),
        Character('く','ク','ku'),
        Character('け','ケ','ke'),
        Character('こ','コ','ko')
    ),
    # s row
    (
        Character('さ','サ','sa'),
        Character('し','シ','shi'),
        Character('す','ス','su'),
        Character('せ','セ','se'),
        Character('そ','ソ','so')
    ),
    # t row
    (
        Character('た','タ','ta'),
        Character('ち','チ','chi'),
        Character('つ','ツ','tsu'),
        Character('て','テ','te'),
        Character('と','ト','to')
    ),
    # n row
    (
        Character('な','ナ','na'),
        Character('に','ニ','ni'),
        Character('ぬ','ヌ','nu'),
        Character('ね','ネ','ne'),
        Character('の','ノ','no')
    ),
    # h row
    (
        Character('は','ハ','ha'),
        Character('ひ','ヒ','hi'),
        Character('ふ','フ','fu'),
        Character('へ','ヘ','he'),
        Character('ほ','ホ','ho')
    ),
    # m row
    (
        Character('ま','マ','ma'),
        Character('み','ミ','mi'),
        Character('む','ム','mu'),
        Character('め','メ','me'),
        Character('も','モ','mo')
    ),
    # y row
    (
        Character('や','ヤ','ya'),
        Character('ゆ','ユ','yu'),
        Character('よ','ヨ','yo')
    ),
    # r row
    (
        Character('ら','ラ','ra'),
        Character('り','リ','ri'),
        Character('る','ル','ru'),
        Character('れ','レ','re'),
        Character('ろ','ロ','ro')
    ),
    # w row
    (
        Character('わ','ワ','wa'),
        Character('を','ヲ','wo')
    ),
    # n row
    (
        Character('ん','ン','n'),
    )
)




# Get a List of Character instances from the GOJUON_CHART, provided with a boolean list of length 11, which
# each boolean indicates whether to include the Character in corresponding row of GOJUON_ROWS or not.
def get_characters(row_to_include: list[bool]):
    if len(row_to_include) != len(GOJUON_ROWS):
        raise ValueError(f"Length of row to include must equal to length of GOJUON_ROWS! Provided: {row_to_include}")

    characters = [
        character
        for i, row in enumerate(GOJUON_CHART)
        for character in row
        if row_to_include[i]
    ]

    return characters



