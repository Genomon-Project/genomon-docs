Genomon Pipeline 実行の手引き
================================

ここでは，解析手順の説明にユーザアカウント ``lect-1`` を用いますが，実際のユーザアカウントに読み替えてください．

1. 解析実行
=============

.. note::

  | HGCのスパコンをご利用の場合，以下を参照ください．
  | ※ 資料中のバージョンは2.2.0で記載していますが，最新のバージョンをご使用ください．
  |
  | `Genomon2 Tutorial (2016 年 5 月 24 日実施)資料 <https://supcom.hgc.jp/internal/materials/lect-pdf/20160524/Genomon2_Tutorial_3.pdf>`__

1-1. スパコンへのログイン
-------------------------------

お持ちのユーザアカウントでスパコンのログインサーバにSSHで接続します．

1-2. 作業ディレクトリの準備
-------------------------------

シーケンスファイルやGenomonPipeline設定ファイルのパスや名称は任意ですが，ここでは下記のディレクトリ構成を用います．

::
  
  /home/lect-1/Genomon2_5_2/ ：作業ディレクトリ
     ├ config/                 ：サンプル設定ファイル/パイプライン設定ファイル
     │  ├ dna_genomon.cfg
     │  ├ rna_genomon.cfg
     │  └ test5929.csv
     │
     ├ raw/                    ：解析対象ファイル
     │  ├ fastq/                ：Fastqファイル
     │  │  ├ test_1.fastq
     │  │  └ test_2.fastq
     │  └ bam/                  ：BAMファイル
     │      ├ test.bam
     │      └ test.bam.bai
     │
     └ script/                 ：Genomon実行ファイル
         ├ genomon_pipeline.sh
         └ qsub_genomon_pipeline.sh
     

BAMファイルを解析データとして使用する場合，BAM Indexファイル (BAIファイル) も合わせて配置してください．

1-3. サンプル設定ファイルの作成
----------------------------------

サンプル設定ファイルは，解析対象として入力するFastqやBAMファイルのパスや実行する解析の内容を記述するものです．
サンプル設定ファイルの詳細については，下記のGenomonドキュメントを参照ください．

 - `DNAサンプル設定ファイルについて <http://genomon.readthedocs.io/ja/latest/dna_sample_csv.html>`__
 - `RNAサンプル設定ファイルについて <http://genomon.readthedocs.io/ja/latest/rna_sample_csv.html>`__

本書では，前述の作業ディレクトリ内に ``config`` ディレクトリを作成し，この中に配置します．

.. attention::

  **サンプル名とパスの記載について**
  
  | [fastq], [bam_import], [bam_tofastq] ではサンプル名とパスを設定しますが，手動で作成するためどうしても間違いがおこりやすいところです．
  | 十分ご注意ください．
  
  - リード1とリード2の組み合わせはあっていますか？
  - サンプル名とパスの組み合わせはあっていますか？


1-4. パイプライン設定ファイルの準備
-------------------------------------

パイプライン設定ファイルはGenomon各解析ツールのパスやパラメータを設定するものです．

.. note::

  **ANNOVARのインストールについて**
  
  | GenomonのDNA解析ではANNOVARというアノテーションツールを使用しています．
  | ANNOVARをインストールしなくてもGenomonは実行できますが，Genomonの結果をグラフに描画する機能（paplot）ではANNOVARの出力結果を参照していますので，ANNOVARの設定を行うことをお奨めしています．
  | `ANNOVARのインストールとGenomonへの設定方法 <http://genomon.readthedocs.io/ja/latest/dna_quick_start.html#id1>`__

パイプライン設定ファイルの詳細については，下記のGenomonドキュメントを参照ください．
 
 - `DNAパイプライン設定ファイルについて <http://genomon.readthedocs.io/ja/latest/dna_config_info.html>`__
 - `RNAパイプライン設定ファイルについて <http://genomon.readthedocs.io/ja/latest/rna_config_info.html>`__


1-5. Genomon解析コマンドの実行
-------------------------------

Genomonを実行するために以下2つのスクリプトを用意します．一つはGenomonをジョブとして投入するためのスクリプト，もう一つはジョブとして投入されるスクリプトです．

 .. note::
  HGCスパコンの場合，スクリプトは ``/home/w3varann/genomon_pipeline-2.5.2/genomon_script/genomon_pipeline_HGC.sh`` にあります．


以下スクリプトのパスについては環境に合わせて適宜変更ください．

.. code-block:: bash
  :caption: genomon_pipeline.sh
  
  #! /bin/bash
  
  # $1 target_pipeline
  # $2 sample_conf
  # $3 project_dir
  # $4 genomon_conf
  # $5 qsub_option
  # $6 ruffus_option
  
  qsub $5 -o ${project_dir}/log -e ${project_dir}/log /home/lect-1/Genomon2_5_2/script/qsub_genomon_pipeline.sh $1 $2 $3 $4 "$6"

.. code-block:: bash
  :caption: qsub_genomon_pipeline.sh
  
  #$ -S /bin/bash         # set shell in UGE
  #$ -cwd                 # execute at the submitted dir
  #$ -l s_vmem=128G,mem_req=128G
  #$ -q ljobs.q,lmem.q
  #$ -r no
  
  export PYTHONHOME={Pythonのパス}
  export PYTHONPATH={Genomonをインストールしたディレクトリ}/python2.7-packages/lib/python
  export PATH=${PYTHONHOME}/bin:${PATH}
  export LD_LIBRARY_PATH=${PYTHONHOME}/lib:${LD_LIBRARY_PATH}
  export DRMAA_LIBRARY_PATH=/geadmin/N1GE/lib/lx-amd64/libdrmaa.so.1.0
  
  {Genomonをインストールしたディレクトリ}/python2.7-packages/bin/genomon_pipeline $5 $1 $2 $3 $4

上記のようにスクリプトを作成した場合，以下のようにして実行します．

.. code-block:: bash
  :caption: Genomon解析コマンドの使用方法

  $ bash
  /home/lect-1/Genomon2_5_2/script/genomon_pipeline.sh \
  {解析タイプ} \
  {サンプル設定ファイル} \
  {出力ルートディレクトリ} \
  {パイプライン設定ファイル} \
  [qsubオプション]

:第1引数 解析タイプ (必須): DNA解析の場合は ``dna`` を，RNA解析の場合は ``rna`` を指定します．
:第2引数 サンプル設定ファイル (必須): サンプル設定ファイルを指定します．
:第3引数 出力ルートディレクトリ (必須): Genomonによる解析結果を出力するディレクトリです．Genomonの結果はこのディレクトリ配下にすべて出力されます．
:第4引数 パイプライン設定ファイル (必須): パイプライン設定ファイルを指定します．
:第5引数 qsubオプション (任意): グリッドエンジンのqsubオプションを指定します．Genomon解析コマンドを実行すると，グリッドエンジンを介してGenomon本体がジョブとしてサブミットされます．このジョブに対するqsubオプションです．

.. code-block:: bash
  :caption: DNA(Exome) 解析実行例
  
  $ bash
  /home/lect-1/Genomon2_5_2/script/genomon_pipeline.sh \
  dna \
  /home/lect-1/Genomon2_5_2/config/test5929.csv \
  /home/lect-1/Genomon2_5_2/test5929 \
  /home/lect-1/Genomon2_5_2/config/dna_exome_genomon.cfg

.. code-block:: bash
  :caption: RNA解析実行例
  
  $ bash
  /home/lect-1/Genomon2_5_2/script/genomon_pipeline.sh \
  rna \
  /home/lect-1/Genomon2_5_2/config/test5929.csv \
  /home/lect-1/Genomon2_5_2/test5929 \
  /home/lect-1/Genomon2_5_2/config/rna_genomon.cfg


1-6. ジョブ実行状況の確認
-------------------------------

Genomon解析コマンドを実行すると，Genomon本体そのものと，Genomon本体が呼び出す各解析タスクがグリッドエンジンのジョブとしてサブミットされます．

``qstat`` コマンドを用いてジョブの実行状況を確認します．（表示内容の詳細はお使いのUGEシステムによって異なることがあります．）

.. code-block:: bash
  :caption: ジョブの実行状況の確認例
  
  $ qstat
  job-ID   prior   name       user   'state' submit/start at     queue         ...
  ---------------------------------------------------------------------------...
  33808606 0.00000 QLOGIN     lect-1 'r'     08/01/2017 11:30:36 intr.q@sc096i ...
  33919900 0.00000 qsub_genom lect-1 'r'     08/01/2017 12:46:24 ljobs.q@sc427i...
  33919994 0.00000 star_align lect-1 'r'     08/03/2017 13:46:24 ljobs.q@sc427i...
  33920000 0.00000 qsub_genom lect-1 'qw'    08/01/2017 12:46:24 ljobs.q@sc427i...
  ・・・・・・・


state 列がジョブの実行状況を示しています．

+-------------------+----------------+
|  state 列の値     | 意味           |
+===================+================+
| r                 | 実行中         |
+-------------------+----------------+
| qw                | 実行待ち状態   |
+-------------------+----------------+
| t                 | 転送中         |
+-------------------+----------------+
| hqw               | 待機中         |
+-------------------+----------------+
| Eqw               | 実行失敗       |
+-------------------+----------------+
| s                 | 一時停止       |
+-------------------+----------------+

すべての解析が完了すると，実行中のジョブはなくなります．

スパコンの空きリソース容量が少ない場合，ジョブがキューにアサインできずに ``qw`` (実行待ち状態) のまま ``r`` (実行中) に長時間遷移しないことがあります．
計算サーバのリソースが解放され次第ジョブはアサインされますが，お急ぎの場合は，Genomon本体に対して確保するメモリ量を小さく指定することで，スパコンに要求するリソース量を少なくしジョブをアサインさせやすくすることができます．

Genomon使用メモリ量を変更する場合は，Genomon解析コマンドの qsub オプションを用いて指定します．
qsub オプションを省略した場合，デフォルト値としてGenomon本体は ``64GB`` のメモリをスパコンに要求します．

デフォルト値の半分となる ``32GB`` のメモリをスパコンに要求する場合の実行例は以下のとおりです．
ただし，Genomon本体の使用メモリ量が要求したメモリ量を超過した場合，スパコンによりジョブの実行が中止されますのでご注意ください．

.. code-block:: bash
  :caption: Genomonオプションによるメモリ指定の例

  $ bash
  /home/lect-1/Genomon2_5_2/script/genomon_pipeline.sh \
  rna \
  /home/lect-1/Genomon2_5_2/config/test5929.csv \
  /home/lect-1/Genomon2_5_2/test5929 \
  /home/lect-1/Genomon2_5_2/config/rna_genomon.cfg \
  '-l s_vmem=32G,mem_req=32G'

