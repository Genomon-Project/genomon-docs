RNA 解析で出力されるファイルについて
====================================

出力ディレクトリ階層
---------------------

 .. image:: image/rna_tree.png
  :scale: 110%


マッピング結果（BAMファイル)
------------------------------

| {出力ルートディレクトリ}/star/{サンプル名}ディレクトリ内に出力されます．
|

* **{サンプル名}.Aligned.sortedByCoord.out.bam** -- BAMファイル．
* **{サンプル名}.Aligned.sortedByCoord.out.bam.bai** -- BAM indexファイル．


Fusion検出結果
-----------------------

| {出力ルートディレクトリ}/fusion/{サンプル名}ディレクトリ内に出力されます．
|

* **{サンプル名}_fusion_fusion.result.txt** -- 融合遺伝子検出結果ファイル．
* **{サンプル名}_star.fusion.result.txt** -- 中間ファイル．デバッグ用．

expression検出結果
-----------------------

| {出力ルートディレクトリ}/expression/{サンプル名}ディレクトリ内に出力されます．
|

* **{サンプル名}.sym2fkpm.txt** -- 発現量解析結果
* **{サンプル名}.mapped_base_count.txt** -- 中間ファイル．デバッグ用．
* **{サンプル名}.ref2base.txt** -- 中間ファイル．デバッグ用．
* **{サンプル名}.sym2base.txt** -- 中間ファイル．デバッグ用．

Post_analysis結果
-----------------------

| サンプル毎に出力される変異コールやSV検出結果をマージしたファイルを取得できます．
|
| Fusion検出結果
|

* merge_fusionfusion.txt

| fastqのQuality Control結果
|

* merge_starqc.txt

paplot結果
-----------------------

| Fusion検出結果とfastqのQuality Control結果をビジュアライゼーションした結果です．
| paplotディレクトリをダウンロードし，index.htmlをダブルクリックしてください．結果を確認できます．
|
|
| paplotの使い方についてはこちら
| http://paplot-jp.readthedocs.org/ja/latest/
| 

config log script
-----------------------

| 実行時のパラメータやツールの設定情報，log，使用したScriptが保存されます．

