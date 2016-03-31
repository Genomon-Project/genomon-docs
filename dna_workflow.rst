========================================
DNA解析パイプラインschemes
========================================

 .. image:: image/dna_workflow.png
  :scale: 100%
  
 | Inputの方法は [fastq], [bam_tofastq], [bam_import] の3種類あります．すべてsample confで定義します．
 |
 | 解析は変異Call, SV検出, BamSummary出力 の3種類あり、 [mutation_call], [sv_detection], [summary] の項目をsample confで定義すると実行されます．
 |
 | [mutation_call], [sv_detection], [summary]の各解析が完了した後、自動的にpost Analysis Taskが実行されます．実行したくない場合は、dna_genomon.cfg の設定を変更する必要があります．
 |
 | sample confの記載方法は :doc:`dna_sample_csv` をご参照ください．
 | dna_genomon.cfgを変更する場合は :doc:`dna_config_info` をご参照ください．
 
マッピング Task
-----------------------
* **split fastq** -- 並列してアライメントをするためにFASTQをsplitします．
* **map_dna_sequence** -- 分割したFASTQ単位でリファレンスゲノムにアライメント、そしてソートします．
* **markdup** -- 分割されているソートしたBAMを１つにmerge＋mark duplicateします．

変異Call Task
-------------------
* **identify_mutations** -- 変異コールします.

SV検出 Task
-------------------
* **parse_sv** -- bamファイルから、breakpointやSVの証拠となるリードをparseします．
* **merge_sv** -- parse_svの結果から、control panelを作成します．
* **filt_sv** -- parse_svに対して、control panelやnormalサンプルを用いて偽陽性をフィルタして、SVの候補を検出します．

Bam Summary出力 Task
-------------------
* **bam_stats** -- bamのreadとmappingのstatisticsを生成します．
* **coverage** -- bamのcoverageを生成します．
* **merge_summary** -- bam_statsの結果と、coverageの結果をマージします．

Post Analysis Task
-------------------
* **paplot** -- SV検出した候補とsummary結果をplotしグラフを出力します．
* **post_analysis_summary** -- 全サンプルのsummary結果を１つのファイルにマージして出力します．
* **post_analysis_sv** -- 全サンプルのSV検出した候補を１つのファイルにマージして出力します．IGVの画像をキャプチャできるbatファイルを生成します．

その他Task
--------------------------
* **link_input_fastq** -- 指定したFASTQをoutputディレクトリ内にリンクします．
* **link_import_bam** -- 指定したBAMをoutputディレクトリ内にリンクします．
* **bam2fastq** -- 指定したBAMをFASTQにConvertしoutputディレクトリ内に出力します．


