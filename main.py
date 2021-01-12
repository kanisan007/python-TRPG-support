import random

import toml

from define import input_as_int
from define import Dice

# 説明文

print('久遠に臥したるもの　死することなく　怪異なる永劫のうちには　死すら終焉を迎えん')

print('TRPGのお役立ち機能を作ってみました')

print('ダイス機能を使うには「1」を、狂気表を参照する場合は「2」を入力してください')

print('また、技能成功判定を行う場合は「3」、ダメージ計算（ハウスルール用）を行う場合は「4」を入力してください')


############################
# やること決定
############################

yarukoto = input_as_int('なにをしますか？\n> ')

############################
# 処理部分
############################

# ダイス機能
if yarukoto == 1:
    dice = input_as_int('何面ダイス？\n> ')
    kekka = random.randint(1, dice)
    print(kekka)

# 狂気表の参照機能
elif yarukoto == 2:
    list_dottika = input_as_int('リアルタイムなら「１」を、サマリーなら「２」を入力してください\n> ')
    dice_kekka = random.randint(1, 10)

    # 新クトゥルフ神話TRPG ルールブック P418
    madness_dict = {
        'realtime': ['健忘症', '身体症状症', '暴力衝動', '偏執症', '重要な人々', '失神', 'パニックになって逃亡する', '身体的ヒステリーもしくは感情爆発', '恐怖症', 'マニア'],
        'summary': ['健忘症', '盗難', '暴行', '暴力', 'イデオロギー/信念', '重要な人々', '収容', 'パニック', '恐怖症', 'マニア'],
    }

    # どってぃか
    if list_dottika == 1:
        print(madness_dict['realtime'][dice_kekka])

    elif list_dottika == 2:
        print(madness_dict['summary'][dice_kekka])

    else:
        raise Exception('入力が不正です。')

# 技能判定機
elif yarukoto == 3:
    ginou = input_as_int('技能の数値を入力してください。\n> ')

    cc = random.randint(1, 100)

    print(f'目標技能値は{ginou}です。')
    print(f'1d100!結果は{cc}です。')

    if ginou < cc:
        if ginou < 90:
            print('命中したが技能は失敗した。')

        elif cc == 100:
            print('ファンブルです。どんまい！')

        else:
            print('攻撃は命中しなかった。')

    elif ginou >= cc:
        if ginou / 2 >= cc:
            if ginou / 5 >= cc:
                print('エクストリーム成功です。')
            else:
                print('ハード成功です。')

        else:
            print('レギュラー成功です。')

    else:
        raise Exception('入力が不正です。')

# ダメージ計算機（ハウスルール用）
elif yarukoto == 4:
    with open('data.toml', encoding='UTF-8') as f:
        data = toml.loads(f.read())

        damage_bonus = Dice(data['damage_bonus']).roll()
        damage = Dice(data['weapon_damage']).roll()

        result = damage + damage_bonus

        print(f'ダメージボーナスは{damage_bonus}ダメージ。')
        print(f'武器のダメージは{damage}ダメージ。')
        print(f'合計は{result}ダメージです。')

# 今日は満足したので終わり！

else:
    raise Exception('入力が不正です。')
