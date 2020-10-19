# MyReserch2

院生の現在は, 新しい研究テーマ「機械学習を用いたドライバの運転行動の数理モデルの探索」に挑戦しています.

# 研究の概要
人間の運転しやすい自動車,人間の違和感のない自動運転車の開発にとって,ドライバの運転行動理解は重要であることから,ドライバの運転行動の理解のためにドライバモデル等の数理モデルを用いた理解が試みられています. <br>
しかし,どのような情報がドライバの操舵制御にどのような影響を与えるのか, その正確なメカニズムは明らかになっていません. その理由として, ドライバモデルにおいて, 操舵制御に影響を与えうる入力情報が, 主観的に選定されており，それらの表現が自明なものとして扱われていることが挙げられます. <br>
そのため, 機械学習の手法 「Weight Agnostic Neural Networks」[GitHub Pages](https://github.com/google/brain-tokyo-workshop/) を用いて, 多数の入力情報群から最適な入力を選択し，モデルの探索を行うことで解決に貢献しようと考えています．

# プログラムの説明
現在は,Weight Agnostic Neural Networksの理解と,実際に研究に用いることができるかを確認する簡単なシミュレーションを行っています.<br>
* one_point_model_.py:<br>
シミュレーションを行う際の,データセットを作成するプログラム
* Visualization_Partticipant.py:<br>
本実験の被験者のデータを可視化するためのプログラム<br>
* Weight Agnostic Neural Networks[GitHub Pages](https://github.com/google/brain-tokyo-workshop/) <br>

# Author
* 浮田 凌佑
* 立命館大院 情報理工学研究科 情報理工学専攻
* is0343sf@ed.ritsumei.ac.jp
