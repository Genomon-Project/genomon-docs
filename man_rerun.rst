4. 解析再実行
==================

Genomonでは，出力ディレクトリ中に既に解析結果が存在すればその解析をスキップします．
そのため，過去に解析が完了したものに対して解析を再実行するような場合，その解析の出力ディレクトリを別名で退避あるいは削除した後，Genomon解析コマンドを再実行します．

4-1. 特定の解析のみ再実行する
----------------------------------------

例えば，DNA解析において ``pmsignature`` を再実行したい場合，必要な手順は下記のようになります．

1. 出力ディレクトリの退避

はじめに，再実行対象の ``pmsignature`` の出力ディレクトリを退避，あるいは削除します．

.. code-block:: bash
  :caption: pmsignature出力ディレクトリ退避例
  
  $ cd /home/lect-1/Genomon2_5_2/test5929/
  $ mv pmsignature/ pmsignature.old


つぎに， ``pmsignature`` の後続の解析の出力結果を残しておきたい場合はその出力ディレクトリを退避します．解析の前後関係(ワークフロー)については，下記のGenomonドキュメントを参照ください．

 - `DNA解析パイプラインSchemes <http://genomon.readthedocs.io/ja/latest/dna_workflow.html>`__
 - `RNA解析パイプラインSchemes <http://genomon.readthedocs.io/ja/latest/rna_workflow.html>`__

このDNA解析パイプラインSchemesで示されるワークフローより，青枠で表記されているタスクに着目すると，pmsignatureの後続のタスクは ``paplot_pmsignature`` であることがわかります．これより， ``paplot`` の出力ディレクトリも併せて退避します．

退避しない場合，既存の解析結果は上書きされます．

.. code-block:: bash
  :caption: paplot出力ディレクトリの退避例
  
  $ cd /home/lect-1/Genomon2_5_2/test5929/
  $ mv paplot/ paplot.old


2. Genomon解析コマンドの実行

既存のGenomon出力ディレクトリを出力ディレクトリに指定して，Genomon解析コマンドを実行します．

.. code-block:: bash

  $ bash
  /home/lect-1/Genomon2_5_2/script/genomon_pipeline.sh \
  dna \
  /home/lect-1/Genomon2_5_2/config/test5929.csv \
  /home/lect-1/Genomon2_5_2/test5929 \
  /home/lect-1/Genomon2_5_2/config/rna_genomon.cfg
  $

4-2. 特定のサンプルのみ再実行する
------------------------------------------

再実行したいサンプルの出力ディレクトリを退避または削除することにより，解析結果のないサンプルのみ解析が実行されます．

例えば，RNA解析において，サンプル ``test2`` の ``IntronRetention`` のみ再実行したい場合，必要な手順は下記のようになります．

1. 出力ディレクトリの退避

``IntronRetention`` 検出結果出力ディレクトリの中の ``test2`` サンプルディレクトリを退避または削除します．
既存の解析結果を残しておきたい場合は退避を，そうでない場合は削除します．

.. code-block:: bash
  :caption: test2 サンプルディレクトリの退避例
  
  $ cd /home/lect-1/Genomon2_5_2/test5929/intron_retention/
  $ ls
  test1/ test2/ test3/ test4/ test5/
  $ mv test2/ test2.old/


2. Genomon解析コマンドの実行

出力ディレクトリを退避した(出力結果が存在しない) ``test2`` サンプルの ``IntronRetention`` だけが再実行されます．


4-3. サンプルを追加して解析を再実行する
---------------------------------------------------

サンプルを新しく追加する場合，サンプル設定ファイルに追記し，再実行することで追加したサンプルのみ解析が実行されます．
その際，解析結果をマージする ``pmgignature`` や ``post_analysis``, ``paplot`` も再実行し，既存の結果を上書きします．既存の解析結果を残しておきたい場合は，必要に応じて出力ディレクトリを退避してください．

