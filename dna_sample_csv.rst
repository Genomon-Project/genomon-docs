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
| [controlpanel]  | コントロールパネルを定義します                    |
+-----------------+---------------------------------------------------+
| [qc]            | BAMのQuality Controlを出力します                  |
+-----------------+---------------------------------------------------+

| DNA解析では
| [fastq], [bam_tofastq], [bam_import] は入力ファイルの情報を記載します．
| [mutation_call], [sv_detection], [controlpanel], [qc] には解析するための情報を記載します．
| 
| 各項目と処理の流れについては :doc:`dna_workflow` を参照してください．

 :download:`サンプルはこちら <csv/dna_sample.csv>`

[fastq]の記載方法
^^^^^^^^^^^^^^^^^

| 項目[fastq]には入力FASTQファイルのパスを記載します．

.. code-block:: bash

  # {サンプル名},{ペアリードの1つ目のFASTQ},{ペアリードの2つ目のFASTQ} の順にカンマ (,) 区切りで記載してください
  sample1_tumor,/home/genomon/sample1_T_read1.fastq,/home/genomon/sample1_T_read2.fastq
  sample1_normal,/home/genomon/sample1_N_read1.fastq,/home/genomon/sample1_N_read2.fastq
  
[bam_tofastq],[bam_import]の記載方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| 項目[bam_import]には入力BAMファイルのパスを記載します．

.. code-block:: bash

  # {サンプル名},{BAMファイルのパス} の順にカンマ (,) 区切りで記載してください
  sample3_tumor,/home/genomon/sample3_T.bam
  
| BAM indexファイル(.bai)がセットで必要です．
| .bamファイルと同じディレクトリに.baiファイルがあることを確認してください．

.. note::
  
  **サンプル名について**
  
  | [fastq],[bam_tofastq],[bam_import]では，先頭にサンプルの名前を付けます．
  | サンプル名は1行に一つ指定し，他のサンプルと重複することはできません．
  | このサンプル名はこの後指定するすべての項目（[mutation_call],[sv_detection] 等）で使用します．
  | サンプル名は任意で指定できますが，ディレクトリや解析結果の出力ファイル名にも使用しますので，ある程度サンプルの特徴をとらえた名前をお勧めします．
  |
  | 例: 
  |    sample1_tumor
  |    sample1_normal
  |    sample2_tumor
  |    sample2_normal

[mutation_call],[sv_detection]の記載方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| 項目[mutation_call][sv_detection]にはTumorサンプルとNormalサンプルのペア情報を記載します．
| Normalサンプルのコントロールパネルを作る場合は，そちらも記載します．
| コントロールパネル名は項目[controlpanel]で定義した名前を使用します．（次項で説明します）
|
| {Tumorサンプル},{Normalサンプル},{controlpanel} の順にカンマ (,) 区切りで記載してください．
| {Normalサンプル}や{controlpanel}がない場合は以下のように記載します．

=============== ======= =========================== ===========================================
パターン        ペア    コントロールパネル          書き方
=============== ======= =========================== ===========================================
パターン１      ○        ○                          sample1_tumor,sample1_normal,Panel1
パターン２      ○        ×                          sample2_tumor,sample1_normal,None
パターン３      ×        ○                          sample3_tumor,None,Panel1
パターン４      ×        ×                          sample4_tumor,None,None
=============== ======= =========================== ===========================================


.. code-block:: bash

  # Tumorサンプル名,Normalサンプル名,コントロールパネル名 と記載してください．

  # パターン１：TumorとNormalのペアのサンプルで，コントロールパネルがある場合
  # Tumorサンプル名,Normalサンプル名,コントロールパネル名 と記載してください．コントロールパネル名は項目[controlpanel]で定義した名前を使用します．
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

[controlpanel]の記載方法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| 項目[controlpanel]には，Normalサンプル名を複数指定して，コントロールパネル名を付けてNormalサンプルの集まりとして指定します．

.. code-block:: bash

  # コントロールパネル名,Normalサンプル1,Normalサンプル2,Normalサンプル3,・・・,NormalサンプルN と記載してください．
  panel1,sample1_normal,sample2_normal,sample3_normal,sample4_normal
  panel2,sample5_normal,sample6_normal,sample7_normal,sample8_normal
  
| 指定するサンプル数Nに最大値はないです．
| サンプル名は[fastq], [bam_tofastq], [bam_import]のいずれかで定義されていなくてはなりません．
| コントロールパネル名は任意で指定できますが，重複することはできません．

.. note::
  
  | Genomonではペアサンプルとコントロールパネルを用いて，SNPやエラーの除去を行っています．
  | そのため，可能な限りペアサンプルとコントロールパネルをご使用いただくことを推奨しています．
  |
  | **TumorとNormalのペアサンプルについて**
  | 
  | [mutation_call]，[sv_detection]では，Tumorサンプルで検出された変異のうち，Normalサンプルで検出された変異はSNPやエラーとして出力結果から除外します．
  |
  | **コントロールパネルについて**
  |
  | コントロールパネルでは，Normalサンプルのグループを定義します．
  | ペアサンプルで除ききれなかったSNPやエラーがあったとしても，Normalサンプルのグループ（コントロールパネル）で変異リードが複数見つかれば除外することができます．


[qc]の記載方法
^^^^^^^^^^^^^^^^^^

| 項目[qc]にはサンプル名を記載します．

.. code-block:: bash

  # ペアで記載する必要はありません．QC出力するサンプル名を記載してください．記載順も関係ありません．
  sample1_normal
  sample2_normal
  sample3_normal
  sample1_tumor
  sample2_tumor
  sample3_tumor


| この項目に定義するサンプル名は[fastq], [bam_tofastq], [bam_import]のいずれかで定義されていなくてはなりません．

