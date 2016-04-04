========================================
DNA解析結果ファイルの各項目の説明
========================================

結果ファイル
------------------

:変異Call結果: ${sample}_genomon_mutations.result.(filt).txt
:SV検出結果: ${sample}_genomon.genomonSV.result.(filt).txt
:BAM Summary結果: ${sample}.tsv

変異Call結果(Tumor V.S. Normalで比較)
-------------------------------------

genomon_mutations.result.filt.txt(フィルタ済み結果)ファイルはgenomon_mutations.result.txtをdna_genomon.cfgで設定した以下のハイライトの値でフィルタしています．詳細は :doc:`dna_config_info` を参照ください

.. code-block:: cfg
    :linenos:
    :emphasize-lines: 2,3,7,13

    [realignment_filter]
    disease_min_mismatch=4
    control_max_mismatch=2
    score_diff=5
    window_size=200
    max_depth=5000
    fisher_pval-log10_thres = 1.0
    post_10_q_thres = 0.1

    [eb_filter]
    map_quality = 20
    base_quality = 15
    ebcall_pval-log10_thres = 4.0


各カラムの説明
**************
`Chr Start End`
 変異候補のポジション
`Ref`
 変異候補のポジションのリファレンス塩基です．Insertion の場合は"-"ハイフンが表示されます．
`Alt`
 変異候補のポジションの塩基配列です．Deletion の場合は"-"ハイフンになります．
`annovarの結果`
  `annovar`_ をご使用の方はこのカラムに結果が出力されます．各カラムの説明は `annovar`_ のwebページでチェックしてください．
`depth_tumor`
 Tumorのdepth
`variantNum_tumor`
 Tumorの変異アレルの数
`depth_normal`
 Normalのdepth
`variantNum_normal`
 Normalの変異アレルの数
`bases_tumor`
 Tumorの塩基数．フォーマットは(depth_strand+,variantNum_strand+,depth_strand-,variantNum_strand-)の数になります．
`bases_normal`
 Normalの塩基数．
`A_C_G_T_tumor`
 Tumorの塩基数．SNVの場合は（A,C,G,T) の各個数，indel の場合は (Depth, indelのリード数) になります．
`A_C_G_T_normal`
 Normalの塩基数．
`misRate_tumor`
 Tumorのミスマッチ率．
`strandRatio_tumor`
 Tumorのstrand ratio．
`misRate_normal`
 Normalのミスマッチ率
`strandRatio_normal`
 Normalのstrand ratio.変異数がない場合は-が出力されます．
`P-value(fisher)`
 Fisher -log10(p値)
`RefNum_tumor`
 変異を含まないリード数
`AltNum_tumor`
 変異を含むリード数
`OtherNum_tumor`
 リアライメントできなかったリード数
`RefNum_normal`
 変異を含まないリード数
`AltNum_normal`
 変異を含むリード数
`OtherNum_normal`
 リアライメントできなかったリード数
`P-value(fisher)_realignment`
 Fisher-log10(p値).tableは((RefNum_tumor,RefNum_normal),(AltNum_tumor,AltNum_normal))
`indel_variantNum`
 変異候補周辺のindelを含むリード数(indelは同一ポジションであれば加算される)
`indel_mismatch_rate`
 上記indelのミスマッチ率
`bp_mismatch_count`
 変異候補周辺のbreakpointを含むリード数(breakpointは同一ポジションにあれば加算される)
`distance_from_breakpoint`
 変異候補からbreakpoointが何塩基離れているか表示されます．
`simple_repeat_pos`
 変異候補のポジションとSimpleRepeatに登録されているポジションがintersectした場合にSimpleRepeatのポジションが表示されます．
`simple_repeat_seq`
 上記SimpleRepeatの配列
`P-value(EBCall)`
 EBCall -log10(p値) sample.csvにcontrolパネルがNoneの場合は出力されません
`HGVDの結果`
 HGVDをご使用の方はここにHGVDの結果が出力されます．



変異Call結果 比較なしパターン
-----------------------------

genomon_mutations.result.filt.txt(フィルタ済み結果)ファイルはgenomon_mutations.result.txtをdna_genomon.cfgで設定した以下のハイライトの値でフィルタしています．詳細は :doc:`dna_config_info` を参照ください

.. code-block:: cfg
    :linenos:
    :emphasize-lines: 2,8,13

    [realignment_filter]
    disease_min_mismatch=4
    control_max_mismatch=2
    score_diff=5
    window_size=200
    max_depth=5000
    fisher_pval-log10_thres = 1.0
    post_10_q_thres = 0.1

    [eb_filter]
    map_quality = 20
    base_quality = 15
    ebcall_pval-log10_thres = 4.0

各カラムの説明
**************

`Chr Start End` 
 変異候補のポジション
`Ref`
 変異候補のポジションのリファレンス塩基です．Insertion の場合は"-"ハイフンが表示されます．
`Alt`
 変異候補のポジションの塩基配列です．Deletion の場合は"-"ハイフンになります．
`annovarの結果`
 `annovar`_ をご使用の方はannovarの結果が出力されます．各カラムの説明は `annovar`_ のwebページでチェックしてください．
`depth`
 depth
`variantNum`
 変異アレルのリード数
`bases`
 フォーマットは(depth_strand+,variantNum_strand+,depth_strand-,variantNum_strand-)の数になります．
`A_C_G_T`
 SNVの場合は（A,C,G,T) の各個数，indel の場合は (Depth, indelのリード数) になります．
`misRate`
 ミスマッチ率．
`strandRatio`
 strand ratio．
`10%_posterior_quantile`
 depthと変異アレルの数は二項分布でモデル化するためにβ分布を利用.10%の値
`posterior_mean`
 mean値
`90%_posterior_quantile`
 depthと変異アレルの数は二項分布でモデル化するためにβ分布を利用.90%の値
`readPairNum`
 変異を含まないリード数
`variantPairNum`
 変異を含むリード数
`otherPairNum`
 リアライメントできなかったリード数
`10%_posterior_quantile(realignment)`
 realignmentのreadPairNumとvariantPairNumでβ分布を利用.10%の値
`posterior_mean(realignment)`
 mean値
`90%_posterior_quantile(realignment)`
 realignmentのreadPairNumとvariantPairNumでβ分布を利用.90%の値
`simple_repeat_pos`
 SimpleRepeatに登録されているか
`simple_repeat_seq`
 上記SimpleRepeatの配列
`P-value(EBCall)`
 EBCall -log10(p値) sample.csvにcontrolパネルがNoneの場合は出力されません
`HGVDの結果`
 HGVDをご使用の方はここにHGVDの結果が出力されます．


SV検出結果
----------

各カラムの説明
**************

:1: chromosome for the 1st breakpoint
:2: coordinate for the 1st breakpoint
:3: direction of the 1st breakpoint
:4: chromosome for the 2nd breakpoint
:5: coordinate for the 2nd breakpoint
:6: direction of the 2nd breakpoint
:7: inserted nucleotides within the breakpoints
:8: type of the structural variation
:9: gene overlapping the 1st breakpoint
:10: gene overlapping the 2nd breakpoint
:11: exon overlapping the 1st breakpoint
:12: exon overlapping the 2nd breakpoint
:13: #read_pairs not supporting the variant (reference read pairs) for the tumor sample
:14: #read_pairs supporting the variant (variant read paris) for the tumor sample
:15: frequency of variant read pairs for the tumor sample
:16: #read_pairs not supporting the variant for the matched control sample
:17: #read_pairs supporting the variant for the matched control sample
:18: frequency of variant read pairs for the matched control sample
:19: p-value for the Fisher's exact text (on contingency table of (tumor v.s. matched control) and (reference v.s. variant read pairs)


BAM Summary 結果
-------

各カラムの説明
**************
`bam_filename`
 the name of the bam file stats have been collected for.
`sample`
 the name of the sample (taken from the bam file).
`platform`
 the name of the hardware platform (taken from the bam file).
`platform_unit`
 the platform unit (i.e. lane/run) of the hardware platform (taken from the bam file).
`library`
 the library name associated with the read group.	
`readgroup`
 the read group name.
`read_length_r1`
 the read length associated with read 1.
`read_length_r2`
 the read length associated with read 2.
`#_mapped_bases`
 the total number of mapped bases.
:#_mapped_bases_r1: the total number of mapped bases for all read 1s.
:#_mapped_bases_r2: the total number of mapped bases for all read 2s.
`#_divergent_bases`
 the total number of bases divergent from the reference.
:#_divergent_bases_r1: the total number of bases divergent from the reference for all read 1s.
:#_divergent_bases_r2: the total number of bases divergent from the reference for all read 2s.
`#_total_reads`
 the total number of reads.
`#_total_reads_r1`
 the total number of read 1s.
`#_total_reads_r2`
 the total number of read 2s.
`#_mapped_reads`
 the total number of unmapped reads.
:#_mapped_reads_r1: the total number of unmapped read 1s.
:#_mapped_reads_r2: the total number of unmapped read 2s.
`#_mapped_reads_properly_paired`
 the total number of properly paired reads.
`#_gc_bases_r1`
 the total number of G/C bases in read 1s.
`#_gc_bases_r2`
 the total number of G/C bases in read 2s.
`mean_insert_size`
 the mean insert size.
`insert_size_sd`
 the insert size standard deviation.
`median_insert_size`
 the median insert size.
`#_duplicate_reads`
 the total number of duplicate reads.
`total_depth`
 the total number of depth.
`bait_size`
 bait size.
`average_depth`
 the mean depth. (total_depth/bait_size)
`depth_stdev`
 the depth standard deviation.
`Nx_ratio`
 coverage N※以上のdepthを持つbaseの比率. (Nx/bait_size)
`Nx`
 N以上のdepthを持つbase総数
 

※ coverage Nは設定ファイル `dna_task_param.cfg` で指定した値です。:doc:`dna_config_info`

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

.. _annovar: http://annovar.openbioinformatics.org/en/latest/user-guide/download/
