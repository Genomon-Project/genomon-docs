========================================
Quick Start DNA解析
========================================

このページの目次
---------------------
+ Genomon2のインストール
+ sampleシートに解析対象サンプルを記載しましょう
+ コマンドの実行
+ 結果ファイルを見てみましょう

Genomon2のインストール
---------------------
| HGCには、Genomon2で使用するツール(BWA,Samtools等)が既にインストールされています(ANNOVARを除く)。
| そのためご自身のユーザディレクトリにGenomon2をインストールするだけで、解析をはじめることができます。
| HGCスパコンユーザの方はこちら
| →インストール方法は :doc:`install` に記載しました．
|
| HGC以外のコンピュータにGenomonをインストールしたい方はこちら
| →記載中

sample.csvを記載しましょう
--------------------------

| Genomonでは解析対象のサンプルをsample.csvに記述します。
| sample.csvに複数のサンプルを記述することにより、同時に解析できます．
| .csvファイルの形式は,(カンマ区切り) 、ファイル名はこのように例)sample_AML_project.csv作成しても大丈夫です．

.. code-block:: bash
  
  # 項目[fastq]にはinput fastqファイルを記載します．
  # 形式はサンプル名,read1.fastq,read2.fastqです。順不同です．
  [fastq]
  sample1_tumor,/home/genomon/sample1_T_read1.fastq,/home/genomon/sample1_T_read2.fastq
  sample1_normal,/home/genomon/sample1_N_read1.fastq,/home/genomon/sample1_N_read2.fastq

  # 項目[compare]にはtumorとmatched normalで比較するペアを記述します．
  # 形式はtumorサンプル名,normalサンプル名,non-matched_normal_panelです。順不同です．
  # non-matched_normal_panelはなくてもOKです。
  [compare]
  sample1_tumor,sample1_normal,None

| sample_confの書き方詳細は :doc:`sample_csv` に記載があります．
| いくつかの解析パターンがありますのでご覧ください．
| 

コマンドの実行
--------------

.. code-block:: bash
  
  # usage
  genomon_pipeline dna [sample.csv] [output_root_directory] genomon.cfg dna_task_param.cfg
  
:dna/rna: DNA解析を実行するときはdnaを指定します
:sample.csv: 解析対象のサンプルを記述したファイルになります
:output_root_directory: 結果出力のルートディレクトリを指定します

.. code-block:: bash

  # 実行例
  genomon_pipeline dna DNA_sample.csv ~/tmp/ALL_project genomon.cfg dna_task_param.cfg

| commandの実行方法詳細は :doc:`command` に記載があります．
| 

結果ファイル
------------------
:bam: output_root_directory/bam/sample/sample_markdup.bam
:変異Call結果: output_root_directory/mutation/sample名/sample名_genomon_mutations.result.txt
:SV検出結果: output_root_directory/sv/sample名/sample名.genomonSV.result.txt

| 結果ファイルの各項目の説明は :doc:`dna_results` に記載があります．

