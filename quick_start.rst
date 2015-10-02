========================================
Quick Start
========================================
Human Genome Center (HGC)ではGenomonはインストール済みです．早速動かしてみましょう。

DNA解析コマンドの実行
-------

::
    
   >genomon_pipeline dna sample_conf project_root_directory

:dna/rna: DNA解析を実施するときはdnaを指定します
:sample conf: 解析対象のサンプルを記述したファイルになります
:project root directory: 結果出力のルートディレクトリを指定します

sample confの記述方法
--------------------
Genomonでは解析対象のサンプルをsample confに入力します。sample confに複数のサンプルを記述することにより、同時に解析できます．

::
  
  # 項目[fastq]にはinput fastqファイルを記載します．
  # 形式はサンプル名,read1.fastq,read2.fastqです。順不同です．
  [fastq]
  sample1_disease,/home/genomon/S1_D_read1.fastq,/home/genomon/S1_D_read2.fastq
  sample1_control,/home/genomon/S1_C_read1.fastq,/home/genomon/S1_C_read2.fastq
  sample2_disease,/home/genomon/S2_D_read1.fastq,/home/genomon/S2_D_read2.fastq
  sample2_control,/home/genomon/S2_C_read1.fastq,/home/genomon/S1_C_read2.fastq
  sample2_disease,/home/genomon/S2_D_read1.fastq,/home/genomon/S2_D_read2.fastq
  sample2_control,/home/genomon/S2_C_read1.fastq,/home/genomon/S1_C_read2.fastq
  
  # 項目[compare]にはdiseaseとmatched controlで比較するペアを記述します．
  # 形式はdiseaseサンプル名,controlサンプル名,non-matched_control_panelです。順不同です．
  # non-matched_control_panelはなくてもOKです。
  [compare]
  sample1_disease,sample1_control,panel2
  sample2_disease,sample2_control,panel3
  sample3_disease,sample3_control,panel1
  
  # 項目[controlpanel]にはpanel名とリストに登録するcontrolサンプル名を記述します．
  # 形式はpanel名,サンプル名1,サンプル名2,・・・です。
  # panelに登録するcontrolサンプルの数は10～20サンプルが良いです（詳細はこちら）．
  [controlpanel]
  panel1,sample1_control,sample2_control
  panel2,sample1_control,sample3_control
  panel3,sample2_control,sample3_control
  

結果ファイル
------------------
:bam: 指定したproject_root_directory/bam/sample/sample_markdup.bam
:変異call結果: 指定したproject_root_directory/mutation/sample名/sample名_genomon_mutations.result.txt
:SV検出結果: 指定したproject_root_directory/sv/sample名/sample名.genomonSV.result.txt


