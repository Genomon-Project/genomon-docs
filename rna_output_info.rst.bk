RNA 解析で出力されるファイルについて
====================================

paplotディレクトリに出力されている index.html が Genomon パイプラインの最終成果物であり，Genomonが正常終了したかどうかの目安になります．

出力ディレクトリ階層
---------------------

.. code-block:: bash
  :caption: RNA解析結果
  
  {出力ルートディレクトリ}
    └ fastq/                            ：Fastqファイル
    └ star/                             ：1) BAMファイル
        └{サンプル名}
            └{サンプル名}.Aligned.sortedByCoord.out.bam
            └{サンプル名}.Aligned.sortedByCoord.out.bam.bai

    └ fusion/                           ：2) 融合遺伝子検出結果
        └{サンプル名}/
            └{サンプル名}.Chimeric.count
        └control_panel/

    └expression/                        ：3) 発現量解析結果
        └{サンプル名}/
            └{サンプル名}.sym2fkpm.txt

    └intron_retention/                  ：Intron Retention検出結果
    └post_analysis/                     ：4) 融合遺伝子検出結果とFastqのQC結果をマージした結果
    └paplot/                            ：5) 解析結果をビジュアライゼーションしたレポート
        └{サンプル設定ファイル名}/
            └'index.html'
    └config/                            ：6) Other
    └log/
    └script/


1. BAMファイル
----------------

:{サンプル名}.Aligned.sortedByCoord.out.bam: BAMファイル．
:{サンプル名}.Aligned.sortedByCoord.out.bam.bai: BAM indexファイル．

2. Fusion検出結果
-----------------------

:{サンプル名}_fusion_fusion.result.txt: 融合遺伝子検出結果ファイル．

3. 発現量解析結果
-----------------------

:{サンプル名}.sym2fkpm.txt: 発現量解析結果

4. Post_analysis結果
-----------------------

| サンプル毎に出力される変異コールやSV検出結果をマージします．

5. paplot結果
-----------------------

| Fusion検出結果とfastqのQuality Control結果をビジュアライゼーションした結果です．
| paplotディレクトリをダウンロードし，index.htmlをダブルクリックしてください．結果を確認できます．
|
|
| paplotの使い方についてはこちら
| http://paplot-jp.readthedocs.org/ja/latest/
| 

6. config, log, script
-----------------------

| 実行時のパラメータやツールの設定情報，log，使用したScriptが保存されます．

