RNA サンプル設定ファイルについて
==================================

項目は1種類です．

+-----------------+---------------------------------------------------+
| [fastq]         | FASTQファイルを入力として解析します               |
+-----------------+---------------------------------------------------+

RNA解析では[fastq]のみ指定します．FASTQファイルを指定しGenomonを実行するだけで融合遺伝子検出結果が出力されます.

[fastq]の記載方法
^^^^^^^^^^^^^^^^^

項目[fastq]には入力FASTQファイルのパスを記載します．

.. code-block:: bash

  # サンプル名,ペアリードの1つ目のFASTQ,ペアリードの2つ目のFASTQ  と記載します（カンマ区切りです）
  sample1_tumor,/home/genomon/sample1_T_read1.fastq,/home/genomon/sample1_T_read2.fastq
  sample1_normal,/home/genomon/sample1_N_read1.fastq,/home/genomon/sample1_N_read2.fastq

サンプル名は任意で指定してください．ディレクトリやファイル名で使用されます．
