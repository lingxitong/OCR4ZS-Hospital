# OCR4ZS-Hospital
OCR scripts for WSI rename of ZS-Hospital

## Rename Pipeline
### 1.get label images from sdpc
`python get_ocr_jpg_menitor.py`

(A)linux-environment: `pip install opensdpc`

(B)win-environment: 
`pip install sdpc-win` 

`Use Sdpc.py to replace the Sdpc.py in XXX/Anaconda3/envs/ZN-OCR/Lib/site-packages/sdpc/Sdpc.py`


### 2.use paddle-ocr for rename

`python rename.py`
environment: `pip install paddlepaddle,paddleocr`

### 3.manually fix naming
 
the name after `rename.py` will be `{ORI_NAME}#{OCR_NAME}`,but the `{OCR_NAME}` may has error, so you should fix the `{OCR_NAME}` manually

### 4.get rename map csv

`python get_rename_map_csv.py`

you will get csv like this:
```
ori,rename
ori_1,F20121121_1
ori_2,F20381108_2
```

### 5.Rename it!!

