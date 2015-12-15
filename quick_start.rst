========================================
Quick Start DNA解析
========================================

Genomonのインストール
-------
| インストール方法は :doc:`install` に記載しました．
難しくないと思いますので、がんばってください．

コマンドの実行
-------

.. code-block:: bash
  
  # usage  
  genomon_pipeline dna [DNA_sample.csv] [project_root_directory] genomon.cfg dna_task_param.cfg
  
:dna/rna: DNA解析を実行するときはdnaを指定します
:sample_conf.[csv/tsv]: 解析対象のサンプルを記述したファイルになります
:project_root_directory: 結果出力のルートディレクトリを指定します

| commandの実行方法詳細は :doc:`command` に書いてあります．

sample_conf.csvを記載しましょう
--------------------

| Genomonでは解析対象のサンプルをsample_conf.csvに入力します。
| sample_conf.csvに複数のサンプルを記述することにより、同時に解析できます．
| .csvの拡張子の場合は,(カンマ区切り) ファイル名は変更しても大丈夫です．例)sample_conf_AML_project.csv

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

| sample_confの例 :any:`csv/quick_start_sample`
| sample_confの書き方詳細は :doc:`sample_conf` に書いてあります．

結果ファイル
------------------
:bam: project_root_directory/bam/sample/sample_markdup.bam
:変異Call結果: project_root_directory/mutation/sample名/sample名_genomon_mutations.result.txt
:SV検出結果: project_root_directory/sv/sample名/sample名.genomonSV.result.txt

結果ファイルの各項目の説明は :doc:`dna_results` に書いてあります．

.. code-block:: bash

    # 実行例
  genomon_pipeline dna DNA_sample.csv ~/tmp/ALL_project genomon.cfg dna_task_param.cfg
