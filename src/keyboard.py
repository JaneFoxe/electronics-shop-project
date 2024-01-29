from src.item import Item


class MixinLog:
    def __init__(self, language='EN'):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self.__language



class Keyboard(Item, MixinLog):
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        MixinLog.__init__(self, language)


