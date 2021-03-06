# Dragonfly鍵交換について
Dragonfly key exchangeは，
- パスワードとかパスフレーズを使っている
- 離散対数問題(の困難性)を使っている
- 鍵交換プロトコルの一つ

# 定義

- パスワード ..... 秘密かつ2者間で共有された単語とかの，要するに証明鍵
- a | b ..... ビット列aとビット列bの連結を示す
- len(a) ..... ビット列aの長さを返す関数
- lsb(a) ..... ビット列aの最後のビットを返す関数
- lgr(a, b) ..... aと素数bをとって，ルジャンドル記号を返す関数
  - ルジャンドル記号 .....aとbが互いに素で, bを法としてaが平方剰剰であるとき+1，それ以外(平方非余剰)のとき-1と定義する記号のこと
- min(a,b) ..... aとbの文字列を辞書順にみたときに小さいほうを返し，aとbが等しい時は0を返す関数
- max(a,b)..... aとbの文字列を辞書順にみたときに大きいほうを返し，aとbが等しい時は0を返す関数

# 命名規則

- 大文字または大文字で始まる語は群の要素(ここでは，有限巡回群のみを考える)である
- 小文字または小文字で始まる語は，スカラーである
- 楕円曲線上の点は，必ずx,y座標を持つ

# 離散対数ベースの暗号について

- Dragonflyは離散対数ベースの暗号を使う
  - 鍵共有と認証のため
- 交換する人同士はパラメータの一つの集合の中で，短命の鍵(=一時的な鍵)を計算する
- 群は，短命の鍵の計算のことだと言える
- 群はFinite Field CryptographyまたはElliptic Curve Cryptographyのベースとなるもの

# 演算の定義
- スカラーの全体をS, 群をGとする. このとき，スカラー演算とは，写像scalar-op: S×G ∋ (x, Y) |-> Z ∈ Gである. これは関数のように Z = scalar-op(x, Y) とも書かれる. 言いかえれば, scalar-opとはスカラーxと群の元Yを群の元Zへと移す写像である.

- element-opでは，群全体をGと置いたとき，群の要素{A,B: A ∈ G かつ B ∈ G}の足し算の結果はZになる．ZはZ ∈ Gとなる要素である．このことを関数的に表わすと，Z = element-op(X, Y)となる．

- 群Gにおいて，Xという要素(X ∈ G)の単位元をとると，Yという要素(Y ∈ G)がつくられる．これを関数のように， Y = inverse(X)と表す．

# 楕円曲線ベースの暗号の定義
ECC群のための領域パラメータについて述べる

- 素数がp，素数の領域がGF(p)であると定義する．
- 暗号群は， 楕円曲線上の点からなる楕円曲線群の部分群である．
- GF(p)について，曲線方程式の条件を満たす要素は，無限遠の点を特定する要素
- ECC群の群演算(=楕円曲線上の点の演算)は楕円曲線上の足し算(加算)である

FFC群についての領域パラメータ

- {a, b: a ∈ GF(p),b ∈ GF(p)}
- 点(x, y) {x,y : x ∈ GF(p) * GF(p),y ∈ GF(p) * GF(p)}は，(y^2 - x^3 - a*x - b) mod p = 0のときだけ楕円曲線上の点となる
- 楕円曲線上の点Gは十分に大きい素数のあまり
  - q >> ((p-1)/2)
- Gの位数かつGでできた暗号部分群の大きさの素数q



## (x,y)ペアの条件

1. x > 0 かつ y > 0 かつ根底となる領域の素数より小さい
2. (x,y)が曲線の方程式の条件を満たし，曲線上の点となる(ただし点の位置は無限遠ではない)
- どちらも満たされているとき，(x,y)のペアは有効な要素となる

## 演算の定義

- 点自身の何倍かの曲線の点をつくることをスカラー演算とする．
  - 点Yのx倍の点は，Z = x * Y とみることができる．よって，

  Z = x * Y = scalar-op(x, Y)

- 要素演算は，曲線上の2点を加算する．
  - 今回の場合，点Xと点Yの加算はZ = X + Y となる．よって，

  Z = X + Y = element-op(X, Y)

- 逆関数　 ..... 要素の加算で，逆元との加算は0となる．
  - つまり，楕円曲線群の無限遠の点のようにふるまう．

  R + inverse(R) = "0"

- 楕円曲線群は，群の要素を整数に変換する写像関数で，q = F(Q)と表せる．これは，X座標をqとして，関数の返り値がX座標となるようにしている．

- scalar-opは，element-opの反復として見ることができる

    つまり，
    Y = scalar-op(x, Y)

    x = 1に関して，

    Y = scalar-op(1, Y) = element-op(Y, scalar-op(x-1,Y))

element-op(X, Y)の定義はRFC6090を参照

# 有限領域ベースの暗号の定義

- pは素数，GF(p)は素数領域と定義する．GF(p)は整数pを法とする

- FFC群 ..... GF(p)* の部分群．
  - *は0を除くという意味．

FFC群の群演算はpを法とする掛け算だ．これは群要素をA,B,Cとおいたとき，C = A * B mod pと同一である．

要素GはGF(p)*の一つの要素で，乗法の位数は(p - 1)/2より十分大きな素数の余りであるような
- FFC群の生成元として使える．

qは素数，Gの乗法の位数，つまりG^qのq．

    -> Gによって生成されるGF(p)の部分群のサイズ

[](なにこれは．．．)
スカラ演算は素数の余剰の発生源の累乗法

## 数字がFFC群で恒等の要素の条件
次の2つの条件を両方満たす必要がある

1. 1 < 要素 < p - 1
2. 群の位数の要素の掛け算のmod pは1

# Dragonfly Key Exchangeの定義

## 二人の参加者の条件
1. 二人の参加者はは共通のパスワードを持っている
   1. 検証者がいるときは拡張しない

   ->クライアントサーバープロトコルがP2P Appと同時に使われることを許可する
2. 両方がEECまたはFFCのどちらかを使う(どちらも使われることはない)

## 前処理
- 両方のピアはドメインパラメータの集合の中で，秘密の要素を導く
  - これを"hunting-and-pecking"技術と呼ぶ．FFC，ECCそれぞれにある．

   これらはSection3.2.に書かれている

    - しかし，合意された安全で決定的な方法ならなんでもよい
      - 例えば[hash2ec]の技術はECC群のために使われている

## Dragonfly Exchangeの構成
- 2つのメッセージ交換から構成される
1. Commit exchange

お互いが，「パスワードがただ1つに決まる」，ということを約束する

2. Confirm exchange

パスワードの情報を確認する．つまり，パスワードが本物かどうかを確かめる

## 副作用
Dragonfly Exchangeを実行すると，秘密鍵が本物であることも証明される

## 使用関数
 - H() .....ランダム関数
 - F() ..... マッピング関数
 - KDF() ..... 鍵導出関数

# 前提

- 攻撃回避のための前提

1. 関数H ..... 可変長のバイナリ列をxビットの長さのバイナリ列で出力するランダムオラクル([RANDOR]を参照)．今回は(というか一般的に)暗号学的ハッシュ関数を用いる．

    H: {0,1}^* --> {0,1}^x

2. 関数F ..... 群の中から要素を選んで，整数を返すマッピング関数．
   1. EEC群において，関数Fは楕円曲線上の点のx座標を返す

        ECC: x = F(P), where P=(x,y)

   2. FFC群のとき，関数Fは鍵の長さxに等しい
      - FFC群のすべての要素がすでに素数より小さい整数であるため(仮に素数をpとおくと，x < pが証明できる)

      FFC: x = F(x)

3. 関数KDF ..... k，label，nを必要とする鍵導出関数
- k ..... キーを引き延ばすためのキー(ハッシュ値とか)
- label ..... キーに結合するラベル (文字列とか)
- n ..... 目的の出力(長)を指し示す (nは長さ)

stretch = KDF-n(k, label)

※len(stretch) = n となるようにする

4. 選ばれた群に関しての離散対数問題の困難性

G，PとY = G^x mod pが与えられたとき，xを決定することは計算的に実行不可能だということから，

同様に，ECC群に関して，曲線定義(aとb)と生成元とY = x * Gが与えられたとき，xを決定するのは計算的に実行不可能だということ

5. 共有されているパスワードがあるパスワードのプールが存在する

- 例 : 辞書の文字
  - プールの各パスワードは，共有されたパスワードである確率が等しい
  - 潜在的な攻撃者.....プールを入手する機会を持っている

6. 当事者は，質のいい乱数を生成する能力を持っている

つまり，メルセンヌツイスターではない，よりランダム性の高い疑似乱数生成器を使用する必要がある．理論的には，"完全な乱数"が必要．

# パスワード(ここでは秘密鍵の意味)の導出

## 交換前にやること

- PE(Password Element)を導く
  - PEは傍から見るとランダムな要素
二つの例(ECCとFCC)が完全性(現状ではこの二つが候補)のために記載されている

選択した群の要素からsecret stringをマッピングする方法であればなんでもよい．

ECCとFFC以外の手法を利用するなら，secret string にピアのID(MACアドレスとか)を含める必要がある．


## PEの操作

パスワードの共通認識をもたなければならない

必要な処理を行ったパスワードは共有の情報として使える

ハッシュ化したパスワード(ソルト)があれば交換の前に相手に伝える必要がある．

必要な処理を行ったパスワード ⇔ ソルト

## PEを選ぶために

- seedを選ぶ
- hunting-and-pecking技術を使う


## サイドチャネル攻撃を阻止するために

- hunting-and-pecking技術のループの回数がわかってしまうと，PEを見つけやすくなってしまう．
  - このことをサイドチャネル攻撃という
- サイドチャネル攻撃を避けるためには，kがループの終端になってはいけない

- kは，hunting-and-pecking 技術によるループがkより小さい回数で終わるであろう確率が大きくなるようにセットすべきである．

## 流れ

1. 8ビットカウンタを1にセットする
2. 暗号学的一方向性関数，ここでは暗号学的ハッシュ関数で，baseを生成する
   1. baseは固有値の合成(文字列の結合)
      1. AliceとBobの固有の値の大きいほうをとる
      2. AliceとBobの固有の値の小さいほうをとる
      3. passwordをとる
      4. 文字列に変換したcounterをとる
   2. counterはhunting-and-peckingループを繰り返すごとに変わるので，実質，毎回異なる値がハッシュ関数から出てくる
3. 鍵導出関数でseedを生成する
   1. 鍵の長さnは，pをバイナリ列にしたときの長さ + 64で求められる
   2. baseと"Dragonfly Hunting and Pecking"という文字列を連結してハッシュ関数に通してnビットだけ抽出する
   3. 抽出した値を(p-1)で割った余り + 1 をseedとする
   -> 0 < seed < p
   - 文字列"Dragonfly Hunting and Pecking"は，baseが一時的な値なので固定文字列でよい．

- この操作によって，seedがhunting-and-pecking技術に移される
- もしパスワードがランダムなワンタイムパスワードなら，















