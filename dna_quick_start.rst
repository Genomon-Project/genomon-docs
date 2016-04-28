Quick Start DNA解析
===================

HGCスパコンでのDNA解析に必要な手順をまとめました．

| 1. サンプル設定ファイルをつくる
| 2．パイプライン設定ファイルをつくる
| 3．Genomonを実行する
| 4．結果ファイルを確認する

1. サンプル設定ファイルをつくる
-------------------------------

サンプル設定ファイルには解析対象のFASTQやBAMファイルや，どの解析（変異コール，SV検出，BAMのQuality Control)を実行するのかを指定します．

サンプル設定ファイルの記載方法は  :doc:`dna_sample_csv` を参照ください．


2. パイプライン設定ファイルをつくる
-----------------------------------

最適化されたパラメータが記載されたパイプライン設定ファイルをHGCスパコンにあります。こちらのファイルを

/home/w3varann/genomon_pipeline-2.2.0/genomon_conf/dna_exome_genomon.cfg
/home/w3varann/genomon_pipeline-2.2.0/genomon_conf/dna_wgs_genomon.cfg

3．Genomonを実行する
--------------------

作成した設定ファイルを指定して、Genomonを実行しましょう．

.. code-block:: bash
  
  # qloginする
  $qlogin
  # Genomonを実行する
  bash /home/w3varann/genomon_pipeline-2.2.0/genomon_script/genomon_pipeline_HGC.sh {解析タイプ dna を指定する} {サンプル設定ファイル} {出力ルートディレクトリ} {パイプライン設定ファイル}

4．結果ファイルを確認する
-------------------------

結果ファイルは実行時に指定した 出力ルートディレクトリに以下に出力されます．

.. code-block:: bash

  # Mutation Call結果
  {出力ルートディレクトリ}/mutation/sample名/sample名_genomon_mutations.result.txt
  # SV検出結果
  {出力ルートディレクトリ}/sv/sample名/sample名.genomonSV.result.txt
  # summary
  {出力ルートディレクトリ}/sv/sample名/sample名.xls

結果ファイルの各項目の説明など詳細は :doc:`dna_results` を参照ください．

