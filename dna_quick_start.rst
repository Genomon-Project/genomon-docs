Quick Start DNA解析
===================

こちらはHGCスパコン利用者向けのページになります．HGCスパコン以外でGenomonをご使用の方はGenomonをインストールしていただく必要があります．Genomonインストール方法については，:doc:`install` を参照してください．

.. code-block:: none 

  DNA解析に必要な手順．
    1．パイプライン設定ファイルをつくる
    2．テストサンプルでGenomonを実行してみる．
    3. サンプル設定ファイルをつくる
    4．Genomonを実行する
    5．結果ファイルを確認する


DNA解析に必要な手順
^^^^^^^^^^^^^^^^^^^
HGCスパコンでのDNA解析に必要な手順をまとめました．

**1. パイプライン設定ファイルを作成する**

最適化されたパラメータが記載されたパイプライン設定ファイルがHGCスパコンに用意してあります．
パラメータを変更する場合はExome解析の場合はdna_exome_genomon.cfg，Whole Genome解析の場合はdna_wgs_genomon.cfgをローカルディレクトリにコピーしてご使用ください．

.. code-block:: bash

  # Exome解析用パイプライン設定ファイル
  /home/w3varann/genomon_pipeline-2.2.0/genomon_conf/dna_exome_genomon.cfg
  # Whole Genome解析用パイプライン設定ファイル
  /home/w3varann/genomon_pipeline-2.2.0/genomon_conf/dna_wgs_genomon.cfg

変異コールの結果にANNOVARによるアノテーションを行うことをお奨めします．以下にHGCスパコンへのANNOVARのインストールとGenomonへの設定方法を記載しました．

各ユーザがANNOVARを使用するためにはUser License Agreementをする必要があります．ANNOVARのホームページ（http://www.openbioinformatics.org/annovar/annovar_download_form.php）にてUser License Agreementをしてください．その時に登録したメールアドレスにANNOVARをダウンロードするためのリンクが記載されたメールが届きます．そのリンクを使用してANNOVARをダウンロードします．ダウンロード後にANNOVARのスクリプトを使用してdbSNP131など各種データベースをダウンロードします．

.. code-block:: bash

  # qloginする
  $qlogin
  # ANNOVARをダウンロードします．
  wget {Eメールに記載されたannovar.latest.tar.gzのURL}
  # ANNOVARを解凍します．
  tar xzvf annovar.latest.tar.gz
  # ANNOVARのディレクトリに移動します．
  cd annovar
  # Genomonで必要なANNOVARのデータベースをダウンロードするスクリプトをコピーします
  cp /home/w3varann/genomon_pipeline-2.2.0/genomon_script/annovar_database_download.sh .
  # ANNOVARのスクリプトを使用してダウンロードを実行します．
  bash ./annovar_database_download.sh

ANNOVARを使用するようにパイプライン設定ファイルを編集します．以下の2か所を変更する必要があります．

.. code-block:: bash

  [SOFTWARE]
  annovar = [ダウンロードしたANNOVARのパス]に変更する．
  (例)annovar = /home/genomon/tools/annovar

  [annotation]
  active_annovar_flag = True
  FalseをTrueに変更する (ANNOVARを使用する/しない)を管理しているフラグです．デフォルトはFalseになります．

**2．テストサンプルでGenomonを実行してみる**

テストサンプルでGenomonを実行してみましょう．Genomonが正しく使用できるか、パイプライン設定ファイルの記述ができているか確認することができます。テストサンプルはファイルサイズが小さいので数分で処理が完了します．

.. code-block:: bash
  
  # qloginする
  $qlogin
  # Genomonを実行する
  bash /home/w3varann/genomon_pipeline-2.2.0/genomon_script/genomon_pipeline_HGC.sh {解析タイプ：dna} {サンプル設定ファイル} {出力ルートディレクトリ} {パイプライン設定ファイル}
  
`解析タイプ`
'dna'を指定します．
`サンプル設定ファイル`
/home/w3varann/genomon_pipeline-2.2.0/test_data/test_dna/sample_config_DNA.csv
`出力ルートディレクトリ`
任意の出力ルートディレクトリを指定します．
`パイプライン設定ファイル`
2.で作成したパイプライン設定ファイルを指定します．

**3. サンプル設定ファイルを作成する**

サンプル設定ファイルには解析対象のFASTQやBAMファイル，どの解析（変異コール，SV検出，BAMのQuality Control)を実行するのかを指定します．

サンプル設定ファイルの記載方法は  :doc:`dna_sample_csv` を参照ください．


**4．Genomonを実行する**

作成したサンプル設定ファイルを指定して，Genomonを実行しましょう．

.. code-block:: bash
  
  # qloginする
  $qlogin
  # Genomonを実行する
  bash /home/w3varann/genomon_pipeline-2.2.0/genomon_script/genomon_pipeline_HGC.sh {解析タイプ：dna} {サンプル設定ファイル} {出力ルートディレクトリ} {パイプライン設定ファイル}
  
`解析タイプ`
'dna'を指定します．
`サンプル設定ファイル`
1.で作成したサンプル設定ファイルを指定します．
`出力ルートディレクトリ`
任意の出力ルートディレクトリを指定します．
`パイプライン設定ファイル`
2.で作成したパイプライン設定ファイルを指定します．

**5．結果ファイルを確認する**

結果ファイルは実行時に指定した 出力ルートディレクトリに以下に出力されます．

.. code-block:: bash

  # Mutation Call結果
  {出力ルートディレクトリ}/mutation/sample名/sample名_genomon_mutations.result.txt
  # SV検出結果
  {出力ルートディレクトリ}/sv/sample名/sample名.genomonSV.result.txt
  # summary
  {出力ルートディレクトリ}/sv/sample名/sample名.xls

結果ファイルの各項目の説明など詳細は :doc:`dna_results` を参照ください．

