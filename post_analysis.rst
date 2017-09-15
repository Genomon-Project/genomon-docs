Post Analysis
-------------------------------------------------

GenomonPipelineで解析した結果をまとめ，レポートを作成する機能です．

ファイルをまとめる GenomonPostAnalysis とレポートを作成する paplot から構成されています．

==================================
GenomonPostAnalysis
==================================

https://github.com/aokad/GenomonPostAnalysis

GenomonPipelineで解析した結果をまとめる処理を行います．

 - 解析結果を一つのファイルにまとめます
 - 解析結果をIGVでキャプチャーするスクリプトを作成します
 - 変異の場所だけを抜き出して新しいbamを作成するスクリプトを作成します

出力ファイルに関する解説は `post-analysis <./dna_output_info.html#post-analysis>`_ 参照．

デフォルトで有効になっていますので，無効化する場合は以下の設定をFalseにします．

.. code-block:: cfg
  :caption: genomon.cfg
  
    ##########
    ## Post Analysis
    [post_analysis]
    enable = True 

====================
paplot
====================

https://github.com/Genomon-Project/paplot

GenomonPipelineで解析した結果を使用してレポートを作成します．

【DNA】

 - mutation-matrix: [mutation-call] の結果をサンプルと遺伝子のマトリックスとして表現します．
 - SV: [sv-detection] の結果のうち，breakpoint1と2を結び，circos様のグラフを作成します．
 - QC: [qc] の結果をプロットします．
 - pmsignature: pmsignature (type=independent) により作成されたシグネチャをプロットします．
 - signature: pmsignature (type=full) により作成されたシグネチャをプロットします．

出力ファイルに関する解説は `post-analysis <./dna_output_info.html#paplot>`_ 参照．

【RNA】

 - fusion: [fusion] の結果のうち，breakpoint1と2を結び，circos様のグラフを作成します．
 - star-QC: [star] によるアライメントで作成されるbamの情報を使用してQCグラフとしてプロットします．

出力ファイルに関する解説は `post-analysis <./rna_output_info.html#paplot>`_ 参照．

デフォルトで有効になっていますので，無効化する場合は以下の設定をFalseにします．

.. code-block:: cfg
  :caption: genomon.cfg

    [paplot]
    enable = True 

=======================================
GenomonPipelineでの設定について
=======================================

---------------------------------
ANNOVAR
---------------------------------

mutation-matrixを作成するにはGene情報とfunction情報が必須ですので，annovar設定をOFFにしていると表示されません．

Genomon設定ファイルをご確認ください．

`ANNOVARのインストールとGenomonへの設定方法 <./dna_quick_start.html#id1>`_ 

---------------------------------
mutation-matrixのfunction項目
---------------------------------

Genomonでは，functionとして"Func.refGene"列と"ExonicFunc.refGene"列をマージして使用しています．

マージは"ExonicFunc.refGene"列の値が"splicing"であれば，"ExonicFunc.refGene"列の値を採用し，それ以外の場合は"Func.refGene"列の値を採用するというルールで行います．
マージしたfunctionは"Merge_Func"として新しく列を作ります．
この処理はGenomonPostAnalysisで変異の結果をまとめるときに行っています．

paplotは新しく作られた"Merge_Func"列をfunctionのデータとして使用しています．

.. code-block:: cfg
  :caption: paplot_dna.cfg
  :emphasize-lines: 4

  [result_format_mutation]
  
  # column index (required)
  col_func = Merge_Func
  col_gene = Gene.refGene
  
  # column index (option)
  col_opt_chr = Chr
  col_opt_start = Start
  col_opt_end = End
  col_opt_ref = Ref
  col_opt_alt = Alt
  col_opt_ID = id

そのため，Genomonで用意しているpaplot_dna.cfgはマージされた解析結果専用です．（マージ前の解析結果ファイルには"Merge_Func"列が存在しないため）

マージ前の解析結果ファイルを使用してpaplotでmutation-matrixを作成する場合は ``col_func = Func.refGene`` と変更する必要があります．

---------------------------------
mutation-matrixのフィルタリング
---------------------------------

paplotでmutation-matrixレポートを作成する際，以下設定でフィルタリングを行うことができます．レポート中の変異の数にはこの時除かれた変異は含まれていません．

Genomonでは，functionが(空白), unknown, synonymous_SNV のうちどれかである変異は除外しているため，レポート中の変異の数はフィルタリング後の値になります．

.. code-block:: cfg
  :caption: paplot_dna.cfg

  [mut]
  # geneごとの変異の発生率が一定以上のもののみ使用する
  ## Genomonでは0にしているので，すべて使用する
  use_gene_rate = 0
  
  # 指定したgeneのみ使用する
  ## Genomonでは設定していないので，すべて使用する
  limited_genes =
  
  # 指定したgeneを使用しない
  ## Genomonでは設定していないので，すべて使用する
  nouse_genes = 
  
  # 指定したfuncsのみ使用する
  ## Genomonでは設定していないので，すべて使用する
  limited_funcs =
  
  # 指定したfuncsを使用しない
  ## Genomonでは(空白),unknown,synonymous_SNVの場合の変異を除外する
  nouse_funcs = _blank_,unknown,synonymous_SNV

---------------------------------
SV, fusionのフィルタリング
---------------------------------

paplotでCA (GenomonでのSV, fusion) レポートを作成する際，以下設定でフィルタリングを行うことができます．レポート中の変異の数にはこの時除かれた変異は含まれていません．

Genomonでは，SV, fusionともにchrが1～22,X,Yの変異のみ使用しているため，レポート中の変異の数はフィルタリング後の値になります．

.. code-block:: cfg
  :caption: paplot_dna.cfg

  [ca]
  use_chrs = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,X,Y

  ##################
  # グループ設定
  # [result_format_ca] col_opt_group が設定されている場合のみ有効
  ## Genomonではグループ設定を行っていないため，以下の項目は無効
  ##################
  
  # 入力されていた場合，そのgroupのみ出力する
  limited_group = 
  
  # 入力されていた場合，そのgroupはplot対象から除外する
  nouse_group = 

---------------------------------
fusionの列名
---------------------------------

fusionfusionの解析結果にはヘッダ（列名）がないため，GenomonPostAnalysisで変異の結果をまとめるときにヘッダを付与しています．

paplotはGenomonPostAnalysisで作られたヘッダを使用して設定を行っています．

.. code-block:: cfg
  :caption: paplot_rna.cfg

  [result_format_ca]
  header = True
  # column index (required)
  col_chr1 = v0
  col_break1 = v1
  col_chr2 = v3
  col_break2 = v4
  
  # column index (option)
  col_opt_dir1 = v2
  col_opt_dir2 = v5
  col_opt_gene_name1_1 = v7
  col_opt_gene_name1_2 = v8
  col_opt_gene_name2_1 = v9
  col_opt_gene_name2_2 = v10
  col_opt_value1 = v11

そのため，Genomonで用意しているpaplot_rna.cfgはマージされた解析結果専用です．（マージ前の解析結果ファイルにはヘッダが存在しないため）

マージ前の解析結果ファイルを使用してpaplotでCA (Genomonでのfusion) レポートを作成する場合は以下のように変更する必要があります．

.. code-block:: cfg
  :caption: paplot_rna.cfg

  [result_format_ca]
  header = False
  # column index (required)
  col_chr1 = 1
  col_break1 = 2
  col_chr2 = 4
  col_break2 = 5
  
  # column index (option)
  col_opt_dir1 = 3
  col_opt_dir2 = 6
  col_opt_gene_name1_1 = 8
  col_opt_gene_name1_2 = 9
  col_opt_gene_name2_1 = 10
  col_opt_gene_name2_2 = 11
  col_opt_value1 = 12

