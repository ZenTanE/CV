from person import Person

class Developer(Person):

    def __init__(self, name, languages, 
                 email, phone, LinkedIn, GitHub, 
                 programming_languages, 
                 bio):
        Person.set_name(self, name)
        Person.set_languages(self, languages)
        self.set_email(email)
        self.set_phone(phone)
        self.set_LinkedIn(LinkedIn)
        self.set_GitHub(GitHub)
        self.set_programming_languages(programming_languages)
        self.set_bio(bio)
    
    def __str__(self):
        text = super().__str__()
        text += f"\nEmail: {self.get_email()}"
        text += f"\nPhone: {self.get_phone()}"
        text += f"\nLinkedIn: {self.get_LinkedIn()}"
        text += f"\nGitHub: {self.get_GitHub()}"
        
        languages = self.get_programming_languages()
        if len(languages) > 0:
            language_counter = 0
            text += f"\nProgramming languages: {languages[language_counter]}"
            language_counter += 1
            while language_counter < len(languages):
                if (language_counter != len(languages)):
                    text += ", "
                text += languages[language_counter]

                language_counter += 1

        text += f"\nBio: {self.get_bio()}"
        return text
    
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email
    
    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_LinkedIn(self):
        return self.__LinkedIn

    def set_LinkedIn(self, LinkedIn):
        self.__LinkedIn = LinkedIn
    
    def get_GitHub(self):
        return self.__GitHub

    def set_GitHub(self, GitHub):
        self.__GitHub = GitHub

    def get_programming_languages(self):
        return self.__programming_languages
    
    def set_programming_languages(self, programming_languages):
        self.__programming_languages = programming_languages
    
    def get_bio(self):
        return self.__bio

    def set_bio(self, bio):
        self.__bio = bio