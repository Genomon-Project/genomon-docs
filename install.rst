--------------------------------
Genomonインストール
--------------------------------

HGCスパコン以外のコンピュータにインストールする場合に必要な手順です．

必須要件
^^^^^^^^
* Linux
* Drmaa(http://www.drmaa.org/)が使用できるDRMシステム
* DRMシステムを入れて運用する程度のスペックのあるサーバ
 ※HGCではGrid Engineを使用しています
 
 
Genomonのインストール
^^^^^^^^^^^^^^^^^^^^^
GenomonとGenomonを動かすのに必要なpythonパッケージのインストールについて記載します．
必要なパッケージは４つです→Genomon，ruffus，PyYAML，drmaa

.. code-block:: bash

  # Genomonのダウンロードとインストール
  wget https://github.com/Genomon-Project/GenomonPipeline/archive/v2.2.0.tar.gz
  tar xzvf v2.2.0.tar.gz
  cd GenomonPipeline-v2.2.0
  python setup.py install --user

  # ruffusのダウンロードとインストール
  wget https://github.com/bunbun/ruffus/archive/v2.6.3.tar.gz
  tar xzvf v2.6.3.tar.gz
  cd ruffus-2.6.3
  python setup.py install --user
  
  # PyYAMLのダウンロード
  git clone https://github.com/ravenac95/PyYAML
  cd PyYAML
  python setup.py install --user

  # drmaa
  pip install drmaa --user


Genomonで使用するデータベースのインストール
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

インストールが必要なデータベースはパイプライン設定ファイルに記載されています．

`ref_fasta`
 | cfgに指定したリファレンスゲノムと，それに紐づくbwa indexファイル，FASTA indexファイルを用意する必要があります．まずはメインのリファレンスゲノムですが，Genomon2では以下の3つのFASTAファイルをマージしたものを使用しています．
 
 | 1) Human Genome                                                                                                   
 | `GRCh37-lite.fa.gz`_
 | 2) Human herpesvirus 4 complete wild type genome
 | http://www.ncbi.nlm.nih.gov/nuccore/82503188?report=fasta
 | 3) decoy
 | `hs37d5cs.fa.gz`_
 
 | リファレンスの特性について詳細は上記の各webサイトの説明よんでください．たとえば，GRCh37-liteはpseudo-autosomal regions on chrY masked with Nsしているなどの記載があります．他にbwa index, fasta indexを生成する必要があります．
 |
 | ・bwa index ファイルの作成コマンド
 | /home/w3varann/genomon_pipeline-2.0.5/tools/bwa-0.7.8/bwa index {マージしたファイル}
 | ・FASTA index ファイルの作成コマンド
 | /home/w3varann/genomon_pipeline-2.0.5/tools/samtools-1.2/samtools faidx {マージしたファイル}
 |
 
`interval_list`
 | 並列処理をするために使用します．以下のサイトからダウンロードしてください
 | https://github.com/Genomon-Project/genomon_utils/blob/master/GRCh37_noScaffold_noDecoy.interval_list

`star_genome`
 | Star indexファイルを作成する必要があります．解析対象のreadのおよその長さに合わせてオプション --sjdbOverhang の指定を変えることができますが，100で大体よいとマニュアルに書いてあって，実際に問題なく検出できているので，現在はread lengthによって変えなくても良しとしています

.. code-block:: bash
    #STAR index ファイルの作成コマンド
    STAR \
    --runThreadN 8 \
    --runMode genomeGenerate \
    --genomeDir $HOME/database/GRCh37.STAR-STAR_2.4.0k \
    --genomeFastaFiles $HOME/database/GRCh37.fa/GRCh37.fa \
    --sjdbGTFfile $HOME/database/GTF/Homo_sapiens.GRCh37.74.gtf \
    --sjdbOverhang 100

`gaptxt`
 | NCBIからダウンロードして解凍してご使用ください（originalのままを使用しています）
 | http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/gap.txt.gz

`bait_file`
 | exomeの場合のbam summaryのcoverageを計算するとき使います．SureSelectなど使用したbaitファイルがある場合はそちらを設定してください．無い場合はrefGene.coding.exon.bedを使用してもらえればと思います．refGene.coding.exon.bed はrefGene.txtのcoding exon領域だけをとりだして，そちらをbaitの範囲としています．作成方法は以下のwebサイトに記載しています．
 | https://github.com/ken0-1n/RefGeneTxtToBed
 | Whole genomeシーケンスの場合はbait_fileを使用しません．WGSの場合はdna_genomon.cfgの以下のハイライトのパラメタをTrueに変更してください．
 
.. code-block:: cfg
    :linenos:
    :emphasize-lines: 4
     
    [coverage]
    qsub_option = -l s_vmem=1G,mem_req=1G
    coverage    = 2,10,20,30,40,50,100
    wgs_flag = False
    wgs_incl_bed_width = 1000000
    wgs_i_bed_lines = 10000
    wgs_i_bed_width = 100


`simple_repeat_tabix_db`
 | NCBIからsimpleRepeat.bedをダウンロードしてtabixのindexファイルをはります．
 | http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/simpleRepeat.txt.gz

.. code-block:: bash

    # tabixを作成する
    cut -f2- simpleRepeat.txt > simpleRepeat.bed
    tabix-0.2.6/bgzip simpleRepeat.bed
    tabix-0.2.6/tabix simpleRepeat.bed.gz

`HGVD_tabix_db`
 | 京都大学からHGVDのファイルをダウンロード，VCF→TAB変換し，tabixのindexファイルをはります．
 | http://www.genome.med.kyoto-u.ac.jp/SnpDB/HGVD1208-V1_42-dbSNP137.tar.gz

.. code-block:: bash

    # tabixを作成する
    python annotator_HGVD.py DBexome20131010.tab | sort -k1,1 -k2,2n -k3,3n -k4,4 -k5,5 -k6,6 > DBexome20131010.bed
    tabix-0.2.6/bgzip DBexome20131010.bed
    tabix-0.2.6/tabix DBexome20131010.bed.gz


・パイプライン設定ファイルの[REFERENCE]に記載されているデータベース一覧

+---------------+--------------------------------------------------------------+----------------------------+
| 項目          | webサイト                                                    | コメント                   |
+===============+==============================================================+============================+
| ref_fasta     | http://www.ncbi.nlm.nih.gov/refseq/publications/             |                            |
|               |                                                              |                            |
+---------------+--------------------------------------------------------------+----------------------------+
| interval_list | https://github.com/Genomon-Project/genomon_utils/blob/master |                            |
|               | GRCh37_noScaffold_noDecoy.interval_list                      |                            |
+---------------+--------------------------------------------------------------+----------------------------+
| star_genome   | SOFTWARE.STARと同じwebサイト                                 | STAR index                 |
+---------------+--------------------------------------------------------------+----------------------------+
| hg19_genome   | SOFTWARE.bedtoolsと同じwebサイト                             | bedtoolsに含まれているFile |
+---------------+--------------------------------------------------------------+----------------------------+
| gaptxt        | http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/     |                            |
+---------------+--------------------------------------------------------------+----------------------------+
| bait_file     | http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/     | refGene.txtをもとに作成    |
+---------------+--------------------------------------------------------------+----------------------------+
| simple_repeat | http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/     | simpleRepeat.txtにtabixをつ|
| _tabix_db     |                                                              | けたもの                   |
+---------------+--------------------------------------------------------------+----------------------------+
| HGVD_tabix_db | http://www.genome.med.kyoto-u.ac.jp/SnpDB/index.html?        | HGVDにtabixをつけたもの    |
+---------------+--------------------------------------------------------------+----------------------------+


・ソフトウェアについて記載一覧

+--------------+-------------------------------------------------------------+----------------------------+
| 項目         | webサイト                                                   | コメント                   |
+==============+=============================================================+============================+
| blat         | https://genome.ucsc.edu/FAQ/FAQblat.html#blat3              | BLAT v. 34                 |
+--------------+-------------------------------------------------------------+----------------------------+
| bwa          | http://bio-bwa.sourceforge.net/                             | bwa-0.7.8                  |
+--------------+-------------------------------------------------------------+----------------------------+
| samtools     | http://samtools.sourceforge.net/                            | samtools-1.2               |
+--------------+-------------------------------------------------------------+----------------------------+
| bedtools     | http://code.google.com/p/bedtools/                          | bedtools-2.24.0            |
+--------------+-------------------------------------------------------------+----------------------------+
| biobambam    | https://github.com/gt1/biobambam                            | biobambam-0.0.191          |
+--------------+-------------------------------------------------------------+----------------------------+
| PCAP         | https://github.com/ICGC-TCGA-PanCancer/PCAP-core            | v1.8.0                     |
+--------------+-------------------------------------------------------------+----------------------------+
| tophat2      | http://ccb.jhu.edu/software/tophat/index.shtml              | 2.0.14.Linux               |
+--------------+-------------------------------------------------------------+----------------------------+
| STAR         | https://github.com/alexdobin/STAR                           | 2.4                        |
+--------------+-------------------------------------------------------------+----------------------------+
| STAR-Fusion  | https://github.com/STAR-Fusion/STAR-Fusion                  | Genomon-v2.0.5では未使用   |
+--------------+-------------------------------------------------------------+----------------------------+
| genomon_sv   | https://github.com/Genomon-Project/GenomonSV                | v0.1.2                     |
+--------------+-------------------------------------------------------------+----------------------------+
| fusionfusion | https://github.com/Genomon-Project/fusionfusion             | v0.1.0                     |
+--------------+-------------------------------------------------------------+----------------------------+
| sv_utils     | https://github.com/friend1ws/sv_utils                       | -0.4.0beta                 |
+--------------+-------------------------------------------------------------+----------------------------+
| mutfilter    | https://github.com/Genomon-Project/GenomonMutationFilter    | v0.2.1                     |
+--------------+-------------------------------------------------------------+----------------------------+
| ebfilter     | https://github.com/Genomon-Project/EBFilter                 | v0.1.1                     |
+--------------+-------------------------------------------------------------+----------------------------+
| fisher       | https://github.com/Genomon-Project/GenomonFisher            | v0.1.1                     |
+--------------+-------------------------------------------------------------+----------------------------+
| mutanno      | https://github.com/Genomon-Project/GenomonMutationAnnotator | v0.1.0                     |
+--------------+-------------------------------------------------------------+----------------------------+
| genomon_pa   | https://github.com/aokad/GenomonPostAnalysis                | v1.0.2                     |
+--------------+-------------------------------------------------------------+----------------------------+
| pa_plot      | https://github.com/Genomon-Project/paplot                   | v0.2.8                     |
+--------------+-------------------------------------------------------------+----------------------------+
| mutil        | https://github.com/Genomon-Project/GenomonMutationAnnotator | v0.3.0                     |
+--------------+-------------------------------------------------------------+----------------------------+
| ANNOVAR      | http://annovar.openbioinformatics.org/en/latest/            | versionは最新でよい        |
+--------------+-------------------------------------------------------------+----------------------------+








実行時の環境設定
^^^^^^^^^^^^^^^^
ジョブを投入するときに使うDRAMMのライブラリを設定します．

.. code-block:: bash

  # N1GE用のDRMAA（HGCスパコンであればこちらでOK）です．ご使用しているDRMシステムのライブラリに変更をお願いします．
  export DRMAA_LIBRARY_PATH= the path to the libdrmaa.so.1.0

 
2-2. ANNOVARを使用したい場合，ANNOVARのインストールをします

| ANNOVARのダウンロードにはユーザ登録 (User License Agreement) が必要です．
| http://www.openbioinformatics.org/annovar/annovar_download_form.php
| ANNOVARのホームページにてユーザ登録 (User License Agreement) が完了した後に，登録したメールアドレスにANNOVARをダウンロードするためのリンクが記載されたメールが届きます．そのリンクを使用してANNOVARをダウンロードします．ダウンロード後はANNOVARのPerlスクリプトを使用して各種データ (dbsnp131など) をダウンロードします．

.. code-block:: bash

  # Genomonで必要なANNOVARのデータベースをダウンロードします．Copy and Pasteして使ってください． 
  DATABASE_LIST="
  refGene
  avsift
  ljb26_all
  cosmic68wgs
  cosmic70
  esp6500siv2_all
  1000g2010nov
  1000g2014oct
  snp131
  snp138
  snp131NonFlagged
  snp138NonFlagged
  clinvar_20150629
  "
  for DATABASE in $DATABASE_LIST
  do
    ./annotate_variation.pl -buildver hg19 -downdb -webfrom annovar $DATABASE humandb/
  done
  ./annotate_variation.pl -buildver hg19 -downdb cytoBand humandb/
  ./annotate_variation.pl -buildver hg19 -downdb genomicSuperDups humandb/

ANNOVARを使用するようにdna_genomon.cfgを編集する．以下の2か所の変更をお願いします．

.. code-block:: bash

  [SOFTWARE]
  annovar = [ANNOVARのパスをダウンロードしたANNOVAR]に変更する．
  (例)annovar = /home/genomon/tools/annovar

  [annotation]
  active_annovar_flag = False
  をTrueに変更する (ANNOVARの使用する/しない)を管理しているフラグになります．デフォルトはFalseになります．

2-3. HGVDの使用について

| HGVDのサイトのをお読みいただいた上，使用規約等に問題がなければdna_genomon.cfgを編集する
| http://www.genome.med.kyoto-u.ac.jp/SnpDB/about.html

.. code-block:: bash

  active_HGVD_flag = False
  をTrueに変更する (HGVDの使用する/しない)を管理しているフラグになります．デフォルトはFalseになります．

  



ここからはHGCスパコン以外のコンピュータにインストールする場合に必要な手順です．
GenomonはHGC以外のスパコンではないサーバでも稼働実績があります．



4. Genomonで使用しているデータベースのインストール
^^^^^^^^^^^^^^^^




5. Genomonで使用しているソフトウェアのインストール
^^^^^^^^^^^^^^^^

GenomonPipeline/{dna/rna}_genomon.cfgのカテゴリ[SOFTWARE]に記載されているソフトをインストールする必要があります．ご使用のコンピュータにインストールして${dna/rna}_genomon.cfgを書き換えてください


.. _GRCh37-lite.fa.gz: ftp://ftp.ncbi.nih.gov/genomes/archive/old_genbank/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh37/special_requests/GRCh37-lite.fa.gz
.. _hs37d5cs.fa.gz: ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5cs.fa.gz
