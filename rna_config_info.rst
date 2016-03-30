========================================
RNA Configファイルについて
========================================

rna_genomon.cfg
------------------

 | RNAパイプライン実行時に使用されるファイルです。
 | 各ツールオプションのパラメータを設定することができます。
 | またパイプラインの各Taskのqsubで使用するメモリ量を設定できます。

.. code-block:: cfg
    :linenos:
    
    #
    # Genomon pipeline configuration file
    #
    
    [REFERENCE]
    # prepared reference fasta file
    star_genome                             = /home/w3varann/genomon_pipeline-2.2.0/database/GRCh37.STAR-STAR_2.4.0k
    
    [SOFTWARE]
    # prepared tools
    samtools                                = /home/w3varann/genomon_pipeline-2.2.0/tools/samtools-1.2/samtools
    tophat2                                 = /home/w3varann/genomon_pipeline-2.2.0/tools/tophat-2.0.14.Linux_x86_64/tophat2
    STAR                                    = /home/w3varann/genomon_pipeline-2.2.0/tools/STAR-STAR_2.4.0k/bin/Linux_x86_64/STAR
    STAR-Fusion                             = /home/w3varann/genomon_pipeline-2.2.0/tools/STAR-Fusion-master/STAR-Fusion
    fusionfusion                            = /home/w3varann/genomon_pipeline-2.2.0/python2.7-packages/bin/fusionfusion
    
    # annovar needs to be installed individually
    annovar                                 = /your_annovar
    
    [ENV]
    PERL5LIB                                = /home/w3varann/.local/lib/perl/lib:/home/w3varann/.local/lib/perl/lib/perl5:/home/w3varann/.local/lib/perl/lib/perl5/x86_64-linux-thread-multi
    PYTHONHOME                              = /usr/local/package/python2.7/current
    PYTHONPATH                              = /home/w3varann/genomon_pipeline-2.2.0/python2.7-packages/lib/python
    LD_LIBRARY_PATH                         = /usr/local/package/python2.7/current/lib:/home/w3varann/genomon_pipeline-2.2.0/python2.7-packages/lib
    
    
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
