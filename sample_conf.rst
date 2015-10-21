========================================
Sample Configの書き方
========================================

項目は5種類あります。

:[fastq]: FASTQを入力としてパイプラインを実行します．
:[bam_tofastq]: BAMを入力してFASTQに戻して、再アライメントして解析します．
:[bam_import]: 入力したBAMで解析を実行します．
:[compare]: tumor normalペアのサンプル、controlパネルを指定します．
:[control_panel]: controlパネルのペアを指定します．

[fastq], [bam_tofastq], [bam_import]は入力ファイルの情報を記載します．
[compare],[control_panel]には解析するための情報をきさいします．


項目[fastq]の記載方法
---------------------

::
  # 項目[fastq]にはinput fastqファイルのパスを記載します．
  # 形式はカンマ区切りで、  
  # サンプル名,read1.fastq,read2.fastq  と記載してください
  sample1_tumor,/home/genomon/sample1_T_read1.fastq,/home/genomon/sample1_T_read2.fastq
  sample1_normal,/home/genomon/sample1_N_read1.fastq,/home/genomon/sample1_N_read2.fastq

サンプル名は任意で指定してください。ディレクトリやファイル名で使用されます。


項目[bam_import]の記載方法
---------------------

::
  # 項目[bam_import]にはbamファイルのパスを記載します．
  # 形式はカンマ区切りで、
  # サンプル名,bam  と記載してください
  sample3_tumor,/home/genomon/sample3_T.bam
  
bam indexファイル(.bai)がセットで必要です。


項目[compare]の記載方法
---------------------

::
  # 項目[compare]にはtumorとnormalのペア情報を記載します．normalのコントロールパネルを作る場合は、そちらも記載します．
  #
  # 形式はカンマ区切りで、
  # Tumorサンプル名，Normalサンプル名,Controlパネル名 と記載してください．
  #
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


項目[controlpanel]の記載方法
---------------------

::
  # 項目[controlpanel]には、normalのサンプル名を複数指定して、panel名を付けてnormalサンプルの集まりとして指定します．
  # panel名,normalサンプル1,normalサンプル2,normalサンプル3,・・・,normalサンプルNと記載してください。サンプル数Nに最大値はないです。
  panel1,sample1_normal,sample2_normal,sample3_normal,sample4_normal

こちらに記載している、サンプル名も[fastq], [bam_tofastq], [bam_import]のいずれかで定義されていなくてはなりません．
パネル名は任意で指定してください。







   genomon_pipeline dna sample_conf.csv(.tsv) project_root_directory

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

変異Call結果 各カラムの説明
---------------------------
:Chr Start End: 変異候補のポジション
:Ref: 変異候補のポジションのリファレンス塩基です．Insertion の場合は"-"ハイフンが表示されます．
:Alt: 変異候補のポジションの塩基配列です．Deletion の場合は"-"ハイフンになります．
:A,C,G,T: Tumorの塩基数．SNVの場合は（A,C,G,T) の各個数，indel の場合は (Depth, indelのリード数) になります．
:A,C,G,T: Normalの塩基数．
:dis_mis: Tumorのミスマッチ率．
:dis_s_ratio: Tumorのstrand ratio．
:ctrl_mis: Normalのミスマッチ率
:ctrl_s_ratio: Normalのstrand ratio.
:P-value(fisher): Fisher -log10(p値)
:readPairNum_tumor: 変異が含まれるリード数
:variantPairNum_tumor: 変異が含まれないリード数
:otherPairNum_tumor: リアライメントできなかったリード数
:readPairNum_normal: 変異が含まれるリード数
:variantPairNum_normal: 変異が含まれないリード数
:otherPairNum_normal: リアライメントできなかったリード数
:indel_variantNum: 変異候補周辺のindelを含むリード数(indelは同一ポジションであれば加算される)
:indel_mismatch_rate: 上記indelのミスマッチ率
:bp_mismatch_count: 変異候補周辺のbreakpointを含むリード数(breakpointは同一ポジションにあれば加算される)
:distance_from_breakpoint: 変異候補からbreakpoointが何塩基離れているか表示されます．
:simple_repeat_pos: 変異候補のポジションとSimpleRepeatに登録されているポジションがintersectした場合にSimpleRepeatのポジションが表示されます．
:simple_repeat_seq: 上記SimpleRepeatの配列
:P-value(EBCall): EBCall -log10(p値)

おすすめフィルタ
------------------
  | Fisher（P-value）>= 1.0
  | EBCall（P-value）>= 3.0
  | variantPairNum_tumor >= 4
  | variantPairNum_normal <= 1

気をつけること
------------------
NormalサンプルにTumor contentが入っているとP値が低くなります。がん原因遺伝子がフィルタで消えてないか確認しましょう．


