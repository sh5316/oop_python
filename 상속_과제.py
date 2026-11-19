# 1. 전체게임구조 클래스

class GameObject:
    def __init__(self, name):
        self.name = name


# 2. HP클래스 구조만들기
class HP:
    def __init__(self, max_hp):
        self.max_hp = max_hp
        self.current = max_hp

    def damage(self, amount):
    
        before = self.current
        self.current = max(0, self.current - amount)
        return before - self.current

    def heal_full(self):
        self.current = self.max_hp
        
    def is_alive(self):
        return self.current > 0

#3. 아이템 클래스 (부모)

class Item:
    def __init__(self, name):
        self.name = name
#8 element 속성 반영하기

class Element:
    def __init__(self, name):
        self.name = name

    def multiplier(self, target):
        strong = {
            "불": "풀",
            "풀": "물",
            "물": "불"
        }
        if self.name == target.name:
            return 1.0

        if strong[self.name] == target.name:
            return 2.0

        return 0.5

#9 Weapon 클래스 만들기

class Weapon(Item):
    def __init__(self, name, power, element):
        super().__init__(name)
        self.power = power
        self.element = Element(element)
        self.enhance = 0

    def upgrade(self):
        self.enhance +=1
        self.power +=5

    def __str__(self):
        if self.enhance == 0:
            return f"{self.name}[{self.element.name}]"
        return f"+{self.name}[{self.element.name}]"

fire = Element("불")
print(fire.multiplier(Element("풀")), fire.multiplier(Element("물")), fire.multiplier(Element("불")))



#12 레벨추가(퀘스트2)
class Level:
    def __init__(self):
        self.level = 1
        self.exp = 0

    def need(self):
        return self.level * 100

    def gain(self, amount):
        self.exp += amount
        up = 0
        while self.exp >= self.need():
            self.exp -= self.need()
            self.level += 1
            up += 1
        return up


#13. 인벤토리 추가(퀘스트3)
class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add(self, item):
        if len(self.items) >= self.capacity:
            return False
        self.items.append(item)
        return True

    def take(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return item
        return None

#10 캐릭터 클래스 만들기 12, 13 추가
class Character(GameObject):
    def __init__(self, name, max_hp, weapon):
        super.__init__(name)
        self.hp = HP(max_hp)
        self.weapon = weapon
        self.level = Level()              
        self.inventory = Inventory(5) 

    def attack(self, target):
        multiplier = self.weapon.element.multiplier(target.element)
        dmg = int(self.weapon.power * multiplier)
        target.hp.damage(dmg)
        log = [f"{self.name}의 {self.weapon} 공격! {target.name}에게 {dmg} 피해 (x{multiplier})"]
        if not target.hp.is_alive():
            log.append(f"{target.name} 처치! EXP +{target.exp_reward}")
            up = self.level.gain(target.exp_reward)
            if up:
                self.hp.max_hp += 20 * up
                self.hp.heal_full()
                log.append(f"레벨 업! Lv.{self.level.level} (최대 HP {self.hp.max_hp})")
            if target.drop and self.inventory.add(target.drop):
                log.append(f"'{target.drop.name}' 획득!")
        return log


    def equip(self, name):
        item = self.inventory.take(name)
        if item is None or not isinstance(item, Weapon):
            return False
        self.inventory.add(self.weapon)
        self.weapon = item
        return True

    def upgrade_weapon(self):
        stone = self.inventory.take("강화석")
        if stone is None:
            return False
        self.weapon.upgrade()
        return True

#11 전사캐릭터 클래스만들기(웹폰 장착)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 150, Weapon("화염검", 30, "불"))



#4 몬스터 부모 클래스만들기
class Monster(GameObject):
    def __init__(self, name, max_hp, element, exp_reward, drop=None):
        super().__init__(name)

        self.hp = HP(max_hp)
        self.element = Element(element)
        self.exp_reward = exp_reward
        self.drop = drop

#5 슬라임 클래스만들기
class Slime(Monster):
    def __init__(self):
        super().__init__("슬라임", 40, "풀", 60, Weapon("물의 창", 25, "물"))

#6 골렘 클래스만들기 
class Golem(Monster):
    def __init__(self):
        super().__init__("골렘", 120, "풀", 90, Item("강화석"))

#7 드래곤 클래스만들기
class Dragon(Monster):
    def __init__(self):
        super().__init__("드래곤", 300, "불", 500, None)