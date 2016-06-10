# -*- coding: utf-8 -*-
"""
Created on Fri Apr 01 09:36:08 2016

@author: okada
"""

import os
    
def fild_all_files(directory, output):
    
    for root, dirs, files in os.walk(directory):

        output.write("<dt><icon/>" + os.path.basename(root) + "</dt>\n<dl>\n")

        for d in dirs:
            fild_all_files(os.path.join(root, d), output)
            
        for f in files:
            ext = os.path.splitext(f)
            ext = ext[1].lower()

            icon = "<icon_text/>"

            if ext == ".xls":
                icon = "<icon_xls/>"
            elif (ext == ".png") or (ext == ".jpg") or (ext == ".jpeg") or (ext == ".gif") or (ext == ".bmp"):
                icon = "<icon_image/>"
            elif (ext == ".tbi") or (ext == ".gz") or (ext == ".zip") or (ext == ".tgz") or (ext == ".tar") or (ext == ".lzh"):
                icon = "<icon_archive/>"

            output.write("<dd>" + icon + os.path.basename(f) + "</dd>\n")  

        output.write("</dl>\n")
        break;
        
def main():
    import argparse
    
    parser = argparse.ArgumentParser("tree")
    
    parser.add_argument("--version", action = "version", version = "1.0")
    parser.add_argument("input_dir", help = "input dir path", type = str)
    parser.add_argument("output_file", help = "output file path", type = str)
    
    args = parser.parse_args()
    
    header = """<html lang="ja">
<head>
  <title>tree</title>

  <meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
  <style type="text/css">
  .filelist{
    background-color: #EEEEEE;
    padding: 12px 24px 12px 24px;
    border: 1px solid #CCCCCC;
    margin: 4px;
    font-size: 16px;
    font-family: sans-serif, "Helvetica Neue", Helvetica, Arial;
    display: block;
    color: #333333;
  }
  .filelist dt, .filelist dd{
    margin: 0px;
    padding: 4px 0 4px 0;
  }
  .filelist dl{
    margin: 0px;
    padding: 0px 0px 0px 30px;
  }
  /* dir style */
  .filelist dl dt:before, .filelist dl dd:before{
    content: "┗";
    float: left;
    width: 20px;
    margin-left: -20px;
    color: #D36015;
  }
  .filelist dt icon:before{
    content: "\\f07c";
    font-family: FontAwesome;
    width: 20px;
    text-align: center;
    display: inline-block;
    color: #D36015;
  }
  /* files icons */
  .filelist dd icon_text:before{
    content: "\\f15c";
    font-family: FontAwesome;
    width: 20px;
    text-align: center;
    display: inline-block;
    color: #2660A1;
  }
  .filelist dd icon_archive:before{
    content: "\\f1c6";
    font-family: FontAwesome;
    width: 20px;
    text-align: center;
    display: inline-block;
    color: #2660A1;
  }
  .filelist dd icon_xls:before{
    content: "\\f1c3";
    font-family: FontAwesome;
    width: 20px;
    text-align: center;
    display: inline-block;
    color: #2660A1;
  }
  .filelist dd icon_image:before{
    content: "\\f1c5";
    font-family: FontAwesome;
    width: 20px;
    text-align: center;
    display: inline-block;
    color: #2660A1;
  }
  </style>
</head>
<body>
<dl class="fa filelist">
"""
    footer = """
</dl>
</body>
</html>
"""
    
    f = open(args.output_file, "w")
    f.write(header)
    
    fild_all_files(os.path.abspath(args.input_dir), f)
        
    f.write(footer)
    f.close()
    
if __name__ == "__main__":
    main()

    
