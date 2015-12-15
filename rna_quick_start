========================================
Quick Start RNA解析
========================================

Genomonのインストール
-------
| インストール方法は :doc:`install` に記載しました．
| うまくいかないことがあれば、xxxxxにご連絡ください．
| DNA解析とRNA解析で同じツールです．

sample.csvを記載しましょう
--------------------
| Genomonでは解析対象のサンプルをsample.csvに記述します。
| sample.csvに複数のサンプルを記述することにより、同時に解析できます．
| .csvファイルの形式は,(カンマ区切り) 、ファイル名はこのように例)sample_AML_project.csv作成しても大丈夫です．

.. code-block:: bash
  
  # 項目[fastq]にはinput fastqファイルを記載します．
  # 形式はサンプル名,read1.fastq,read2.fastqです。順不同です．
  [fastq]
  sample1,/home/genomon/sample1_read1.fastq,/home/genomon/sample1_read2.fastq

| sample_confの書き方詳細は :doc:`sample_conf` に記載があります．しかし項目[fastq]だけしか使わないので、読まなくても良いかもしれません．

コマンドの実行
-------

.. code-block:: bash
  
  # usage  
  genomon_pipeline dna [sample.csv] [output_root_directory] genomon.cfg rna_task_param.cfg
  
:dna/rna: RNA解析を実行するときはrnaを指定します
:sample.csv: 解析対象のサンプルを記述したファイルになります
:output_root_directory: 結果出力のルートディレクトリを指定します

.. code-block:: bash

    # 実行例
  genomon_pipeline dna DNA_sample.csv ~/tmp/RNA_project genomon.cfg rna_task_param.cfg

| commandの実行方法詳細は :doc:`command` に記載があります．


結果ファイル
------------------
:fusion検出結果: output_root_directory/fusion/sample名/sample名_fusion_fusion.result.txt

結果ファイルの各項目の説明は :doc:`rna_results` に記載があります．

