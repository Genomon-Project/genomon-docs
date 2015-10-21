========================================
DNA解析パイプラインworkfllow
========================================

 .. image:: dna_workflow.png

 | Inputは
 | [fastq], [bam_tofastq], [bam_import] の3種類あります。すべてsample confで定義します。
 | 記載方法は「Sample Configの書き方」をみてください。
 
 
リードアライメントstage
-----------------------

  :split fastq: 並列してアライメントをするためにFASTQをsplitします。
  :map_dna_sequence: リファレンスゲノムにアライメントします．分割したままの単位でソートします．
  :markdup: sorted BAMに対してmerge＋mark duplicateします．


変異Call stage
-------------------

  :identify_mutations: interval_listに指定されたゲノムの範囲で変異コールします．ゲノムの範囲毎にジョブを投入します（並列処理します）
  :map_dna_sequence: ゲノムの範囲毎に出力された結果をマージします．


SV検出 stage
-------------------

   :parse_sv: bamファイルから、breakpointやSVの証拠となるリードをparseします．
   :merge_sv: parse_svの結果から、control panelを作成します．
   :filt_sv: parse_svに対して、control panelやnormalサンプルを用いて偽陽性をフィルタして、SVの候補を検出します。



