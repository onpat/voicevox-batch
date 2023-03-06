# voicevox-batch
VOICEVOXの音声合成をバッチ処理するためのPythonスクリプトです。

## 想定使用状況
作業PC上でVOICEVOXが使えないなどで、離れた場所にあるコンピューターで音声合成を行いたい場合。

## 必要条件
実行側でpython3、音声合成側でVOICEVOX ENGINEが必要です。

runを実行し、変数`host`をVOICEVOX ENGINEが起動しているPCのアドレスに編集してから使用してください。

## バッチ処理スクリプトの記法
このスクリプトはコマンドライン引数にバッチ処理スクリプトのパスを与える必要があります。
その構造はexample.txtを参考にしてほしいのですが、
```
3 ← ボイス指定
テキストテキスト
テキスト
<> ← 区切り指定
1
テキスト
テキスト
<> ← 最後に区切り指定
```
というような感じになってます。

ボイスの番号は、`vv-batch.py voices`で確認できます。

## 出力
wav形式で、最初のものから連番で出力されます。
