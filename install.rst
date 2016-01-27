--------------------------------
Genomonインストール
--------------------------------

| HGCスパコンユーザの方は以下2つの設定をしていただければ使用可能になります。
+ pythonの環境設定
+ Genomonと実行に必要なパッケージのインストール
| Annovarを使用したい場合は別途Annovarのインストールをしてください。
| 
| HGCスパコン以外のコンピュータにインストールする場合
| 必要な環境
1. Linux
2. Drmaa(http://www.drmaa.org/)が使用できるDRMシステム(HGCではGrid Engineを使用しています)  

pythonの環境設定
----------------
バージョンが2.7以外である場合は以下をExportしてください.

.. code-block:: bash

  $export PYTHONHOME=/usr/local/package/python2.7/current
  $export PATH=$PYTHONHOME/bin:$PATH
  $export LD_LIBRARY_PATH=/usr/local/package/python2.7/current/lib:$LD_LIBRARY_PATH
  $export PYTHONPATH=~/.local/lib/python2.7/site-packages
  $export DRMAA_LIBRARY_PATH=/geadmin/N1GE/lib/lx-amd64/libdrmaa.so.1.0

これらを~/.bash_profileに記載しておいた方がいいです．

Genomonと必要なパッケージのインストール
---------------------------------------
必要なパッケージはこちら→GenomonPipeline,ruffus,PyYAML,drmaa, xlwt,xlrd

.. code-block:: bash

  # genomon-pipeline(本体)のダウンロード
  $wget https://github.com/Genomon-Project/GenomonPipeline/archive/v2.0.2.tar.gz
  $tar xzvf v2.0.2.tar.gz
  # ruffusのダウンロード
  $wget https://github.com/bunbun/ruffus/archive/v2.6.3.tar.gz
  $tar xzvf v2.6.3.tar.gz
  # PyYAMLのダウンロード
  $git clone https://github.com/ravenac95/PyYAML
  # drmaa,xlwt,xlrdのインストール
  $pip install drmaa --user
  $pip install xlwt --user
  $pip install xlrd --user
  # genomon-pipeline(本体)のインストール
  $cd GenomonPipeline-2.0.2
  $python setup.py install --user
  # ruffusのインストール
  $cd ../ruffus-2.6.3
  $python setup.py install --user
  # PyYAMLのインストール
  $cd ../PyYAML
  $python setup.py install --user
  
Genomonで使用しているソフトウェア
---------------------------------  

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
| STAR-Fusion  | GNU GPL v3            | https://github.com/STAR-Fusion/STAR-Fusion                  | Genomon2-v2.0.5では未使用  |
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


