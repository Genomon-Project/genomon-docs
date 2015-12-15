========================================
DNA解析結果
========================================
Human Genome Center (HGC)ではGenomonはインストール済みです．早速動かしてみましょう。

結果ファイル
------------------
:bam: project_root_directory/bam/sample/sample_markdup.bam
:変異Call結果: project_root_directory/mutation/sample名/sample名_genomon_mutations.result.txt
:SV検出結果: project_root_directory/sv/sample名/sample名.genomonSV.result.txt

変異Call結果 各カラムの説明
---------------------------
:Chr Start End: 変異候補のポジション
:Ref: 変異候補のポジションのリファレンス塩基です．Insertion の場合は"-"ハイフンが表示されます．
:Alt: 変異候補のポジションの塩基配列です．Deletion の場合は"-"ハイフンになります．
:annovarの結果:annovarをご使用の方はannovarの結果が出力されます．各カラムの説明はannovarのwebページでチェックしてください．http://annovar.openbioinformatics.org/en/latest/user-guide/download/
:depth_tumor: Tumorのdepth
:variantNum_tumor: Tumorのvariantの数
:depth_normal: Normalのdepth
:variantNum_normal: Normalのvariantの数
:A,C,G,T_tumor: Tumorの塩基数．SNVの場合は（A,C,G,T) の各個数，indel の場合は (Depth, indelのリード数) になります．
:A,C,G,T_normal: Normalの塩基数．
:mismatch_rate_tumor: Tumorのミスマッチ率．
:strand_ratio_tumor: Tumorのstrand ratio．
:mismatch_rate_normal: Normalのミスマッチ率
:strand_ratio_normal: Normalのstrand ratio.
:P-value(fisher): Fisher -log10(p値)
:RefNum_tumor: 変異を含まないリード数
:AltNum_tumor: 変異を含むリード数
:OtherNum_tumor: リアライメントできなかったリード数
:RefNum_normal: 変異を含まないリード数
:AltNum_normal: 変異を含むリード数
:OtherNum_normal: リアライメントできなかったリード数
:P-value(fisher)_realignment: Fisher -log10(p値) tableは((RefNum_tumor,RefNum_normal),(AltNum_tumor,AltNum_normal))
:indel_variantNum: 変異候補周辺のindelを含むリード数(indelは同一ポジションであれば加算される)
:indel_mismatch_rate: 上記indelのミスマッチ率
:bp_mismatch_count: 変異候補周辺のbreakpointを含むリード数(breakpointは同一ポジションにあれば加算される)
:distance_from_breakpoint: 変異候補からbreakpoointが何塩基離れているか表示されます．
:simple_repeat_pos: 変異候補のポジションとSimpleRepeatに登録されているポジションがintersectした場合にSimpleRepeatのポジションが表示されます．
:simple_repeat_seq: 上記SimpleRepeatの配列
:P-value(EBCall): EBCall -log10(p値)

変異Callおすすめフィルタ
------------------
 | Fisher（P-value）>= 1.0
 | EBCall（P-value）>= 4.0
 | variantPairNum_tumor >= 4
 | variantPairNum_normal <= 1(固形腫瘍) <= 2(血液腫瘍)
 | 
 | NormalサンプルにTumor contentが入っているとP値が低くなります。がん原因遺伝子がフィルタで消えてないか確認しましょう．


SV検出結果 各カラムの説明
---------------------------
:1: chromosome for the 1st breakpoint
:2: coordinate for the 1st breakpoint
:3: direction of the 1st breakpoint
:4: chromosome for the 2nd breakpoint
:5: coordinate for the 2nd breakpoint
:6: direction of the 2nd breakpoint
:7: inserted nucleotides within the breakpoints
:8: type of the structural variation
:9: gene overlapping the 1st breakpoint
:10: gene overlapping the 2nd breakpoint
:11: exon overlapping the 1st breakpoint
:12: exon overlapping the 2nd breakpoint
:13: #read_pairs not supporting the variant (reference read pairs) for the tumor sample
:14: #read_pairs supporting the variant (variant read paris) for the tumor sample
:15: frequency of variant read pairs for the tumor sample
:16: #read_pairs not supporting the variant for the matched control sample
:17: #read_pairs supporting the variant for the matched control sample
:18: frequency of variant read pairs for the matched control sample
:19: p-value for the Fisher's exact text (on contingency table of (tumor v.s. matched control) and (reference v.s. variant read pairs)



