コマンドの実行
==============

コマンドは下記のように実行してください．

.. code-block:: None

  genomon_pipeline [Analysis type: dna,rna] sample_cfg.csv(.tsv) output_root_directory genomon_conf_file task_conf_file

  #Analysis type         : DNA解析をする場合は、dna を、RNA解析をする場合は、rna を指定してください．
  #sample_conf_file      : 解析するサンプルと入力ファイルを指定します．
  #output_root_directory : 結果ファイルを出力するディレクトリを指定してください。指定したディレクトリをルートにoutputが生成されます．
  #genomon_conf_file     : 使用するソフトウェアやデータベースファイルの指定をします．
  #task_conf_file        : DNA解析用(dna_task_param.cfg)とRNA解析用(dna_task_param.cfg)のファイルが用意されています．
                          コマンドオのパラメータは基本的に最適化されております．閾値の問題で候補が出力されない場合は、
                          これらデフォルトのファイルをコピーして編集してください．
 
sample_conf_fileの記述方法は、:doc:`sample_csv` を参照してください。

DNA解析実行例
^^^^^^^^^^

.. code-block:: bash

    genomon_pipeline dna DNA_sample.csv dna_outputdir genomon.cfg dna_task_param.cfg
    
    # DNA_sample.csv     : 自分でつくる 
    # dna_outputdir      : 任意の出力場所を指定する
    # genomon.cfg        : genomonが用意しているもので基本ok RNA解析と共通
    # dna_task_param.cfg : prefixがdna_のほうを使う

RNA解析実行例
^^^^^^^^^^

.. code-block:: bash

    genomon_pipeline rna RNA_sample.csv rna_outputdir genomon.cfg rna_task_param.cfg

    # RNA_sample.csv     : 自分でつくる 
    # rna_outputdir      : 任意の出力場所を指定する
    # genomon.cfg        : genomonが用意しているもので基本ok DNA解析と共通
    # rna_task_param.cfg : prefixがrna_のほうを使う
