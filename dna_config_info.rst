DNA パイプライン設定ファイルについて
====================================

パイプライン設定ファイルはGenomon実行時に読込まれるファイルです．各ツールのパスやパラメータを設定することができます．

 .. note::
  HGCスパコンの場合，このファイルは ``/home/w3varann/genomon_pipeline-2.5.0/genomon_conf/`` にあります．

  :Exome解析用: dna_exome_genomon.cfg
  :WGS解析用:   dna_wgs_genomon.cfg
  :Target解析用: dna_target_genomon.cfg
  
  ANNOVARの設定が必要ですので，まずは :doc:`dna_quick_start` から始めてください．

.. code-block:: cfg
    :linenos:

    #
    # Genomon pipeline configuration file
    #

    [REFERENCE]
    # prepared reference fasta file
    ref_fasta                               = # the path to the GRCh37.fa
    interval_list                           = # the path to the GRCh37_noScaffold_noDecoy.interval_list
    genome_size                             = # the path to the bedtools-2.24.0/genomes/human.hg19.genome
    gaptxt                                  = # the path to the gap.txt
    bait_file                               = # the path to the refGene.coding.exon.151207.bed
    simple_repeat_tabix_db                  = # the path to the simpleRepeat.bed.bgz
    HGVD_2013_tabix_db                      = # the path to the DBexome20131010.bed.gz
    HGVD_2016_tabix_db                      = # the path to the DBexome20160412.bed.gz
    ExAC_tabix_db                           = # the path to the ExAC.r0.3.1.sites.vep.bed.gz
    hotspot_db                              = # the path to the GRCh37_hotspot_database_v20161219.txt

    [SOFTWARE]
    # prepared tools
    blat                                    = # the path to the blat_x86_64/blat
    bwa                                     = # the path to the bwa-0.7.8/bwa
    samtools                                = # the path to the samtools-1.2/samtools
    bedtools                                = # the path to the bedtools-2.24.0/bin/bedtools
    biobambam                               = # the path to the biobambam-0.0.191/bin
    bamstats                                = # the path to the PCAP-core-dev.20150511/bin/bam_stats.pl
    htslib                                  = # the path to the htslib-1.3
    r_scripts                               = # the path to the genomon_Rscripts-0.1.2
    genomon_sv                              = # the path to the bin/GenomonSV
    sv_utils                                = # the path to the bin/sv_utils
    mutfilter                               = # the path to the bin/mutfilter
    ebfilter                                = # the path to the bin/EBFilter
    fisher                                  = # the path to the bin/fisher
    mutanno                                 = # the path to the bin/mutanno
    genomon_qc                              = # the path to the bin/genomon_qc
    genomon_pa                              = # the path to the bin/genomon_pa
    paplot                                  = # the path to the bin/paplot
    mutil                                   = # the path to the bin/mutil
    hotspot                                 = # the path to the bin/hotspotCall

    # annovar needs to be installed individually
    annovar                                 = # the path to the annovar

    ######################################################################
    #
    # Analysis parameters
    #
    #   If not defined, default values are going to be used in the pipeline.
    #
    
    ##########
    # parameters for bam2fastq
    [bam2fastq]
    qsub_option = -l s_vmem=1G,mem_req=1G
    
    ##########
    # parameters for split fastq
    [split_fastq]
    qsub_option = -l s_vmem=1G,mem_req=1G
    split_fastq_line_number = 40000000
    fastq_filter = False
    
    ##########
    # parameters for bwa_mem
    [bwa_mem]
    qsub_option = -l s_vmem=10.6G,mem_req=10.6G
    bwa_params = -T 0 
    
    ##########
    ## BAM markduplicates
    [markduplicates]
    qsub_option = -l s_vmem=10.6G,mem_req=10.6G
    java_memory = 10.6G
    
    ##########
    # BAM file statistics
    [qc_bamstats]
    qsub_option = -l s_vmem=1G,mem_req=1G
    
    [qc_coverage]
    qsub_option = -l s_vmem=1G,mem_req=1G
    coverage    = 2,10,20,30,40,50,100
    wgs_flag = False
    wgs_incl_bed_width = 1000000
    wgs_i_bed_lines = 10000
    wgs_i_bed_width = 100
    samtools_params = -F 3072 -f 2
    
    [qc_merge]
    qsub_option = -l s_vmem=1G,mem_req=1G
    
    ###########
    # mutation call
    [mutation_call]
    qsub_option = -l s_vmem=5.3G,mem_req=5.3G
    
    [fisher_mutation_call]
    # pair_params: ペアリードに使用します．
    # single_params: シングルリードに使用します．
    #
    #      --min_depth: 変異ポジションのリード数が指定した数以下であれば候補の対象となりません．Tumor Normalともに指定した本数以上なければなりません．
    #      --base_quality: Base Qualityが指定した値以下であればその情報は使用されません．
    #      --min_variant_read: Tumorの変異を含んだリードの数がこの値以上でなければ候補の対象となりません．
    #      --min_allele_freq: Tumorのアレル比がこの値以下であれば候補の対象となりません．
    #      --max_allele_freq: Normalのアレル比がこの値以上であれば候補の対象となりません．
    #      --fisher_value: Fihser検定による結果の閾値です．
    #      --post_10_q: 変異アレルのリード数は二項分布でモデル化できますが，これをベイズ的にやろうとしてベータ分布を利用し，その結果の10% posterio quantileを閾値としています.
    #      --samtools_params: samtool mpileupで使用するのパラメータです．
    
    pair_params = --min_depth 8 --base_quality 15 --min_variant_read 4 --min_allele_freq 0.02 --max_allele_freq 0.1 --fisher_value 0.1 --samtools_params "-q 20 -BQ0 -d 10000000 --ff UNMAP,SECONDARY,QCFAIL,DUP"
    single_params = --min_depth 8 --base_quality 15 --min_variant_read 4 --min_allele_freq 0.02 --post_10_q 0.02 --samtools_params "-q 20 -BQ0 -d 10000000 --ff UNMAP,SECONDARY,QCFAIL,DUP"
    
    [realignment_filter]
    #      --score_difference: リードリアライメント時にはマルチアライメントしているのですが，1番目に良いスコアと2番目に良いスコアの差が指定した値以内であったら，そのリードを使用しないという設定です
    #      --window_size: リアライメントするときのリファレンスゲノムを作るときの設定ですwindow size(bases) + 変異サイズ + window size(bases)のリファレンスゲノムを作っています．
    #      --max_depth: 対象の変異positionがこの値以上のdepthであればリアライメントしません．
    #      --exclude_sam_flags: 指定された値を含むsam flagのリードは対象から除かれます。
    params = --score_difference 5 --window_size 200 --max_depth 5000 --exclude_sam_flags 3328
    
    [indel_filter]
    #      --search_length: indelを検索するときの範囲を指定します search_length(bases) + 変異サイズ + search_length(bases)の範囲で探しに行きます．
    #      --neighbor: 探し出したindelが候補のポジションから指定した値の範囲内にいればindelフィルタの対象とします．
    #      --min_depth: Depthと書かれている場合は変異ポジションのリード数の閾値になります．
    #      --min_mismatch: 指定された値以上のミスマッチ数であればその変異を出力しません．
    #      --af_thres: 指定された値以上のアレル比であればその変異を出力しません．
    #      --samtools_params: samtool mpileupのパラメータです．
    
    params = --search_length 40 --neighbor 5 --min_depth 8 --min_mismatch 100000 --af_thres 1 --samtools_params "-q 20 -BQ0 -d 10000000 --ff UNMAP,SECONDARY,QCFAIL,DUP"
    
    [breakpoint_filter]
    # --max_depth: 対象の変異positionがこの値以上のdepthであればBreakpoint Filterを行いません．
    # --min_clip_size: ソフトクリッピングの長さが指定した値以下であればその情報は使用されません．
    # --junc_num_thres: junctionの数が指定の値より小さければその変異を出力しません。
    # --map_quality: Mapping Qualityが指定した値以下であればその情報は使用されません．
    # --exclude_sam_flags:　指定された値を含むsam flagのリードは対象から除かれます。
    
    params = --max_depth 1000 --min_clip_size 20 --junc_num_thres 0 --mapq_thres 10 --exclude_sam_flags 3332
    
    [eb_filter]
    # mapping qualityが指定した値以下であればその情報は使用されません．
    map_quality = 20
    # base qualityが指定した値以下であればその情報は使用されません．
    base_quality = 15
    filter_flags = UNMAP,SECONDARY,QCFAIL,DUP
    
    [hotspot]
    # hotspot　callを使用するにはこのflagをTrueにしてください．
    active_hotspot_flag = True
    params = -t 0.1 -c 0.1 -R 0.1 -m 8.0 -S "-B -q 20 -Q2 -d 10000000" 
    
    [annotation]
    # annovarを使用するにはこのflagをTrueにしてください．
    active_annovar_flag = False
    annovar_buildver = hg19
    # annovarのオプションを変更することができます．
    table_annovar_params = -buildver hg19 -remove --otherinfo -protocol refGene,cytoBand,genomicSuperDups,esp6500siv2_all,1000g2010nov_all,1000g2014oct_all,1000g2014oct_afr,1000g2014oct_eas,1000g2014oct_eur,snp131,snp138,snp131NonFlagged,snp138NonFlagged,cosmic68wgs,cosmic70,clinvar_20150629,ljb26_all -operation g,r,r,f,f,f,f,f,f,f,f,f,f,f,f,f,f
    annovar_database = /your_annovar/humandb
    # Use of this HGVD database is subject to compliance with the terms of use.
    # Please refere to the site below:
    # http://www.genome.med.kyoto-u.ac.jp/SnpDB/about.html
    active_HGVD_2013_flag = False
    active_HGVD_2016_flag = False
    # Use of this ExAC database is subject to compliance with the terms of use.
    # Please refere to the site below:
    # http://exac.broadinstitute.org/faq
    active_ExAC_flag = False
    
    [mutation_merge]
    qsub_option = -l s_vmem=2G,mem_req=2G
    
    [mutation_util]
    # 
    pair_params = --fish_pval 1.0 --realign_pval 1.0 --eb_pval 4.0 --tcount 4 --ncount 2
    single_params = --post10q 0.1 --r_post10q 0.1 --count 4
    
    ##########
    ## Genomon SV
    
    [sv_parse]
    qsub_option = -l s_vmem=2G,mem_req=2G
    params =
    
    [sv_merge]
    qsub_option = -l s_vmem=2G,mem_req=2G
    params = 
    
    [sv_filt]
    qsub_option = -l s_vmem=2G,mem_req=2G
    params = --min_junc_num 2 --max_control_variant_read_pair 10 --min_overhang_size 30  
    annotation_dir = # the path to the GenomonSV-0.4.0beta/resource
    sv_utils_params = --min_tumor_allele_freq 0.07 --max_control_variant_read_pair 1 --control_depth_thres 10 --inversion_size_thres 1000 --remove_simple_repeat
    sv_utils_annotation_dir = # the path to the sv_utils-0.4.0beta/resource 
    
    ##########
    ## Post Analysis
    [paplot]
    # paplotを使用しない場合はFalse
    enable = True 
    qsub_option = -l s_vmem=2G,mem_req=2G
    # ペアを設定していないサンプルをpaplotの対象から除く場合はFalse
    include_unpair = True
    # コントロールパネルを使用しないサンプルをpaplotの対象から除く場合はFalse
    include_unpanel = True
    title = Genomon
    remarks = Data used in this report were generated using below software.
    software = genomon_pipeline:Genomon-Pipeline, genomon_sv:GenomonSV, sv_utils:sv_utils, fisher:GenomonFisher, mutfilter:GenomonMutationFilter, ebfilter:EBFilter, mutanno:mutanno, mutil:mutil, genomon_qc:GenomonQC
    
    config_file = # the path to the paplot-0.5.0/paplot.cfg
    
    [post_analysis]
    # Genomon Post Analysisを使用しない場合はFalse
    enable = True
    qsub_option = -l s_vmem=2G,mem_req=2G
    config_file = # the path to the GenomonPostAnalysis-1.0.2/genomon_post_analysis.cfg
    
    ############
    # pmsignature
    
    [pre_pmsignature]
    qsub_option = -l s_vmem=2G,mem_req=2G
    
    [pmsignature_full]
    # pmsignature (type=full) を実行しない場合はFalse
    enable = False
    qsub_option = -l s_vmem=2G,mem_req=2G
    signum_min = 2
    signum_max = 6
    trdirflag = F
    trialnum = 10
    
    [pmsignature_ind]
    # pmsignature (type=independent) を実行しない場合はFalse
    enable = True
    qsub_option = -l s_vmem=2G,mem_req=2G
    signum_min = 2
    signum_max = 6
    trdirflag = T
    trialnum = 10
    
    
