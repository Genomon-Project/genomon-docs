RNA 解析結果ファイル詳細
==========================

結果ファイルは実行時に指定した 出力ルートディレクトリに出力されます．

.. code-block:: bash

  # 発現量解析結果
  {出力ルートディレクトリ}/expression/{サンプル名}/{サンプル名}.sym2fkpm.txt
  
  # 融合遺伝子検出結果
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_fusionfusion_filt.txt
  # BAMのQuality Controlの結果
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_starqc.txt
  
  # paplotの結果
  # index.htmlをクリックすることで結果が表示されます．
  {出力ルートディレクトリ}/paplot/{サンプル設定ファイル名}


融合遺伝子検出(fusionfusion)結果
---------------------------------------

| 融合遺伝子検出の概要については https://github.com/Genomon-Project/fusionfusion を参照してください．
|
| 融合遺伝子検出結果はサンプルシートに入力したパターンによって少し異なります．
|
| サンプルシートのパターンについては :doc:`rna_sample_csv` を参照ください．
|
| fusionfusionのコール結果は次のように出力されますが，サンプルシートのパターンによって，出力されないファイルもあります．
| たとえば，すべてパターン１で入力した場合，パターン２のファイルは出力されません．
|

**フィルタリングなし**

.. code-block:: bash

  # すべての結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_fusionfusion.txt
  
  # パターン1の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_fusionfusion_controlpanel.txt
  
  # パターン2の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_fusionfusion_no_controlpanel.txt


**フィルタリングあり**

.. code-block:: bash

  # すべての結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_fusionfusion_filt.txt
  
  # パターン1の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_fusionfusion_controlpanel_filt.txt
  
  # パターン2の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_fusionfusion_no_controlpanel_filt.txt


融合遺伝子検出結果ファイルはパイプライン設定ファイルの以下のハイライトの値でフィルタしています．

.. code-block:: cfg
    :linenos:
    :emphasize-lines: 6

    [fusionfusion]
    qsub_option = -l ljob,s_vmem=5.3G,mem_req=5.3G
    annotation_dir = # the path to the fusionfusion/resource
    params=
    # 以下の設定では，同一遺伝子で検出されたfusionは除外する
    filt_params = --filter_same_gene


各カラムの説明
^^^^^^^^^^^^^^^^^^^^

:v0:
  chromosome for the 1st breakpoint

:v1:
  coordinate for the 1st breakpoint

:v2:
  direction of the 1st breakpoint

:v3:
  chromosome for the 2nd breakpoint

:v4:
  coordinate for the 2nd breakpoint

:v5:
  direction of the 2nd breakpoint

:v6:
  inserted nucleotides within the breakpoints

:v7:
  gene overlapping the 1st breakpoint

:v8:
  exon-intron junction overlapping the 1st breakpoint

:v9:
  gene overlapping the 2nd breakpoint

:10:
  exon-intron junction overlapping the 2nd breakpoint

:v11:
  #read_pairs supporting the variant (by STAR)
  

発現量解析結果
----------------------------------

| 発現量解析の概要については https://github.com/Genomon-Project/GenomonExpression を参照してください．
|

各カラムの説明
^^^^^^^^^^^^^^^^^

 #. 遺伝子名
 #. 発現量(FKPM value.)


Intron Retention検出結果
----------------------------------

| Intron Retention検出の概要については https://github.com/friend1ws/intron_retention_utils のsimple_countの項目を参照してください．
|

各カラムの説明
^^^^^^^^^^^^^^^^^

:Chr: chromosome of the exon-intron boundary
:Boundary_Pos: coordinate of the exon-intron boundary (the last exonic base)
:Gene_Symbol: gene symbol from refGene.txt.gz
:Motif_Type: splicing donor or acceptor
:Strand: transcription starnd of the gene
:Junction_List: cannonical splicing junction list from that exon-intron boundary
:Gene_ID_List: refGene ID list with that exon-intron boundary
:Exon_Num_List: exon numbers for each refGene IDs
:Edge_Read_Count: the number of reads covering each exon-intron boundary
:Intron_Retention_Read_Count: the number of putative intron retention reads


STAR-QC結果 (BAMのQuality Control)
----------------------------------

各カラムの説明
^^^^^^^^^^^^^^^^^

 #. Started job on
 #. Started mapping on
 #. Finished on
 #. Mapping speed, Million of reads per hour
 #. Number of input reads
 #. Average input read length
 #. Uniquely mapped reads number
 #. Uniquely mapped reads %
 #. Average mapped length
 #. Number of splices: Total
 #. Number of splices: Annotated (sjdb)
 #. Number of splices: GT/AG
 #. Number of splices: GC/AG
 #. Number of splices: AT/AC
 #. Number of splices: Non-canonical
 #. Mismatch rate per base, %
 #. Deletion rate per base
 #. Deletion average length
 #. Insertion rate per base
 #. Insertion average length
 #. Number of reads mapped to multiple loci
 #. % of reads mapped to multiple loci
 #. Number of reads mapped to too many loci
 #. % of reads mapped to too many loci
 #. % of reads unmapped: too many mismatches
 #. % of reads unmapped: too short
 #. % of reads unmapped: other

