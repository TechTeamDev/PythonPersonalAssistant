name = input("ユーザー名を入力してください：")
print("こんにちは、"+name+"さん。")
print("Python Personal Assistant へようこそ！")
print("Python Personal Assistantは以下のようなことをお手伝いします")
print("ご用件入力画面・・・私に「こんにちは」とあいさつしてみてください")
print("計算機・・・「計算して」と入力してください")
print("ミニゲーム・・・「一緒に遊ぼうよ」と入力してください")
print("                         みなさんご存知のあの遊びでちょっとした暇つぶしができます")
print("カレンダー・・・「カレンダー見せて」と入力してください ")
print("現在時刻・・・「今何時？」と訊くと現在時刻を答えます ")
print(name+"さん、何かお手伝いできることはありますか")
youken = input("ご用件を教えてください")
#①あいさつ

if youken == ("こんにちは"):
    print(name+"さん、何かお手伝いできることはありますか")
    youken = input("ご用件を教えてください")
    
if youken == ("おはよう"):
    print(name+"さん、何かお手伝いできることはありますか")
    youken = input("ご用件を教えてください")
    
if youken == ("よう"):
    print(name+"さん、何かお手伝いできることはありますか")
    youken = input("ご用件を教えてください")
    
if youken == ("やあ"):
    print(name+"さん、何かお手伝いできることはありますか")
    youken = input("ご用件を教えてください")
    
#②計算
    
if youken == ("計算して"):
# 足し算の関数 
    def add(num1, num2):
        return num1 + num2

# 引き算の関数
    def subtract(num1, num2):
        return num1 - num2

# 掛け算の関数
    def multiply(num1, num2):
        return num1 * num2

# 割り算の関数
    def divide(num1, num2):
        return num1 / num2

    print("どの計算をするか選択してください -\n" \
        "1. 足し算\n" \
        "2. 引き算\n" \
        "3. 掛け算\n" \
        "4. 割り算\n")

# 入力内容取得
    select = input("1,2,3,4の選択肢から選んで半角で入力してください :")

    number_1 = int(input("一つ目の数をどうぞ: "))
    number_2 = int(input("二つ目の数をどうぞ: "))

    if select == '1':
        print(number_1, "+", number_2, "=",
                    add(number_1, number_2))

    elif select == '2':
        print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))

    elif select == '3':
        print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))

    elif select == '4':
        print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
    else:
        print("申し訳ございませんが、その計算はできません")
        
#③カレンダー機能
        
if youken == ("カレンダー見せて"):
    
    import calendar
    import datetime
    
    year = int(input("何年のカレンダーをお見せしましょうか: "))
    month = int(input("何月のカレンダーをお見せしましょうか: "))
    
    print(calendar.month(year,month, w=3, l=2))

# ④じゃんけんミニゲーム

if youken == ("一緒にあそぼうよ"):
    import random

    def janken():
        print("では、ジャンケンで遊びましょう")
        i = input("あなたの手を選んでください（1:グー 2:チョキ 3:パー 0:終了）=>")
        if i.isdigit():
            i = int(i)
        else:
            print("正しい数字を入力してください")
            return 5

        if i == 0:
            print("では、ジャンケンを終わりにしましょう")
            return i

        if not 0 < i <= 3:
            print("0~3の数字を選んでください")
            return i

        ih = "グー"
        if i == 2:
            ih = "チョキ"
        if i == 3:
            ih = "パー"
        print("あなたの手は{}です".format(ih))

        c = random.randint(1,3)
        ch = "グー"
        if c == 2:
            ch = "チョキ"
        if c == 3:
            ch = "パー"

        print("私の手は",ch,"です")

        if i == 1:
            if c == 1:
                print("あいこでした、気が合うんですね(^_^)")
            elif c == 2:
                print("あなたの勝ちです")
            else:
                print("あなたの負けです、なんで負けたか明日まで考えといてください")
        elif i == 2:
            if c == 1:
                print("あなたのの負けです,なんで負けたか明日まで考えといてください")
            elif c == 2:
                print("あいこでした、気が合うんですね(^_^)")
            else:
                print("あなたの負けです、なんで負けたか明日まで考えといてください")
        else:
            if c == 1:
                print("あなたの勝ちです")
            elif c == 2:
                print("あなたの負けです、なんで負けたか明日まで考えといてください")
            else:
                print("あいこでした、気が合うんですね(^_^)")
        return i

    v = 100
    while v != 0:
        v = janken()

#⑤現在時刻表示
        
if youken == ("今何時？"):
    import datetime
    dt_now = datetime.datetime.now()
    print(dt_now)

#⑥小ネタ
    
if youken == ("Hey, Siri"):
    print("どうやら違う方をお呼びしているようですね")
    print(name+"さん、何かお手伝いできることはありますか")
    youken = input("ご用件を教えてください")
if youken == ("OK Google"):
    print("どうやら違う方をお呼びしているようですね")
    print(name+"さん、何かお手伝いできることはありますか")
    youken = input("ご用件を教えてください")

#⑦終了
    
if youken == ("さようなら"):
    print("お役に立てたなら幸いです")
    import sys
    sys.exit()
    
if youken == ("じゃあね"):
    print("お役に立てたなら幸いです")
    import sys
    sys.exit()
    
if youken == ("またね"):
    print("お役に立てたなら幸いです")
    import sys
    sys.exit()
    
if youken == ("消えろ"):
    print("お会いできてうれしかったです、、、")
    import sys
    sys.exit()
if youken == ("死ね"):
    print("お会いできてうれしかったです、、、")
    import sys
    sys.exit()

#⑧バージョン情報
if youken == ("about Python Personal Assistant"):
    
    print("Test Release Developed by TechTeam")
    print("Under development 2021,3,6")

