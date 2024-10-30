class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False  # Set hidden as an instance variable
        Animal.alive.append(self)

    def __len__(self) -> int:
        return len(Animal.alive)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def remove_if_dead(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @classmethod
    def bite(cls, goal: Animal) -> None:
        if isinstance(goal, Herbivore) and not goal.hidden:
            goal.health -= 50
            goal.remove_if_dead()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @classmethod
    def bite(cls, goal: Animal) -> None:
        if isinstance(goal, Herbivore) and not goal.hidden:
            goal.health -= 50
            if goal.health <= 0:
                Animal.alive.remove(goal)
