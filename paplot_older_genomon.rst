**********************************************
過去バージョンの解析結果でレポート出力
**********************************************

※paplotのインストールに関しては `paplot-doc <http://paplot-doc.readthedocs.io/ja/latest/quick_start.html>`_ を参照ください

-----------------------------
paplot 設定ファイル
-----------------------------

過去バージョンのGenomon-pipelineの解析結果に対して，設定ファイルを用意しています．

``{paplotをダウンロードしたディレクトリ}/config_template``

====================================== ===============================
file name                              version
====================================== ===============================
genomon_v2_0_0.cfg                     Genomon 2.0.0 ～ 2.0.3 
genomon_v2_0_5_v2_0_4.cfg              Genomon 2.0.4 ～ 2.0.5
genomon_v2_2_0_merge.cfg               Genomon 2.2.0
genomon_v2_3_0_merge.cfg               Genomon 2.3.0
genomon_v2_4_0_dna_merge.cfg           Genomon 2.4.0 (dna)
genomon_v2_4_0_rna_merge.cfg           Genomon 2.4.0 (rna)
====================================== ===============================

※ Genomon 2.4.0 よりrna結果のpaplot出力に対応しました．

----------------------------------
Genomonバージョンの見分け方
----------------------------------

Genomon-pipeline の結果ファイルをもとにして，Genomonのバージョンを判断します

============================= ================== ================= =============== ==================
version                       mutation           sv                qc              post-analysis
============================= ================== ================= =============== ==================
Genomon 2.0.0 ～ 2.0.3        ヘッダなし         ヘッダなし        結果なし        結果なし
Genomon 2.0.4 ～ 2.0.5        ヘッダあり         ヘッダなし        結果あり        結果なし
Genomon 2.2.0                 ヘッダあり         ヘッダあり        結果あり        結果あり
============================= ================== ================= =============== ==================

※genomon 2.3.0 以降はpaplot/{サンプルファイル名}/index.html にGenomon-pipeline のバージョン名を出力しています．

-----------------------------
paplot実行例
-----------------------------

Genomon 2.4.0

.. code-block:: bash

  genomon_root={Genomonを実行したディレクトリ}
  sample={Genomon実行時のサンプルファイル名}
  output_dir={paplotの出力ディレクトリ, 任意}
  paplot_dir={paplotをダウンロードしたディレクトリ}

  ### dna
  # QC
  paplot qc \
  ${genomon_root}/post_analysis/${sample}/merge_qc.txt \
  ${output_dir} \
  Genomon \
  --config_file ${paplot_dir}/config_template/genomon_v2_4_0_dna_merge.cfg

  # SV
  paplot ca \
  ${genomon_root}/post_analysis/${sample}/merge_sv_filt_pair_controlpanel.txt \
  ${output_dir} \
  Genomon \
  --config_file ${paplot_dir}/config_template/genomon_v2_4_0_dna_merge.cfg
  
  # mutation
  paplot mutation \
  ${genomon_root}/post_analysis/${sample}/merge_mutation_filt_pair_controlpanel.txt \
  ${output_dir} \
  Genomon \
  --config_file ${paplot_dir}/config_template/genomon_v2_4_0_dna_merge.cfg
  
  ### rna
  
  # star-QC
  paplot qc \
  ${genomon_root}/post_analysis/${sample}/merge_starqc.txt \
  ${output_dir} \
  Genomon_RNA \
  --config_file ${paplot_dir}/config_template/genomon_v2_4_0_rna_merge.cfg
  
  # fusion
  paplot ca \
  ${genomon_root}/post_analysis/${sample}/merge_fusionfusion_filt.txt \
  ${output_dir} \
  Genomon_RNA \
  --config_file ${paplot_dir}/config_template/genomon_v2_4_0_rna_merge.cfg

Genomon 2.3.0 (DNAのみ)

.. code-block:: bash

  genomon_root={Genomonを実行したディレクトリ}
  sample={Genomon実行時のサンプルファイル名}
  output_dir={paplotの出力ディレクトリ, 任意}
  paplot_dir={paplotをダウンロードしたディレクトリ}
  
  # QC
  paplot qc \
  ${genomon_root}/post_analysis/${sample}/merge_qc.txt \
  ${output_dir} \
  Genomon \
  --config_file ${paplot_dir}/config_template/genomon_v2_3_0_merge.cfg
  
  # SV
  paplot ca \
  ${genomon_root}/post_analysis/${sample}/merge_sv_filt_pair_controlpanel.txt \
  ${output_dir} \
  Genomon \
  --config_file ${paplot_dir}/config_template/genomon_v2_3_0_merge.cfg
  
  # mutation
  paplot mutation \
  ${genomon_root}/post_analysis/${sample}/merge_mutation_filt_pair_controlpanel.txt \
  ${output_dir} \
  Genomon \
  --config_file ${paplot_dir}/config_template/genomon_v2_3_0_merge.cfg

Genomon 2.2.0 (DNAのみ)

.. code-block:: bash

  genomon_root={Genomonを実行したディレクトリ}
  sample={Genomon実行時のサンプルファイル名}
  output_dir={paplotの出力ディレクトリ, 任意}
  paplot_dir={paplotをダウンロードしたディレクトリ}
  
  # QC
  paplot qc ${genomon_root}/post_analysis/${sample}/merge_qc.txt \
  ${output_dir} \
  Genomon \
  --config_file ${paplot_dir}/config_template/genomon_v2_2_0_merge.cfg
  
  # SV
  paplot ca ${genomon_root}/post_analysis/${sample}/merge_sv_filt_pair_controlpanel.txt \
  ${output_dir} \
  Genomon \
  --config_file ${paplot_dir}/config_template/genomon_v2_2_0_merge.cfg
  
  # mutation
  paplot mutation \
  ${genomon_root}/post_analysis/${sample}/merge_mutation_filt_pair_controlpanel.txt \
  ${output_dir} \
  Genomon \
  --config_file ${paplot_dir}/config_template/genomon_v2_2_0_merge.cfg

Genomon 2.0.4 or Genomon 2.0.5 (DNAのみ)

.. code-block:: bash

  genomon_root={Genomonを実行したディレクトリ}
  sample={Genomon実行時のサンプルファイル名}
  output_dir={paplotの出力ディレクトリ, 任意}
  paplot_dir={paplotをダウンロードしたディレクトリ}
  
  # QC
  paplot qc \
  "${genomon_root}/summary/*/*.tsv" \
  ${output_dir} \
  Genomon \
  --config_file ${paplot_dir}/config_template/genomon_v2_0_5_v2_0_4.cfg

  # SV
  paplot ca \
  "${genomon_root}/sv/*/*.genomonSV.result.txt" \
  ${output_dir} \
  Genomon \
  --config_file ${paplot_dir}/config_template/genomon_v2_0_5_v2_0_4.cfg

  # mutation
  paplot mutation \
  "${genomon_root}/mutation/*/*_genomon_mutations.result.txt" \
  ${output_dir} \
  Genomon \
  --config_file ${paplot_dir}/config_template/genomon_v2_0_5_v2_0_4.cfg

Genomon 2.0.0 ～ 2.0.3 (DNAのみ)

.. code-block:: bash

  genomon_root={Genomonを実行したディレクトリ}
  sample={Genomon実行時のサンプルファイル名}
  output_dir={paplotの出力ディレクトリ, 任意}
  paplot_dir={paplotをダウンロードしたディレクトリ}
  
  # SV
  paplot ca \
  "${genomon_root}/sv/*/*.genomonSV.result.txt" \
  ${output_dir} \
  Genomon \
  --config_file ${paplot_dir}/config_template/genomon_v2_0_0.cfg
  
  # mutation
  paplot mutation \
  "${genomon_root}/mutation/*/*_genomon_mutations.result.txt" \
  ${output_dir} \
  Genomon \
  --config_file ${paplot_dir}/config_template/genomon_v2_0_0.cfg


-------------------------------------
過去の変異結果でsignature出力
-------------------------------------

Genomon最新版で再度実行するのが最も簡単ですが，手動で行うこともできます．

以下を参照ください．

 - `signature <http://paplot-doc.readthedocs.io/ja/latest/exec_signature.html>`_ 
 - `pmsignature <http://paplot-doc.readthedocs.io/ja/latest/exec_pmsignature.html>`_ 

