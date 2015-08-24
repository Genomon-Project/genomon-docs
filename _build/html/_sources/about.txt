========================
このドキュメントについて
========================

Contuct Us
========================

ご質問やバグを発見の際にはメールにてご連絡ください.

xxxx@xxxx

------------------------

For Editors
========================

このドキュメントはSphinxを利用して作成しています。

記述方法はこちらを参照してください。

 - Sphinx公式　reStructuredText入門_

.. _reStructuredText入門: http://docs.sphinx-users.jp/rest.html

 - Sphinx公式　Sphinxマークアップ集_

.. _Sphinxマークアップ集: http://docs.sphinx-users.jp/markup/index.html

 - reStructuredTextチートシート日本語化プロジェクト rst-cheatsheet_

.. _rst-cheatsheet: https://github.com/takuan-osho/rst-cheatsheet/blob/japanese/rst-cheatsheet.rst


ドキュメントのビルド方法

.. sourcecode:: shell

    ## PythonにSphinxをインストール
    $ pip install Sphinx

    ## git-hubからgenomon-docをclone
    $ git clone -b develop https://github.com/Genomon-Project/genomon-docs.git

    ## ディレクトリルートの*.rstファイルを編集

    ## ビルド
    $ sphinx-build -b html . _build/html

    {doc root}/_build/html/ ディレクトリ配下に *.html ファイルができているので確認

    ## 必要に応じて、commit/push
    $ git commit
    $ git push https://github.com/Genomon-Project/genomon-docs.git develop


