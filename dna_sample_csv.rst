DNA サンプル設定ファイルについて
================================

項目は6種類あります．

+-----------------+---------------------------------------------------+
| [fastq]         | FASTQファイルを入力として解析します               |
+-----------------+---------------------------------------------------+
| [bam_tofastq]   | BAMを入力してFASTQファイルに戻してから解析します  |
+-----------------+---------------------------------------------------+
| [bam_import]    | 入力したBAMを再マッピングせずに解析を実行します   |
+-----------------+---------------------------------------------------+
| [mutation_call] | 変異コールが実行されます                          |
+-----------------+---------------------------------------------------+
| [sv_detection]  | SV検出が実行されます                              |
+-----------------+---------------------------------------------------+
| [controlpanel]  | コントロールパネルのペアを指定します    　        |
+-----------------+---------------------------------------------------+
| [qc]            | BAMのQuality Controlを出力します                  |
+-----------------+---------------------------------------------------+

| DNA解析では
| [fastq], [bam_tofastq], [bam_import] は入力ファイルの情報を記載します．
| [mutation_call], [sv_detection], [controlpanel], [qc] には解析するための情報を記載します．
|

[fastq]の記載方法
^^^^^^^^^^^^^^^^^

| 項目[fastq]には入力FASTQファイルのパスを記載します．

.. code-block:: bash

  # サンプル名,ペアリードの1つ目のFASTQ,ペアリードの2つ目のFASTQ と記載します（カンマ区切りです）
  sample1_tumor,/home/genomon/sample1_T_read1.fastq,/home/genomon/sample1_T_read2.fastq
  sample1_normal,/home/genomon/sample1_N_read1.fastq,/home/genomon/sample1_N_read2.fastq

| サンプル名は任意で指定してください．ディレクトリやファイル名で使用されます．
| 

[bam_import]の記載方法
^^^^^^^^^^^^

| 項目[bam_import]には入力BAMファイルのパスを記載します．

.. code-block:: bash

  # サンプル名,BAMファイルのパス　と記載してください（カンマ区切りです）
  sample3_tumor,/home/genomon/sample3_T.bam
  
| bam indexファイル(.bai)がセットで必要です．
| 

[mutation_call],[sv_detection]の記載方法
^^^^^^^^^^^^

| 項目[mutation_call][sv_detection]にはTumorサンプルとNormalサンプルのペア情報を記載します．
| Normalサンプルのコントロールパネルを作る場合は，そちらも記載します．

.. code-block:: bash

  # Tumorサンプル名,Normalサンプル名,コントロールパネル名 と記載してください．

  # パターン１：TumorとNormalのペアのサンプルで，コントロールパネルがある場合
  # Tumorサンプル名,Normalサンプル名,コントロールパネル名 と記載してください．コントロールパネル名は項目[control_panel]で定義した名前を使用します．
  sample1_tumor,sample1_normal,Panel1
  
  # パターン２：TumorとNormalのペアのサンプルで，コントロールパネルがない場合
  # Tumorサンプル名,Normalサンプル名,None と記載してください．
  sample1_tumor,sample1_normal,None
  
  # パターン３：Tumorだけで，Normalのペアのサンプルがない．コントロールパネルがある場合
  # Tumorサンプル名,None,コントロールパネル名 と記載してください．
  sample3_tumor,None,Panel1

  # パターン４：Tumorだけで，Normalのペアのサンプルがない．コントロールパネルがない場合
  # Tumorサンプル名,None,None と記載してください．
  sample4_tumor,None,None

| この項目に定義するサンプル名は[fastq], [bam_tofastq], [bam_import]のいずれかで定義されていなくてはなりません．
| 

[controlpanel]の記載方法
^^^^^^^^^^^^

項目[controlpanel]には，Normalのサンプル名を複数指定して，コントロールパネル名を付けてNormalサンプルの集まりとして指定します．

.. code-block:: bash

  # コントロールパネル名,Normalサンプル1,Normalサンプル2,Normalサンプル3,・・・,NormalサンプルN　と記載してください．
  panel1,sample1_normal,sample2_normal,sample3_normal,sample4_normal
  panel2,sample5_normal,sample6_normal,sample7_normal,sample8_normal
  
| 指定するサンプル数Nに最大値はないです．
| サンプル名は[fastq], [bam_tofastq], [bam_import]のいずれかで定義されていなくてはなりません．
| コントロールパネル名は任意で指定してください．
| 

[qc]の記載方法
^^^^^^^^^^^^

項目[qc]にはサンプル名を記載します．

.. code-block:: bash

  # ペアで記載する必要はありません．QC出力するサンプル名を記載してください
  sample1_normal
  sample2_normal
  sample3_normal
  sample1_tumor
  sample2_tumor
  sample3_tumor


| この項目に定義するサンプル名は[fastq], [bam_tofastq], [bam_import]のいずれかで定義されていなくてはなりません．
| 

