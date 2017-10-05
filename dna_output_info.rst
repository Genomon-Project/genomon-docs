DNA 解析で出力されるファイルについて
====================================

paplotディレクトリに出力されている index.html が Genomon パイプラインの最終成果物であり，Genomonが正常終了したかどうかの目安になります．

出力ディレクトリ階層
---------------------

.. code-block:: bash
  :caption: DNA解析結果
  
  {出力ルートディレクトリ}
    └ fastq/                            ：Fastqファイル
    └ bam/                              ：1) BAMファイル
        └{サンプル名}/
            └{サンプル名}.markdup.bam
            └{サンプル名}.markedup.bam.bai

    └ mutation/                         ：2) 変異コール結果
        └{サンプル名}/
            └{サンプル名}.genomon_mutation.result.txt
            └{サンプル名}.genomon_mutation.result.filt.txt
        └control_panel/
        └hotspot/
        
    └sv/                                ：3) SV検出結果
        └{サンプル名}/
            └{サンプル名}.genomonSV.result.txt
            └{サンプル名}. genomonSV.result.filt.txt
        └control_panel/
        └non_matched_control_panel/
        
    └qc/                                ：4) QC結果 (BAMのQuality Control結果)
        └{サンプル名}/
            └{サンプル名}.genomonQC.result.txt
    └pmsignature/                       ：pmsignatureによるsignature出力結果
    └post_analysis/                     ：5) 変異コール，SV検出結果とBAMのQC結果をマージした結果
    └paplot/                            ：6) 解析結果をビジュアライゼーションしたレポート
        └{サンプル設定ファイル名}/
            └'index.html'
    └config/                            ：7) Other
    └log/
    └script/

1. BAMファイル
----------------

:{サンプル名}.markdup.bam: BAMファイル．
:{サンプル名}.markdup.bam.bai: BAM indexファイル．
:{サンプル名}.markdup.metrics: markduplicateしたリードのmetrics情報．

2. 変異コール結果
-----------------------

:{サンプル名}.genomon_mutation.result.filt.txt: 変異コール結果．P値などで適切なフィルタ済み．
:{サンプル名}.genomon_mutation.result.txt: 変異コール結果．フィルタなしのrawデータ．advanced user向け．

3. SV検出結果
-----------------------

:{サンプル名}.genomonSV.result.filt.txt: SV検出結果．P値などで適切なフィルタ済み．
:{サンプル名}.genomonSV.result.txt: SV検出結果．フィルタなしのrawデータ．advanced user向け．

4. QC 結果
------------------------

:{サンプル名}.genomonQC.result.txt: QC結果．

5. Post_analysis結果
-----------------------

| サンプル毎に出力される変異コールやSV検出結果をマージします．
| :doc:`dna_sample_csv` の[mutation_call][sv_detection]の記載方法にはパターン１～パターン４がありますが，その単位でマージしたファイルがpost_analysisの結果に出力されます．

:{}_pair_controlpanel.txt: サンプルがペア，コントロールパネルありの結果をマージしたファイル．[パターン1]
:{}_pair.txt: サンプルがペア，コントロールパネルなしの結果をマージしたファイル．[パターン2]
:{}_unpair_controlpanel.txt: サンプルがペアでない，コントロールパネルありの結果をマージしたファイル．[パターン3]
:{}_unpair.txt: サンプルがペアでない，コントロールパネルなしの結果をマージしたファイル．[パターン4]
:{}.txt: 上記４つのファイルをマージしたファイル．

:capture.bat: The Integrative Genomics Viewer (IGV) で読み込み実行すると，変異CAll結果とSVのポジションが画像として保存されます．mutationもしくはsvディレクトリの下に出力されています

| IGVのBAT取り込み方法についてはこちら
| https://www.broadinstitute.org/software/igv/batch

6. paplot結果
-----------------------

| 変異コール，SV検出結果とQC結果をビジュアライゼーションした結果です．
| paplotディレクトリをダウンロードし，index.htmlをダブルクリックしてください．結果を確認できます．
|
| paplotの使い方についてはこちら
| http://paplot-jp.readthedocs.org/ja/latest/

7. config, log, script
-----------------------

| 実行時のパラメータやツールの設定情報，log，使用したScriptが保存されます．

