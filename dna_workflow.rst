========================================
DNA 解析パイプラインSchemes
========================================

 .. image:: image/dna_workflow.png
  :scale: 100%
  
 | Inputの方法は [fastq], [bam_tofastq], [bam_import] の3種類あります．これらはサンプル設定ファイルで定義します．
 |
 | 解析は変異コール, SV検出, BAMのQuality Control出力の3種類あり， [mutation_call], [sv_detection], [qc] の項目をサンプル設定ファイルで定義すると実行されます．
 |
 | [mutation_call], [sv_detection], [qc]の各解析が完了した後，自動的にpost Analysis Taskが実行されます．実行したくない場合は，パイプライン設定ファイルを変更する必要があります．
 |
 | サンプル設定ファイルの記載方法は :doc:`dna_sample_csv` をご参照ください．
 | パイプライン設定ファイルを変更する場合は :doc:`dna_config_info` をご参照ください．
 
マッピング Task
-----------------------
* **split fastq** -- 並列してマッピングをするためにFASTQを分割します．
* **map_dna_sequence** -- 分割したFASTQ単位でリファレンスゲノムにマッピング，そしてソートします．
* **markdup** -- 分割されているソートしたBAMを１つにマージして＋重複リードをマークします．

変異コール Task (mutation_call)
------------------------------------
* **identify_mutations** -- 変異コールします.

SV検出 Task (sv_detection)
------------------------------

* **parse_sv** -- BAMファイルから，breakpointやSVの証拠となるリードをparseします．
* **merge_sv** -- parse_svの結果から，control panelを作成します．
* **filt_sv** -- parse_svに対して，control panelやNormalサンプルを用いて偽陽性をフィルタして，SVの候補を検出します．

BAMのQuality Control出力 Task (qc)
--------------------------------------

* **bam_stats** -- BAMのリードとマッピングのstatisticsを生成します．
* **coverage** -- BAMのcoverageを生成します．
* **merge_qc** -- bam_statsの結果と，coverageの結果をマージします．

Post Analysis Task
-------------------
* **paplot** -- 各結果をplotしグラフを出力します．
* **post_analysis_qc** -- 全サンプルのBAMのQuality Control結果を１つのファイルにマージして出力します．
* **post_analysis_sv** -- 全サンプルのSV検出した候補を１つのファイルにマージして出力します．IGVの画像をキャプチャできるbatファイルを生成します．
* **post_analysis_mutation** -- 全サンプルの変異コールを１つのファイルにマージして出力します．IGVの画像をキャプチャできるbatファイルを生成します．

その他Task
----------
* **link_input_fastq** -- 指定したFASTQを出力ルートディレクトリ内にリンクします．
* **link_import_bam** -- 指定したBAMを出力ルートディレクトリ内にリンクします．
* **bam2fastq** -- 指定したBAMをFASTQにConvertし出力ルートディレクトリ内に出力します．

