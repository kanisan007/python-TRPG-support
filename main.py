import random

#説明文

print('久遠に臥したるもの　死することなく　怪異なる永劫のうちには　死すら終焉を迎えん')

print('TRPGのお役立ち機能を作ってみました')

print('ダイス機能を使うには「１」を、狂気表を参照する場合は「２」を入力してください')

print('また、技能成功判定を行う場合は「３」を入力してください')


############################
#やること決定
############################

yarukoto = int(input('なにをしますか？'))


############################
#処理部分
############################

if yarukoto==1:
#ダイス機能   
    dice = int(input('何面ダイス？'))

    kekka = random.randint(1,dice)

    print(kekka)
elif yarukoto==2:
#狂気表の参照機能
    list_dottika = int(input('リアルタイムなら「１」を、サマリーなら「２」を入力してください'))


    dice_kekka = random.randint(1,10)
    
    listA = ['健忘症','身体症状症','暴力衝動','偏執症','重要な人々','失神','パニックになって逃亡する','身体的ヒステリーもしくは感情爆発','恐怖症','マニア']
    listB = ['健忘症','盗難','暴行','暴力','イデオロギー/信念','重要な人々','収容','パニック','恐怖症','マニア']

    if list_dottika==1:
        
        print(listA[dice_kekka])

    elif list_dottika==2:

        print(listB[dice_kekka])

    else:
        print('入力が不正です。もう一度やり直してください。')

elif yarukoto==3:
#技能判定機能
    ginou = input('技能の数値を入力してください')

    cc = random.randint(1,100)

    ginou = int(ginou)

    print(f'目標技能値は{ginou}です。')
    print(f'1d100!結果は{cc}です。')


    if ginou<cc:
        if ginou<90:
            print('命中したが技能は失敗した。')

        elif cc==100:
            print('ファンブルです。どんまい！')

        else:
            print('攻撃は命中しなかった。')

    elif ginou>=cc:
        if ginou/2>=cc:
            if ginou/5>=cc:
                print('エクストリーム成功です。')
            else:
                print('ハード成功です')

        else:
            print('レギュラー成功です。')

    else:
        print('エラーなのでもう一度やり直してください')

else:
        print('入力が不正です。もう一度やり直してください。')



