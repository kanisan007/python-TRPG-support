import random

def input_as_int(prompt: any) -> int:
    return int(input(prompt))

class Dice:
    def __init__(self, dice_notation: str):
        dice_notation.replace('D', 'd')
        dice_data_list = dice_notation.split('d')

        self.times = int(dice_data_list[0])
        self.faces = int(dice_data_list[1])

    def roll(self) -> int:
        result = 0
        for _ in range(self.times):
            result += random.randint(1, self.faces)
        return result



