HGCスパコンでGenomonを実行する
==============================

ヒトゲノム解析センタースーパーコンピュータ（HGCスパコン)にはGenomonはすでにインストールされております。HGCスパコンアカウントをお持ちの方は，以下のコマンドを実行するだけで，DNA，RNA解析ができます．

.. code-block:: bash

  bash /home/w3varann/genomon_pipeline-2.2.0/genomon_script/genomon_pipeline_HGC.sh 
 　パラメータ１：{DNA解析をする場合は、dna を、RNA解析をする場合は、rna を指定する}
 　パラメータ２：{サンプル設定ファイルを指定する}
 　パラメータ３：{出力ルートディレクトリを指定する}
 　パラメータ４：{パイプライン設定ファイルを指定する}

ご使用者にやっていただくことは、この4つのパラメータを指定していただき、HGCにインストール済みのGenomonを実行するだけです。

各引数の説明
**************

`DNA解析かRNA解析のどちらかを実行するか決める
`FASTQなど解析するファイルを指定したサンプル設定ファイルを作成する
`出力ルートディレクトリを決める
`パイプライン設定ファイルを指定する
  

sample_cfg.csvの記述方法は、:doc:`dna_sample_csv` を参照してください．

.. code-block:: bash

  # DNA解析の実行例
  bash /home/w3varann/genomon_pipeline-2.2.0/genomon_script/genomon_pipeline_HGC.sh dna sample_config.csv /home/genomon/sample_DNA_ACC dna_genomon.cfg

  # RNA解析の実行例
  bash /home/w3varann/genomon_pipeline-2.2.0/genomon_script/genomon_pipeline_HGC.sh rna sample_config.csv /home/genomon/sample_RNA_ACC rna_genomon.cfg

