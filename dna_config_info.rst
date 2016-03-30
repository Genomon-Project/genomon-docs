========================================
DNA Configファイルについて
========================================

dna_task_param.cfg
------------------

 | DNAパイプライン実行時に使用されるファイルです。
 | 各ツールオプションのパラメータを設定することができます。
 | またパイプラインの各Taskのqsubで使用するメモリ量を設定できます。

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
   
   # annovar needs to be installed individually
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
   [bam_stats]
   qsub_option = -l s_vmem=1G,mem_req=1G
   
   [coverage]
   qsub_option = -l s_vmem=1G,mem_req=1G
   coverage    = 2,10,20,30,40,50,100
   wgs_flag = False
   wgs_incl_bed_width = 1000000
   wgs_i_bed_lines = 10000
   wgs_i_bed_width = 100
   
   [summary]
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
   fisher_pval-log10_thres = 1.0
   post_10_q_thres = 0.1
   
   [realignment_filter]
   disease_min_mismatch=4
   control_max_mismatch=2
   score_diff=5
   window_size=200
   max_depth=5000
   fisher_pval-log10_thres = 1.0
   post_10_q_thres = 0.1
   
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
   ebcall_pval-log10_thres = 4.0
   
   [annotation]
   active_annovar_flag = False
   table_annovar_params = -buildver hg19 -remove --otherinfo -protocol refGene,cytoBand,genomicSuperDups,esp6500siv2_all,1000g2010nov_all,1000g2014oct_all,1000g2014oct_afr,1000g2014oct_eas,1000g2014oct_eur,snp131,snp138,snp131NonFlagged,snp138NonFlagged,cosmic68wgs,cosmic70,clinvar_20150629,ljb26_all -operation g,r,r,f,f,f,f,f,f,f,f,f,f,f,f,f,f
   active_HGVD_flag = False
   
   [mutation_merge]
   qsub_option = -l s_vmem=2G,mem_req=2G
   
   ##########
   ## Genomon SV
   [genomon_sv]
   param_file = /home/w3varann/genomon_pipeline-2.1.0/database/GenomonSV/param.yaml
   
   [sv_parse]
   qsub_option = -l s_vmem=2G,mem_req=2G
   
   [sv_merge]
   qsub_option = -l s_vmem=2G,mem_req=2G
   
   [sv_filt]
   qsub_option = -l s_vmem=2G,mem_req=2G
   
   ##########
   ## Post Analysis
   [pa_plot]
   enable = True
   title = Genomon
   config_file = /home/w3varann/genomon_pipeline-2.1.0/tools/paplot-0.2.7/paplot.cfg
   qsub_option = -l s_vmem=2G,mem_req=2G
   
   [post_analysis]
   enable = True
   config_file = /home/w3varann/genomon_pipeline-2.1.0/tools/GenomonPostAnalysis-1.0.1/genomon_post_analysis.cfg
   qsub_option = -l s_vmem=2G,mem_req=2G
