import random

class BaseCharacter:
    def __init__(self, name, hp, normal_power):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.normal_power = normal_power

    def normal_attack(self, target):
        damage = random.randint(int(self.normal_power*0.8), int(self.normal_power*1.2))
        target.current_hp -= damage
        print(f"{self.name}의 일반 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.current_hp <= 0:
            print(f"{target.name}이(가) 쓰러졌습니다!")
        else:
            print(f"{target.name}의 남은 체력: {target.current_hp}")

    def show_status(self):
        print(f"{self.name}의 남은 체력은 {self.current_hp}입니다")

class Player(BaseCharacter):
    def __init__(self, name, hp, mp, normal_power, magic_power):
        super().__init__(name, hp, normal_power)
        self.max_mp = mp
        self.current_mp = mp
        self.magic_power = magic_power
        self.type_ = "인간"

    def magic_attack(self, target):
        damage = random.randint(int(self.magic_power*0.8), int(self.magic_power*1.2))
        self.current_mp -= 10  # magic_attack 메소드가 10 MP소모
        target.current_hp -= damage
        print(f"{self.name}의 마법 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.current_hp <= 0:
            print(f"{target.name}이(가) 쓰러졌습니다!")
        else:
            print(f"{target.name}의 남은 체력: {target.current_hp}")

class Monster(BaseCharacter):
    def __init__(self, name, hp, normal_power):
        super().__init__(name, hp, normal_power)
        self.type_ = "몬스터"


# 플레이어로 부터 정보 입력받기
print("이름을 입력해 주세요: ")
name = str(input(" "))


player = Player(name, 100, 50, 20, 25)
monster = Monster("몬스터", 100, 20)
while True:
    print("공격을 선택해주세요.")
    print("1. 일반 공격")
    print("2. 마법 공격")
    action = input("입력: ")

    if action == "1":
        player.normal_attack(monster)
    elif action == "2":
        if player.current_mp < 10:
            print("mp가 부족합니다.")
            continue
        player.magic_attack(monster)
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")
        continue

    if monster.current_hp <= 0:
        print(f"{player.name}님이 승리했습니다.")
        break

    monster.normal_attack(player)

    if player.current_hp <= 0:
        print(f"{player.name}님이 패배했습니다.")
        break

    player.show_status()