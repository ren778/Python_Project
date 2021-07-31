import os

正しい答え = ["ja", "en"]
while True:
  Language = input("[ja/en]")
  正しい答え状態 = False
  for 答え in 正しい答え:
    if Language == 答え:
      正しい答え状態 = True
      break
  if 正しい答え状態:
    break

if Language == "en":
  print("Warning 1: All future text uses Google Translate. Please note that there are some mistakes.\nWarning 2: The game language is written in Japanese.\n")
print("ようこそ、サイコロのインストーラーへ" if Language == "ja" else "Welcome to the saikoro installer")
print("© 2021 RSTokyo All Rights Reserved.\n")
input("続けるにはEnterキーを押してください\n" if Language == "ja" else "Press Enter to continue\n")
while True:
  global location
  location = input("インストールする場所を指定してください(デフォルト: {0})".format(os.getcwd()) if Language == "ja" else "Specify the installation location (default: {0})".format(os.getcwd()))
  if len(location) == 0:
    location = os.getcwd()
  answer = ["yes", "no"]
  while True:
    ans = input("{0} この場所でよろしいでしょうか[yes/no]".format(location) if Language == "ja" else "{0} Are you sure you want this place?[yes/no]".format(location))
    ansswi = False
    for i in answer:
      if ans == i:
        ansswi = True
        break
    if ansswi:
      break
  if ansswi and ans == "yes":
    break

print("new folder...")
try:
  os.mkdir("{0}/saikoro".format(location))
  location = "{0}/saikoro".format(location)
  os.chdir(location)
except:
  location = "{0}/saikoro".format(location)
  os.chdir(location)
print("new folder...OK!")
print("install start")
print("datafile...")
def program1():
  import os
  os.chdir(location)
  new_dir_path = 'data/'
  if not os.path.exists(new_dir_path):
    os.mkdir(new_dir_path)
  else:
    import shutil
    shutil.rmtree(new_dir_path)
    import sys
    sys.exit(program1())

  f = open("data/data.txt", "w")
  f.write("")
  f.close()

  import os
  import urllib.error
  import urllib.request

  def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)
  url = 'https://github.com/ren778/Python_Images/raw/main/1/%E3%82%B5%E3%82%A4%E3%82%B3%E3%83%AD2.png'
  dst_path = './サイコロ1.png'
  download_file(url, dst_path)
  url = 'https://github.com/ren778/Python_Images/raw/main/1/%E3%82%B5%E3%82%A4%E3%82%B3%E3%83%AD2.png'
  dst_path = './サイコロ2.png'
  download_file(url, dst_path)
  url = 'https://github.com/ren778/Python_Images/raw/main/1/%E3%82%B5%E3%82%A4%E3%82%B3%E3%83%AD3.png'
  dst_path = './サイコロ3.png'
  download_file(url, dst_path)
  url = 'https://github.com/ren778/Python_Images/raw/main/1/%E3%82%B5%E3%82%A4%E3%82%B3%E3%83%AD4.png'
  dst_path = './サイコロ4.png'
  download_file(url, dst_path)
  url = 'https://github.com/ren778/Python_Images/raw/main/1/%E3%82%B5%E3%82%A4%E3%82%B3%E3%83%AD5.png'
  dst_path = './サイコロ5.png'
  download_file(url, dst_path)
  url = 'https://github.com/ren778/Python_Images/raw/main/1/%E3%82%B5%E3%82%A4%E3%82%B3%E3%83%AD6.png'
  dst_path = './サイコロ6.png'
  download_file(url, dst_path)
program1()
print("datafile...OK!")
print("scriptfile...")
with open("{0}/saikoro.py".format(location), mode="w", encoding="UTF-8") as f:
  f.write("import tkinter as tk\nimport random\nimport sys\n\ndef 準備():\n  global データ\n  print(\"読込中\")\n  うまく行ったか = False\n  初期 = True\n  try:\n    with open(\"data/data.txt\", encoding=\"UTF-8\") as ファイル:\n      データ = []\n      for データ行 in ファイル:\n        データ行 = データ行.rstrip(\"\\n\")\n        データ.append(データ行)\n        初期 = False\n      うまく行ったか = True\n      print(\"読み込み完了\")\n  except:\n    pass\n  if not うまく行ったか:\n    print(\"読み込み失敗\")\n    sys.exit()\n  if 初期:\n    print(\"初期設定をします\")\n    with open(\"data/data.txt\", mode=\"w\", encoding=\"UTF-8\") as ファイル:\n      データ = [str(random.randint(1, 6))]\n      for データ行 in データ:\n        ファイル.write(データ行)\n    print(\"初期設定完了 プログラムを再起動します\")\n    sys.exit(プログラム())\n\ndef メイン():\n  print(\"ウィンドウ準備中\")\n\n  global データ, サイコロの目\n  サイコロの目 = データ[0]\n\n  root = tk.Tk()\n  root.resizable(width=False, height=False)\n  root.title(\"サイコロ\")\n\n  タイトル = tk.Label(root, text=\"サイコロ!\")\n  タイトル.pack(padx=100)\n\n  サイコロ = tk.PhotoImage(file=\"サイコロ{0}.png\".format(データ[0]))\n  サイコロ画像 = tk.Label(root, image=サイコロ)\n  サイコロ画像.pack(padx=100)\n\n  def サイコロを振る():\n    global サイコロ, サイコロの目\n    サイコロの目 = random.randint(1, 6)\n    サイコロ = tk.PhotoImage(file=\"サイコロ{0}.png\".format(サイコロの目))\n    サイコロ画像['image'] = サイコロ\n\n  def 終了時():\n    global サイコロの目\n    print(\"終了準備中 書き込み中\")\n    with open(\"data/data.txt\", mode=\"w\", encoding=\"UTF-8\") as ファイル:\n      データ[0] = int(サイコロの目)\n      for データ行 in データ:\n        ファイル.write(str(データ行))\n    print(\"書き込み完了 プログラムを終了します\")\n    root.destroy()\n  root.protocol(\"WM_DELETE_WINDOW\", 終了時)\n\n  サイコロを振るボタン = tk.Button(root, text=\"サイコロを振る\", font=(\"\", 20), command=サイコロを振る)\n  サイコロを振るボタン.pack(padx=100)\n\n  print(\"ウィンドウ準備完了\")\n  root.mainloop()\n\ndef プログラム():\n  準備()\n  メイン()\n\nプログラム()")
print("scriptfile...OK!")
print("install finish")
