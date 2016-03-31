========================================
DNA解析パイプラインschemes
========================================

 .. image:: image/dna_workflow.png

 | Inputの方法は
 | [fastq], [bam_tofastq], [bam_import] の3種類あります．すべてsample confで定義します．
 | 
 | 解析は変異Call, SV検出, BamSummary出力 の3種類あり、
 | [mutation_call], [sv_detection], [summary] の項目を定義すると実行されます．
 | sample confで定義します．
 | 
 | 記載方法は :doc:`sample_csv` をみてください．
 | 
 
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

Summary出力 Task
-------------------
* **bam_stats** -- bamのreadとmappingのstatisticsを生成します．
* **coverage** -- bamのcoverageを生成します．
* **merge_summary** -- bam_statsの結果と、coverageの結果をマージします．

その他Task
--------------------------
* **link_input_fastq** -- 指定したFASTQをoutputディレクトリ内にリンクします．
* **link_import_bam** -- 指定したBAMをoutputディレクトリ内にリンクします．
* **bam2fastq** -- 指定したBAMをFASTQにConvertしoutputディレクトリ内にリンクします．


