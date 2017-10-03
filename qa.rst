Q & A
==================

よくお問い合わせいただく内容をまとめました．

入力サンプルについて
-----------------------

| Q：シングルリードを使用できますか？
| A：できません．Genomonではペアリードのみ使用できます．
|
| Q：Illumina以外のシーケンスデータを使用できますか？
| A：できません．
|
| Q：tophatで作成したbamファイルを [bam_import] で入力できますか？
| A：できません．Genomonではアライメントに ``bwa mem`` を使用していますので，それ以外の手法で作成したbamファイルは [bam_tofastq] で再アライメントする必要があります．
|
| Q：圧縮ファイルを入力できますか？
| A：dna (bwa) は ``.gz`` 形式に対応しています．rna (STAR) は圧縮形式に対応していませんので，解凍してからご使用ください．
|
| Q：分割ファイルを入力できますか？
| A：できます．以下のように ``;`` で区切って入力してください．

.. code-block:: bash
  :caption: 分割されたサンプルを入力する場合の記述例
  
  [fastq]
  tumor,/path/to/tumor_R1_1.fastq;/path/to/tumor_R1_2.fastq,/path/to/tumor_R2_1.fastq;/path/to/tumor_R2_2.fastq

| Q：同じ腫瘍サンプルを異なるノーマルサンプルとペアにして解析結果を比較したいのですが，それぞれGenomonを実行しないといけないのでしょうか？
| A：腫瘍サンプルのサンプル名を別名にすることで同時に解析できます．

.. code-block:: bash
  :caption: tumorAをnormal1, normal2 とそれぞれペアにする場合の記述例
  
  [bam_import]
  tumorA1,/path/to/tumorA
  tumorA2,/path/to/tumorA
  normal1,/path/to/normal1
  normal2,/path/to/normal2
  
  [mutation_call]
  tumorA1,normal1,List1
  tumorA2,normal2,List1

コントロールパネルについて
------------------------------

| Q：そもそもコントロールパネルってなんですか？
| A：腫瘍サンプルで検出された変異がsomatic mutationかどうかを判断するときに使用します．腫瘍サンプルで検出された変異がほかのノーマルサンプルでも検出されていればsomatic mutationとして検出結果から取り除く，という考え方です． [mutation_call], [sv_detection], [fusionfusion] で使用しています．
|
| Q：ノーマルサンプルが１つしかないんですが，それでも入れたほうがいいんですか？
| A：解析手法によりアルゴリズムが異なります．SVとfusionfusionは少ないサンプルでも入れた方がよいです．mutation_call (EBCall※ という手法を使用しています) は，8個以下なら使わない方がよいです．※ EBCall (Shiraishi et al., NAR, 2013)

変異コールについて
---------------------

| Q：mutation のところにhotspotというディレクトリが作成されましたが，空でした．正常に終了したのでしょうか？
| A：hotsoptとして，何も検出されないことはありえます．こちらの開発時の検証では100検体中，20候補の検出率です．正常終了したかどうかはpaplotディレクトリの下にindex.htmlファイルが作成されているかどうかで判断してください．

インストールについて
---------------------

| Q：うちのスパコンにインストールできますか？
| A：Univa Grid Engine (UGE) を使用していればインストールできます．

その他
---------

| Q：解析アルゴリズムについて説明資料が欲しい
| A：次の資料を参考にしてください．(HGCアカウントが必要です) `Genomon2 Tutorial 実践編 <https://supcom.hgc.jp/internal/materials/lect-pdf/20160624/20160624-genomon2.pdf>`__
|
| Q：トラブルシューティングについて
| A：よくあるエラーは次にまとめましたので参考にしてください．`トラブルシューティングについて <./man_trouble.html>`__

