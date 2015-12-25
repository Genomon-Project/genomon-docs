========================================
Configファイルについて
========================================

sample.cfg
-----------

 | 入力ファイルの設定や、tumor, normalのサンプルのペア情報を記載します

  くわしい使い方は :doc:`sample_csv` に書かれています.

genomon.cfg
-----------

 | 使用するソフトウェアやデータベースを管理しているファイルです。


.. code-block:: cfg
    :linenos:

    #
    # Genomon pipeline configuration file
    #

    [REFERENCE]
    # prepared reference fasta file
    ref_fasta                               = /home/w3varann/genomon_pipeline-2.0.2/database/GRCh37/GRCh37.fa
    genome_size                             = /home/w3varann/genomon_pipeline-2.0.2/database/GRCh37/GRCh37.fa.chrom.sizes
    interval_list                           = /home/w3varann/genomon_pipeline-2.0.2/database/GRCh37/GRCh37_noScaffold_noDecoy.interval_list
    star_genome                             = /home/w3varann/genomon_pipeline-2.0.2/database/GRCh37.STAR-STAR_2.4.0k
    hg19_genome                             = /home/w3varann/genomon_pipeline-2.0.2/tools/bedtools-2.24.0/genomes/human.hg19.genome
    gaptxt                                  = /home/w3varann/genomon_pipeline-2.0.2/database/hg19.fa/gap.txt
    bait_file                               = /home/w3varann/genomon_pipeline-2.0.2/database/bait/refGene.coding.exon.151207.bed
    simple_repeat_tabix_db                  = /home/w3varann/genomon_pipeline-2.0.2/database/tabix/simpleRepeat.bed.bgz
    HGVD_tabix_db                           = /home/w3varann/genomon_pipeline-2.0.2/database/tabix/DBexome20131010.bed.gz

    [SOFTWARE]
    # prepared tools
    python                                  = /usr/local/package/python2.7/current/bin/python
    R                                       = /usr/local/package/r/current3_gcc/bin/R
    blat                                    = /home/w3varann/genomon_pipeline-2.0.2/tools/blat_x86_64/blat
    bwa                                     = /home/w3varann/genomon_pipeline-2.0.2/tools/bwa-0.7.8/bwa
    samtools                                = /home/w3varann/genomon_pipeline-2.0.2/tools/samtools-1.2/samtools
    bedtools                                = /home/w3varann/genomon_pipeline-2.0.2/tools/bedtools-2.24.0/bin/bedtools
    biobambam                               = /home/w3varann/genomon_pipeline-2.0.2/tools/biobambam-0.0.191/bin
    PCAP                                    = /home/w3varann/genomon_pipeline-2.0.2/tools/PCAP-core-dev.20150511
    tophat2                                 = /home/w3varann/genomon_pipeline-2.0.2/tools/tophat-2.0.14.Linux_x86_64/tophat2
    STAR                                    = /home/w3varann/genomon_pipeline-2.0.2/tools/STAR-STAR_2.4.0k/bin/Linux_x86_64/STAR
    STAR-Fusion                             = /home/w3varann/genomon_pipeline-2.0.2/tools/STAR-Fusion-master/STAR-Fusion
    genomon_sv                              = /home/w3varann/genomon_pipeline-2.0.2/python2.7-packages/bin/GenomonSV
    fusionfusion                            = /home/w3varann/genomon_pipeline-2.0.2/python2.7-packages/bin/fusionfusion
    mutfilter                               = /home/w3varann/genomon_pipeline-2.0.2/python2.7-packages/bin/mutfilter
    ebfilter                                = /home/w3varann/genomon_pipeline-2.0.2/python2.7-packages/bin/EBFilter
    fisher                                  = /home/w3varann/genomon_pipeline-2.0.2/python2.7-packages/bin/fisher
    mutanno                                 = /home/w3varann/genomon_pipeline-2.0.2/python2.7-packages/bin/mutanno


    # annovar needs to be installed individually
    annovar                                 = /home/your_directory

    [ENV]
    # biobambam needs libmaus library. libmaus_PATH is going to be added in LD_LIBRARY_PATH.
    libmaus_PATH                            = /home/w3varann/tools/libmaus/lib
    # drmaa needs libdrmaa library. drmaa_PATH is goint to be set in DRMAA_LIBRARY_PATH.
    drmaa_PATH                              = /geadmin/N1GE/lib/lx-amd64/libdrmaa.so.1.0
    # STAR-Fusion needs to set perl lib path.
    PERL5LIB                                = /home/w3varann/.local/lib/perl/lib:/home/w3varann/.local/lib/perl/lib/perl5:/home/w3varann/.local/lib/perl/lib/perl5/x86_64-linux-thread-multi

    R_LIBS                                  = /home/w3varann/.R

    PYTHONHOME                              = /usr/local/package/python2.7/current
    PYTHONPATH                              = /home/w3varann/genomon_pipeline-2.0.2/python2.7-packages/lib/python

    # Add LD_LIBRARY_PATH to the current LD_LIBRARY_PATH
    #add_LD_LIBRARY_PATH			= /usr/local/package/python2.7/current/lib:/home/w3varann/.local/lib

    # Change LD_LIBRARY_PATH to the following LD_LIBRARY_PATH
    LD_LIBRARY_PATH                         = /usr/local/package/python2.7/current/lib:/home/w3varann/genomon_pipeline-2.0.2/python2.7-packages/lib

dna_task_param.cfg
------------------

 | DNAパイプライン実行時に使用されるファイルです。
 | 各ツールオプションのパラメータを設定することができます。
 | またパイプラインの各Taskのqsubで使用するメモリ量を設定できます。

.. code-block:: cfg
    :linenos:

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
    [bam_stats]
    qsub_option = -l s_vmem=1G,mem_req=1G

    [coverage]
    qsub_option = -l s_vmem=1G,mem_req=1G
    coverage    = 2,10,20,30,40,50,100
    wgs_flag = False
    wgs_incl_bed_width = 1000000
    wgs_i_bed_lines = 10000
    wgs_i_bed_width = 100

    [merge]
    qsub_option = -l s_vmem=1G,mem_req=1G

    ###########
    # mutation call
    [mutation_call]
    qsub_option = -l s_vmem=5.3G,mem_req=5.3G

    [fisher_mutation_call]
    min_depth = 8
    map_quality = 20
    base_quality = 15
    disease_min_allele_frequency = 0.02
    control_max_allele_frequency = 0.1
    fisher_thres_hold = 0.1
    post_10_q = 0.02

    [realignment_filter]
    disease_min_mismatch=0
    control_max_mismatch=100000
    score_diff=5
    window_size=200
    max_depth=5000

    [indel_filter]
    search_length=40
    neighbor=5
    base_quality=20
    min_depth=8
    max_mismatch=100000
    max_allele_freq=1

    [breakpoint_filter]
    max_depth=1000
    min_clip_size=20
    junc_num_thres=0
    map_quality=10

    [eb_filter]
    map_quality = 20
    base_quality = 15

    [annotation]
    active_annovar_flag = False
    table_annovar_params = -buildver hg19 -remove --otherinfo -protocol refGene,cytoBand,genomicSuperDups,esp6500siv2_all,1000g2010nov_all,1000g2014oct_all,1000g2014oct_afr,1000g2014oct_eas,1000g2014oct_eur,snp131,snp138,snp131NonFlagged,snp138NonFlagged,cosmic68wgs,cosmic70,clinvar_20150629,ljb26_all -operation g,r,r,f,f,f,f,f,f,f,f,f,f,f,f,f,f
    active_HGVD_flag = False

    [mutation_merge]
    qsub_option = -l s_vmem=2G,mem_req=2G

    ##########
    ## Genomon SV
    [genomon_sv]
    param_file = /home/w3varann/database/GenomonSV-0.1.0/param.yaml

    [sv_parse]
    qsub_option = -l s_vmem=2G,mem_req=2G

    [sv_merge]
    qsub_option = -l s_vmem=2G,mem_req=2G

    [sv_filt]
    qsub_option = -l s_vmem=2G,mem_req=2G



rna_task_param.cfg
------------------

 | RNAパイプライン実行時に使用されるファイルです。
 | 使用方法としてはdna_task_param.cfgと同じ

.. code-block:: cfg
    :linenos:
    
    ######################################################################
    #
    # Analysis parameters
    #
    #   If not defined, default values are going to be used in the pipeline.
    #

    ##########
    # parameters for bam2fastq
    [bam2fastq]
    qsub_option = -l ljob,s_vmem=1G,mem_req=1G

    ##########
    # parameters for star alignment 
    [star_align]
    qsub_option = -pe def_slot 6 -l s_vmem=5.3G,mem_req=5.3G
    star_params = --runThreadN 6 --outSAMstrandField intronMotif --outSAMunmapped Within --alignMatesGapMax 500000 --alignIntronMax 500000 --outSJfilterOverhangMin 12 12 12 12 --outSJfilterCountUniqueMin 1 1 1 1 --outSJfilterCountTotalMin 1 1 1 1 --chimSegmentMin 12 --chimJunctionOverhangMin 12 --outSAMtype BAM Unsorted
    samtools_sort_params = -@ 6 -m 3G

    ##########
    # parameters for fusionfusion
    [fusionfusion]
    qsub_option = -l ljob,s_vmem=5.3G,mem_req=5.3G
    param_file = /home/w3varann/database/fusionfusion_hg19/param.cfg