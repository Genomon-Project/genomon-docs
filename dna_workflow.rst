========================================
DNA 解析パイプラインSchemes
========================================

GenomonパイプラインのDNA解析において，各工程の流れを解説します．

 .. image:: image/dna_workflow.png
  :scale: 100%
 
| サンプル設定ファイルの記載方法は :doc:`dna_sample_csv` を参照ください．
| パイプライン設定ファイルを変更する場合は :doc:`dna_config_info` を参照ください．

1. 入力とアライメント
--------------------------------

Inputの方法は [fastq], [bam_tofastq], [bam_import] の3種類あります．これらはサンプル設定ファイルで定義します．

:fastq: fastqを扱いやすい大きさに分割してからアライメントを行います
:bam_tofastq: bamファイルを一旦fastqに変換し，アライメントします．Genomon以外でアライメントしたbamなどはこちらを使用してください
:bam_import: アライメント済みのbamファイルが対象です．アライメントは行わず解析を行います
:markdup.bam: アライメント結果として，bamファイルを作成します

2. 変異コール (mutation_call)
------------------------------------

[mutation_call] の項目をサンプル設定ファイルで定義すると実行されます．

:identify_mutations: 変異コールします.
:post_analysis: 全サンプルの変異コールを１つのファイルにマージして出力します．
:pmsignature: 変異コールの結果を使用して，signatureを出力します．
:paplot: レポートを出力します．

3. SV検出 (sv_detection)
------------------------------

[sv_detection] の項目をサンプル設定ファイルで定義すると実行されます．

:parse_sv, merge_sv, filt_sv: SVを検出します．
:post_analysis: 全サンプルのSVを１つのファイルにマージして出力します．
:paplot: レポートを出力します．

4. Quality Control (qc)
--------------------------------------

[qc] の項目をサンプル設定ファイルで定義すると実行されます．

:bam_stats, coverage, merge_qc: QCを作成します．
:post_analysis: 全サンプルのQCを１つのファイルにマージして出力します．
:paplot: レポートを出力します．

