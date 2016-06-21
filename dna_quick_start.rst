Quick Start DNA解析
===================

| こちらはHGCスパコン利用者向けのページになります．
|
| HGCスパコン以外でGenomonをご使用の方はGenomonをインストールしていただく必要があります．
| Genomonインストール方法については，:doc:`install` を参照してください．
|

.. code-block:: none 

  HGCスパコンでDNA解析に必要な手順
    1．パイプライン設定ファイルをつくる
    2．テストサンプルでGenomonを実行してみる
    3．サンプル設定ファイルをつくる
    4．Genomonを実行する
    5．結果ファイルを確認する


HGCスパコンでDNA解析に必要な手順
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| HGCスパコンでのDNA解析に必要な手順をまとめました．
|

1. パイプライン設定ファイルを作成する
-------------------------------------

| 一般的なExome解析，Whole Genome解析のためのパイプライン設定ファイルはすでにHGCスパコンに用意してあります．
| ローカルディレクトリにコピーしてご使用ください．
|
| 設定ファイルはこちらにあります．
|

.. code-block:: bash

  # Exome解析用パイプライン設定ファイル
  /home/w3varann/genomon_pipeline-2.3.0/genomon_conf/dna_exome_genomon.cfg
  # Whole Genome解析用パイプライン設定ファイル
  /home/w3varann/genomon_pipeline-2.3.0/genomon_conf/dna_wgs_genomon.cfg

.. note::

  **ANNOVARのインストールについて**
  
  | GenomonではANNOVARというアノテーションツールを使用しています．
  | ANNOVARをインストールしなくてもGenomonは実行できますが，Genomonの結果をグラフに描画する機能（paplot）ではANNOVARの出力結果を参照していますので，ANNOVARの設定を行うことをお奨めしています．
  |
  | 次にHGCスパコンへのANNOVARのインストールとGenomonへの設定方法を記載しました．
  |
  | ANNOVARのインストールが必要ない方は，次の「2．テストサンプルでGenomonを実行してみる」にお進み下さい．
  |

**ANNOVARのインストールとGenomonへの設定方法**

| 各ユーザがANNOVARを使用するためにはANNOVARのウェブページ（http://www.openbioinformatics.org/annovar/annovar_download_form.php）にてUser License Agreementをしてください．
| その時に登録したメールアドレスにANNOVARをダウンロードするためのリンクが記載されたメールが届きます．
| そのリンクを使用してANNOVARをダウンロードします．
| ダウンロード後にANNOVARのスクリプトを使用してdbSNP131など各種データベースをダウンロードします．
|

.. code-block:: bash

  # qloginする
  qlogin
  # ANNOVARをダウンロードします．
  wget {Eメールに記載されたannovar.latest.tar.gzのURL}
  # ANNOVARを解凍します．
  tar xzvf annovar.latest.tar.gz
  # ANNOVARのディレクトリに移動します．
  cd annovar
  # Genomonで必要なANNOVARのデータベースをダウンロードするスクリプトをコピーします
  cp /home/w3varann/genomon_pipeline-2.3.0/genomon_script/annovar_database_download.sh .
  # ANNOVARのスクリプトを使用してダウンロードを実行します．
  bash ./annovar_database_download.sh

| ダウンロードが完了したらANNOVARを使用するようにパイプライン設定ファイルを編集します．
| 以下の2か所を変更する必要があります．
|

.. code-block:: bash

  [SOFTWARE]
  annovar = [ダウンロードしたANNOVARのパス]に変更する．
  (例)annovar = /home/genomon/tools/annovar
  
  [annotation]
  active_annovar_flag = True
  FalseをTrueに変更する (ANNOVARを使用する/しない)を管理しているフラグです．デフォルトはFalseになります．


2．テストサンプルでGenomonを実行してみる
----------------------------------------

| テストサンプルでGenomonを実行してみましょう．
| Genomonが正しく使用できるか，パイプライン設定ファイルの記述が正しくできているか確認することができます．
| テストサンプルはファイルサイズが小さいので数分で処理が完了します．
|

.. code-block:: bash
  
  # qloginする
  qlogin
  # Genomonを実行する
  bash /home/w3varann/genomon_pipeline-2.3.0/genomon_script/genomon_pipeline_HGC.sh dna /home/w3varann/genomon_pipeline-2.3.0/test_data/test_dna/sample_config_DNA.csv {出力ルートディレクトリ} {1.で作成したパイプライン設定ファイル}
  #
  # 解析タイプ
  #   'dna'を指定します．
  # サンプル設定ファイル
  #   /home/w3varann/genomon_pipeline-2.3.0/test_data/test_dna/sample_config_DNA.csvを指定します．
  # 出力ルートディレクトリ
  #   任意の出力ルートディレクトリを指定します．
  # パイプライン設定ファイル
  #   1.で作成したパイプライン設定ファイルを指定します．

3. サンプル設定ファイルを作成する
---------------------------------

| サンプル設定ファイルには解析対象のFASTQやBAMファイル，どの解析（変異コール，SV検出，BAMのQuality Control）を実行するのかを指定します．
| サンプル設定ファイルの記載方法は  :doc:`dna_sample_csv` を参照ください．
| サンプル設定ファイルの名前は任意で設定可能ですが，拡張子は ``.csv`` としてください．
| 

4．Genomonを実行する
--------------------

| 作成したサンプル設定ファイルを指定して，Genomonを実行しましょう．
|

.. code-block:: bash
  
  # qloginする
  qlogin
  # Genomonを実行する
  bash /home/w3varann/genomon_pipeline-2.3.0/genomon_script/genomon_pipeline_HGC.sh dna {3.で作成したサンプル設定ファイル} {出力ルートディレクトリ} {1.作成したパイプライン設定ファイル}
  #
  # 解析タイプ
  #   'dna'を指定します．
  # サンプル設定ファイル
  #    3.で作成したサンプル設定ファイルを指定します．拡張子は.csvにしてください．
  # 出力ルートディレクトリ
  #    任意の出力ルートディレクトリを指定します．
  # パイプライン設定ファイル
  #    1.で作成したパイプライン設定ファイルを指定します．


5．結果ファイルを確認する
-------------------------

| 結果ファイルは実行時に指定した出力ルートディレクトリ以下に出力されます．
|

.. code-block:: bash

  # 変異コール結果
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_mutation_filt.txt
  # SV検出結果
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_sv_filt.txt
  # BAMのQuality Controlの結果
  {出力ルートディレクトリ}/post_analysis/{サンプル設定ファイル名}/merge_qc.txt
  # paplotの結果
  # index.htmlをクリックすることで結果が表示されます．
  {出力ルートディレクトリ}/paplot/{サンプル設定ファイル名}
  
| 結果ファイルの説明は :doc:`dna_results` を参照ください．
|
