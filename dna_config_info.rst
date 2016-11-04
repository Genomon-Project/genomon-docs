DNA パイプライン設定ファイルについて
====================================

パイプライン設定ファイルはGenomon実行時に読込まれるファイルです．各ツールのパスやパラメータを設定することができます．

 .. note::
  HGCスパコンの場合，このファイルは ``/home/w3varann/genomon_pipeline-2.5.0/genomon_conf/`` にあります．

  :exome解析用: dna_exome_genomon.cfg
  :wgs解析用:   dna_wgs_genomon.cfg

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

    [SOFTWARE]
    # prepared tools
    blat                                    = # the path to the blat_x86_64/blat
    bwa                                     = # the path to the bwa-0.7.8/bwa
    samtools                                = # the path to the samtools-1.2/samtools
    bedtools                                = # the path to the bedtools-2.24.0/bin/bedtools
    biobambam                               = # the path to the biobambam-0.0.191/bin
    bamstats                                = # the path to the PCAP-core-dev.20150511/bin/bam_stats.pl
    htslib                                  = # the path to the htslib-1.3
    r_scripts                               = # the path to the genomon_Rscripts-0.1.0
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

    # annovar needs to be installed individually
    annovar                                 = # the path to the annovar

    [ENV]
    PERL5LIB                                = # the path to the perl module
    PYTHONHOME                              = # the path to the python home
    PYTHONPATH                              = # the path to the python path
    LD_LIBRARY_PATH                         = # the path to the python library
    R_PATH                                  = # the path to the R bin
    R_LD_LIBRARY_PATH                       = # the path to the R library
    R_LIBS                                  = # the path to the R packages

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
    pair_params = --min_depth 8 --base_quality 15 --min_variant_read 4 --min_allele_freq 0.02 --max_allele_freq 0.1 --fisher_value 0.1 --samtools_params "-q 20 -BQ0 -d 10000000 --ff UNMAP,SECONDARY,QCFAIL,DUP"
    single_params = --min_depth 8 --base_quality 15 --min_variant_read 4 --min_allele_freq 0.02 --post_10_q 0.02 --samtools_params "-q 20 -BQ0 -d 10000000 --ff UNMAP,SECONDARY,QCFAIL,DUP"

    [realignment_filter]
    params = --score_difference 5 --window_size 200 --max_depth 5000 --exclude_sam_flags 3328

    [indel_filter]
    params = --search_length 40 --neighbor 5 --min_depth 8 --min_mismatch 100000 --af_thres 1 --samtools_params "-q 20 -BQ0 -d 10000000 --ff UNMAP,SECONDARY,QCFAIL,DUP"

    [breakpoint_filter]
    params = --max_depth 1000 --min_clip_size 20 --junc_num_thres 0 --mapq_thres 10 --exclude_sam_flags 3332

    [eb_filter]
    map_quality = 20
    base_quality = 15
    filter_flags = UNMAP,SECONDARY,QCFAIL,DUP

    [annotation]
    active_annovar_flag = False
    annovar_buildver = hg19
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
    enable = True 
    qsub_option = -l s_vmem=2G,mem_req=2G
    include_unpair = True
    include_unpanel = True
    title = Genomon
    remarks = Data used in this report were generated using below software.
    software = genomon_pipeline:Genomon-Pipeline, genomon_sv:GenomonSV, sv_utils:sv_utils, fisher:GenomonFisher, mutfilter:GenomonMutationFilter, ebfilter:EBFilter, mutanno:mutanno, mutil:mutil, genomon_qc:Geno  monQC

    config_file = # the path to the paplot-0.5.0/paplot.cfg

    [post_analysis]
    enable = True
    qsub_option = -l s_vmem=2G,mem_req=2G
    config_file = # the path to the GenomonPostAnalysis-1.0.2/genomon_post_analysis.cfg

    ############
    # pmsignature

    [pre_pmsignature]
    qsub_option = -l s_vmem=2G,mem_req=2G

    [pmsignature_full]
    enable = False
    qsub_option = -l s_vmem=10.6G,mem_req=10.6G
    signum_min = 2
    signum_max = 6
    trdirflag = F
    trialnum = 10

    [pmsignature_ind]
    enable = True
    qsub_option = -l s_vmem=10.6G,mem_req=10.6G
    signum_min = 2
    signum_max = 6
    trdirflag = T
    trialnum = 10



