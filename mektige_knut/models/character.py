class Character():
    __race: str
    __gender: str
    __hair: str
    __hair_color: str
    __height: str

    __pain_remark: str
    __celebration_remark: str
    __flirtatious_remark: str
    __sexy_remark: str
    __angry_remark: str


    # Character remarks

    def sound_pain(self) -> None:
        print(self.__pain_remark)

    def sound_celebration(self) -> None:
        print(self.__celebration_remark)

    def sound_flirtatious(self) -> None:
        print(self.__flirtatious_remark)

    def sound_sexy(self) -> None:
        print(self.__sexy_remark)

    def sound_angry(self) -> None:
        print(self.__angry_remark)

    # Getters and setters

    def get_race(self) -> str:
        return self.__race

    def set_race(self, race: str) -> None:
        self.__race = race

    def get_gender(self) -> str:
        return self.__gender

    def set_gender(self, gender: str) -> None:
        self.__gender = gender

    def get_hair(self) -> str:
        return self.__hair

    def set_hair(self, hair: str) -> None:
        self.__hair = hair

    def get_hair_color(self) -> str:
        return self.__hair_color

    def set_hair_color(self, hair_color: str) -> None:
        self.__hair_color = hair_color

    def get_height(self) -> str:
        return self.__height

    def set_height(self, height: str) -> None:
        self.__height = height

    
