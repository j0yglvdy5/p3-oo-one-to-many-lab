class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def pets(self):
        return self.pets_list

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added as pets.")
        pet.set_owner(self)
        self.pets_list.append(pet)

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets_list, key=lambda pet: pet.name)
        return sorted_pets



class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of {', '.join(self.PET_TYPES)}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.add_to_all_pets()

    def add_to_all_pets(self):
        self.__class__.all_pets.append(self)

    @classmethod
    def get_all_pets(cls):
        return cls.all_pets

    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner.")
        self.owner = owner
