RNA パイプライン設定ファイルについて
====================================

RNA解析パイプライン実行時に読込まれるファイルです．各ツールのフィルタリングの閾値などのパラメータを設定することができます．基本的にはこちらの値は最適化されているため，まずはデフォルトの最適化された値でGenomonを実行してみてください．

.. code-block:: cfg
    :linenos:
    
    #
    # Genomon pipeline configuration file
    #
    
    [REFERENCE]
    # prepared reference fasta file
    star_genome                 = # the path to the GRCh37.STAR-STAR_2.4.0k

    [SOFTWARE]
    # prepared tools
    samtools                    = # the path to the samtools-1.2/samtools
    tophat2                     = # the path to the tophat-2.0.14.Linux_x86_64/tophat2
    STAR                        = # the path to the STAR-STAR_2.4.0k/bin/Linux_x86_64/STAR
    STAR-Fusion                 = # the path to the STAR-Fusion-master/STAR-Fusion
    fusionfusion                = # the path to the bin/fusionfusion

    [ENV]
    PERL5LIB                    = # the path to the perl module
    PYTHONHOME                  = # the path to the python home
    PYTHONPATH                  = # the path to the python path
    LD_LIBRARY_PATH             = # the path to the python library

    
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
    
    
    
