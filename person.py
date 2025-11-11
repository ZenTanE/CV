class Person:

    def __init__(self, name, languages):
        self.set_name(name)
        self.set_languages(languages)
    
    def __str__(self):
        text = f"Name: {self.get_name()}"

        languages = self.get_languages()
        if len(languages) > 0:
            language_counter = 0
            text += f"\nLanguages: {languages[language_counter]}"
            language_counter += 1
            while language_counter < len(languages):
                if (language_counter != len(languages)):
                    text += ", "
                text += languages[language_counter]

                language_counter += 1
        
        return text

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_languages(self):
        return self.__languages
    
    def set_languages(self, languages):
        self.__languages = languages