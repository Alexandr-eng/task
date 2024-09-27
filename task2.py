class Superhero:
    def __init__(self, name):
        self.name = name

    def attack(self):
        raise NotImplementedError("Subclasses should implement this!")


class ChuckNorris(Superhero):
    def attack(self):
        return "PIU PIU"


class City:
    def __init__(self, name, antagonist):
        self.name = name
        self.antagonist = antagonist

    def get_antagonist_action(self):
        return f"{self.antagonist} stands near a skyscraper"


class MediaChannel:
    def __init__(self, name):
        self.name = name

    def announce_victory(self, superhero, city):
        return f"Today in {self.name}: {superhero.name} saved {city.name}!"


class Newspaper(MediaChannel):
    pass


class TV(MediaChannel):
    pass


# Функция для сценария
def save_city(superhero, city, media_channel):
    antagonist_action = city.get_antagonist_action()
    attack_action = superhero.attack()
    announcement = media_channel.announce_victory(superhero, city)

    print(antagonist_action)
    print(attack_action)
    print(announcement)


# Пример использования
chuck_norris = ChuckNorris("Chuck Norris")
tokyo = City("Tokyo", "Godzilla")
newspaper = Newspaper("newspapers")

save_city(chuck_norris, tokyo, newspaper)

# Другой пример
kostroma = City("Kostroma", "Aliens")
tv = TV("the first channel")

save_city(chuck_norris, kostroma, tv)