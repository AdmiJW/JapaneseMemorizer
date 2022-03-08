import random

from src.utils.enums import Topic, GameMode
from src.utils.japanese import Character



# A class to encapsulate details on a game session
class Question:
    def __init__(
        self,
        question_no: int,
        topic: Topic,
        game_mode: GameMode,
        character: Character
    ):
        # Mixed value - Randomly select
        if topic == Topic.MIXED: topic = random.choice( (Topic.HIRAGANA, Topic.KATAKANA) )
        if game_mode == GameMode.MIXED: game_mode = random.choice( (GameMode.WRITING, GameMode.RECOGNITION) )

        self.question_no = question_no
        self.topic = topic
        self.game_mode = game_mode
        self.character = character
        self.player_ans = 'N/A'
        self.peeked = False
        self.answer = Question.get_answer(self.topic, self.game_mode, self.character)
        self.question = Question.get_question(self.topic, self.game_mode, self.character)


    @staticmethod
    def get_question(topic: Topic, game_mode: GameMode, character: Character) -> str:
        if topic == Topic.MIXED or game_mode == GameMode.MIXED:
            raise ValueError("get_question() does not allow MIXED values!")

        # Writing
        if game_mode == GameMode.WRITING:
            return f"Write the {topic.value} character for romaji '{character.romaji}'."
        # Recognizing
        return f"Enter the romaji for this {topic.value} character: " \
               f"({character.hiragana if topic == Topic.HIRAGANA else character.katakana} )"



    @staticmethod
    def get_answer(topic: Topic, game_mode: GameMode, character: Character) -> str:
        if topic == Topic.MIXED or game_mode == GameMode.MIXED:
            raise ValueError("get_answer() does not allow MIXED values!")

        # Writing
        if game_mode == GameMode.WRITING:
            return character.hiragana if topic == Topic.HIRAGANA else character.katakana
        # Recognizing
        return character.romaji


    # To be shown in reports
    def get_summary(self) -> str:
        return f'<< Question {self.question_no} >>\n\n' \
               f'{self.topic.value} ({self.game_mode.value})\n' \
               f'{self.question}\n\n' \
               f'You answered: {self.player_ans}\n' \
               f'Answer: ({self.answer} )\n' \
               f'Peeked at answer?: {"Yes" if self.peeked else "No"}'



# A generator for questions, which implements iterator and can be used in a for loop to get Question(s).
# For the Question(s) that are generated, will be added to the records for later report generating use.
class QuestionGenerator:
    def __init__(
        self,
        topic: Topic,
        game_mode: GameMode,
        characters: list[Character]
    ):
        self.topic = topic
        self.game_mode = game_mode
        self.characters = characters
        self.records: list[Question] = []


    def __iter__(self): return self

    def __next__(self) -> Question:
        if not len(self.characters): raise StopIteration
        self.records.append(Question(
            len(self.records) + 1,
            self.topic,
            self.game_mode,
            self.characters.pop()
        ))
        return self.records[-1]

