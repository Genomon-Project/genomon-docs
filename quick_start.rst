========================================
Quick Start
========================================
Human Genome Center (HGC)ではGenomonはインストール済みです．早速動かしてみましょう。

DNA解析
-------
DNAパイプライン解析:

::
    
   >genomon_pipeline dna sample_conf project_root_directory

:dna/rna: DNA解析を実施するときはdnaを指定します
:sample conf: 解析対象のサンプルを記述したファイルになります
:project root directory: 結果出力のルートディレクトリを指定してください

sample confの記述方法
--------------------
Genomonでは解析対象のサンプルをsample confに入力します。複数のサンプルをsample confに記述することにより、複数サンプルを同時に解析できます．

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
  





{text}

コマンドの実行
--------------

{text}

結果ファイルの確認
------------------

{text}

