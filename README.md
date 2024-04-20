# typst_font_list
typst で用いることができるフォントの一覧を表示する

## 使い方
typst をインストールしたのち，コマンドラインから以下を実行してフォント一覧を得る．
```bash
typst fonts > fonts.txt
```
python で適当にフォーマットし，jsonファイルにする．
```bash
python format.py
```
typ ファイルをコンパイルする．
```bash
typst compile fonts.typ fonts{n}.png
```

## 参考文献
* [typst フォント まとめ](https://qiita.com/1taroh/items/aee1043d366a4a7c3219)
