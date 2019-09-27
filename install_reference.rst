-------------------------------------
リファレンスゲノムの変更方法
-------------------------------------

Genomon2の実行時に指定するパイプライン設定ファイルの内容を変更することにより，ヒトゲノム以外の解析やGRCh38での解析が可能です．このマニュアルではGRCh38 Reference Sequenceの使用を例にあげて説明しております．


(A) DNA解析の設定について
=========================

パイプライン設定ファイルの内容を解析したいゲノムに変更します．

以下のパイプラン設定ファイルを任意のディレクトリにコピーして，内容を変更してください．

/share/pub/genomon/genomon_pipeline-2.6.2/genomon_conf/dna_exome_genomon.cfg

今回のGenomon環境は以下のとおりとします．

 - ここで作成するパイプライン設定ファイル： dna_exome_genomon_GRCh38.cfg
 - ここで作成するデータベースのディレクトリ： /path/to/database
 - annovarをインストールしたディレクトリ: /path/to/annovar

.. code-block:: cfg
  :caption: パイプライン設定ファイル (dna_exome_genomon_GRCh38.cfg)
  :name: dna_exome_genomon_GRCh38.cfg_a
  
  [REFERENCE]
  # prepared reference fasta file
  ref_fasta = /path/to/database/GRCh38/GRCh38.d1.vd1.fa
  interval_list = /path/to/database/GRCh38/GRCh38_noScaffold_noDecoy.interval_list
  genome_size = /share/pub/genomon/.genomon_local/genomon_pipeline-2.6.2/install/bedtools-2.24.0/genomes/human.hg38.genome
  gaptxt = /path/to/database/hg38.fa/gap.txt
  bait_file = /path/to/database/bait/refGene.coding.exon.hg38.161116.bed
  simple_repeat_tabix_db = /path/to/database/tabix/simpleRepeat_hg38.bed.gz
  HGVD_2013_tabix_db =
  HGVD_2016_tabix_db =
  ExAC_tabix_db =
  hotspot_db = 
  
  [sv_filt]
  params = --grc --genome_id hg38
  sv_utils_params = --grc --simple_repeat_file /share/pub/genomon/.genomon_local/genomon_pipeline-2.6.2/database/GenomonSV-0.6.0rc1/hg38/simpleRepeat.txt.gz --genome_id hg38
  
  [paplot]
  config_file = /path/to/database/paplot-0.5.5/paplot_dna_GRCh38.cfg
  
  [SOFTWARE]
  bwa = /path/to/bwa-0.7.17/bwa
  annovar = /path/to/annovar
  
  [annotation]
  active_annovar_flag = True
  iannovar_buildver = hg38
  table_annovar_params = -buildver hg38 -remove --otherinfo -protocol   refGene,cytoBand,genomicSuperDups,ljb26_all,cosmic70,esp6500siv2_all,avsnp150,clinvar_20180603 -operation g,r,r,f,f,f,f,f
  annovar_database = /path/to/annovar/humandb
  active_HGVD_2013_flag = False
  active_HGVD_2016_flag = False
  active_ExAC_flag = False

各項目で指定するファイルの準備方法を次項から解説します．

(A-1) ref_fasta
------------------------------------------

ref_fastaにはリファレンスゲノムを指定します．同ディレクトリ内にbwa
indexファイル，fasta indexファイルを作成しておく必要があります．

・リファレンスゲノム(FASTA形式)をダウンロードし，圧縮されている場合は解凍してください．こちらのFASTA形式のファイルのファイルパスをref_fastaに指定します．

.. code-block:: bash

  # Genomic Data Commons WebSite
  https://gdc.cancer.gov/about-data/data-harmonization-and-generation/gdc-reference-files
  # Reference Sequenceをダウンロード
  GRCh38.d1.vd1.fa.tar.gz
  
.. attention::

  我々はChromosomeのPrefixにchrが付かないようにファイルを変更して使用しています

・BWA index ファイルを作成します．

``bwa index`` コマンドを使用してindexファイルを作成します．(shirokane3で約1時間)

.. code-block:: bash

  /share/pub/genomon/.genomon_local/genomon_pipeline-2.6.2/install/bwa-0.7.8/bwa index GRCh38.d1.vd1.fa

以下のBWA indexが作成されます．

 - GRCh38.d1.vd1.amb
 - GRCh38.d1.vd1.ann
 - GRCh38.d1.vd1.bwt
 - GRCh38.d1.vd1.pac
 - GRCh38.d1.vd1.sa

・samtools indexファイルを作成します．

samtools faidxコマンドを使用してindexファイルを作成します．

.. code-block:: bash

  /share/pub/genomon/.genomon_local/genomon_pipeline-2.6.2/install/samtools-1.2/samtools faidx GRCh38.d1.vd1.fa

Fasta indexが作成されます．

 - GRCh38.d1.vd1.fai

(A-2) interval_list
----------------------------------------------

interval_listには変異コールを並列化して実行するためのファイルを設定します．

以下にインターバルリストの中身を記載しましたが，Chromosomeポジションの範囲が複数記載されています．指定した範囲が変異コールされる範囲となります．1行が1ジョブとなり，以下のファイルでは省略されていますが実際には24行ありますので，24並列でジョブが実行されます．

◆記載ルール◆

- Chromosomeをまたいで範囲を記載することはできません．
- Chromosome内で範囲を分ける場合はgap領域で範囲を分割します．
- 最後の行に改行を入れてはいけません．

.. code-block:: text
  :caption: インターバルリスト (GRCh38_noScaffold_noDecoy.interval_list)
  
  1:10000-121976459
  1:121976459-248946422
  2:10000-97439618
  2:97439618-242183529
  3:60000-90550102
  3:90550102-198285559
  4:10000-190204555
  5:10000-181528259
  (以下略)
  
Genomon-Projectからダウンロードしてご使用ください．

https://github.com/Genomon-Project/genomon_database


(A-3) genome_size
--------------------------------------------

Whole GenomeシークエンスのBAM QCを算出する際に使用します．

Chromosome名とサイズがタブ区切りで記載されたファイルを指定します．

.. code-block:: text
  :caption: Genome_size ファイル (human.hg38.genome)
  
  chr1 248956422
  chr2 242193529
  chr3 198295559
  chr4 190214555
  chr5 181538259
  (以下略)

Genomon-Projectからダウンロードしてご使用ください．

https://github.com/Genomon-Project/genomon_database

(A-4) gaptxt
------------------------------------------

こちらもWhole GenomeシークエンスのBAM QCを算出する際に使用するファイルになります．

NCBIからダウンロードして解凍してご使用ください．

http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/gap.txt.gz

.. code-block:: text
  :caption: Gaptxt (hg38.fa/gaptxt)
  
  585 chr1 0 10000 1 N 10000 telomere no
  586 chr1 207666 257666 5 N 50000 contig no
  587 chr1 297968 347968 7 N 50000 contig no
  589 chr1 535988 585988 10 N 50000 contig no
  605 chr1 2702781 2746290 48 N 43509 scaffold yes
  (以下略)

(A-5) bait_file
------------------------------------------

ExomeやTargeシークエンスのBAM QCを算出する際に使用します．ExomeやTargetシークエンスした領域が記載されたファイルを指定します．このファイルに記載されている領域のDepthやCoverageなどを計算し出力します．

SureSelectなど使用したbaitファイルがある場合はそちらを設定してください．

無い場合はrefGene.coding.exon.bedを使用してもらえればと思います．refGene.coding.exon.bedはrefGene.txtのcoding exon領域だけをとりだして，そちらをbaitの範囲としています．

http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/refGene.txt.gz

作成方法は以下のwebサイトに記載しています．

https://github.com/ken0-1n/RefGeneTxtToBed

ベイトファイルはBED形式で記載してください．対応するファイルがない場合は ``touch`` コマンドでダミーファイルを作成して指定してください．

.. code-block:: text
  :caption: ベイトファイル (refGene.coding.exon.hg38.161116.bed)
  
  chr1 69090 70008
  chr1 450739 451678
  chr1 685715 686654
  chr1 925941 926013
  chr1 930154 930336
  (以下略)

(A-6) simple_repeat_tabix_db
---------------------------------------------------------

変異コールでシンプルリピートのアノテーションを付けるためのファイルを用意します．

・作成方法

以下のサイトからシンプルリピートファイルをダウンロードしてください．

http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/simpleRepeat.txt.gz

BED形式のファイルを作成します．

.. code-block:: bash

  cut -f2- simpleRepeat.txt > simpleRepeat_hg38.bed

Tabixというツールを使用してindexを張ります．ツールに付属している(binに入っている)bgzipを使用してファイルを圧縮します．

.. code-block:: bash

  /share/pub/genomon/.genomon_local/genomon_pipeline-2.6.2/install/htslib-1.3/bgzip simpleRepeat_hg38.bed

tabixでindexを張ります．

.. code-block:: bash

  /share/pub/genomon/.genomon_local/genomon_pipeline-2.6.2/install/htslib-1.3/tabix simpleRepeat_hg38.bed.gz

simpleRepeat_hg38.bed.gzをsimple_repeat_tabix_dbに指定します．

UCSCにsimpleRepeat.txtが存在しない場合は，ダミーファイルを作成する必要があります．

(A-7) HGVD_2013_tabix_db HGVD_2016_tabix_db ExAC_tabix_db　hotspot_db
-------------------------------------------------------------------------------------------

HGVD, ExAC, hotspotはHG38に未対応のため空白にする．

.. code-block:: cfg
  :caption: パイプライン設定ファイル (dna_exome_genomon_GRCh38.cfg)
  :name: dna_exome_genomon_GRCh38.cfg_a7
    
  [REFERENCE]
  HGVD_2013_tabix_db =
  HGVD_2016_tabix_db =
  ExAC_tabix_db =
  hotspot_db = 


(A-8) SV検出のAnnotationのリソースディレクトリを変更する
--------------------------------------------------------

パイプライン設定ファイルを変更します．更新したファイルを以下の項目に指定してください．

.. code-block:: cfg

  [sv_filt]
  params = --grc --genome_id hg38
  sv_utils_params = --grc --simple_repeat_file /share/pub/genomon/.genomon_local/genomon_pipeline-2.6.2/database/GenomonSV-0.6.0rc1/hg38/simpleRepeat.txt.gz --genome_id hg38

(A-9) paplotの設定ファイルを変更する．
--------------------------------------

paplotを使用する場合は，パイプライン設定ファイルに指定されているpaplotの設定ファイルの中身を書き換える必要があります．

まずはpaplot.cfgファイルを適当なディレクトリにコピーして内容を変更します．

.. code-block:: bash

  cp /share/pub/genomon/genomon_pipeline-2.6.2/genomon_conf/paplot/paplot_dna.cfg \
     /path/to/database/paplot-0.5.5/paplot_dna_GRCh38.cfg

変更する箇所は [genome] path と [ca] use_chrs(ヒトと染色体数が異なる場合) です．

まずはpathに設定するファイルを作成しましょう．

(A-1)で作成したfasta indexファイルを使用すると簡単に作成できます．

use_chrsを解析するゲノムの染色体数に合わせてください．

.. code-block:: cfg
  :caption: paplot_dna_GRCh38.cfg
  
  [genome]
  path= /path/to/database/GRCh38/GRCh38.genome_size
  
  [ca]
  use_chrs = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,X,Y

変更したpaplot.cfgのファイルパスをパイプライン設定ファイルに記載します．

.. code-block:: cfg
  :caption: パイプライン設定ファイル (dna_exome_genomon_GRCm38.cfg)
  
  [paplot]
  config_file = /path/to/database/paplot-0.5.5/paplot_dna_GRCh38.cfg

paplotのマニュアルを読んでいただけると，こちらの設定についての理解が深まると思います．

・paplotマニュアル

http://paplot-jp.readthedocs.io/ja/latest/config.html#ca-genome

『表示する染色体を限定する』，『ヒト以外のゲノムを使用する』をご参照ください．

(A-10) ANNOVAR
--------------

ANNOVARのダウンロードにはユーザ登録 (User License Agreement) が必要です．

http://www.openbioinformatics.org/annovar/annovar_download_form.php

ANNOVARのホームページにてユーザ登録 (User License Agreement) が完了した後に，登録したメールアドレスにANNOVARをダウンロードするためのリンクが記載されたメールが届きます．そのリンクを使用してANNOVARをダウンロードします．

.. code-block:: bash

  wget {メールで通知されたリンク}
  tar zxvf annovar.latest.tar.gz
  cd annovar

ダウンロード後はANNOVARのPerlスクリプトを使用してdbSNP131などの各種データをダウンロードします．

# Genomonで必要なANNOVARのデータベースをダウンロードします．Copy and Pasteして使ってください．
# データベースの追加は可能です．

.. code-block:: bash

  DATABASE_LIST="
  refGene
  ljb26_all
  cosmic70
  esp6500siv2_all
  avsnp150
  clinvar_20180603
  "
  
  for DATABASE in $DATABASE_LIST
  do
      ./annotate_variation.pl -buildver hg38 -downdb -webfrom annovar $DATABASE humandb/
  done
  
  ./annotate_variation.pl -buildver hg38 -downdb cytoBand humandb/
  ./annotate_variation.pl -buildver hg38 -downdb genomicSuperDups humandb/


ANNOVARを使用するようにパイプライン設定ファイルを編集します．以下の2か所の変更をお願いします．
データベースを追加した場合は，table_annovar_paramsにも追加設定が必要です．

.. code-block:: cfg

  [SOFTWARE]
  annovar = [ANNOVARのパスをダウンロードしたANNOVAR]に変更する．
  (例)annovar = path/to/annovar
  
  [annotation]
  active_annovar_flag = True
  iannovar_buildver = hg38
  table_annovar_params = -buildver hg38 -remove --otherinfo -protocol refGene,cytoBand,genomicSuperDups,ljb26_all,cosmic70,esp6500siv2_all,avsnp150,clinvar_20180603 -operation g,r,r,f,f,f,f,f
  annovar_database = /path/to/annovar/humandb
  active_HGVD_2013_flag = False
  active_HGVD_2016_flag = False
  active_ExAC_flag = False

(B) RNA解析の設定について
=========================

パイプライン設定ファイルの内容を解析したいゲノムに変更します．

以下のパイプラン設定ファイルを任意のディレクトリにコピーして，内容を変更してください．

/share/pub/genomon/genomon_pipeline-2.6.2/genomon_conf/rna_genomon.cfg

今回のGenomon環境は以下のとおりとします．

 - ここで作成するパイプライン設定ファイル： rna_exome_genomon_GRCh38.cfg
 - ここで作成するデータベースのディレクトリ： /path/to/database

.. code-block:: cfg
  :caption: パイプライン設定ファイル（rna_genomon_GRCh38.cfg）
  
  [REFERENCE]
  star_genome = /path/to/database/GRCh38.STAR-2.5.2a
  ref_fasta = /path/to/database/GRCh38/GRCh38.d1.vd1.fa <- (A-1)と同じ
  
  [fusion_count_control]
  params = --genome_id hg38
  [fusion_merge_control]
  params = --genome_id hg38
  [fusion_fusion]
  params = --grc --genome_id hg38
  filt_params = --filter_same_gene --grc --genome_id hg38
  [genomon_expression]
  params = --grc --genome_id hg38
  [intron_retention]
  params = --grc --genome_id hg38
  
  [paplot]
  config_file = /path/to/database/paplot-0.5.5/paplot_rna_GRCh38.cfg

（B-1）star_genome
-------------------------------------------------

star_genomeにはSTARのindexファイルが格納されているディレクトリのパスを指定します．

・STAR index ファイルを作成します．

STARにはのindexファイルを作成するには，FASTAファイル以外にGTFファイルが必要です．

ftp://ftp.sanger.ac.uk/pub/gencode/Gencode_human/release_25/gencode.v25.annotation.gtf.gz

.. attention::

  GRCh38.p7.genome.faと同じでPrefixにchrが付かないようにファイルの中身を変更しております．

STARコマンドを使用してSTAR indexを作成します．

.. code-block:: bash

  /share/pub/genomon/.genomon_local/genomon_pipeline-2.6.2/install/STAR-2.5.2a/bin/Linux_x86_64_static/STAR \
  --runThreadN 8 \
  --runMode genomeGenerate \
  --genomeDir /path/to/database/GRCh38.STAR-2.5.2a \
  --genomeFastaFiles /path/to/database/GRCh38/GRCh38.d1.vd1.fa \
  --sjdbGTFfile /path/to/database/GTF/gencode.v25.annotation.gtf \
  --sjdbOverhang 100

メモリが足りない場合はqloginするときに ``-l s_vmem=64G,mem_req=64G`` オプションを指定してください

.. code-block:: bash

  $bash make.sh

  # 以下はmake.shのログです
  /path/to/database/GRCh38.STAR-2.5.2a
  sc092
  arg1=
  2016年 11月 18日 金曜日 18:38:19 JST
  Nov 18 18:38:20 ..... started STAR run
  Nov 18 18:38:20 ... starting to generate Genome files
  Nov 18 18:39:27 ... starting to sort Suffix Array. This may take a long time...
  Nov 18 18:39:44 ... sorting Suffix Array chunks and saving them to disk...
  Nov 18 19:23:03 ... loading chunks from disk, packing SA...
  Nov 18 19:25:21 ... finished generating suffix array
  Nov 18 19:25:21 ... generating Suffix Array index
  Nov 18 19:29:16 ... completed Suffix Array index
  Nov 18 19:29:16 ..... processing annotations GTF
  Nov 18 19:29:29 ..... inserting junctions into the genome indices
  Nov 18 19:32:43 ... writing Genome to disk ...
  Nov 18 19:32:47 ... writing Suffix Array to disk ...
  Nov 18 19:33:14 ... writing SAindex to disk
  Nov 18 19:33:16 ..... finished successfully

(B-2) fusionfusionの設定ファイルを変更する
------------------------------------------

パイプライン設定ファイルを変更します．更新したファイルを以下の項目に指定してください．

.. code-block:: cfg

  [fusion_count_control]
  params = --genome_id hg38
  [fusion_merge_control]
  params = --genome_id hg38
  [fusion_fusion]
  params = --grc --genome_id hg38
  filt_params = --filter_same_gene --grc --genome_id hg38
  

(B-3) Expressionの設定ファイルを変更する
----------------------------------------

パイプライン設定ファイルを変更します．更新したファイルを以下の項目に指定してください．

.. code-block:: cfg

  [genomon_expression]
  params = --grc --genome_id hg38

(B-4) intron retentionの設定ファイルを変更する
------------------------------------------------------------

パイプライン設定ファイルを変更します．更新したファイルを以下の項目に指定してください．

.. code-block:: cfg

  [intron_retention]
 　params = --grc --genome_id hg38

(B-5) paplotの設定ファイルを変更する
-------------------------------------

paplotを使用する場合は，パイプライン設定ファイルに指定されているpaplotの設定ファイルの中身を書き換える必要があります．

まずはpaplot.cfgファイルを適当なディレクトリにコピーして内容を変更します．

.. code-block:: bash

  cp /share/pub/genomon/genomon_pipeline-2.6.2/genomon_conf/paplot/paplot_rna.cfg \
     /path/to/database/paplot-0.5.5/paplot_rna_GRCh38.cfg

RNA用のコンフィグファイル，paplot_rna.cfgのコピー後の作業はDNAの「(A-9) paplotの設定ファイルを変更する」と同じです.(A-9)の設定方法を参照ください．
