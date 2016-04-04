========================================
DNA解析で出力されるファイルについて
========================================

出力ディレクトリ階層
---------------------

 .. image:: image/dna_tree.png
  :scale: 100%

マッピング結果（BAM)
-----------------------
| bam/$sample(各サンプル)ディレクトリ内に出力されます．

* **${sample}.markdup.bam** -- BAMファイル．
* **${sample}.markdup.bam.bai** -- BAM indexファイル．
* **${sample}.markdup.metrics** -- markduplicateしたリードのmetrics情報．
* **${sample}.markdup.bam.md5** -- BAMのmd5値．

変異Call結果
-----------------------
| mutation/$sample(各サンプル)ディレクトリ内に出力されます．

* **${sample}_genomon_mutations.result.filt.txt** -- 変異Call結果．P値などで適切なフィルタ済み．
* **${sample}_genomon_mutations.result.txt** -- 変異Call結果．フィルタなしのrawデータ．advanced user向け．

SV検出結果
-----------------------
| sv/$sample(各サンプル)ディレクトリ内に出力されます．

* **${sample}.genomonSV.result.filt.txt** -- SV検出結果．P値などで適切なフィルタ済み．
* **${sample}.genomonSV.result.txt** -- SV検出結果．フィルタなしのrawデータ．advanced user向け．
* **他 bedpe.gzファイルなど** -- デバッグ用のファイル．advanced user向け．

BAM Summary結果
-----------------------
| sv/$sample(各サンプル)ディレクトリ内に出力されます．

* **${sample}.tsv** -- Summary結果．
* **${sample}.xls** -- Summary結果．${sample}.tsvをExcelにしたもの．
* **${sample}.bamstats** -- BAMのアライメント率の結果など．${$summary}.tsvに含まれている．
* **${sample}.coverage** -- BAMのカバレッジ結果など．${$summary}.tsvに含まれている．

Post_analysis結果
-----------------------
| サンプル毎に出力される変異CallやSV検出結果をマージしたファイルを取得できます．
| 同じ名前のファイルがある場合、ファイルは上書きされます．

* **merge_genomon_mutations.result.filt.txt** -- 変異Call結果をマージしたファイル．
* **merge_genomon_mutations.result.txt** -- 変異Call結果をマージしたファイル(フィルタなし）．
* **merge_genomon_sv.result.filt.txt** -- SV検出結果をマージしたファイル．
* **merge_genomon_sv.result.txt** -- SV検出結果をマージしたファイル(フィルタなし）．
* **merge_genomon_bam_summary.txt** -- BAM Summary結果をマージしたファイル．

| このThe Integrative Genomics Viewer (IGV) で読み込むと、変異CAll結果とSVのポジションが画像として保存されます．

* **mutation/capture_script/capture.bat** -- 変異Call結果の周辺ポジションをIGVでsnapshotする.
* **sv/capture_script/capture.bat** -- SV検出結果の周辺ポジションをIGVでnapshotする.

IGVのBAT取り込み方法についてはこちら
https://www.broadinstitute.org/software/igv/batch

paplot結果
-----------------------

| SV検出結果とSummary結果をビジュアライゼーションした結果です．
| paplotディレクトリをダウンロードし、index.htmlをダブルクリックしてください．結果を確認できます．

config log script
-----------------------

| 実行時のパラメータやツールの設定情報、log、使用したScriptが保存されます．


