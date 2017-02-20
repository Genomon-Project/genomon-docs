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

    (省略)
