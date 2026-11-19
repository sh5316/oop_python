class GameObject:
    def __init__(self,name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def info(self):
        return f"{self.name} ({self.x}, {self.y})"


class Character(GameObject):
    def __init__(self, name):
        super().__init__(name)
       
class Monster(GameObject):
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power

class Warrior(Character):
    pass

# 5. 마법사 클래스
class Wizard(Character):
    pass

# 6. 드래곤 클래스
class Dragon(Monster):
    pass

# 7. 슬라임 클래스
class Slime(Monster):
    pass

d = Dragon("드래곤", 50)
d.move(3, 4)
print(d.info())
print(isinstance(d, Monster), isinstance(d, GameObject), isinstance(d, Character))


