Genomonインストール
-------------------

HGCスパコン以外のコンピュータにインストールする場合に必要な手順です．

`ライセンスを順守してください． <./license.html>`__

インストール必須要件
^^^^^^^^^^^^^^^^^^^^
* Linux
* python2.7
* Drmaa(http://www.drmaa.org/)が使用できるDRMシステム
* DRMシステムを入れて運用する程度のスペックのあるコンピュータ

| ※HGCスパコンではGrid Engineを使用しています

Genomonのインストール
^^^^^^^^^^^^^^^^^^^^^
GenomonとGenomonを動かすのに必要なpythonパッケージのインストールについて記載します．
必要なパッケージは６つです→Genomon，ruffus，PyYAML，drmaa，pmsignature，annot_utils

.. code-block:: bash

  # インストールを始める前に，
  # python2.7であることを確認してください．

  # Genomonのダウンロードとインストール
  wget https://github.com/Genomon-Project/GenomonPipeline/archive/v${version}.tar.gz
  tar xzvf v${version}.tar.gz
  cd GenomonPipeline-v${version}
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
 
  # pmsignature
  # https://github.com/friend1ws/pmsignature を参照してください
  
  # annot_utilsのダウンロードとインストール
  wget -nc https://github.com/friend1ws/annot_utils/archive/v0.1.0.zip
  unzip v0.1.0.zip
  cd annot_utils-0.1.0
  python setup.py install


Genomonで使用するデータベースのインストール
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

インストールが必要なデータベースはパイプライン設定ファイルに記載されています．ご使用のコンピュータに各データベースをインストールしてパイプライン設定ファイルの[REFERENCE]に記載されているパスを書き換えてください．

`ref_fasta`
 | cfgに指定したリファレンスゲノムと，それに紐づくBWA indexファイル，FASTA indexファイルを用意する必要があります．まずはメインのリファレンスゲノムですが，Genomon2では以下の3つのFASTAファイルをマージしたものを使用しています．
 
 | 1) Human Genome                                                                                                   
 | `GRCh37-lite.fa.gz`_
 | 2) Human herpesvirus 4 complete wild type genome
 | http://www.ncbi.nlm.nih.gov/nuccore/82503188?report=fasta
 | 3) decoy
 | `hs37d5cs.fa.gz`_
 
 | リファレンスの特性について詳細は上記の各webサイトの説明よんでください．たとえば，GRCh37-liteはpseudo-autosomal regions on chrY masked with Nsしているなどの記載があります．他にBWA index, FASTA indexを生成する必要があります．
 |
 | ・BWA index ファイルの作成コマンド
 | /share/pub/genomon/.genomon_local/genomon_pipeline-2.6.3/install/bwa-0.7.8/bwa index {マージしたファイル}
 | ・FASTA index ファイルの作成コマンド
 | /share/pub/genomon/.genomon_local/genomon_pipeline-2.6.3/install/samtools-1.2/samtools faidx {マージしたファイル}
 
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
    --genomeDir $HOME/database/GRCh37.STAR-${STAR_version} \
    --genomeFastaFiles $HOME/database/GRCh37.fa/GRCh37.fa \
    --sjdbGTFfile $HOME/database/GTF/Homo_sapiens.GRCh37.74.gtf \
    --sjdbOverhang 100

`gaptxt`
 | NCBIからダウンロードして解凍してご使用ください.（originalのままを使用しています）
 | http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/gap.txt.gz

`bait_file`
 | exomeの場合のbam summaryのcoverageを計算するとき使います．SureSelectなど使用したbaitファイルがある場合はそちらを設定してください．無い場合はrefGene.coding.exon.bedを使用してもらえればと思います．refGene.coding.exon.bed はrefGene.txtのcoding exon領域だけをとりだして，そちらをbaitの範囲としています．作成方法は以下のwebサイトに記載しています．
 | (スクリプト修正中です)https://github.com/ken0-1n/RefGeneTxtToBed（しばらくお待ちください）
 | Whole genomeシーケンスの場合はbait_fileを使用しません．Whole Genomeの解析の場合はパイプライン設定ファイルの以下のハイライトのパラメタをTrueに変更してください．
 
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

    # TAB変換のツールはこちら
    git clone https://github.com/Genomon-Project/genomon_utils
    # tabixを作成する
    python genomon_utils/annotator_HGVD.py DBexome20131010.tab | sort -k1,1 -k2,2n -k3,3n -k4,4 -k5,5 -k6,6 > DBexome20131010.bed
    tabix-0.2.6/bgzip DBexome20131010.bed
    tabix-0.2.6/tabix DBexome20131010.bed.gz


Genomonで呼び出されるソフトウェアのインストール
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

インストールが必要なソフトウェアはパイプライン設定ファイルに記載されています．ご使用のコンピュータに各ソフトウェアをインストールしてパイプライン設定ファイルの[SOFTWARE]に記載されているパスを書き換えてください

**DNAパイプライン設定ファイル**

+------------------------+-------------------------------------------------------------+----------------------------+
| 項目                   | webサイト                                                   | バージョン                 |
+========================+=============================================================+============================+
| blat                   | https://genome.ucsc.edu/FAQ/FAQblat.html#blat3              | BLAT v.34                  |
+------------------------+-------------------------------------------------------------+----------------------------+
| bwa                    | http://bio-bwa.sourceforge.net/                             | bwa-0.7.8                  |
+------------------------+-------------------------------------------------------------+----------------------------+
| samtools               | http://samtools.sourceforge.net/                            | samtools-1.2               |
+------------------------+-------------------------------------------------------------+----------------------------+
| bedtools               | http://code.google.com/p/bedtools/                          | bedtools-2.24.0            |
+------------------------+-------------------------------------------------------------+----------------------------+
| biobambam              | https://github.com/gt1/biobambam                            | biobambam-0.0.191          |
+------------------------+-------------------------------------------------------------+----------------------------+
| bamstats               | https://github.com/ICGC-TCGA-PanCancer/PCAP-core            | PCAP-core-v1.8.1           |
+------------------------+-------------------------------------------------------------+----------------------------+
| hstlib                 | http://www.htslib.org/download/                             | htslib-1.3                 |
+------------------------+-------------------------------------------------------------+----------------------------+
| r_scripts              | https://github.com/Genomon-Project/genomon_Rscripts         | v0.1.3                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| genomon_sv             | https://github.com/Genomon-Project/GenomonSV                | v0.6.1rc                   |
+------------------------+-------------------------------------------------------------+----------------------------+
| sv_utils               | https://github.com/friend1ws/sv_utils                       | v0.5.1                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| mutfilter              | https://github.com/Genomon-Project/GenomonMutationFilter    | v0.2.1                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| ebfilter               | https://github.com/Genomon-Project/EBFilter                 | v0.2.1                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| fisher                 | https://github.com/Genomon-Project/GenomonFisher            | v0.2.0                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| mutanno                | https://github.com/Genomon-Project/GenomonMutationAnnotator | v0.1.0                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| genomon_qc             | https://github.com/Genomon-Project/GenomonQC                | v2.0.1                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| genomon_pa             | https://github.com/aokad/GenomonPostAnalysis                | v1.4.1                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| paplot                 | https://github.com/Genomon-Project/paplot                   | v0.5.5                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| mutil                  | https://github.com/ken0-1n/mutation_util                    | v0.5.0                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| hotspot                | https://github.com/ken0-1n/GenomonHotspotCall/releases      | v0.1.0                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| ANNOVAR                | http://annovar.openbioinformatics.org/en/latest/            | latest                     |
+------------------------+-------------------------------------------------------------+----------------------------+

**RNAパイプライン設定ファイル**

+------------------------+-------------------------------------------------------------+----------------------------+
| 項目                   | webサイト                                                   | バージョン                 |
+========================+=============================================================+============================+
| samtools               | http://samtools.sourceforge.net/                            | samtools-1.2               |
+------------------------+-------------------------------------------------------------+----------------------------+
| tophat2                | http://ccb.jhu.edu/software/tophat/index.shtml              | 2.0.14.Linux               |
+------------------------+-------------------------------------------------------------+----------------------------+
| STAR                   | https://github.com/alexdobin/STAR                           | 2.5.2a                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| STAR-Fusion            | https://github.com/STAR-Fusion/STAR-Fusion                  | Genomon-v2.5.0では未使用   |
+------------------------+-------------------------------------------------------------+----------------------------+
| bedtools               | http://code.google.com/p/bedtools/                          | bedtools-2.24.0            |
+------------------------+-------------------------------------------------------------+----------------------------+
| biobambam              | https://github.com/gt1/biobambam                            | biobambam-0.0.191          |
+------------------------+-------------------------------------------------------------+----------------------------+
| blat                   | https://genome.ucsc.edu/FAQ/FAQblat.html#blat3              | BLAT v.34                  |
+------------------------+-------------------------------------------------------------+----------------------------+
| hstlib                 | http://www.htslib.org/download/                             | htslib-1.3                 |
+------------------------+-------------------------------------------------------------+----------------------------+
| fusionfusion           | https://github.com/Genomon-Project/fusionfusion             | v0.4.0                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| fusion_utils           | https://github.com/friend1ws/fusion_utils                   | v0.2.0                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| chimera_utils          | https://github.com/friend1ws/chimera_utils                  | v0.5.1                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| intron_retention_utils | https://github.com/friend1ws/intron_retention_utils         | v0.5.1                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| genomon_expression     | https://github.com/Genomon-Project/GenomonExpression        | v0.4.0                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| genomon_pa             | https://github.com/aokad/GenomonPostAnalysis                | v1.4.1                     |
+------------------------+-------------------------------------------------------------+----------------------------+
| paplot                 | https://github.com/Genomon-Project/paplot                   | v0.5.5                     |
+------------------------+-------------------------------------------------------------+----------------------------+

STAR-FusionはGenomon-v2.6.3 では未使用ですが，現バージョンでは設定のみ必要ですので，適当な空ファイルへのリンクを設定してください．

**ANNOVARを使用する場合の設定について**

| 以下を参考にしてください。
| https://genomon.readthedocs.io/ja/latest/dna_quick_start.html#annovargenomon

**HGVDを使用する場合の設定について**

| HGVDのサイトのをお読みいただいた上，使用規約等に問題がなければパイプライン設定ファイルを編集する
| http://www.genome.med.kyoto-u.ac.jp/SnpDB/about.html

.. code-block:: bash

  active_HGVD_2013_flag = False
  active_HGVD_2016_flag = False
  FalseをTrueに変更する (HGVDの使用する/しない)を管理しているフラグになります．デフォルトはFalseになります．


**ExACを使用する場合の設定について**

| ExACのサイトのをお読みいただいた上，使用規約等に問題がなければパイプライン設定ファイルを編集する
| http://exac.broadinstitute.org/faq

.. code-block:: bash

  active_ExAC_flag = False
  FalseをTrueに変更する (ExACの使用する/しない)を管理しているフラグになります．デフォルトはFalseになります．
 

実行時の環境設定
^^^^^^^^^^^^^^^^
ジョブを投入するときに使うDRAMMのライブラリを設定します．

.. code-block:: bash

  # N1GE用のDRMAA（HGCスパコンであればこちらでOK）です．ご使用しているDRMシステムのライブラリに変更をお願いします．
  export DRMAA_LIBRARY_PATH= the path to the libdrmaa.so.1.0


.. _GRCh37-lite.fa.gz: ftp://ftp.ncbi.nih.gov/genomes/archive/old_genbank/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh37/special_requests/GRCh37-lite.fa.gz
.. _hs37d5cs.fa.gz: ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5cs.fa.gz
