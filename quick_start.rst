========================================
Quick Start DNA解析
========================================
Human Genome Center (HGC)ではGenomonはインストール済みです．早速動かしてみましょう。

コマンドの実行
-------

::
    
   >genomon_pipeline dna sample_conf.csv(.tsv) project_root_directory

:dna/rna: DNA解析を実行するときはdnaを指定します
:sample_conf.csv(.tsv): 解析対象のサンプルを記述したファイルになります
:project_root_directory: 結果出力のルートディレクトリを指定します

sample confの記述方法
--------------------
Genomonでは解析対象のサンプルをsample_conf.csv(.tsv)に入力します。sample_conf.csv(.tsv)に複数のサンプルを記述することにより、同時に解析できます．.csvの拡張子の場合は,(カンマ区切り) .tsvの拡張子の場合は (タブ区切り)でカラムを区切ってください．ファイル名は変更しても大丈夫です．例)sample_conf_AML_project.csv

::
  
  # 項目[fastq]にはinput fastqファイルを記載します．
  # 形式はサンプル名,read1.fastq,read2.fastqです。順不同です．
  [fastq]
  sample1_tumor,/home/genomon/sample1_T_read1.fastq,/home/genomon/sample1_T_read2.fastq
  sample1_normal,/home/genomon/sample1_N_read1.fastq,/home/genomon/sample1_N_read2.fastq
  sample2_tumor,/home/genomon/sample2_T_read1.fastq,/home/genomon/sample2_T_read2.fastq
  sample2_normal,/home/genomon/sampel2_N_read1.fastq,/home/genomon/sample2_N_read2.fastq
  sample3_tumor,/home/genomon/sample3_T_read1.fastq,/home/genomon/sample3_T_read2.fastq
  sample3_normal,/home/genomon/samptl3_N_read1.fastq,/home/genomon/sample3_N_read2.fastq
  
  # 項目[compare]にはtumorとmatched normalで比較するペアを記述します．
  # 形式はtumorサンプル名,normalサンプル名,non-matched_normal_panelです。順不同です．
  # non-matched_normal_panelはなくてもOKです。
  [compare]
  sample1_tumor,sample1_normal,panel1
  sample2_tumor,sample2_normal,panel2
  sample3_tumor,sample3_normal,panel3
  
  # 項目[normalpanel]にはpanel名とリストに登録するnormalサンプル名を記述します．
  # 形式はpanel名,サンプル名1,サンプル名2,・・・サンプル名Nです。
  # panelに登録するnormalサンプルの数は10～20サンプルが良いです（詳細はこちら）．
  [normalpanel]
  panel1,sample2_normal,sample3_normal
  panel2,sample1_normal,sample3_normal
  panel3,sample1_normal,sample2_normal
  
サンプルファイルのリンク：<https://www.hgc.jp/w3varann/sample.csv>

結果ファイル
------------------
:bam: project_root_directory/bam/sample/sample_markdup.bam
:変異Call結果: project_root_directory/mutation/sample名/sample名_genomon_mutations.result.txt
:SV検出結果: project_root_directory/sv/sample名/sample名.genomonSV.result.txt


おすすめフィルタ
Fisher（P-value）>= 1.0
EBCall（P-value）>= 3.0


