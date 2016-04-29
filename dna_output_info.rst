DNA解析で出力されるファイルについて
===================================

出力ディレクトリ階層
---------------------

 .. image:: image/dna_tree.png
  :scale: 100%

マッピング結果（Bamファイル)
-----------------------
| {出力ルートディレクトリ}/bam/{各サンプル}ディレクトリ内に出力されます．

* **{各サンプル}.markdup.bam** -- Bamファイル．
* **{各サンプル}.markdup.bam.bai** -- Bam indexファイル．
* **{各サンプル}.markdup.metrics** -- markduplicateしたリードのmetrics情報．
* **{各サンプル}.markdup.bam.md5** -- Bamのmd5値．

変異コール結果
-----------------------
| {出力ルートディレクトリ}/mutation/{各サンプル}ディレクトリ内に出力されます．

* **{各サンプル}.genomon_mutation.result.filt.txt** -- 変異コール結果．P値などで適切なフィルタ済み．
* **{各サンプル}.genomon_mutation.result.txt** -- 変異コール結果．フィルタなしのrawデータ．advanced user向け．

SV検出結果
-----------------------
| {出力ルートディレクトリ}/sv/{各サンプル}ディレクトリ内に出力されます．

* **{各サンプル}.genomonSV.result.filt.txt** -- SV検出結果．P値などで適切なフィルタ済み．
* **{各サンプル}.genomonSV.result.txt** -- SV検出結果．フィルタなしのrawデータ．advanced user向け．
* **他 bedpe.gzファイルなど** -- デバッグ用のファイル．advanced user向け．

BamのQuality Control結果
------------------------
| {出力ルートディレクトリ}/qc/{各サンプル}ディレクトリ内に出力されます．

* **{各サンプル}.genomonQC.result.txt** -- QC結果．
* **{各サンプル}.bamstats** -- Bamのアライメント率の結果など．{各サンプル}.genomonQC.result.txtに含まれている．
* **{各サンプル}.coverage** -- Bamのカバレッジ結果など．{各サンプル}.genomonQC.result.txtに含まれている．

Post_analysis結果
-----------------------
| サンプル毎に出力される変異コールやSV検出結果をマージしたファイルを取得できます．
| 同じ名前のファイルがある場合，ファイルは上書きされます．

* **merge_genomon_mutations.result.filt.txt** -- 変異コール結果をマージしたファイル．
* **merge_genomon_mutations.result.txt** -- 変異コール結果をマージしたファイル(フィルタなし)．
* **merge_genomon_sv.result.filt.txt** -- SV検出結果をマージしたファイル．
* **merge_genomon_sv.result.txt** -- SV検出結果をマージしたファイル(フィルタなし)．
* **merge_genomon_qc.result.txt** -- BamのQuality Control結果をマージしたファイル．

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


