class Animal:
    def __init__(self, species: str, name: str, age: int, weight: float, height: float, illness: str):

        assert type(species) == str, f"Species should be a string"
        assert species.strip() != "", f"Species must be provided"
        assert type(name) == str, f"Name should be a string"
        assert name.strip() != "", f"A name must be provided"
        assert type(age) == int, f"Age should be a integer"
        assert age > 0, f"Age must be greater than 0"
        assert type(weight) == float, f"Weight must be a number"
        assert weight > 0, f"Weight must be greater than 0"
        assert type(height) == float, f"Height must be a number"
        assert height > 0; f"Height must be greater than 0"
        assert type(illness) == str, f"Illness should be a string"
        assert illness.strip() != "", f"Illness must be provided"

        self.__species = species
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height
        self.__illness = illness

    @property
    def species(self):
        return self.__species

    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age

    @property
    def weight(self):
        return self.__weight

    @property
    def height(self):
        return self.__height

    @property
    def illness(self):
        return self.__illness