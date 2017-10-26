DNA パイプライン設定ファイルについて
====================================

パイプライン設定ファイルはGenomon実行時に読込まれるファイルです．各ツールのパスやパラメータを設定することができます．

 .. note::
  HGCスパコンの場合，このファイルは ``/home/w3varann/genomon_pipeline-2.5.3/genomon_conf/`` にあります．

  :Exome解析用: dna_exome_genomon.cfg
  :WGS解析用:   dna_wgs_genomon.cfg
  :Target解析用: dna_target_genomon.cfg
  
  ANNOVARの設定が必要ですので，まずは :doc:`dna_quick_start` から始めてください．

解析ツールのパス設定
-------------------------

| 解析に使用するリファレンスファイル ([REFERENCE] セクション) やソフトウェア ([SOFTWARE] セクション) のパスをパイプライン設定ファイルに記入します．
| 各種ソフトウェアのインストールについは :doc:`install` を参照してください．

.. code-block:: cfg

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

annotation
------------

| 変異コールで見つけた変異に対して，遺伝子名や変異タイプなどの情報を追加する機能です．（アノテーションといいます）
| GenomonではANNOVARを採用していますが，ライセンスの都合上あらかじめインストールしたものを使用していただくことができないため，各自でインストールする必要があります．
| この設定はなくてもGenomonによる解析は可能ですが，設定することをお勧めしています．

.. code-block:: cfg

    [annotation]
    # annovarを使用するにはこのflagをTrueにしてください．
    active_annovar_flag = False
    annovar_buildver = hg19
    # annovarのオプションを変更することができます．
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
 　　qsub_option = -q '!mjobs_rerun.q' -l s_vmem=2G,mem_req=2G
   
    # Genomonが次のコマンドの実行時、{params}に設定するオプションを指定できます
    # /path/to/bamtofastq {params} \
    # filename=$in.bam F=$out1.fastq F2=$out2.fastq　\
    # T=$temp S=$single O=$unmatched_pair1 O2=unmatched_pair2
 　　params = collate=1 exclude=QCFAIL,SECONDARY,SUPPLEMENTARY tryoq=0
    
    ##########
    # Genomonでは，入力されたfastqを適切な大きさに分割してからアライメントを並行で行います．
    [split_fastq]
    qsub_option = -q '!mjobs_rerun.q' -l s_vmem=2G,mem_req=2G
    
    # ファイルを分割する大きさです．fastqファイルの行数を示していますので，4の倍数である必要があります
    split_fastq_line_number = 40000000
    
    # fastqのフィルタリングを行いたい場合はTrueに設定します
    # Trueに設定すると，次の正規表現に該当しないリードは削除されます
    # grep -A 3 '^@.* [^:]*:N:[^:]*:' 
    fastq_filter = False
    
    ##########
    # アライメントのオプションです
    [bwa_mem]
    qsub_option = -q '!mjobs_rerun.q' -l s_vmem=10.6G,mem_req=10.6G

    # Genomonが次のコマンドの実行時、{bwa_params}に設定するオプションを指定できます
    # /path/to/bwa mem {bwa_params} $ref_genome \
    # $fastq1 $fastq2 > $output.sam
 　　 bwa_params = -T 0 
    
    ##########
    # アライメントののち，重複リードに対して重複フラグを設定します
    [markduplicates]
    qsub_option = -q '!mjobs_rerun.q' -l s_vmem=10.6G,mem_req=10.6G
    java_memory = 10.6G


変異コール
--------------

| ここでは変異コールに関するオプションについて解説します．
| [mutation_call] で設定したサンプルに対して解析を行います．

.. code-block:: cfg

    ###########
    # mutation call
    [mutation_call]
    qsub_option = -l s_vmem=5.3G,mem_req=5.3G
    
    # 1) fisher検定
    # Genomonでは検出した変異に対して，まずfisher検定を行います．
    # 以下の基準を満たす変異のみ，候補として次のステップに進みます
    [fisher_mutation_call]
    
    # サンプルペアがある解析で実行されます．
    # Genomonが次のコマンドの実行時、{pair_params}に設定するオプションを指定できます
    # /path/to/fisher　comparison -R $region \
    # -o $output.txt --ref_fa $reference_genome.fa \
    # -1 $disease_bam -2 $control_bam 　\
    # --samtools_path $path_to_samtools {pair_params}
    pair_params = --min_depth 8 --base_quality 15 --min_variant_read 4 --min_allele_freq 0.02 --max_allele_freq 0.1 --fisher_value 0.1 --samtools_params "-q 20 -BQ0 -d 10000000 --ff UNMAP,SECONDARY,QCFAIL,DUP"

    # サンプルペアでない解析で実行されます．
    # Genomonが次のコマンドの実行時、{pair_params}に設定するオプションを指定できます
    # /path/to/fisher　single -R $region \
    # -o $output.txt --ref_fa $reference_genome.fa \
    # -1 $disease_bam -2 $control_bam 　\
    # --samtools_path $path_to_samtools {single_params}    
    single_params = --min_depth 8 --base_quality 15 --min_variant_read 4 --min_allele_freq 0.02 --post_10_q 0.02 --samtools_params "-q 20 -BQ0 -d 10000000 --ff UNMAP,SECONDARY,QCFAIL,DUP"
    
    # パラメータの説明
    # --min_depth: 変異ポジションのリード数が指定した数以下であれば候補の対象となりません．
    #              Tumor Normalともに指定した本数以上なければなりません．
    # --base_quality: Base Qualityが指定した値以下であればその情報は使用されません．
    # --min_variant_read: Tumorの変異を含んだリードの数がこの値以上でなければ候補の対象となりません．
    # --min_allele_freq: Tumorのアレル比がこの値以下であれば候補の対象となりません．
    # --max_allele_freq: Normalのアレル比がこの値以上であれば候補の対象となりません．
    # --fisher_value: Fihser検定による結果の閾値です．
    # --post_10_q: 変異アレルのリード数は二項分布でモデル化できますが，
    #              これをベイズ的にやろうとしてベータ分布を利用し，
    #              その結果の10% posterio quantileを閾値としています.
    # --samtools_params: samtool mpileupで使用するのパラメータです．
    
    # 2) リアライメント
    # つぎに，変異が見つかったリードをblatを使用して再度アライメントします（これをリアライメントと呼びます）
    # Genomonが次のコマンドの実行時、{params}に設定するオプションを指定できます
    # /path/to/mutfilter realignment \
    # --target_mutation_file $input.txt \
    # -1 $disease_bam (-2 $control_bam) \
    # --output $output.txt --ref_genome $reference_genome.fa \
    # --blat_path $path_to_blat {params}
    [realignment_filter]    
    params = --score_difference 5 --window_size 200 --max_depth 5000 --exclude_sam_flags 3328
    
    # パラメータの説明
    # --score_difference: リアライメント時にマルチアライメントしているが，
    #                     1番目に良いスコアと2番目に良いスコアの差が指定した値以内であったら，
    #                     そのリードを使用しないという設定です（基本的にスコアに差がある方がUniqueにアライメントされています)
    # --window_size: リアライメントするときのリファレンスゲノムを作るときの設定です
    #                window size(bases) + 変異サイズ + window size(bases)のリファレンスゲノムを作っています．
    # --max_depth: 対象の変異positionがこの値以上のdepthであればリアライメントしません．
    # --exclude_sam_flags: 指定された値を含むsam flagのリードは対象から除かれます．


    # 3) indel判定
    # Normalサンプルの検出した変異ポジションの周辺にindelがあるか確認します．サンプルペアでないとこの処理は動きません．
    # indelとみなされた変異はアノテーションされます．この判定で変異候補の数は変わりません．
    # indel判定に使用した値は解析結果ファイル中，"indel_mismatch_count", と "indel_mismatch_rate" 列に出力されます
    # Genomonが次のコマンドの実行時、{params}に設定するオプションを指定できます
    # /path/to/mutfilter indel \
    # --target_mutation_file $input.txt \
    # -2 $control.bam --output $output.txt \
    # --samtools_path $path_to_samtools {params} 
    [indel_filter]
    params = --search_length 40 --neighbor 5 --min_depth 8 --min_mismatch 100000 --af_thres 1 --samtools_params "-q 20 -BQ0 -d 10000000 --ff UNMAP,SECONDARY,QCFAIL,DUP"
    
    # パラメータの説明
    # --search_length: indelを検索するときの範囲を指定します
    #                  search_length(bases) + 変異サイズ + search_length(bases)の範囲で探しに行きます．
    # --neighbor: 探し出したindelが候補のポジションから指定した値の範囲内にいればindelフィルタの対象とします．
    # --min_depth: Depthと書かれている場合は変異ポジションのリード数の閾値になります．
    # --min_mismatch: 指定された値以上のミスマッチ数であればその変異を出力しません．
    # --af_thres: 指定された値以上のアレル比であればその変異を出力しません．
    # --samtools_params: samtool mpileupのパラメータです．
    
    # 4) breakpoint
    # Normalサンプルの検出した変異ポジションの周辺にbreakpointがあるか確認します．サンプルペアでないとこの処理は動きません．
    # breakpointとみなされた変異はアノテーションされます．この判定で変異候補の数は変わりません．
    # Genomonが次のコマンドの実行時、{params}に設定するオプションを指定できます
    # /path/to/mutfilter breakpoint \
    # --target_mutation_file $input.txt \
    # -2 $control_bam --output $output.txt \
    # {params} 
    [breakpoint_filter]
    params = --max_depth 1000 --min_clip_size 20 --junc_num_thres 0 --mapq_thres 10 --exclude_sam_flags 3332
    
    # パラメータの説明
    # --max_depth: 対象の変異positionがこの値以上のdepthであればBreakpoint Filterを行いません．
    # --min_clip_size: ソフトクリッピングの長さが指定した値以下であればその情報は使用されません．
    # --junc_num_thres: junctionの数が指定の値より小さければその変異を出力しません．
    # --map_quality: Mapping Qualityが指定した値以下であればその情報は使用されません．
    # --exclude_sam_flags: 指定された値を含むsam flagのリードは対象から除かれます．
    
    # 5) EBCall
    # サンプル設定ファイルに記載されたコントロールパネルを使用してEBCallを行います
    [eb_filter]
    # mapping qualityが指定した値以下であればその情報は使用されません．
    map_quality = 20
    # base qualityが指定した値以下であればその情報は使用されません．
    base_quality = 15
    # SAM Flagで以下のフラグが立っているリードをスキップします.
    filter_flags = UNMAP,SECONDARY,QCFAIL,DUP
    
    # 6) Hot sopt
    # サンプルペアでないとこの処理は動きません．
    # hotspot callを使用するにはこのflagをTrueにしてください．
    [hotspot]
    active_hotspot_flag = True
    
    # Genomonが次のコマンドの実行時、{params}に設定するオプションを指定できます
    # /path/to/hotspot {params} \
    # $disease_bam $control.bam \
    # $output.txt $hotspot_database
    params = -t 0.1 -c 0.1 -R 0.1 -m 8.0 -S "-B -q 20 -Q2 -d 10000000" 

    # パラメータの説明
    # -t: Tumorのミスマッチ率がこの値より小さければ候補の対象となりません．
    # -c: Normalのミスマッチ率がこの値より大きければ候補の対象となりません．
    # -R: Normalのミスマッチ率 > Tumorのミスマッチ率 * 指定した値にであれば候補になりません．
    # -m: scoreの値が指定した値より小さければ候補になりません．
    # -S: samtool mpileupのパラメータです．
    
    # 7) 変異結果のマージ
    # Genomonでは 1)～6) までの処理をシーケンスデータを分割して変更して行います．
    # ここで一つのファイル {サンプル名}.genomon_mutation.result.txtから{サンプル名}.genomon_mutation.result.txt に結果をまとめます．
    [mutation_merge]
    qsub_option = -q '!mjobs_rerun.q' -l s_vmem=2G,mem_req=2G
    
    # 8) Genomonおすすめフィルタ
    # 7) で作成した結果ファイルに対して，よく使用されるフィルタリングをあらかじめ実施します
    # {サンプル名}.genomon_mutation.result.txtから{サンプル名}.genomon_mutation.result.filt.txtファイルを作成するためのフィルタ条件です．
    [mutation_util]
    
    # サンプルペアの解析で実行されます．
    # Genomonが次のコマンドの実行時、{single_params}に設定するオプションを指定できます
    # /path/to/mutil filter \
    # -i $input.txt -o $output.txt \
    # {single_params}
    pair_params = --fish_pval 1.0 --realign_pval 1.0 --eb_pval 4.0 --tcount 4 --ncount 2

    # サンプルペアでない解析で実行されます．
    # Genomonが次のコマンドの実行時、{single_params}に設定するオプションを指定できます
    # /path/to/mutil filter \
    # -i $input.txt -o $output.txt \
    # {single_params}
    single_params = --post10q 0.1 --r_post10q 0.1 --count 4

    # パラメータの説明
    # たとえば--fish_pvalに 1.0 を指定すると、その値以上のレコードがresult.filt.txtに出力されます.
    #  --fish_pval: カラム"P-value(fisher)" >= 
    #  --realign_pval: カラム"P-value(fisher)_realignment" >= 
    #  --eb_pval: カラム"P-value(EBCall)" >= 
    #  --tcount: カラム"AltNum_tumor" >= 
    #  --ncount: カラム"AltNum_normal" <= 
    #  --post10q: カラム"10%_posterior_quantile" >= 
    #  --r_post10q: カラム"10%_posterior_quantile(realignment)" >= 
    #  --count: カラム"readPairNum" >= 


構造変異解析 (SV)
------------------

| ここでは SV 検出に関するオプションについて解説します．
| Genomonでは SV の検出にGenomonSVというソフトウェアを使用しており， [sv_detection] で設定したサンプルに対して解析を行います．

.. code-block:: cfg

    ##########
    ## Genomon SV
    
    # 1) svの検出を行います 
    # Genomonが次のコマンドの実行時、{params}に設定するオプションを指定できます
    # paramsに設定できるパラメータについてはGenomonSVのドキュメントをご確認ください．
   　# /path/to/genomon_sv parse \
    # $input_bam output_prefix {params}
    [sv_parse]
    qsub_option = -q '!mjobs_rerun.q' -l s_vmem=5.3G,mem_req=5.3G
    params = 
    
    # 2) svのマージを行います
    # Genomonが次のコマンドの実行時、{params}に設定するオプションを指定できます
    # paramsに設定できるパラメータについてはGenomonSVのドキュメントをご確認ください．
    # /path/to/genomon_sv merge \
    # $control_info $merge_output_file {params} 
    [sv_merge]
    qsub_option = -q '!mjobs_rerun.q' -l s_vmem=5.3G,mem_req=5.3G
    params = 
    
    # 3) svのフィルタリングを行います
    ### フィルタその1：
    # {サンプル名}.genomon_sv.result.txtファイルを作成するためのフィルタ条件です
    # Genomonが次のコマンドの実行時、{params}に設定するオプションを指定できます
    # /path/to/genomon_sv filt \
    # $input_bam $output_prefix $reference_genome \
    # $annotation_dir {params} 
    [sv_filt]
    qsub_option = -q '!mjobs_rerun.q' -l s_vmem=5.3G,mem_req=5.3G
    params = --min_junc_num 2 --max_control_variant_read_pair 10 --min_overhang_size 30  
    
    # パラメータの説明
    #    --min_junc_num: minimum required number of supporting junction read pairs
    #    --max_control_variant_read_pair maximum allowed number of read pairs in matched control sample
    #    --min_overhang_size minimum region size arround each break-point which have to be covered by at least one aligned short read
    # GenomonSVではアノテーションに独自リソースを使用していますので
    # リソースの場所を指定します．
    # GenomonSV をインストールした場所にあります．
    annotation_dir = # the path to the GenomonSV-0.4.0beta/resource
    
    ### フィルタその2：Genomonおすすめフィルタ
    # {サンプル名}.genomon_sv.result.txtから{サンプル名}.genomon_mutation.result.filt.txtファイルを作成するためのフィルタ条件です
    # Genomonが次のコマンドの実行時、{sv_utils_params}に設定するオプションを指定できます
    # /path/to/sv_utils filter \
    # input.txt output.txt $sv_utils_annotation_dir \
    # {sv_utils_param} 
    sv_utils_params = --min_tumor_allele_freq 0.07 --max_control_variant_read_pair 1 --control_depth_thres 10 --inversion_size_thres 1000 --remove_simple_repeat
    
    # パラメータの説明
    # たとえば--min_tumor_allele_freqに 0.007 を指定すると、その値以上のレコードがresult.filt.txtに出力されます.
    #    --min_tumor_allele_freq >= 
    #    --max_control_variant_read_pair >=
    #    --control_depth_thres >=
    #    --inversion_size_thres >=
    
    # sv_utilsではアノテーションに独自リソースを使用していますので
    # リソースの場所を指定します．
    # sv_utils をインストールした場所にあります．
    sv_utils_annotation_dir = # the path to the sv_utils-0.4.0beta/resource 

Quality Control (QC)
----------------------------

| ここではQCに関するオプションについて解説します．
|
| Genomonでは QC の算出にPCAP (bam_stats.pl) と GenomonQC (depthのカバレッジ計算) というソフトウェアを使用しています．
| [qc] で設定したサンプルに対して解析を行います．

.. code-block:: cfg

    ######
    # bamstats
    # PCAP (bam_stats.pl) 実行時オプションです．
    # 特別な設定はありません．
    [qc_bamstats]
    qsub_option = -q '!mjobs_rerun.q' -l s_vmem=2G,mem_req=2G
    
    ######
    # カバレッジ
    # PCAP (bam_stats.pl) ではカバレッジ計算ができませんので，GenomonQC を使用します．
    # exomeとwgsでは計算方法が異なりますのでwgsの場合は設定が必要です
    [qc_coverage]
    
    ### 共通
    qsub_option = -q '!mjobs_rerun.q' -l s_vmem=2G,mem_req=2G
    
    # カバレッジ率 (%)
    # 以下の場合，2% 10% 20% 30% 40% 50% 100% のカバレッジをそれぞれ計算します
    coverage    = 2,10,20,30,40,50,100
    
    # 指定したリードのみカバレッジ計算に使用します
    # Genomoではdepth計算の対象リードの取得に "samtools view" を使用しており，そこで使用するオプションです．
    # 【参考】その後，depthの計算に "samtools depth" を使用しています．
    samtools_params = -F 3072 -f 2
    
    ### WGS用の設定
    # wgsはsamtoolsで全リードを計算するにはサイズが大きすぎるため，
    # "bedtools shuffle" を用いてリードをランダムに抽出する処理を行っています．
    # 
    # wgsかどうか(wgsの場合はTrue)
    wgs_flag = False

    # リード抽出に使用する bedファイルを作成するオプションで，
    # bedファイル1行に記載する領域の大きさを指定します．
    # "bedtools shuffle" ではbedファイル1行から領域を選択するため，
    # 1行に記載された bed の領域に差があると抽出に偏りが生じるためこのようにサイズを統一しています．
    wgs_incl_bed_width = 1000000
    
    # 抽出するリードの本数
    wgs_i_bed_lines = 10000
    # 抽出するリードの長さ
    wgs_i_bed_width = 100    
    
    # bamstats とカバレッジの結果をマージして{サンプル名}.genomonQC.result.txtファイルを作成します．
    [qc_merge]
    qsub_option = -q '!mjobs_rerun.q' -l s_vmem=2G,mem_req=2G

Post Analysis
----------------------------

| ここでは変異コール，SV，QCの解析結果をレポート出力するPost Analysisという機能のオプションについて解説します．
|
| Post Analysisによるマージされた結果が必要ですので，レポート出力するには [post_analysis] と [paplot] 両方が有効(enable = True)にする必要があります．

.. code-block:: cfg

    # GenomonではGenomonPostAnalysisというソフトウェアを用いて，サンプル毎の結果ファイルを1つのファイルにマージしています
    [post_analysis]
    qsub_option = -q '!mjobs_rerun.q' -l s_vmem=2G,mem_req=2G

    # Genomon Post Analysisを使用しない場合はFalse
    enable = True
    
    # post analysisの設定ファイルです．インストールした場所にありますので，パスを設定してください
    config_file = # the path to the GenomonPostAnalysis-1.0.2/genomon_post_analysis.cfg
    
    # paplotというソフトウェアを用いてレポートを作成します
    [paplot]
    qsub_option = -q '!mjobs_rerun.q' -l s_vmem=2G,mem_req=2G
    
    # paplotを使用しない場合はFalse
    enable = True 
    
    # ペアを設定していないサンプルをpaplotの対象から除く場合はFalse
    include_unpair = True
    # コントロールパネルを使用しないサンプルをpaplotの対象から除く場合はFalse
    include_unpanel = True

    # paplotの設定ファイルです．
    # paplotをインストールした場所/config_template/ 配下にGenomon用の設定ファイルがありますので，パスを設定してください
    config_file = # the path to the paplot-0.5.5/paplot.cfg

    # index.htmlの設定です．通常変更する必要はありません
    title = Genomon
    remarks = Data used in this report were generated using below software.
    software = genomon_pipeline:Genomon-Pipeline, genomon_sv:GenomonSV, sv_utils:sv_utils, fisher:GenomonFisher, mutfilter:GenomonMutationFilter, ebfilter:EBFilter, mutanno:mutanno, mutil:mutil, genomon_qc:GenomonQC


pmsignature
------------------

| ここではシグネチャ解析のオプションについて解説します．
|
| Genomonでは変異コールで見つかった変異を使用してシグネチャ解析を行います．
| Post Analysisによるマージされた結果が必要であり，プロットによる確認が必要なため以下条件をすべて満たすときのみ実行します

 - サンプル設定ファイル [mutation_call] でサンプルが設定されている
 - Genomon Post Analysisが有効である ([post_analysis] enable = True)
 - paplotが有効である ([paplot] enable = True)

.. code-block:: cfg

    ############
    # pmsignature
    
    [pre_pmsignature]
    qsub_option = -q '!mjobs_rerun.q' -l s_vmem=2G,mem_req=2G
    
    [pmsignature_full]
    # pmsignature (type=full) を実行しない場合はFalse
    enable = False
    qsub_option = -q '!mjobs_rerun.q' -l s_vmem=2G,mem_req=2G
    signum_min = 2
    signum_max = 6
    trdirflag = F
    trialnum = 10
    
    [pmsignature_ind]
    # pmsignature (type=independent) を実行しない場合はFalse
    enable = True
    qsub_option = -q '!mjobs_rerun.q' -l s_vmem=2G,mem_req=2G
    signum_min = 2
    signum_max = 6
    trdirflag = T
    trialnum = 10
    
    
