RNA パイプライン設定ファイルについて
====================================

RNA解析パイプライン実行時に読込まれるファイルです．各ツールのフィルタリングの閾値などのパラメータを設定することができます．

 .. note::
  HGCスパコンの場合，このファイルは ``/home/w3varann/genomon_pipeline-2.5.2/genomon_conf/`` にあります．

  :rna解析用: rna_genomon.cfg


解析ツールのパス設定
-------------------------

| 解析に使用するリファレンスファイル ([REFERENCE] セクション) やソフトウェア ([SOFTWARE] セクション) のパスをパイプライン設定ファイルに記入します．
| 各種ソフトウェアのインストールについは :doc:`install` を参照してください．

.. code-block:: cfg

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
    

アライメント
------------------

| ここではアライメント処理に関するオプションについて解説します．
| 
| [bam_tofastq] もしくは [fastq] でシーケンスファイルを指定したとき，使用します．
| [bam_import] ではアライメントを行いませんので，このオプションは使用しません．

.. note::

  **共通**
  
  | ``qsub_option`` はジョブ投入時のオプションです．
  | メモリ超過エラー発生時や処理時間が長すぎるため特定のキューに投入したいとき等，適宜調整してください．

.. code-block:: cfg

    ##########
    # bamをfastqに変換するジョブの設定です
    # [bam_tofastq] でシーケンスファイルを指定したときのみ，使用します．
    [bam2fastq]
    qsub_option = -l s_vmem=1G,mem_req=1G
    
    ##########
    # Genomonでは STAR にてアライメントを行っており，
    # Genomonが次のコマンドの実行時、{star_params}に設定するオプションを指定できます
    # STAR に関する解説はSTARドキュメントを別途参照してください．
    # /path/to/star --genomeDir $star_genome \
    # --readFilesIn $fastq1 $fastq2 \
    # --outFileNamePrefix $out_prefix \
    # {star_params} 
    [star_align]
    qsub_option = -pe def_slot 6 -l s_vmem=5.3G,mem_req=5.3G
    star_params = --runThreadN 6 --outSAMstrandField intronMotif --outSAMunmapped Within --alignMatesGapMax 500000 --alignIntronMax 500000 --alignSJstitchMismatchNmax -1 -1 -1 -1 --outSJfilterDistToOtherSJmin 0 0 0 0 --outSJfilterOverhangMin 12 12 12 12 --outSJfilterCountUniqueMin 1 1 1 1 --outSJfilterCountTotalMin 1 1 1 1 --chimSegmentMin 12 --chimJunctionOverhangMin 12 --outSAMtype BAM Unsorted

    # Genomonでは STARでアライメントしたbamに対して，"samtools sort" を使用してソートしており，
    # Genomonが次のコマンドの実行時、{star_params}に設定するオプションを指定できます.
    # "samtools sort" に関する解説はsamtoolsドキュメントを別途参照してください．
    # /path/to/samtools sort -T $Aligned.sortedByCoord.out \
    # {samtools_sort_params} $Aligned.out.bam \
    # -O bam > $Aligned.sortedByCoord.out.bam 
    samtools_sort_params = -@ 6 -m 3G

    
融合遺伝子
--------------

| ここでは融合遺伝子に関するオプションについて解説します．
| [fusionfusion] で設定したサンプルに対して解析を行います．

.. code-block:: cfg

    # 1) Count supporting read pairs for each chimera junction
    [fusion_count_control]
    qsub_option = -l s_vmem=5.3G,mem_req=5.3G
    params =
    
    # 2) Merge chimeric junction count file
    [fusion_merge_control]
    qsub_option = -l s_vmem=5.3G,mem_req=5.3G
    params =
    
    3)  融合遺伝子を検出します．
    [fusionfusion]
    qsub_option = -l s_vmem=5.3G,mem_req=5.3G
    params = --grc
    
    # Genomonおすすめフィルタ
    # 検出された融合遺伝子に対して，よく使用されるフィルタリングをあらかじめ実施します
    # {sample}.fusion.fusion.result.txt から {sample}.fusion.fusion.result.filt.txt を作成します
    filt_params = --filter_same_gene --grc

発現量
--------------

| ここでは発現量に関するオプションについて解説します．
| [expression] で設定したサンプルに対して解析を行います．

.. code-block:: cfg

    [genomon_expression]
    qsub_option = -l s_vmem=5.3G,mem_req=5.3G
    params = --grc

Intron Retention
------------------------

| ここではIntron Retentionに関するオプションについて解説します．
| [intron_retention] で設定したサンプルに対して解析を行います．

.. code-block:: cfg

    [intron_retention]
    qsub_option = -l s_vmem=5.3G,mem_req=5.3G
    params = --grc

Post Analysis
----------------------------

| ここでは STAR, fusionfusion の解析結果をレポート出力するPost Analysisという機能のオプションについて解説します．
|
| Post Analysisによるマージされた結果が必要ですので，レポート出力するには [post_analysis] と [paplot] 両方が有効(enable = True)にする必要があります．

.. code-block:: cfg

    # GenomonではGenomonPostAnalysisというソフトウェアを用いて，サンプル毎の結果ファイルを1つのファイルにマージしています
    [post_analysis]
    qsub_option = -l s_vmem=2G,mem_req=2G

    # Genomon Post Analysisを使用しない場合はFalse
    enable = True
    
    # post analysisの設定ファイルです．インストールした場所にありますので，パスを設定してください
    config_file = # the path to the GenomonPostAnalysis-1.0.2/genomon_post_analysis.cfg
    
    # paplotというソフトウェアを用いてレポートを作成します
    [paplot]
    qsub_option = -l s_vmem=2G,mem_req=2G
    
    # paplotを使用しない場合はFalse
    enable = True
    
    # ペアを設定していないサンプルをpaplotの対象から除く場合はFalse
    include_unpair = True
    # コントロールパネルを使用しないサンプルをpaplotの対象から除く場合はFalse
    include_unpanel = True
    
    # paplotの設定ファイルです．
    # paplotをインストールした場所/config_template/ 配下にGenomon用の設定ファイルがありますので，パスを設定してください
    config_file = # the path to the paplot-0.5.0/paplot.cfg
    
    # index.htmlの設定です．通常変更する必要はありません
    title = Genomon_RNA
    remarks = Data used in this report were generated using below software.
    software = genomon_pipeline:Genomon-Pipeline, STAR:STAR, fusionfusion:fusionfusion
