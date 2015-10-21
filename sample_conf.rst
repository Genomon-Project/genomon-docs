========================================
Sample Configの書き方
========================================

項目は5種類あります。

:[fastq]: FASTQを入力としてパイプラインを実行します．
:[bam_tofastq]: BAMを入力してFASTQに戻して、再アライメントして解析します．
:[bam_import]: 入力したBAMで解析を実行します．
:[compare]: tumor normalペアのサンプル、controlパネルを指定します．
:[control_panel]: controlパネルのペアを指定します．

| [fastq], [bam_tofastq], [bam_import]は入力ファイルの情報を記載します．
| [compare],[control_panel]には解析するための情報をきさいします．


[fastq]の記載方法
---------------------

| 項目[fastq]にはinput fastqファイルのパスを記載します．

::

  # サンプル名,read1.fastq,read2.fastq  と記載してください
  sample1_tumor,/home/genomon/sample1_T_read1.fastq,/home/genomon/sample1_T_read2.fastq
  sample1_normal,/home/genomon/sample1_N_read1.fastq,/home/genomon/sample1_N_read2.fastq

サンプル名は任意で指定してください。ディレクトリやファイル名で使用されます。


[bam_import]の記載方法
--------------------------

| 項目[bam_import]にはbamファイルのパスを記載します．

::

  # サンプル名,bam  と記載してください
  sample3_tumor,/home/genomon/sample3_T.bam
  
bam indexファイル(.bai)がセットで必要です。


[compare]の記載方法
---------------------

| 項目[compare]にはtumorとnormalのペア情報を記載します．normalのコントロールパネルを作る場合は、そちらも記載します．

::

  # Tumorサンプル名,Normalサンプル名,Controlパネル名 と記載してください．

  # パターン１：tumorとnormalのペアのサンプルで、コントロールパネルがある場合
  # tumorサンプル名,normalサンプル名,コントロールパネル名 と記載してください。コントロールパネル名は項目[control_panel]で定義した名前を使用します。
  sample1_tumor,sample1_normal,Panel1
  
  # パターン２：tumorとnormalのペアのサンプルで、コントロールパネルがない場合
  # tumorサンプル名,normalサンプル名,None と記載してください。
  sample1_tumor,sample1_normal,None
  
  # パターン３：tumorだけで、normalのペアのサンプルがない。コントロールパネルがある場合
  # tumorサンプル名,None,Panel1 と記載してください。
  sample3_tumor,None,Panel1

  # パターン４：tumorだけで、normalのペアのサンプルがない。コントロールパネルがない場合
  # tumorサンプル名,None,None と記載してください。
  sample4_tumor,None,None

こちらに記載している、サンプル名は[fastq], [bam_tofastq], [bam_import]のいずれかで定義されていなくてはなりません．


[controlpanel]の記載方法
----------------------------

項目[controlpanel]には、normalのサンプル名を複数指定して、panel名を付けてnormalサンプルの集まりとして指定します．

::

  # panel名,normalサンプル1,normalサンプル2,normalサンプル3,・・・,normalサンプルNと記載してください。
  panel1,sample1_normal,sample2_normal,sample3_normal,sample4_normal

| サンプル数Nに最大値はないです。
| サンプル名は[fastq], [bam_tofastq], [bam_import]のいずれかで定義されていなくてはなりません．
| パネル名は任意で指定してください。




