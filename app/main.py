class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}"
        )

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)


class Herbivore(Animal):
    def hide(self) -> None:
        super().hide()
