--------------------------------
Genomonインストール
--------------------------------

.. code-block:: none 

  HGCスパコンユーザの方は以下の設定をしていただければ使用可能になります.
  1. 環境設定
    1-1. pythonの環境設定
    1-2. DRMAAの環境設定
  2. Genomonのインストール
    2-1. Genomon＆必要なパッケージのインストール
    2-2. Annovarを使用したい場合、Annovarのインストールをします
    2-3. HGVDの使用について
  3. Genomonで使用するデータベースとソフトウェアのライセンスについてご理解ください

  HGCスパコンユーザ以外の方は以下の設定が追加で必要です.
  4. 必要な環境
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



4. 必要な環境
^^^^^^^^^^^^^^^^

ここからはHGCスパコン以外のコンピュータにインストールする場合に必要な手順です

* そこそこ大規模な解析ができるサーバ
* Linux
* Drmaa(http://www.drmaa.org/)が使用できるDRMシステム
 ※HGCではGrid Engineを使用しています

5. Genomonで使用しているデータベースのインストール
^^^^^^^^^^^^^^^^
執筆中

6. Genomonで使用しているソフトウェアのインストール
^^^^^^^^^^^^^^^^

GenomonPipeline/genomon.cfgのカテゴリ[SOFTWARE]に記載されているソフトをインストールする必要があります．ご使用のコンピュータにインストールしてgenomon.cfgを書き換えてください

