# PetrinetGenerator
 
# 使い方


最初はファイル名，プレース，トランジションを入力しないと他が入力できない使用になっている為，この3項目を入力する

![image](https://user-images.githubusercontent.com/39249651/108157364-df5bdc00-7125-11eb-9994-416cfbb79bc1.png)



これらを入力するとRange of Loop Sizeが入力できる．この部分では共通路出口から入口までのループの大きさを範囲入力する．また，最大値の制限が右に表示される（最小値は常に4）

![image](https://user-images.githubusercontent.com/39249651/108157469-2ba71c00-7126-11eb-966a-77e8b6019b0e.png)



ループ長の設定が終了するとCommonPath項目が入力できるようになる．BFVではネット内にある共通路が全て同じブランチ数(NotAvailavle)になるか，それともばらつく(Available)ようにするか決定する．Availableを選択した場合は自由度(Degree of freedom)が入力可能となり，自由度を入力する．
　出口数(Branch Variance)は，NotAvairableの場合，そのまま共通路出口の本数となり，Availableの場合はとりうる出口数の最小の数となる．

![image](https://user-images.githubusercontent.com/39249651/108157858-12eb3600-7127-11eb-80da-55a331da5ec0.png)


# 環境構築
NASでMinami->PetriGeneratorが存在するため，これを取ってくる

PetrinetGanerator->Form1.pyを選択して適当なエディターで起動



## VScodeを使う場合

1:Form1.pyを開く

2:表示>コマンドパレットを選択して，「インタープリターを選択」し，anaconda環境のものを選択

## コンパイルがうまくいかない場合

Anaconda3環境が必要のため，ない人はhttps://www.anaconda.com/products/individualからダウンロードする

ダウンロード後，Anaconda promptで

'conda activate'

を入力する．その他モジュール等が足りない時は，ここからcondaコマンドを使ってインストール