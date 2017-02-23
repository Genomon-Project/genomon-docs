RNA パイプライン設定ファイルについて
====================================

RNA解析パイプライン実行時に読込まれるファイルです．各ツールのフィルタリングの閾値などのパラメータを設定することができます．

 .. note::
  HGCスパコンの場合，このファイルは ``/home/w3varann/genomon_pipeline-2.5.0/genomon_conf/`` にあります．

  :rna解析用: rna_genomon.cfg

.. code-block:: cfg
    :linenos:
    
    #
    # Genomon pipeline configuration file
    #

    [REFERENCE]
    # prepared reference fasta file
    star_genome                             = # the path to the GRCh37.STAR-2.5.2a
    ref_fasta                               = # the path to the reference genome

    [SOFTWARE]
    # prepared tools
    samtools                                = # the path to the samtools-1.2/samtools
    tophat2                                 = # the path to the tophat-2.0.14.Linux_x86_64/tophat2
    STAR                                    = # the path to the STAR-2.5.2a/bin/Linux_x86_64_static/STAR
    STAR-Fusion                             = # the path to the STAR-Fusion-master/STAR-Fusion
    bedtools                                = # the path to the bedtools-2.24.0/bin/bedtools
    biobambam                               = # the path to the biobambam-0.0.191/bin
    blat                                    = # the path to the blat_x86_64/blat
    htslib                                  = # the path to the htslib-1.3
    fusionfusion                            = # the path to the bin/fusionfusion
    fusion_utils                            = # the path to the bin/fusion_utils
    chimera_utils                           = # the path to the bin/chimera_utils
    intron_retention_utils                  = # the path to the bin/intron_retention_utils
    genomon_expression                      = # the path to the bin/genomon_expression
    genomon_pa                              = # the path to the bin/genomon_pa
    paplot                                  = # the path to the bin/paplot
    
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
    # parameters for star alignment
    [star_align]
    qsub_option = -pe def_slot 6 -l s_vmem=5.3G,mem_req=5.3G
    star_params = --runThreadN 6 --outSAMstrandField intronMotif --outSAMunmapped Within --alignMatesGapMax 500000 --alignIntronMax 500000 --alignSJstitchMismatchNmax -1 -1 -1 -1 --outSJfilterDistToOtherSJmin 0 0 0 0 --outSJfilterOverhangMin 12 12 12 12 --outSJfilterCountUniqueMin 1 1 1 1 --outSJfilterCountTotalMin 1 1 1 1 --chimSegmentMin 12 --chimJunctionOverhangMin 12 --outSAMtype BAM Unsorted
    samtools_sort_params = -@ 6 -m 3G
    
    ##########
    # parameters for fusionfusion
    [fusion_count_control]
    qsub_option = -l s_vmem=5.3G,mem_req=5.3G
    params =
    
    [fusion_merge_control]
    qsub_option = -l s_vmem=5.3G,mem_req=5.3G
    params =
    
    [fusionfusion]
    qsub_option = -l s_vmem=5.3G,mem_req=5.3G
    params = --grc
    filt_params = --filter_same_gene --grc
    
    [genomon_expression]
    qsub_option = -l s_vmem=5.3G,mem_req=5.3G
    params = --grc
    
    [intron_retention]
    qsub_option = -l s_vmem=5.3G,mem_req=5.3G
    params = --grc
    
    ##########
    ## Post Analysis
    [paplot]
    # paplotを使用しない場合はFalse
    enable = True
    # ペアを設定していないサンプルをpaplotの対象から除く場合はFalse
    include_unpair = True
    # コントロールパネルを使用しないサンプルをpaplotの対象から除く場合はFalse
    include_unpanel = True
    title = Genomon_RNA
    remarks = Data used in this report were generated using below software.
    software = genomon_pipeline:Genomon-Pipeline, STAR:STAR, fusionfusion:fusionfusion
    
    config_file = # the path to the paplot-0.5.0/paplot.cfg
    qsub_option = -l s_vmem=2G,mem_req=2G
    
    [post_analysis]
    # Genomon Post Analysisを使用しない場合はFalse
    enable = True
    config_file = # the path to the GenomonPostAnalysis-1.2.0/genomon_post_analysis.cfg
    qsub_option = -l s_vmem=2G,mem_req=2G
    
