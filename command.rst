========================================
コマンドの実行
========================================

コマンドは下記のように実行してください。

.. code-block:: bash

    ./Genomon [Analysis type: DNA|RNA] [Output directory] [sample list file]

Analysis typeには、DNA解析をする場合は、'DNA'を、RNA解析をする場合は、'RNA'を指定してください。


DNA解析
========================================
実行例

.. code-block:: bash

    ./Genomon DNA ~/tmp DNA_sample.xlsx


test

RNA解析
========================================

実行例

.. code-block:: bash

    ./Genomon RNA ~/tmp RNA_sample.xlsx


その他の設定
=========================================

.. code-block:: bash


    positional arguments:
      analysis_type
                            Analysis type [DNA|RNA]
      output_directory
                            Output directory
      sample_file
                            Sample list file [csv/tsv/xlsx]

    optional arguments:
      -h, --help            show this help message and exit
      -s CONFIG_FILE, --config_file CONFIG_FILE
                            Genomon pipeline configuration file
      -f JOB_FILE, --job_file JOB_FILE
                            Genomon pipeline job configuration file
      -p PARAM_FILE, --param_file PARAM_FILE
                            Genomon pipeline analysis parameter file
      -v VERBOSE, --verbose VERBOSE
                            Print more verbose messages for each additional
                            verbose level.
      -L LOG_FILE, --log_file LOG_FILE
                            Name and path of log file
      -j JOBS, --jobs JOBS  Allow N jobs (commands) to run simultaneously.
      -o MULTIPROCESS, --multiprocess MULTIPROCESS
                            Number of multiprocesses to run
      -r MULTITHREAD, --multithread MULTITHREAD
                            Number of multithread to run
      -u, --use_threads     Use multiple threads rather than processes. Needs
                            --jobs N with N > 1
      --stop_pipeline       Stop pipeline if a job failed.
      --touch_files_only TOUCH_FILES_ONLY
                            Don't actually run the pipeline; just 'touch' the
                            output for each tasks to make them appear up to date.
      --recreate_database RECREATE_DATABASE
                            Don't actually run the pipeline; just recreate the
                            checksum database.
      --checksum_file_name FILE
                            Path of the checksum file.
      -d, --drmaa           Use DRMAA job submission
      -l, --abpath          Use absolute path in scripts
