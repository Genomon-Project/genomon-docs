========================================
DNA Configファイルについて
========================================

dna_genomon.cfg
------------------

 DNA解析パイプライン実行時に読込まれるファイルです．各ツールのフィルタリングの閾値などのパラメータを設定することができます．基本的にはこちらの値は最適化されているため、まずはデフォルトの最適化された値でGenomonを実行してみてください．

.. code-block:: cfg
    :linenos:

    #
    # Genomon pipeline configuration file
    #
    
    [REFERENCE]
    # prepared reference fasta file
    ref_fasta              = /home/w3varann/genomon_pipeline-2.2.0/database/GRCh37/GRCh37.fa
    interval_list          = /home/w3varann/genomon_pipeline-2.2.0/database/GRCh37/GRCh37_noScaffold_noDecoy.interval_list
    hg19_genome            = /home/w3varann/genomon_pipeline-2.2.0/tools/bedtools-2.24.0/genomes/human.hg19.genome
    gaptxt                 = /home/w3varann/genomon_pipeline-2.2.0/database/hg19.fa/gap.txt
    bait_file              = /home/w3varann/genomon_pipeline-2.2.0/database/bait/refGene.coding.exon.151207.bed
    simple_repeat_tabix_db = /home/w3varann/genomon_pipeline-2.2.0/database/tabix/simpleRepeat.bed.bgz
    HGVD_tabix_db          = /home/w3varann/genomon_pipeline-2.2.0/database/tabix/DBexome20131010.bed.gz
    
    [SOFTWARE]
    # prepared tools
    blat                   = /home/w3varann/genomon_pipeline-2.2.0/tools/blat_x86_64/blat
    bwa                    = /home/w3varann/genomon_pipeline-2.2.0/tools/bwa-0.7.8/bwa
    samtools               = /home/w3varann/genomon_pipeline-2.2.0/tools/samtools-1.2/samtools
    bedtools               = /home/w3varann/genomon_pipeline-2.2.0/tools/bedtools-2.24.0/bin/bedtools
    biobambam              = /home/w3varann/genomon_pipeline-2.2.0/tools/biobambam-0.0.191/bin
    PCAP                   = /home/w3varann/genomon_pipeline-2.2.0/tools/PCAP-core-dev.20150511
    genomon_sv             = /home/w3varann/genomon_pipeline-2.2.0/python2.7-packages/bin/GenomonSV
    mutfilter              = /home/w3varann/genomon_pipeline-2.2.0/python2.7-packages/bin/mutfilter
    ebfilter               = /home/w3varann/genomon_pipeline-2.2.0/python2.7-packages/bin/EBFilter
    fisher                 = /home/w3varann/genomon_pipeline-2.2.0/python2.7-packages/bin/fisher
    mutanno                = /home/w3varann/genomon_pipeline-2.2.0/python2.7-packages/bin/mutanno
    genomon_pa             = /home/w3varann/genomon_pipeline-2.2.0/python2.7-packages/bin/genomon_pa
    pa_plot                = /home/w3varann/genomon_pipeline-2.2.0/python2.7-packages/bin/pa_plot
    mutil                  = /home/w3varann/genomon_pipeline-2.2.0/python2.7-packages/bin/mutil
    
    # ANNOVAR needs to be installed individually
    annovar                = /your_annovar
    
    [ENV]
    PERL5LIB               = /home/w3varann/.local/lib/perl/lib:/home/w3varann/.local/lib/perl/lib/perl5:/home/w3varann/.local/lib/perl/lib/perl5/x86_64-linux-thread-multi
    PYTHONHOME             = /usr/local/package/python2.7/current
    PYTHONPATH             = /home/w3varann/genomon_pipeline-2.2.0/python2.7-packages/lib/python
    LD_LIBRARY_PATH        = /usr/local/package/python2.7/current/lib:/home/w3varann/genomon_pipeline-2.2.0/python2.7-packages/lib
    
    
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
    
    [qc_merge]
    qsub_option = -l s_vmem=1G,mem_req=1G
    
    ###########
    # mutation call
    [mutation_call]
    qsub_option = -l s_vmem=5.3G,mem_req=5.3G
    
    [fisher_mutation_call]
    # 変異ポジションのリード数が指定した数以下であれば候補の対象となりません,tumor normalともに指定した本数以上なければなりません
    min_depth = 8
    # mapping qualityが指定した値以下であればその情報は使用されません．
    map_quality = 20
    # base qualityが指定した値以下であればその情報は使用されません．
    base_quality = 15
    # tumorのallele比がこの値以下であれば候補の対象となりません．
    disease_min_allele_frequency = 0.02
    # normalのallele比がこの値以上であれば候補の対象となりません．
    control_max_allele_frequency = 0.1
    # fihser検定による結果の閾値です．
    fisher_thres_hold = 0.1
    # 変異アレルのリード数は二項分布でモデル化できますが、これをベイズ的にやろうとしてベータ分布を利用し、その結果の10% posterio quantileを閾値としています.
    post_10_q = 0.02
    # fisher_thres_holdとの違いは、こちらの値はmutation.result.txtからmutation.result.filt.txtというフィルタ済みファイルを生成する際に使用されます．
    fisher_pval-log10_thres = 1.0
    # post_10_qとの違いは、こちらの値はフィルタ済み結果ファイルを生成する際に使用されます．
    post_10_q_thres = 0.1
    
    [realignment_filter]
    # tumorの変異数が指定した値以上であれば、フィルタ済み結果ファイルに出力されます
    disease_min_mismatch=4
    # normalの変異数が指定した値以下であれば、フィルタ済み結果ファイルに出力されます
    control_max_mismatch=2
    # リードリアライメント時にはマルチアライメントしているのですが、1番目に良いスコアと2番目に良いスコアの差が指定した値以内であったら、そのリードを使用しないという設定です
    score_diff=5
    # リアライメントするときのリファレンスゲノムを作るときの設定ですwindow size(bases) + 変異position + window size(bases)のリファレンスゲノムを作っています．
    window_size=200
    # 対象の変異positionがこの値以上であればrealignment対象となりません．
    max_depth=5000
    # こちらの値はmutation.result.txtからmutation.result.filt.txtというフィルタ済みファイルを生成する際に使用されます．
    fisher_pval-log10_thres = 1.0
    # こちらの値はフィルタ済み結果ファイルを生成する際に使用されます．
    post_10_q_thres = 0.1
    
    [indel_filter]
    # indelをsearchするときの範囲をしていします search_length(bases) + 変異position + search_length(bases)の範囲で探しに行きます
    search_length=40
    # 探し出したindelが候補のポジションから指定した値のrange内にいればindelフィルタの対象とします
    neighbor=5
    # samtools mpileupをつかって、indelをサーチするのですが、mpileupのオプションである-qの値となります．deletionの場合はbasequalityは無視されます．
    base_quality=20
    #depthと書かれている場合は変異ポジションのリード数のthresholdになります．
    min_depth=8
    max_mismatch=100000
    max_allele_freq=1
    
    [breakpoint_filter]
    max_depth=1000
    # ソフトクリッピングの長さが指定した値以下であればその情報は使用されません．
    min_clip_size=20
    junc_num_thres=0
    # mapping qualityが指定した値以下であればその情報は使用されません．
    map_quality=10
    
    [eb_filter]
    # mapping qualityが指定した値以下であればその情報は使用されません．
    map_quality = 20
    # base qualityが指定した値以下であればその情報は使用されません．
    base_quality = 15
    # こちらの値はフィルタ済み結果ファイルを生成する際に使用されます．
    ebcall_pval-log10_thres = 4.0
    
    [annotation]
    # annovarを使用するにはこのflagをTrueにしてください．
    active_annovar_flag = False
    # annovarのオプションを変更することができます．
    table_annovar_params = -buildver hg19 -remove --otherinfo -protocol refGene,cytoBand,genomicSuperDups,esp6500siv2_all,1000g2010nov_all,1000g2014oct_all,1000g2014oct_afr,1000g2014oct_eas,1000g2014oct_eur,snp131,snp138,snp131NonFlagged,snp138NonFlagged,cosmic68wgs,cosmic70,clinvar_20150629,ljb26_all -operation g,r,r,f,f,f,f,f,f,f,f,f,f,f,f,f,f
    # HGVDを使用するにはこのflagをTrueにしてください．
    active_HGVD_flag = False
    
    [mutation_merge]
    qsub_option = -l s_vmem=2G,mem_req=2G
    
    ##########
    ## Genomon SV
    [genomon_sv]
    param_file = /home/w3varann/genomon_pipeline-2.2.0/database/GenomonSV/param.yaml
    
    [sv_parse]
    qsub_option = -l s_vmem=2G,mem_req=2G
    
    [sv_merge]
    qsub_option = -l s_vmem=2G,mem_req=2G
    
    [sv_filt]
    qsub_option = -l s_vmem=2G,mem_req=2G
    
    ##########
    ## Post Analysis
    [pa_plot]
    # paplotを使用しない場合はFalse
    enable = True
    # pairを設定していないサンプルをpaplotの対象から除く場合はFalse
    include_unpair = True
    # controlpanelを使用しないサンプルをpaplotの対象から除く場合はFalse
    include_unpanel = True
    title = Genomon
    remarks = Data used in this report were generated using below software.
    software = genomon_pipeline:Genomon-Pipeline, genomon_sv:GenomonSV, sv_utils:sv_utils, fisher:GenomonFisher, mutfilter:GenomonMutationFilter, ebfilter:EBFilter, mutanno:mutanno, mutil:mutil
    config_file = # the path to the paplot-0.2.8/paplot.cfg
    qsub_option = -l s_vmem=2G,mem_req=2G
    
    [post_analysis]
    # Genomon Post Analysisを使用しない場合はFalse
    enable = True
    config_file = # the path to the GenomonPostAnalysis-1.0.2/genomon_post_analysis.cfg
    qsub_option = -l s_vmem=2G,mem_req=2G

