from src.item import Item


class MixinKeyboard:
    lang = ['EN', 'RU']

    def __init__(self, name, price, quantity):
        self.__language = self.lang[0]
        super().__init__(name, price, quantity)

    def change_lang(self):
        index = self.lang.index(self.__language)
        if index < len(self.lang) - 1:
            self.__language = self.lang[index + 1]
        else:
            self.__language = self.lang[0]
        return self

    @property
    def language(self):
        return f'{self.__language}'


class Keyboard(MixinKeyboard, Item):
    pass
