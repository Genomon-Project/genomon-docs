========================================
DNA解析パイプラインworkfllow
========================================

 .. image:: dna_workflow.png

 | Inputは
 | [fastq], [bam_tofastq], [bam_import] の3種類あります．すべてsample confで定義します．
 | 記載方法は「Sample Configの書き方」をみてください．
 
 
リードアライメント
-----------------------

  :split fastq: 並列してアライメントをするためにFASTQをsplitします．
  :map_dna_sequence: リファレンスゲノムにアライメントします．分割したままの単位でソートします．
  :markdup: sorted BAMに対してmerge＋mark duplicateします．


変異Call
-------------------

  :identify_mutations: interval_listに指定されたゲノムの範囲で変異コールします．ゲノムの範囲毎にジョブを投入します（並列処理します）
  :merge_mutation: ゲノムの範囲毎に出力された結果をマージします．


SV検出
-------------------

   :parse_sv: bamファイルから、breakpointやSVの証拠となるリードをparseします．
   :merge_sv: parse_svの結果から、control panelを作成します．
   :filt_sv: parse_svに対して、control panelやnormalサンプルを用いて偽陽性をフィルタして、SVの候補を検出します．


その他、個別で機能するTask
--------------------------

  :link_input_fastq: project root directory内にFASTQファイルをリンクします．
  :link_input_bam: project root directory内にBAMファイルをリンクします．セットのBAIファイルもlinkします．
  :bam_to2fastq: BAMをFASTQにConvertします．


