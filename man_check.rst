2. 解析結果確認
===================

GenomonPipelineは，下記の出力ディレクトリ階層にて解析結果ファイルを出力します．

.. code-block:: bash
  :caption: DNA解析結果ディレクトリ構成
  
  /home/lect-1/Genomon2_5_2/test5929/  ：出力ルートディレクトリ
    └ fastq/                            ：Fastqファイル
    └ bam/                              ：BAMファイル
        └test_1/
        └test_2/
            └test_2.markdup.bam
            └test_2.markedup.bam.bai
    └ mutation/                         ：変異コール結果
        └test_1/
        └test_2/
            └test_2.genomon_mutation.result.txt
            └test_2.genomon_mutation.result.filt.txt
        └control_panel/
        └hotspot/
    └sv/                                ：SV検出結果
        └test_1/
        └test_2/
            └test_2.genomonSV.result.txt
            └test_2. genomonSV.result.filt.txt
        └control_panel/
        └non_matched_control_panel/
    └qc/                                ：QC結果 (BAMのQuality Control結果)
        └test_1/
        └test_2/
            └test_2.genomonQC.result.txt
    └pmsignature/                       ：pmsignatureによるsignature出力結果
    └post_analysis/                     ：変異コール，SV検出結果とBAMのQC結果をマージした結果
    └paplot/                            ：解析結果をビジュアライゼーションしたレポート
        └test5929/
            └'index.html'
    └config/
    └log/
    └script/




.. code-block:: bash
  :caption: RNA解析結果ディレクトリ構成
  
  /home/lect-1/Genomon2_5_2/test5929/  ：出力ルートディレクトリ
    └ fastq/                            ：Fastqファイル
    └ star/                             ：BAMファイル(マッピング結果)
        └test_1/
        └test_2/
            └test_2.Aligned.sortedByCoord.out.bam
            └test_2.Aligned.sortedByCoord.out.bam.bai
    └ fusion/                           ：融合遺伝子検出結果
        └test_1/
        └test_2/
            └test_2.Chimeric.count
        └control_panel/
    └expression/                        ：発現量解析結果
        └test_1/
        └test_2/
            └test_2.mapped_base_count.txt
            └test_2.ref2base.txt
            └test_2.sym2base.txt
            └test_2.sym2fkpm.txt
    └intron_retention/                  ：Intron Retention検出結果
    └post_analysis/                     ：融合遺伝子検出結果とFastqのQC結果をマージした結果
    └paplot/                            ：解析結果をビジュアライゼーションしたレポート
        └test5929/
            └'index.html'
    └config/
    └log/
    └script/


各解析結果のファイルの詳細については，下記のGenomonドキュメントを参照ください．

 - `DNA解析結果ファイルの説明 <http://genomon.readthedocs.io/ja/latest/dna_results.html>`__
 - `DNA解析で出力されるファイルについて <http://genomon.readthedocs.io/ja/latest/dna_output_info.html>`__
 - `RNA解析結果ファイルの説明 <http://genomon.readthedocs.io/ja/latest/rna_results.html>`__
 - `RNA解析で出力されるファイルについて <http://genomon.readthedocs.io/ja/latest/rna_output_info.html>`__

GenomonPipelineは，解析結果のまとめとして，解析結果をビジュアライゼーションしたレポートを ``paplot`` ディレクトリ内に出力します．
この ``paplot`` ディレクトリをローカルの端末にダウンロードし，ディレクトリの中に含まれる ``index.html`` をウェブブラウザで開いて結果を確認してください．

なお，ジョブがすべて完了しているのにも関わらず，解析結果のまとめである ``index.html`` ファイルが出力されていない場合は，ジョブが異常終了した可能性が考えられます．
次項トラブルシューティングの記述をもとに，原因の切り分けと対応を実施ください．

また，発現量解析結果，Intron Retention検出結果は ``paplot`` レポートには含まれませんので， ``expression`` ディレクトリ， ``intron_retention`` ディレクトリ内に出力される結果をそれぞれ確認してください．

