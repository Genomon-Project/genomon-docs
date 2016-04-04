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
| post_analysisディレクトリ内に出力されます．
| サンプル毎に出力される変異CallやSV検出結果をマージしたファイルを取得できます．
| 同じ名前のファイルがある場合、ファイルは上書きされます．

* **merge_genomon_mutations.result.filt.txt** -- 変異Call結果をマージしたファイル．
* **merge_genomon_mutations.result.txt** -- 変異Call結果をマージしたファイル(フィルタなし）．
* **merge_genomon_sv.result.filt.txt** -- SV検出結果をマージしたファイル．
* **merge_genomon_sv.result.txt** -- SV検出結果をマージしたファイル(フィルタなし）．
* **merge_genomon_bam_summary.txt** -- BAM Summary結果をマージしたファイル．



logディレクトリ
---------------
  
| qsubのログファイルが出力されます.


mutationディレクトリ
--------------------

:サンプル名.genomon_mutations.result.txt: 変異Callの結果が出力されます.

scriptディレクトリ
------------------

| qsubされたshell scriptです.
| どのような処理が実行されたかチェックすることができます．
|

summaryディレクトリ
-------------------

:サンプル名.xls: bam summaryがEXCELファイルで出力されます.
:サンプル名.tsv: サンプル名.xlsをテキスト形式で出力したものです.内容は同じです.


SVディレクトリ
--------------

:サンプル名.genomon_SV.result.txt: SV検出の結果が出力されます.
