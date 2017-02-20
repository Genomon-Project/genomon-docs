
DNA 解析結果ファイルの説明
==========================

結果ファイルは実行時に指定した 出力ルートディレクトリに出力されます．

.. code-block:: bash

  # 変異コール結果
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_mutation_filt.txt
  # SV検出結果
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_sv_filt.txt
  # BAMのQuality Controlの結果
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_qc.txt
  # Paplotの結果
  #  * pmsignatureの結果はこちらを参照してください．
  # index.htmlをクリックすることで結果が表示されます．
  {出力ルートディレクトリ}/paplot/{サンプル設定ファイル名}


変異コール結果
---------------

| 変異コールの結果はサンプルシートに入力したパターンによって少し異なります．
| Normalサンプルがないパターン（パターン３，4）では，Normalサンプルの項目が出力されません．
|
| サンプルシートのパターンについては :doc:`dna_sample_csv` を参照ください．
|
| mutationのコール結果は次のように出力されますが，サンプルシートのパターンによって，出力されないファイルもあります．
| たとえば，すべてパターン１で入力した場合，パターン２，３，４のファイルは出力されません．
|

**フィルタリングなし**

.. code-block:: bash

  # すべての結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_mutation.txt
  
  # パターン1の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_mutation_pair_controlpanel.txt
  
  # パターン2の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_mutation_pair.txt
  
  # パターン3の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_mutation_unpair_controlpanel.txt
  
  # パターン4の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_mutation_unpair.txt


**フィルタリングあり**

フィルタの内容はNormalサンプルがあるかないかで異なります．このフィルタはパイプライン設定ファイルの[mutation_util]タグで変更が可能です。Tumor V.S. Normalで比較のパターンは pair_params=のオプションを変更します。Normalなしパターンはsingle_paramsのオプションを変更します。

.. code-block:: cfg
    :linenos:

    [mutation_util]
    pair_params = --fish_pval 1.0 --realign_pval 1.0 --eb_pval 4.0 --tcount 4 --ncount 2
    single_params = --post10q 0.1 --r_post10q 0.1 --eb_pval 4.0 --count 4

.. code-block:: bash

  # すべての結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_mutation_filt.txt
  
  # パターン1の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_mutation_pair_controlpanel_filt.txt
  
  # パターン2の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_mutation_pair_filt.txt
  
  # パターン3の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_mutation_unpair_controlpanel_filt.txt
  
  # パターン4の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_mutation_unpair_filt.txt


Tumor V.S. Normalで比較　(パターン１, パターン２)
**************************************************
各カラムの説明
^^^^^^^^^^^^^^^^^^^

:Chr Start End: 
  変異候補のポジション

:Ref:
  変異候補のポジションのリファレンス塩基です．Insertion の場合は ``-`` (ハイフン) が表示されます．

:Alt:
  変異候補のポジションの塩基配列です．Deletion の場合は ``-`` (ハイフン) になります．

:ANNOVARの結果:
  `ANNOVAR`_ をご使用の方はこのカラムに結果が出力されます．
  各カラムの説明は `ANNOVAR`_ のwebページでチェックしてください．

:depth_tumor:
  Tumorのdepth

:variantNum_tumor:
  Tumorの変異アレルの数

:depth_normal:
  Normalのdepth

:variantNum_normal:
  Normalの変異アレルの数

:bases_tumor:
  Tumorの塩基数．フォーマットは(depth_strand+,variantNum_strand+,depth_strand-,variantNum_strand-)の数になります．

:bases_normal:
  Normalの塩基数．

:A_C_G_T_tumor:
  Tumorの塩基数．SNVの場合は（A,C,G,T) の各個数，indel の場合は (Depth, indelのリード数) になります．

:A_C_G_T_normal:
  Normalの塩基数．

:misRate_tumor:
  Tumorのミスマッチ率．

:strandRatio_tumor:
  Tumorのstrand ratio．

:misRate_normal:
  Normalのミスマッチ率

:strandRatio_normal:
  Normalのstrand ratio.変異数がない場合は ``-`` が出力されます．

:P-value(fisher):
  Fisher -log10(p値)

:RefNum_tumor:
  変異を含まないリード数

:AltNum_tumor:
  変異を含むリード数

:OtherNum_tumor:
  リアライメントできなかったリード数

:RefNum_normal:
  変異を含まないリード数

:AltNum_normal:
  変異を含むリード数

:OtherNum_normal:
  リアライメントできなかったリード数

:P-value(fisher)_realignment:
  Fisher-log10(p値).tableは((RefNum_tumor,RefNum_normal),(AltNum_tumor,AltNum_normal))

:indel_variantNum:
  変異候補周辺のindelを含むリード数(indelは同一ポジションであれば加算される)

:indel_mismatch_rate:
  上記indelのミスマッチ率

:bp_mismatch_count:
  変異候補周辺のbreakpointを含むリード数(breakpointは同一ポジションにあれば加算される)

:distance_from_breakpoint:
  変異候補からbreakpoointが何塩基離れているか表示されます．

:simple_repeat_pos:
  変異候補のポジションとSimpleRepeatに登録されているポジションがintersectした場合にSimpleRepeatのポジションが表示されます．

:simple_repeat_seq:
  上記SimpleRepeatの配列

:P-value(EBCall):
  EBCall -log10(p値) sample.csvにcontrolパネルがNoneの場合は出力されません

:HGVDの結果:
  HGVDをご使用の方はここにHGVDの結果が出力されます．


Normalなし　(パターン３, パターン４)
***************************************
各カラムの説明
^^^^^^^^^^^^^^^^^^^^

:Chr Start End:
  変異候補のポジション

:Ref:
  変異候補のポジションのリファレンス塩基です．Insertion の場合は"-"ハイフンが表示されます．

:Alt:
  変異候補のポジションの塩基配列です．Deletion の場合は"-"ハイフンになります．

:ANNOVARの結果:
  `ANNOVAR`_ をご使用の方はANNOVARの結果が出力されます．各カラムの説明は `ANNOVAR`_ のwebページでチェックしてください．

:depth:
  depth

:variantNum:
  変異アレルのリード数

:bases:
  フォーマットは(depth_strand+,variantNum_strand+,depth_strand-,variantNum_strand-)の数になります．

:A_C_G_T:
  SNVの場合は（A,C,G,T) の各個数，indel の場合は (Depth, indelのリード数) になります．

:misRate:
  ミスマッチ率．

:strandRatio:
  strand ratio．

:10%_posterior_quantile:
  depthと変異アレルの数は二項分布でモデル化するためにβ分布を利用.10%の値

:posterior_mean:
  mean値

:90%_posterior_quantile:
  depthと変異アレルの数は二項分布でモデル化するためにβ分布を利用.90%の値

:readPairNum:
  変異を含まないリード数

:variantPairNum:
  変異を含むリード数

:otherPairNum:
  リアライメントできなかったリード数

:10%_posterior_quantile(realignment):
  realignmentのreadPairNumとvariantPairNumでβ分布を利用.10%の値

:posterior_mean(realignment):
  mean値

:90%_posterior_quantile(realignment):
  realignmentのreadPairNumとvariantPairNumでβ分布を利用.90%の値

:simple_repeat_pos:
  SimpleRepeatに登録されているか

:simple_repeat_seq:
  上記SimpleRepeatの配列

:P-value(EBCall):
  EBCall -log10(p値) sample.csvにcontrolパネルがNoneの場合は出力されません

:HGVDの結果:
  HGVDをご使用の方はここにHGVDの結果が出力されます．


SV検出結果
----------

| サンプルシートのパターンについては :doc:`dna_sample_csv` を参照ください．
|
| SV検出結果は次のように出力されますが，サンプルシートのパターンによって，出力されないファイルもあります．
| たとえば，すべてパターン１で入力した場合，パターン２，３，４のファイルは出力されません．
|

**フィルタリングなし**

.. code-block:: bash

  # すべての結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/sv.txt
  
  # パターン1の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/sv_pair_controlpanel.txt
  
  # パターン2の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/sv_pair.txt
  
  # パターン3の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/sv_unpair_controlpanel.txt
  
  # パターン4の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/sv_unpair.txt


**フィルタリングあり**

フィルタの内容はdna_genomon.cfgで設定したパラメータに基づいていますが，デフォルトは以下です．

::

  min_tumor_allele_freq >= 0.07
  max_control_variant_read_pair >= 1
  control_depth_thres >= 10
  inversion_size_thres >= 1000

.. code-block:: bash

  # すべての結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/sv_filt.txt
  
  # パターン1の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/sv_pair_controlpanel_filt.txt
  
  # パターン2の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/sv_pair_filt.txt
  
  # パターン3の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/sv_unpair_controlpanel_filt.txt
  
  # パターン4の結果をマージ
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/sv_unpair_filt.txt


各カラムの説明
**************

:Chr_1:
  第１ブレークポイントにおける染色体
  chromosome for the 1st breakpoint

:Pos_1:
  第１ブレークポイントにおける座標

:Dir_1:
  第１ブレークポイントの向き

:Chr_2:
  第２ブレークポイントにおける染色体

:Pos_2:
  第２ブレークポイントにおける座標

:Dir_2:
  第２ブレークポイントの向き

:Inserted_Seq:
  ブレークポイント間の挿入塩基配列

:Variant_Type:
  構造変異のタイプ（deletion, inversion, tandem_duplication, translocation）

:Gene_1:
  第１ブレークポイントにおける遺伝子

:Gene_2:
  第２ブレークポイントにおける遺伝子

:Exon_1:
  第１ブレークポイントにおけるエキソンに対応する遺伝子

:Exon_2:
  第２ブレークポイントにおけるエキソンに対応する遺伝子

:Num_Tumor_Ref_Read_Pair:
  tumor sampleにおけるリファレンス配列（構造変異なし配列）をサポートするリードペアの本数

:Num_Tumor_Var_Read_Pair:
  tumor sampleにおける変異配列をサポートするリードペアの本数

:Tumor_VAF:
  tumor sampleにおける変異配列をサポートするリードペアの割合

:Num_Control_Ref_Read_Pair:
  matched control sampleにおけるリファレンス配列（構造変異なし配列）をサポートするリードペアの本数

:Num_Control_Var_Read_Pair:
  matched control sampleにおける変異配列をサポートするリードペアの本数

:Control_VAF:
  matched control sampleにおける変異配列をサポートするリードペアの割合

:Minus_Log_Fisher_P_value:
  -log10 (P-value) fisher's exact test on contingency table of (tumor v.s. matched control) and (reference variant read pairs)

:Non-Matched_Control_Sample_With_Max_Junction:
  non-matched control sampleにおいて対応するjunction read pairが最大となったサンプル

:Num_Max_Non-Matched_Control_Junction:
  non-matched control sampleにおいて対応するjunction read pairの最大数

:Max_Over_Hang_1:
  第１ブレークポイントにおける最大オーバーハングサイズ

:Max_Over_Hang_2:
  第２ブレークポイントにおける最大オーバーハングサイズ


QC結果 (BAMのQuality Control)
----------------------------------

各カラムの説明
**************

:bam_filename:
  the name of the bam file stats have been collected for.

:sample:
  the name of the sample (taken from the bam file).

:platform:
  the name of the hardware platform (taken from the bam file).

:platform_unit:
  the platform unit (i.e. lane/run) of the hardware platform (taken from the bam file).

:library:
  the library name associated with the read group.	

:readgroup:
  the read group name.

:read_length_r1:
  the read length associated with read 1.

:read_length_r2:
  the read length associated with read 2.

:#_mapped_bases:
  the total number of mapped bases.
  
  - #_mapped_bases_r1: the total number of mapped bases for all read 1s.
  - #_mapped_bases_r2: the total number of mapped bases for all read 2s.

:#_divergent_bases:
  the total number of bases divergent from the reference.

  - #_divergent_bases_r1: the total number of bases divergent from the reference for all read 1s.
  - #_divergent_bases_r2: the total number of bases divergent from the reference for all read 2s.

:#_total_reads:
  the total number of reads.

  - #_total_reads_r1: the total number of read 1s.
  - #_total_reads_r2: the total number of read 2s.

:#_mapped_reads:
  the total number of unmapped reads.

  - #_mapped_reads_r1: the total number of unmapped read 1s.
  - #_mapped_reads_r2: the total number of unmapped read 2s.

:#_mapped_reads_properly_paired:
  the total number of properly paired reads.

:#_gc_bases_r1:
  the total number of G/C bases in read 1s.

:#_gc_bases_r2:
  the total number of G/C bases in read 2s.

:mean_insert_size:
  the mean insert size.

:insert_size_sd:
  the insert size standard deviation.

:median_insert_size:
  the median insert size.

:#_duplicate_reads:
  the total number of duplicate reads.

:total_depth:
  the total number of depth.

:bait_size:
  bait size.

:average_depth:
  the mean depth. (total_depth/bait_size)

:depth_stdev:
  the depth standard deviation.

:Nx_ratio:
  coverage N※以上のdepthを持つbaseの比率. (Nx/bait_size)

:Nx:
  N以上のdepthを持つbase総数


※ coverage Nはパイプライン設定ファイルで指定した値です．

.. code-block:: cfg
    :linenos:
    :emphasize-lines: 3
     
    [coverage]
    qsub_option = -l s_vmem=1G,mem_req=1G
    coverage    = 2,10,20,30,40,50,100
    wgs_flag = False
    wgs_incl_bed_width = 1000000
    wgs_i_bed_lines = 10000
    wgs_i_bed_width = 100

.. _ANNOVAR: http://annovar.openbioinformatics.org/en/latest/user-guide/download/

pmsignature
----------------------------------

| pmsignatureの結果はpmsignatureディレクトリに出力しますが、.Rdataおよび.json形式ですので、結果の確認にはpaplotディレクトリを参照ください
|
