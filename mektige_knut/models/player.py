from .character import Character

class Player():
    __username: str
    __characters: list[Character]
    __level: int
    __exp: int