DNA 解析で出力されるファイルについて
====================================

出力ディレクトリ階層
---------------------

 .. image:: image/dna_tree.png
  :scale: 100%

マッピング結果（BAMファイル)
-----------------------
| {出力ルートディレクトリ}/bam/{サンプル名}ディレクトリ内に出力されます．

* **{サンプル名}.markdup.bam** -- BAMファイル．
* **{サンプル名}.markdup.bam.bai** -- BAM indexファイル．
* **{サンプル名}.markdup.metrics** -- markduplicateしたリードのmetrics情報．
* **{サンプル名}.markdup.bam.md5** -- BAMのmd5値．

変異コール結果
-----------------------
| {出力ルートディレクトリ}/mutation/{サンプル名}ディレクトリ内に出力されます．

* **{サンプル名}.genomon_mutation.result.filt.txt** -- 変異コール結果．P値などで適切なフィルタ済み．
* **{サンプル名}.genomon_mutation.result.txt** -- 変異コール結果．フィルタなしのrawデータ．advanced user向け．

SV検出結果
-----------------------
| {出力ルートディレクトリ}/sv/{サンプル名}ディレクトリ内に出力されます．

* **{サンプル名}.genomonSV.result.filt.txt** -- SV検出結果．P値などで適切なフィルタ済み．
* **{サンプル名}.genomonSV.result.txt** -- SV検出結果．フィルタなしのrawデータ．advanced user向け．
* **他 bedpe.gzファイルなど** -- デバッグ用のファイル．advanced user向け．

BAMのQuality Control結果
------------------------
| {出力ルートディレクトリ}/qc/{サンプル名}ディレクトリ内に出力されます．

* **{サンプル名}.genomonQC.result.txt** -- QC結果．
* **{サンプル名}.bamstats** -- BAMのアライメント率の結果など．{サンプル名}.genomonQC.result.txtに含まれている．
* **{サンプル名}.coverage** -- BAMのカバレッジ結果など．{サンプル名}.genomonQC.result.txtに含まれている．

Post_analysis結果
-----------------------
| サンプル毎に出力される変異コールやSV検出結果をマージしたファイルを取得できます．
| :doc:`dna_sample_csv` の[mutation_call][sv_detection]の記載方法にはパターン１～パターン４がありますが、その単位でマージしたファイルがpost_analysisの結果に出力されます。
|
| 変異コール結果
* **merge_mutation_pair_controlpanel.txt** -- サンプルがペア、コントロールパネルありの結果をマージしたファイル．[パターン1]
* **merge_mutation_pair.txt** -- サンプルがペア、コントロールパネルなしの結果をマージしたファイル．[パターン2]
* **merge_mutation_unpair_controlpanel.txt** -- サンプルがペアでない、コントロールパネルありの結果をマージしたファイル．[パターン3]
* **merge_mutation_unpair.txt** -- サンプルがペアでない、コントロールパネルなしの結果をマージしたファイル．[パターン4]
* **merge_mutation.txt** -- 上記４つのファイルをマージしたファイル．
| 変異コール結果 フィルタ済み
* **merge_mutation_filt_pair_controlpanel.txt** -- サンプルがペア、コントロールパネルの結果をマージしたファイル．[パターン1]
* **merge_mutation_filt_pair.txt** -- サンプルがペア、コントロールパネルなしの結果をマージしたファイル．[パターン2]
* **merge_mutation_filt_unpair_controlpanel.txt** -- サンプルがペアでない、コントロールパネルありの結果をマージしたファイル．[パターン3]
* **merge_mutation_filt_unpair.txt** -- サンプルがペアでない、コントロールパネルなしの結果をマージしたファイル．[パターン4]
* **merge_mutation_filt.txt** -- 上記４つのファイルをマージしたファイル．
| SV検出結果
* **merge_sv_pair_controlpanel.txt** -- サンプルがペア、コントロールパネルありの結果をマージしたファイル．[パターン1]
* **merge_sv_pair.txt** -- サンプルがペア、コントロールパネルなしの結果をマージしたファイル．[パターン2]
* **merge_sv_unpair_controlpanel.txt** -- サンプルがペアでない、コントロールパネルありの結果をマージしたファイル．[パターン3]
* **merge_sv_unpair.txt** -- サンプルがペアでない、コントロールパネルなしの結果をマージしたファイル．[パターン4]
* **merge_sv.txt** -- 上記４つのファイルをマージしたファイル．
| SV検出結果 フィルタ済み
* **merge_sv_filt_pair_controlpanel.txt** -- サンプルがペア、コントロールパネルの結果をマージしたファイル．[パターン1]
* **merge_sv_filt_pair.txt** -- サンプルがペア、コントロールパネルなしの結果をマージしたファイル．[パターン2]
* **merge_sv_filt_unpair_controlpanel.txt** -- サンプルがペアでない、コントロールパネルありの結果をマージしたファイル．[パターン3]
* **merge_sv_filt_unpair.txt** -- サンプルがペアでない、コントロールパネルなしの結果をマージしたファイル．[パターン4]
* **merge_sv_filt.txt** -- 上記４つのファイルをマージしたファイル．
| BAMのQuality Control結果
* **merge_qc.txt** -- 結果をマージしたファイル．

| このThe Integrative Genomics Viewer (IGV) で読み込むと，変異CAll結果とSVのポジションが画像として保存されます．

* **mutation/capture_script/capture.bat** -- 変異コール結果の周辺ポジションをIGVでsnapshotする.
* **sv/capture_script/capture.bat** -- SV検出結果の周辺ポジションをIGVでnapshotする.

IGVのBAT取り込み方法についてはこちら
https://www.broadinstitute.org/software/igv/batch

paplot結果
-----------------------

| SV検出結果とQC結果をビジュアライゼーションした結果です．
| paplotディレクトリをダウンロードし，index.htmlをダブルクリックしてください．結果を確認できます．

paplotの使い方についてはこちら
http://paplot-jp.readthedocs.org/ja/latest/

config log script
-----------------------

| 実行時のパラメータやツールの設定情報，log，使用したScriptが保存されます．


