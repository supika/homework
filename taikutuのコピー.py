#3章演習
#数当てゲーム
import random
random_num = random.randint(1,20)
print("１から20までの数を当てて下さい")

for i in range(1,7):
    player = int(input("数を入力してください"))
    if player == random_num:
        print("当たりです!"+str(i)+"回で当てました")
        break
    elif player < random_num:
        print("小さいです")
    else:
        print("大きいです")
if player == random_num:
    None
else:
    print("正解は"+str(random_num)+"です")



#コラッツ数列
def collatz(number):
    if number % 2 == 0 :
        number = number / 2
        print(number)
        if number == 1:
            break
        else:
            return collatz(number)
    else:
        number = (number * 3) + 1
        print(number)
        if number == 1:
            break
        else:
            return collatz(number)

#4章
#カンマ付け
spam = ["apples","bananas","tofu","cats"]
def comma(list):
    for i in range(len(list)-1 ):
        print(list[i]+", ",end = '')
    print("and "+ list[-1],end = '')

comma(spam)

#5章
#整形表示
import pprint
bump = "か か と が ２ つ レ ン ガ の 道 雨 と 晴 れ の 隙 間 で 歌 っ た 匂 い も カ ラー で 思 い 出 せ る  今 が 未 来 だ っ た こ と の こ と"

count = {}

for i in bump:
    count.setdefault(i,0)
    count[i]=count[i]+1

pprint.pprint(count)

#ファンタジーゲームの持ち物リスト
stuff = {"ロープ":1,"たいまつ":6,"金貨":42,"手裏剣":1,"矢":12}

def display_inventory(inventrory):
    print("持ち物リスト")
    item_total = 0
    for i, v in inventrory.items():
        item_total = item_total + v
        print(str(v) + str(" ") + i)
    print("アイテム総数 " + str(item_total))

display_inventory(stuff)

#ファンタジー2
dragon_loot = {"金貨","手裏剣","金貨","金貨","ルビー"}
inv = {"金貨":42,"ロープ":1}

def add_to_inventory(inventrory,added_items):
    print("持ち物リスト")
    total_items = 0
    for i in added_items:
        setdefault(i,0)
        inventrory[i] = inventrory[i] + 1 #ここがうまく機能しない


    for a,v in inventrory.items():
        print(str(v) + a)
        total_items = total_items + v
    print("アイテム総数: " + str(total_items))


add_to_inventory(inv,dragon_loot)

#6章
#peperclipモジュール
import pyperclip
pyperclip.copy("hello world")
pyperclip.paste()

#表の表示

table_date = [["apples","oranges","cherries","banana"],
              ["Alice","Bob","Carol","David"],
              ["dogs","cats","moose","goose"]]

def print_table(x):
    col = len(table_date)
    col_width = [0] * col

    for i in range(col):
        col_width[i] = len(max(table_data[i], key=len))

    for i in range(4):
        for j in range(col):
            print(table_date[j][i].rjust(col_width[j]) + " " ,end="")
        print("")

#7章
#正規表現を用いないテキストパターン検索
def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

message = "明日415-555-4242に電話して下さい。オフィスは415-555-999です"
for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print("電話番号が見つかりました:"+chunk)
print("完了")

#9章
#選択コピー

def walk_copy(folder, ext, dst):
    ''' folder以下にある拡張子がextのファイルを、dstにコピーする
        dstがなければ作成する'''
    os.makedirs(dst, exist_ok=True)
    lower_ext = ext.lower()
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:                                      #どういうこと?
            if filename.lower().endswith(lower_ext):
                print('Copying', os.path.join(foldername, filename), '->', dst)
                shutil.copy(os.path.join(foldername, filename), dst)

# テスト用
if __name__ == "__main__":
    walk_copy('delicious', '.jpg', 'jpgs')
    walk_copy('delicious', '.txt', 'txts')


#巨大なファイルを探す

import os
import os.path

def find_huge_files(folder, min_size=100000000):
    ''' folder以下のmin_sizeを超えるファイルを検索して表示 '''
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            abs_path = os.path.join(foldername, filename) #ルートフォルダからの絶対パスじゃなくていいの?
            try:
                size = os.path.getsize(abs_path)
                if size > min_size:
                    print('Found', abs_path, '(', str(size), 'bytes )')
            except:
                pass

# テスト用
if __name__ == "__main__":
    find_huge_files('C:\\')


#連番の飛びを埋める
import os
import re
import shutil

def find_skiped_files(folder, prefix, rename=False):
    ''' folderの中のprefixから始まるファイルの連番の飛びを調べる。
        renameがTrueなら、飛びを埋めるようにファイル名を変更する。
    '''
    files = {}         # { 連番: 元ファイル名 }
    max_digit_len = 0  # 連番の最大の長さ
    rest = ''          # 残りのファイル名 (例 spam001.txtなら、'.txt')

    # 「prefix 連番 残り」を検索
    pattern = re.compile('^' + prefix + r'(\d+)(.*)')
    for filename in os.listdir(folder):
        mo = pattern.search(filename)
        if not mo:
            continue
        files[int(mo.group(1))] = filename
        max_digit_len = max(max_digit_len, len(mo.group(1)))
        rest = mo.group(2)

    # マッチするファイルがなければ終了
    if len(files) == 0:
        return

    # 連番を小さい順に並べる
    org_index = sorted(files.keys())
    start = org_index[0]
    end = org_index[-1]
    # 連番の飛びを調べる
    for n in range(start, end + 1):
        if not n in files:
            print('Missing', prefix + str(n).rjust(max_digit_len, '0') + rest)

    # 飛びを埋めるようにファイル名を変更する
    if rename:
        for n,ind in enumerate(org_index):
            # 新しいファイル名を作る
            new_filename = prefix + str(start + n).rjust(max_digit_len, '0') + rest
            # 元のファイルと同じなら何もしない
            if new_filename == files[ind]:
                continue
            # ファイル名を変更する
            print('Rename', os.path.join(folder, files[ind]),
                  '->', os.path.join(folder, new_filename))
            shutil.move(os.path.join(folder, files[ind]),
                        os.path.join(folder, new_filename))

# テスト用
if __name__ == "__main__":
    find_skiped_files('seqfiles', 'spam')
    find_skiped_files('seqfiles', 'spam', True)





#授業 ９章復習

def find_file_huge_size(path,max_size):
    for foldername, subfolders, filenames in os.wolk(path):
        print("現在のファイルは" + foldername)
        for i in filenames:
            if os.path.getsize(path + "/ " + i ) > max_size:
                print(i)

find_file_huge_size("/etc",100*1024)


#14章
#csvモジュール
import csv
example_file = open("example.csv")
example_reader = csv.reader(example_file)
example_date = list(example_reader)
example_date

#forループでReaderオブジェクトからデータを読み出す
import csv
example_file = open("example_csv")
example_reader = csv.reader(example_file)
for row in example_reader:
    print("Row #" + str(example_reader.line_num)+ " " + str(row))

#Writeオブジェクト
import csv
output_file = open("out.csv","w")
output_writer = csv.writer(output_file)
output_writer.writerow(["spam","eggs","bacon","ham"])

#ExcelからCSVへの変換
