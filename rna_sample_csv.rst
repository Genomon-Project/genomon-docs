========================================
RNA Sample_conf.csvの書き方
========================================

項目は1種類です。

+-----------------+---------------------------------------------------+
| [fastq]         | FASTQファイルを入力として解析します               |
+-----------------+---------------------------------------------------+

| RNA解析では
| [fastq]のみ指定できます．FASTQファイルを指定しgenomonを実行するだけでfusionの結果まで出力されます.
|

[fastq]の記載方法
^^^^^^^^^^^^

| 項目[fastq]にはinput fastqファイルのパスを記載します．

.. code-block:: bash

  # サンプル名,read1.fastq,read2.fastq  と記載します（カンマ区切りです）
  sample1_tumor,/home/genomon/sample1_T_read1.fastq,/home/genomon/sample1_T_read2.fastq
  sample1_normal,/home/genomon/sample1_N_read1.fastq,/home/genomon/sample1_N_read2.fastq

| サンプル名は任意で指定してください。ディレクトリやファイル名で使用されます。
| 

