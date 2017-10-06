-------------------------------------
リファレンスゲノムの変更方法
-------------------------------------

Genomon2の実行時に指定するパイプライン設定ファイルの内容を変更することにより、ヒトゲノム以外の解析やGRCh38での解析が可能です．このマニュアルではGRCh38.faの使用を例にあげて説明しております．


(A) DNA解析の設定について
=========================

パイプライン設定ファイルの内容を解析したいゲノムに変更します．

以下のパイプラン設定ファイルを任意のディレクトリにコピーして、内容を変更してください．

/home/w3varann/.genomon_local/genomon_pipeline-2.5.0/genomon_conf/dna_exome_genomon.cfg

今回のGenomon環境は以下のとおりとします．

 - ここで作成するパイプライン設定ファイル： dna_exome_genomon_GRCh38.cfg
 - ここで作成するデータベースのディレクトリ： /path/to/database
 - annovarをインストールしたディレクトリ: /path/to/annovar

.. code-block:: cfg
  :caption: パイプライン設定ファイル (dna_exome_genomon_GRCh38.cfg)
  
  [REFERENCE]
  # prepared reference fasta file
  ref_fasta = /path/to/database/GRCh38/GRCh38.p7.genome.fa
  interval_list = /path/to/database/GRCh38/GRCh38_noScaffold_noDecoy.interval_list
  genome_size = /home/w3varann/.genomon_local/genomon_pipeline-2.5.0/tools/bedtools-2.24.0/genomes/human.hg38.genome
  gaptxt = /path/to/database/hg38.fa/gap.txt
  bait_file = /path/to/database/bait/refGene.coding.exon.hg38.161116.bed
  simple_repeat_tabix_db = /path/to/database/tabix/simpleRepeat_hg38.bed.gz
  HGVD_2013_tabix_db =
  HGVD_2016_tabix_db =
  ExAC_tabix_db =
  
  [sv_filt]
  annotation_dir = /path/to/database/GenomonSV-0.4.0beta/resource_GRCh38
  sv_utils_annotation_dir = /path/to/database/sv_utils-0.4.0beta/resource_GRCh38
  
  [paplot]
  config_file = /path/to/database/paplot-0.5.0/paplot_dna_GRCh38.cfg
  
  [SOFTWARE]
  annovar = /path/to/annovar
  
  [annotation]
  active_annovar_flag = True
  iannovar_buildver = hg38
  table_annovar_params = -buildver hg38 -remove --otherinfo -protocol refGene,esp6500siv2_all,1000g2014oct_all,1000g2014oct_afr,1000g2014oct_eas,1000g2014oct_eur,cosmic70,clinvar_20150629,ljb26_all -operation g,f,f,f,f,f,f,f,f
  annovar_database = /path/to/annovar/humandb
  active_HGVD_2013_flag = False
  active_HGVD_2016_flag = False
  active_ExAC_flag = False

各項目で指定するファイルの準備方法を次項から解説します．

(A-1) ref_fasta
------------------------------------------

ref_fastaにはリファレンスゲノムを指定します．同ディレクトリ内にbwa
indexファイル、fasta indexファイルを作成しておく必要があります．

・リファレンスゲノム(FASTA形式)をダウンロードし、圧縮されている場合は解凍してください．こちらのFASTA形式のファイルのファイルパスをref_fastaに指定します．

.. code-block:: bash

  wget ftp://ftp.sanger.ac.uk/pub/gencode/Gencode_human/release_25/GRCh38.p7.genome.fa.gz


.. attention::

  我々はChromosomeのPrefixにchrが付かないようにファイルを変更して使用しています

・BWA index ファイルを作成します．

``bwa index`` コマンドを使用してindexファイルを作成します．(shirokane3で約1時間)

.. code-block:: bash

  /home/w3varann/.genomon_local/genomon_pipeline-2.5.0/tools/bwa-0.7.8/bwa index GRCh38.p7.genome.fa

以下のBWA indexが作成されます．

 - GRCh38.p7.genome.fa.amb
 - GRCh38.p7.genome.fa.ann
 - GRCh38.p7.genome.fa.bwt
 - GRCh38.p7.genome.fa.pac
 - GRCh38.p7.genome.fa.sa

・samtools indexファイルを作成します．

samtools faidxコマンドを使用してindexファイルを作成します．

.. code-block:: bash

  /home/w3varann/.genomon_local/genomon_pipeline-2.5.0/tools/samtools-1.2/samtools faidx GRCh38.p7.genome.fa

Fasta indexが作成されます．

 - GRCh38.p7.genome.fa.fai

(A-2) interval_list
----------------------------------------------

interval_listには変異コールを並列化して実行するためのファイルを設定します．

以下にインターバルリストの中身を記載しましたが、Chromosomeポジションの範囲が複数記載されています．指定した範囲が変異コールされる範囲となります．1行が1ジョブとなり、以下のファイルでは省略されていますが実際には24行ありますので、24並列でジョブが実行されます．

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

(スクリプト修正中です)https://github.com/ken0-1n/RefGeneTxtToBed（しばらくお待ちください）

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

  /home/w3varann/.genomon_local/genomon_pipeline-2.5.0/tools/htslib-1.3/bgzip simpleRepeat_hg38.bed

tabixでindexを張ります．

.. code-block:: bash

  /home/w3varann/.genomon_local/genomon_pipeline-2.5.0/tools/htslib-1.3/tabix simpleRepeat_hg38.bed.gz

simpleRepeat_hg38.bed.gzをsimple_repeat_tabix_dbに指定します．

UCSCにsimpleRepeat.txtが存在しない場合は、ダミーファイルを作成する必要があります．

(A-7) HGVD_2013_tabix_db HGVD_2016_tabix_db ExAC_tabix_db
-------------------------------------------------------------------------------------------

HGVD (ヒトゲノムのデータベース) はHG38に未対応のため空白．

(A-8) SV検出のAnnotationのリソースディレクトリを変更する
--------------------------------------------------------

SV検出を行う際は、Annotationのためのリソースを変更する必要があります．**2つ変更します！**

◆１つめ：

以下のリソースディレクトリを任意のディレクトリにコピーしてください．

.. code-block:: bash

  cp –r /home/w3varann/.genomon_local/genomon_pipeline-2.5.0/database/GenomonSV-0.4.0beta/resource \
        /path/to/database/GenomonSV-0.4.0beta/resource_GRCh38

resourceディレクトリ内のprepGeneInfo.shの中身を変更します

.. code-block:: bash

  # 変更前
  wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/refGene.txt.gz
  
  # 変更後
  wget http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/refGene.txt.gz

変更が完了したらシェルを実行します．

.. code-block:: bash

  bash prepGeneInfo.sh

◆２つめ：

以下のリソースディレクトリを適当なディレクトリにコピーしてください．

.. code-block:: bash

  cp -r /home/w3varann/.genomon_local/genomon_pipeline-2.5.0/database/sv_utils-0.4.0beta/resource \
        /path/to/database/sv_utils-0.4.0beta/resource_GRCh38

resourceディレクトリ内のprepGeneInfo.shの中身を変更します

.. code-block:: bash

  # 変更前
  rm –rf GCF_000001405.13.assembly.txt
  wget ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/All/GCF_000001405.13.assembly.txt
  python make_ucsc_grch.py GCF_000001405.13.assembly.txt > grch2ucsc.txt
  wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/refGene.txt.gz
  wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/ensGene.txt.gz
  wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/database/simpleRepeat.txt.gz
  
  # 変更後
  rm –rf GCF_000001405.33.assembly.txt
  wget ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/All/GCF_000001405.33.assembly.txt
  python make_ucsc_grch.py GCF_000001405.33.assembly.txt > grch2ucsc.txt
  wget http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/refGene.txt.gz
  wget http://ccb.jhu.edu/software/tophat/downloads/hg38/ensGene.txt.gz
  wget http://hgdownload.soe.ucsc.edu/goldenPath/hg38/database/simpleRepeat.txt.gz
  


※GCF_000001405.33.assembly.txtはGRCh38.p7用です．

※GCF_000001405.33.assembly.txtはSequence-NameとUCSC-style-nameの関係を抽出して、どちらにも対応できるようにするために使用しております．

.. note::

  **ensGene.txt.gzについて**
  
  HG38からensGeneはなくなったらしいです。
  
  https://groups.google.com/a/soe.ucsc.edu/forum/#!topic/genome/uOROZuefx_Y
  
    The Ensembl Genes track has been replaced on hg38 with the GENCODE Genes track as these two tracks have converged. When using the Table Browser, select the Genes and Gene Predictions group and then select the GENCODE V20 track.  Note that there are various tables available with GENCODE.  For a description of these, see the track description page at http://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=wgEncodeGencodeV20.
  
  代わりに今回はtophatからとってきましたが、ヘッダが付いていてtabixでエラーになるので、そこは手動でスクリプトを変更します。
  
  http://ccb.jhu.edu/software/tophat/downloads/hg38/ensGene.txt.gz


変更が完了したらシェルを実行します．

.. code-block:: bash
  
  bash prepGeneInfo.sh

パイプライン設定ファイルを変更します．更新したディレクトリを以下の項目に指定してください

.. code-block:: cfg

  [sv_filt]
  annotation_dir = /path/to/database/GenomonSV-0.4.0beta/resource_GRCh38
  sv_utils_annotation_dir = /path/to/database/sv_utils-0.4.0beta/resource_GRCh38

(A-9) paplotの設定ファイルを変更する．
--------------------------------------

paplotを使用する場合は、パイプライン設定ファイルに指定されているpaplotの設定ファイルの中身を書き換える必要があります．

まずはpaplot.cfgファイルを適当なディレクトリにコピーして内容を変更します．

.. code-block:: bash

  cp /home/w3varann/.genomon_local/genomon_pipeline-2.5.0/genomon_conf/paplot/paplot_dna.cfg \
     /path/to/database/paplot-0.5.0/paplot_dna_GRCh38.cfg

変更する箇所は [genome] path と [ca] use_chrs(ヒトと染色体数が異なる場合) です．

まずはpathに設定するファイルを作成しましょう．

(A-1)で作成したfasta indexファイルを使用すると簡単に作成できます．

.. code-block:: bash

  cut -f1-2 GRCh38.p7.genome.fa.fai | awk '/^[0-9XY]+/{print $1","$2}' > GRCh38.genome_size
  cut -f1-2 GRCh38.d1.vd1.fa.fai | awk '/^[0-9XY]+/{print $1","$2}' > GRCh38.genome_size

作成したGRCh38.genome_sizeを編集して、1_KI270706v1_random,175055以降の行を削除します。

次にuse_chrsを解析するゲノムの染色体数に合わせてください．

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
  config_file = /path/to/database/paplot-0.5.0/paplot_dna_GRCh38.cfg

paplotのマニュアルを読んでいただけると、こちらの設定についての理解が深まると思います．

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

.. code-block:: bash

  DATABASE_LIST="
  refGene
  ljb26_all
  cosmic70
  esp6500siv2_all
  1000g2014oct
  clinvar_20150629
  "
  
  for DATABASE in $DATABASE_LIST
  do
      ./annotate_variation.pl -buildver hg38 -downdb -webfrom annovar $DATABASE humandb/
  done
  
  ./annotate_variation.pl -buildver hg38 -downdb cytoBand humandb/
  ./annotate_variation.pl -buildver hg38 -downdb genomicSuperDups humandb/


ANNOVARを使用するようにパイプライン設定ファイルを編集します．以下の2か所の変更をお願いします．

.. code-block:: cfg

  [SOFTWARE]
  annovar = [ANNOVARのパスをダウンロードしたANNOVAR]に変更する．
  (例)annovar = /home/genomon/tools/annovar
  
  [annotation]
  active_annovar_flag = True
  iannovar_buildver = hg38
  table_annovar_params = -buildver hg38 -remove --otherinfo -protocol refGene,esp6500siv2_all,1000g2014oct_all,1000g2014oct_afr,1000g2014oct_eas,1000g2014oct_eur,cosmic70,clinvar_20150629,ljb26_all -operation g,f,f,f,f,f,f,f,f
  annovar_database = /home/w3varann/tools/annovar/humandb
  active_HGVD_2013_flag = False
  active_HGVD_2016_flag = False
  active_ExAC_flag = False

(B) RNA解析の設定について
=========================

パイプライン設定ファイルの内容を解析したいゲノムに変更します．

以下のパイプラン設定ファイルを任意のディレクトリにコピーして、内容を変更してください．

/home/w3varann/.genomon_local/genomon_pipeline-2.5.0/genomon_conf/rna_genomon.cfg

今回のGenomon環境は以下のとおりとします．

 - ここで作成するパイプライン設定ファイル： rna_exome_genomon_GRCh38.cfg
 - ここで作成するデータベースのディレクトリ： /path/to/database

.. code-block:: cfg
  :caption: パイプライン設定ファイル（rna_genomon_GRCh38.cfg）
  
  [REFERENCE]
  star_genome = /path/to/database/GRCh38.STAR-2.5.2a
  ref_fasta = /path/to/database/GRCh38/GRCh38.p7.genome.fa <- (A-1)と同じ
  
  [fusionfusion]
  annotation_dir = /path/to/database/fusionfusion-0.2.0beta/resource_GRCh38
  
  [genomon_expression]
  annotation_file = /path/to/database/GenomonExpression-0.2.0/resource_GRCh38/exon.GRCh38.bed
  
  [intron_retention]
  ref_gene = /path/to/database/intron_retention_utils-0.2.0beta/resource_GRCh38/refGene.txt.gz
  params = --chr_name_list /path/to/database/intron_retention_utils-0.2.0beta/resource_GRCh38/ucsc2grch.txt
  
  [paplot]
  config_file = /path/to/database/paplot-0.5.0/paplot_rna_GRCh38.cfg

（B-1）star_genome
-------------------------------------------------

star_genomeにはSTARのindexファイルが格納されているディレクトリのパスを指定します．

・STAR index ファイルを作成します．

STARにはのindexファイルを作成するには、FASTAファイル以外にGTFファイルが必要です．

ftp://ftp.sanger.ac.uk/pub/gencode/Gencode_human/release_25/gencode.v25.annotation.gtf.gz

.. attention::

  GRCh38.p7.genome.faと同じでPrefixにchrが付かないようにファイルの中身を変更しております．

STARコマンドを使用してSTAR indexを作成します．

.. code-block:: bash

  /home/w3varann/.genomon_local/genomon_pipeline-2.5.0/tools/STAR-2.5.2a/bin/Linux_x86_64_static/STAR \
  --runThreadN 8 \
  --runMode genomeGenerate \
  --genomeDir /path/to/database/GRCh38.STAR-2.5.2a \
  --genomeFastaFiles /path/to/database/GRCh38/GRCh38.p7.genome.fa \
  --sjdbGTFfile /path/to/database/GTF/gencode.v25.gtf \
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

annotation_dirを作成しましょう．以下のリソースディレクトリを適当なディレクトリにコピーしてください．

.. code-block:: bash

  cp -r /home/w3varann/.genomon_local/genomon_pipeline-2.5.0/tools/fusionfusion-0.2.0beta/resource \
        /path/to/database/fusionfusion-0.2.0beta/resource_GRCh38

コピー先resourceディレクトリ内のprepGeneInfo.shの中身を変更します

.. code-block:: bash

  # 変更前
  rm –rf GCF_000001405.13.assembly.txt
  wget ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/All/GCF_000001405.13.assembly.txt
  python make_ucsc_grch.py GCF_000001405.13.assembly.txt > grch2ucsc.txt
  wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/refGene.txt.gz
  wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/ensGene.txt.gz
  
  # 変更後
  rm –rf GCF_000001405.33.assembly.txt
  wget ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/All/GCF_000001405.33.assembly.txt
  python make_ucsc_grch.py GCF_000001405.33.assembly.txt > grch2ucsc.txt
  wget http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/refGene.txt.gz
  wget http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/ensGene.txt.gz

※GCF_000001405.33.assembly.txtはGRCm38用です．

※GCF_000001405.33.assembly.txtはSequence-NameとUCSC-style-nameの関係を抽出して、どちらにも対応できるようにするために使用しております．

変更が完了したらシェルを実行します．

.. code-block:: bash

  bash prepGeneInfo.sh

パイプライン設定ファイルを変更します．更新したディレクトリを以下の項目に指定してください．

.. code-block:: cfg

  [fusionfusion]
  annotation_dir = /path/to/database/fusionfusion-0.2.0beta/resource_GRCh38

(B-3) Expressionの設定ファイルを変更する
----------------------------------------

annotation_dirを作成しましょう．以下のリソースディレクトリを適当なディレクトリにコピーしてください．

.. code-block:: bash

  cp -r /home/w3varann/.genomon_local/genomon_pipeline-2.5.0/tools/GenomonExpression-0.2.0/resource \
        /path/to/database/GenomonExpression-0.2.0/resource_GRCh38

コピー先resourceディレクトリ内のprepGeneInfo.shの中身を変更します

.. code-block:: bash

  # 変更前
  rm –rf GCF_000001405.13.assembly.txt
  wget ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/All/GCF_000001405.13.assembly.txt
  wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/refGene.txt.gz
  python proc_ref_exon.py refGene.txt.gz | sort -k1,1 -k2,2n -k3,3n - > exon.hg19.bed
  python proc_ref_exon.GRCh37.py refGene.txt.gz GCF_000001405.13.assembly.txt | sort -k1,1 -k2,2n -k3,3n - > exon.GRCh37.bed
  
  # 変更後
  rm –rf GCF_000001405.33.assembly.txt
  wget ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/All/GCF_000001405.33.assembly.txt
  wget http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/refGene.txt.gz
  python proc_ref_exon.py refGene.txt.gz | sort -k1,1 -k2,2n -k3,3n - > exon.hg38.bed
  python proc_ref_exon.GRCh37.py refGene.txt.gz GCF_000001405.33.assembly.txt | sort -k1,1 -k2,2n -k3,3n - > exon.GRCh38.bed"

変更が完了したらシェルを実行します．

.. code-block:: bash
  
  bash prepGeneInfo.sh

パイプライン設定ファイルを変更します．更新したファイルを以下の項目に指定してください．

.. code-block:: cfg

  [genomon_expression]
  annotation_file = /path/to/database/GenomonExpression-0.2.0/resource_GRCh38/exon.GRCh38.bed

(B-4)intron retentionの設定ファイルを変更する
---------------------------------------------

annotation_dirを作成しましょう．以下のリソースディレクトリを適当なディレクトリにコピーしてください．

.. code-block:: bash

  cp -r /home/w3varann/.genomon_local/genomon_pipeline-2.5.0/tools/intron_retention_utils-0.2.0beta/resource \
        /path/to/database/intron_retention_utils-0.2.0beta/resource_GRCh38

コピー先resourceディレクトリ内のmake_ucsc_grch.shの中身を変更します

.. code-block:: bash

  # 変更前
  rm -rf GCF_000001405.13.assembly.txt
  wget ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/All/GCF_000001405.13.assembly.txt
  python make_ucsc_grch.py GCF_000001405.13.assembly.txt ucsc2grch.txt
  
  # 変更後
  rm -rf GCF_000001635.20.assembly.txt
  wget ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/All/GCF_000001635.20.assembly.txt
  python make_ucsc_grch.py GCF_000001635.20.assembly.txt ucsc2grch.txt

変更が完了したらシェルを実行します．

.. code-block:: bash

  bash make_ucsc_grch.sh

refGene.txtをダウンロードします．

.. code-block:: bash

  wget http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/refGene.txt.gz

パイプライン設定ファイルを変更します．更新したファイルを以下の項目に指定してください．

.. code-block:: cfg

  [intron_retention]
  ref_gene = /path/to/database/intron_retention_utils-0.2.0beta/resource_GRCh38/refGene.txt.gz
  params= --chr_name_list /path/to/database/intron_retention_utils-0.2.0beta/resource_GRCh38/ucsc2grch.txt

(B-5)paplotの設定ファイルを変更する．
-------------------------------------

paplotを使用する場合は、パイプライン設定ファイルに指定されているpaplotの設定ファイルの中身を書き換える必要があります．

まずはpaplot.cfgファイルを適当なディレクトリにコピーして内容を変更します．

.. code-block:: bash

  cp /home/w3varann/.genomon_local/genomon_pipeline-2.5.0/genomon_conf/paplot/paplot_rna.cfg \
     /path/to/database/paplot-0.5.0/paplot_rna_GRCh38.cfg

RNA用のコンフィグファイル、paplot_rna.cfgのコピー後の作業はDNAの「(A-9) paplotの設定ファイルを変更する」と同じです。(A-9)の設定方法を参照ください．
