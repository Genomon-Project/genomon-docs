RNA解析コマンドを実行する
==============

コマンドのUsageです.

.. code-block:: bash

  genomon_pipeline [Analysis type: rna] sample_cfg.csv genomon_conf_file

  # Analysis type         : DNA解析をする場合は、dna を、RNA解析をする場合は、rna を指定してください．
  # sample_conf_file      : 解析するサンプルと入力ファイルを指定します．
  # output_root_directory : 結果ファイルを出力するディレクトリを指定してください。指定したディレクトリをルートにoutputが生成されます．
  # genomon_conf_file     : 使用するソフトウェアやデータベースファイルの指定をします．また解析ソフトウェアで使用するパラメータを変更できます．パラメータは最適化されております．変更する場合はこのファイルをコピーして編集してください．
  #                        
 
sample_cfg.csvの記述方法は、:doc:`rna_sample.csv` を参照してください。

RNA解析コマンド実行例
^^^^^^^^^^

.. code-block:: bash

    genomon_pipeline rna rna_sample.csv outputdir rna_genomon.cfg
    
    # rna_sample.csv     : 自分でつくる 
    # outputdir          : 任意の出力場所を指定する
    # rna_genomon.cfg    : Genomonで用意しているもので基本ok
