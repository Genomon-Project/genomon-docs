はじめに
========

ヒトゲノム解析センタースーパーコンピュータ（HGCスパコン）にGenomonはすでにインストールされております．HGCスパコンアカウントをお持ちの方は，以下のコマンドを実行するだけで，DNA／RNA解析ができます．

GenomonはHGCスパコン以外のサーバで稼働実績があります．Genomonインストール方法については，:doc:`install` を参照してください．またご不明な点がございましたら，お気軽にお問い合わせいただければと思います．genomon.devel@gmail.com

.. attention::

  | HGC スパコンの環境変更 (os6→os7) に伴い、Genomon のスクリプトの場所を変更しました．
  | このページは OS7 用ですので、OS6 をご使用の方は https://genomon.readthedocs.io/ja/v2.6.1/ を参照ください．
  
.. code-block:: bash

  # HGCスパコンでのGenomon使用方法
  bash /share/pub/genomon/genomon_pipeline-2.6.2/genomon_script/genomon_pipeline_HGC.sh {解析タイプ} {サンプル設定ファイル} {出力ルートディレクトリ} {パイプライン設定ファイル}

ご使用者にやっていただくことは，コマンドに必要な４つのパラメータを指定していただき，HGCにインストール済みのGenomonを実行するだけです．

`1. 解析タイプ　'dna'，'rna'`
    DNA解析をする場合は，dna を，RNA解析をする場合は，rna を指定します．
`2. サンプル設定ファイル　'sample_config.csv'`
    解析対象のファイル（FASTQやBAM）のパスなどを記載したファイルを作成し，そのファイル名を指定します．
`3. 出力ルートディレクトリ　'output_root_directory'`
    出力ルートディレクトリを指定します．結果がこのディレクトリ以下に出力されます．
`4. パイプライン設定ファイル　'genomon.cfg'`
    パイプライン設定ファイルを指定します．パイプライン設定ファイルはHGCスパコンに用意しております．

.. code-block:: bash

  # DNA exome解析の実行例
  bash /share/pub/genomon/genomon_pipeline-2.6.2/genomon_script/genomon_pipeline_HGC.sh dna /share/pub/genomon/genomon_pipeline-2.6.2/test_data/test_dna/sample_config_DNA.csv {出力ルートディレクトリ} /share/pub/genomon/genomon_pipeline-2.6.2/genomon_conf/dna_exome_genomon.cfg

  # DNA whole genome解析の実行例
  bash /share/pub/genomon/genomon_pipeline-2.6.2/genomon_script/genomon_pipeline_HGC.sh dna /share/pub/genomon/genomon_pipeline-2.6.2/test_data/test_dna/sample_config_DNA.csv {出力ルートディレクトリ} /share/pub/genomon/genomon_pipeline-2.6.2/genomon_conf/dna_wgs_genomon.cfg

  # DNA target genome解析の実行例
  bash /share/pub/genomon/genomon_pipeline-2.6.2/genomon_script/genomon_pipeline_HGC.sh dna /share/pub/genomon/genomon_pipeline-2.6.2/test_data/test_dna/sample_config_DNA.csv {出力ルートディレクトリ} /share/pub/genomon/genomon_pipeline-2.6.2/genomon_conf/dna_target_genomon.cfg

  # RNA解析の実行例
  bash /share/pub/genomon/genomon_pipeline-2.6.2/genomon_script/genomon_pipeline_HGC.sh rna /share/pub/genomon/genomon_pipeline-2.6.2/test_data/test_rna/sample_config_RNA.csv {出力ルートディレクトリ} /share/pub/genomon/genomon_pipeline-2.6.2/genomon_conf/rna_genomon.cfg
  
  * qloginをする必要があります．

