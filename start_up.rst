HGCスパコンでGenomonを実行するのに必要なこと
==============

 | ヒトゲノム解析センタースーパーコンピュータ（HGCスパコン)にはGenomonはすでにインストールされております。
 | 以下のコマンドを実行するだけで、ゲノムもしくはトランスクリプトーム解析ができます。

.. code-block:: bash

  bash /home/w3varann/genomon_pipeline-2.2.0/genomon_script/genomon_pipeline_HGC.sh {dna, rnaを選択する} {サンプル設定ファイル} {出力ルートディレクトリ} {パイプライン設定ファイル}


  | ご使用者にやっていただくことは、
  #. DNA解析かRNA解析のどちらかを実行するか決める
  #. FASTQなど解析するファイルを指定したサンプル設定ファイルを作成する
  #. 出力ルートディレクトリを決める
  #. パイプライン設定ファイルを指定する
  
  
  

sample_cfg.csvの記述方法は、:doc:`dna_sample_csv` を参照してください．


各カラムの説明
**************
`Chr Start End`
 変異候補のポジション
`Ref`
 変異候補のポジションのリファレンス塩基です．Insertion の場合は"-"ハイフンが表示されます．
`Alt`
 変異候補のポジションの塩基配列です．Deletion の場合は"-"ハイフンになります．


DNA解析実行例
^^^^^^^^^^

.. code-block:: bash

    genomon_pipeline dna dna_sample.csv outputdir dna_genomon.cfg
    
    # sample.csv         : 自分でつくる 
    # outputdir          : 任意の出力場所を指定する
    # dna_genomon.cfg    : Genomonで用意しているもので基本ok
