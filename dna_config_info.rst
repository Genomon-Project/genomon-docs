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

    (省略)
