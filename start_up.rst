HGCスパコンでGenomonを実行する
==============================

ヒトゲノム解析センタースーパーコンピュータ（HGCスパコン)にGenomonはすでにインストールされております。HGCスパコンアカウントをお持ちの方は，以下のコマンドを実行するだけで，DNA，RNA解析ができます．

.. code-block:: bash
　
  # HGCスパコンでのGenomon使用方法
  bash /home/w3varann/genomon_pipeline-2.2.0/genomon_script/genomon_pipeline_HGC.sh {analysis type} {sample config file} {output root directory} {pipeline config_file}

ご使用者にやっていただくことは、コマンドに必要な４つのパラメータを指定していただき、HGCにインストール済みのGenomonを実行するだけです。

`1. analysis type`
    DNA解析をする場合は、dna を、RNA解析をする場合は、rna を指定します．
`2. sample config file`
    解析対象のファイル（FASTQやBAMなど）を記載したファイルを作成し、そのファイル名を指定します．
`3. output root directory`
    出力ルートディレクトリを指定します．結果がこのディレクトリ以下に出力されます．
`4. pipeline config_file`
    パイプライン設定ファイルを指定します．最適化されたパラメータが記載されたパイプライン設定ファイルをHGCスパコンに用意しております．

.. code-block:: bash

  # DNA exome解析の実行例
  bash /home/w3varann/genomon_pipeline-2.2.0/genomon_script/genomon_pipeline_HGC.sh dna sample_config.csv /home/genomon/sample_DNA_exome_ACC /home/w3varann/genomon_pipeline-2.2.0/genomon_conf/dna_exome_genomon.cfg

  # DNA whole genome解析の実行例
  bash /home/w3varann/genomon_pipeline-2.2.0/genomon_script/genomon_pipeline_HGC.sh dna sample_config.csv /home/genomon/sample_DNA_WGS_ACC /home/w3varann/genomon_pipeline-2.2.0/genomon_conf/dna_wgs_genomon.cfg

  # RNA解析の実行例
  bash /home/w3varann/genomon_pipeline-2.2.0/genomon_script/genomon_pipeline_HGC.sh rna sample_config.csv /home/genomon/sample_RNA_ACC /home/w3varann/genomon_pipeline-2.2.0/genomon_conf/rna_genomon.cfg
  
  * qloginをする必要があります．

