import random

def hangman(word):
    wrong = 0
    stages = ["","________","|      |","|      0","|     /|\*","|     / \*"] #6こまで
    rletters = list(word) #一文字リストに格納
    board = ["_"]*len(word)
    win = False #初期設定？
    print("ハングマンへようこそ(文字数は{}文字、間違いは{}回まで)".format(len(word),len(stages)-1))

    #ハングマン完成前ならループ
    while wrong < len(stages) - 1:
        print("\n現在{}個間違えました".format(wrong)) #改行
        msg = "1文字を予想してください"
        char = input(msg)
        if char == "exit": #exitで終了
            break
        elif char in rletters: #hit
            cind = rletters.index(char)
            print("hit!! {}文字目は{}".format(cind+1,char))
            rletters[cind] = "$"
            board[cind] = char
        else:
            wrong +=1
            print("no hit")

        print(" ".join(board)) #空白を挟んで、文字を表示
        print("\n".join(stages[0:wrong+1])) #間違いの分、ステージを表示

        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))


wordlist=["dog","cat","egg","moon"]
num = random.randint(0,3)
hangman(wordlist[num])
