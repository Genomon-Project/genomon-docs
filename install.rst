--------------------------------
Genomonインストール
--------------------------------

.. code-block:: none 

  HGCスパコンユーザの方は以下(1,2,3)の設定をしていただければ使用可能になります.
  1. 環境設定
    1-1. pythonの環境設定
    1-2. DRMAAの環境設定
  2. Genomonのインストール
    2-1. Genomon＆必要なパッケージのインストール
    2-2. Annovarを使用したい場合、Annovarのインストールをします
    2-3. HGVDの使用について
  3. Genomonで使用するデータベースとソフトウェアのライセンスについてご理解ください

  HGCスパコンユーザ以外の方は以下の設定が追加で必要です.
  4. 必要なマシンスペック
  5. Genomonで使用しているデータベースのインストール
  6. Genomonで使用しているソフトウェアのインストール

1. 環境設定
^^^^^^^^^^^^^^^^
1-1. pythonの環境設定
Genomonではpythonバージョン2.7を使用します.

.. code-block:: bash

  # python 2.7以外の場合は以下をExportしてください
  export PYTHONHOME=/usr/local/package/python/2.7.10
  export PATH=${PYTHONHOME}/bin:$PATH
  export LD_LIBRARY_PATH=${PYTHONHOME}/lib:${LD_LIBRARY_PATH}
  export PYTHONPATH=~/.local/lib/python2.7/site-packages
  
1-2. DRMAAの環境設定
スパコンにジョブを投入するときに使うライブラリを設定します．

.. code-block:: bash

  # N1GE用のDRMAA（HGCスパコンであればこちらでOK）です。ご使用しているDRMシステムのライブラリに変更をお願いします。
  export DRMAA_LIBRARY_PATH=/geadmin/N1GE/lib/lx-amd64/libdrmaa.so.1.0

これらのexportを~/.bash_profileに記載しておいた方が楽です（今まで使用していたpythonのツールに影響がなければ推奨）．

2. Genomonのインストール
^^^^^^^^^^^^^^^^
2-1. Genomon＆必要なパッケージのインストール
必要なパッケージは６つです→GenomonPipeline,ruffus,PyYAML,drmaa,xlwt,xlrd

.. code-block:: bash

  # genomon-pipeline(本体)のダウンロード
  wget https://github.com/Genomon-Project/GenomonPipeline/archive/v${ダウンロードしたバージョン}.tar.gz
  tar xzvf v${ダウンロードしたバージョン}.tar.gz
  # ruffusのダウンロード
  wget https://github.com/bunbun/ruffus/archive/v2.6.3.tar.gz
  tar xzvf v2.6.3.tar.gz
  # PyYAMLのダウンロード
  git clone https://github.com/ravenac95/PyYAML
  # drmaa,xlwt,xlrdのインストール
  pip install drmaa --user
  pip install xlwt --user
  pip install xlrd --user
  # genomon-pipeline(本体)のインストール
  cd GenomonPipeline-${ダウンロードしたバージョン}
  python setup.py install --user
  # ruffusのインストール
  cd ../ruffus-2.6.3
  python setup.py install --user
  # PyYAMLのインストール
  cd ../PyYAML
  python setup.py install --user
  
2-2. Annovarを使用したい場合、Annovarのインストールをします

| ANNOVARのダウンロードにはユーザ登録 (User License Agreement) が必要です．
| http://www.openbioinformatics.org/annovar/annovar_download_form.php
| ANNOVARのホームページにてユーザ登録 (User License Agreement) が完了した後に，登録したメールアドレスにANNOVARをダウンロードするためのリンクが記載されたメールが届きます．そのリンクを使用してANNOVARをダウンロードします．ダウンロード後はANNOVARのPerlスクリプトを使用して各種データ (snp131など) をダウンロードします．

.. code-block:: bash

  # Genomonで必要なAnnovarのデータベースをダウンロードします．コピペして使ってください． 
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

ANNOVARを使用するようにgenomon.cfgを編集する

.. code-block:: bash

  [SOFTWARE]
  annovar = [annovarのパスをダウンロードしたannovar]に変更する．
  (例)annovar = /home/genomon/tools/annovar

dna_task_param.cfgを編集する

.. code-block:: bash

  [annotation]
  active_annovar_flag = False
  をTrueに変更する (Annovarの使用する/しない)を管理しているフラグになります．デフォルトはFalseになります．

2-3. HGVDの使用について

| HGVDのサイトのをお読みいただいた上、問題がなければdna_task_param.cfgを編集する
| http://www.genome.med.kyoto-u.ac.jp/SnpDB/about.html

.. code-block:: bash

  active_HGVD_flag = False
  をTrueに変更する (HGVDの使用する/しない)を管理しているフラグになります．デフォルトはFalseになります．

  
3. Genomonで使用するデータベースとソフトウェアのライセンスについてご理解ください
^^^^^^^^^^^^^^^^

Genomonで使用するデータベースとソフトウェアは、インストールしたGenomonPipeline/genomon.cfgに記載されています。各々のライセンスについてご理解のうえ、Genomonをご使用いただければと思います。

・REFERENCE　データベースについて記載一覧

+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| 項目         | ライセンス            | webサイト                                                   | コメント                   |
+==============+=======================+=============================================================+============================+
| ref_fasta    | citationのrequest有   | http://www.ncbi.nlm.nih.gov/refseq/publications/            | Reference Genome, bwa index|
|              |                       |                                                             | and fasta index.           |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| interval_lis | freely usable         | ―                                                           | 自作品                     |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| star_genome  | ?                     | ―                                                           | STAR index                 |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| hg19_genome  | bedtoolsに含まれる    | SOFTWARE.bedtoolsと同じwebサイトと同じ                      | bedtoolsに含まれているFile |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| gaptxt       | freely usable         | http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/    |                            |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| bait_file    | freely usable         | http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/    | refGene.txtをもとに作成    |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| simple_repeat| freely usable         | http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/    | simpleRepeat.txtにtabixをつ|
| _tabix_db    |                       |                                                             | けたもの                   |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| HGVD_tabix_db| citationのrequest有   | http://www.genome.med.kyoto-u.ac.jp/SnpDB/index.html?       | HGVDにtabixをつけたもの    |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+

・SOFRWARE　ソフトウェアについて記載一覧

+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| 項目         | ライセンス            | webサイト                                                   | コメント                   |
+==============+=======================+=============================================================+============================+
| blat         | 独自ライセンス        | https://genome.ucsc.edu/FAQ/FAQblat.html#blat3              | BLAT v. 34                 |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| bwa          | GNU GPL v3            | http://bio-bwa.sourceforge.net/                             | bwa-0.7.8                  |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| samtools     | The MIT/Expat License | http://samtools.sourceforge.net/                            | samtools-1.2               |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| bedtools     | GNU GPL v2            | http://code.google.com/p/bedtools/                          | bedtools-2.24.0            |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| biobambam    | GNU GPL v3            | https://github.com/gt1/biobambam                            | biobambam-0.0.191          |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| PCAP         | GNU GPL v2            | https://github.com/ICGC-TCGA-PanCancer/PCAP-core            | v1.8.0                     |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| tophat2      | Artistic License 1.0  | http://ccb.jhu.edu/software/tophat/index.shtml              | 2.0.14.Linux               |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| STAR         | GNU GPL v3            | https://github.com/alexdobin/STAR                           | 2.4                        |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| STAR-Fusion  | GNU GPL v3            | https://github.com/STAR-Fusion/STAR-Fusion                  | Genomon-v2.0.5では未使用   |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| genomon_sv   | GNU GPL v3            | https://github.com/Genomon-Project/GenomonSV                | v0.1.2                     |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| fusionfusion | GNU GPL v3            | https://github.com/Genomon-Project/fusionfusion             | v0.1.0                     |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| mutfilter    | GNU GPL v3            | https://github.com/Genomon-Project/GenomonMutationFilter    | v0.1.0                     |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| ebfilter     | GNU GPL v3            | https://github.com/Genomon-Project/EBFilter                 | v0.1.1                     |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| fisher       | GNU GPL v3            | https://github.com/Genomon-Project/GenomonFisher            | v0.1.1                     |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| mutanno      | GNU GPL v3            | https://github.com/Genomon-Project/GenomonMutationAnnotator | v0.1.0                     |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+
| annovar      | 独自ライセンス        | http://annovar.openbioinformatics.org/en/latest/            | versionは最新でよい        |
+--------------+-----------------------+-------------------------------------------------------------+----------------------------+



4. 必要なマシンスペック
^^^^^^^^^^^^^^^^

ここからはHGCスパコン以外のコンピュータにインストールする場合に必要な手順です．
HGC以外のスパコンではないサーバにもGenomonをインストールさせていただいており、稼働実績があります．

* Linux
* Drmaa(http://www.drmaa.org/)が使用できるDRMシステム
 ※HGCではGrid Engineを使用しています

5. Genomonで使用しているデータベースのインストール
^^^^^^^^^^^^^^^^
GenomonPipeline/${dna/rna}_genomon.cfgのカテゴリ[REFERENCE]に記載されているソフトをインストールする必要があります．ご使用のコンピュータにインストールして${dna/rna}_genomon.cfgを書き換えてください

`ref_fasta`
 | cfgに指定したリファレンスゲノムと、それに紐づくbwa indexファイル、FASTA indexファイルを用意する必要があります。まずはメインのリファレンスゲノムですが、Genomon2では以下の3つのFASTAファイルをマージしたものを使用しています。
 |
 | 1) Human Genome ftpサイトが変更されていた (2016.01.28確認)
 | ftp://ftp.ncbi.nih.gov/genomes/archive/old_genbank/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh37/special_requests/GRCh37-lite.fa.gz
 | 2) Human herpesvirus 4 complete wild type genome
 | http://www.ncbi.nlm.nih.gov/nuccore/82503188?report=fasta
 | 3) decoy
 | ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5cs.fa.gz
 |
 | リファレンスの特性について詳細は上記の各webサイトの説明よんでください。たとえば、GRCh37-liteはpseudo-autosomal regions on chrY masked with Nsしているなどの記載があります。他にbwa index, fasta indexを生成する必要があります。
 |
 | ・bwa index ファイルの作成コマンド
 | /home/w3varann/genomon_pipeline-2.0.5/tools/bwa-0.7.8/bwa index {マージしたファイル}
 | ・FASTA index ファイルの作成コマンド
 | /home/w3varann/genomon_pipeline-2.0.5/tools/samtools-1.2/samtools faidx {マージしたファイル}
 |
 
`interval_list`
 | 自作したファイルです。並列処理をするために使用します。

`star_genome`
 | Star indexファイルを作成する必要があります．解析対象のreadのおよその長さに合わせてオプション --sjdbOverhang の指定を変えることができますが、100で大体よいとマニュアルに書いてあって、実際に問題なく検出できているので、現在はread lengthによって変えなくても良しとしています

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
 | exomeの場合のbam summaryのcoverageを計算するとき使います。SureSelectなど使用したbaitファイルがある場合はそちらを設定してください．無い場合はrefGene.coding.exon.bedを使用してもらえればと思います。refGene.coding.exon.bed はrefGene.txtのcoding exon領域だけをとりだして、そちらをbaitの範囲としています。作成方法は以下のwebサイトに記載しています。
 | https://github.com/ken0-1n/RefGeneTxtToBed
 | Whole genomeシーケンスの場合はbait_fileを使用しません。WGSの場合はdna_genomon.cfgの以下のハイライトのパラメタをTrueに変更してください．
 
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
 | NCBIからsimpleRepeat.bedをダウンロードしてtabixのindexファイルをはります。
 | http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/simpleRepeat.txt.gz

.. code-block:: bash

    # tabixを作成する
    cut -f2- simpleRepeat.txt > simpleRepeat.bed
    tabix-0.2.6/bgzip simpleRepeat.bed
    tabix-0.2.6/tabix simpleRepeat.bed.gz

`HGVD_tabix_db`
 | 京都大学からHGVDのファイルをダウンロード、VCF→TAB変換し、tabixのindexファイルをはります。
 | http://www.genome.med.kyoto-u.ac.jp/SnpDB/HGVD1208-V1_42-dbSNP137.tar.gz

.. code-block:: bash

    # tabixを作成する
    python annotator_HGVD.py DBexome20131010.tab | sort -k1,1 -k2,2n -k3,3n -k4,4 -k5,5 -k6,6 > DBexome20131010.bed
    tabix-0.2.6/bgzip DBexome20131010.bed
    tabix-0.2.6/tabix DBexome20131010.bed.gz



6. Genomonで使用しているソフトウェアのインストール
^^^^^^^^^^^^^^^^

GenomonPipeline/{dna/rna}_genomon.cfgのカテゴリ[SOFTWARE]に記載されているソフトをインストールする必要があります．ご使用のコンピュータにインストールして${dna/rna}_genomon.cfgを書き換えてください

