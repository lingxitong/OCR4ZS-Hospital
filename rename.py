import os
from paddleocr import PaddleOCR
import re
import tqdm

def get_OCR_ANS(img_path,ocr):
    result = ocr.ocr(img_path, cls=True)
    OCR_text = []
    for line in result:
        for sub_line in line:
            OCR_text.append(sub_line[1][0])
    return OCR_text

def remove_non_alphanumeric(s):
    return re.sub(r'[^a-zA-Z0-9]', '', s)

def get_main_id(ocr_ans):
    possible_main_id = [s for s in ocr_ans if s.startswith('F')]
    if len(possible_main_id) == 0:
        return None
    else:
        main_id = possible_main_id[0]
        return remove_non_alphanumeric(main_id)
    
def is_numeric_followed_by_a(s):
    return bool(re.match(r'^\d+a$', s))

def get_ext_id(ocr_ans):
    possible_ext_id = [s for s in ocr_ans if '冰' in s]
    if len(possible_ext_id) == 0:
        return None
    else:
        ext_id = possible_ext_id[0]
        if len(ext_id) == 1:
            return None
        else:
            possible_ext_ids = ext_id.split('冰')
            if possible_ext_ids[0] == '':
                if possible_ext_ids[1].isdigit():
                    last_digit = int(possible_ext_ids[1])
                    front_digit = int(last_digit - 1)
                    return f'{front_digit}_{last_digit}'
                elif is_numeric_followed_by_a(possible_ext_ids[1]):
                    last_digit = possible_ext_ids[1]
                    front_digit = last_digit.replace('a', '')
                    return f'{front_digit}_{last_digit}'
                else:
                    return None
            else:
                if possible_ext_ids[1] == '':
                    if possible_ext_ids[0].isdigit():
                        return possible_ext_ids[0]
                    else:
                        return None
                else:
                    if possible_ext_ids[0].isdigit() and possible_ext_ids[1].isdigit():
                        return f'{possible_ext_ids[0]}_{possible_ext_ids[1]}'
                    elif possible_ext_ids[0].isdigit() and is_numeric_followed_by_a(possible_ext_ids[1]):
                        return f'{possible_ext_ids[0]}_{possible_ext_ids[1]}'
                    else:
                        return None
            


def rename_one(ocr_tool,ocr_jpg_path):
    ocr_ans = get_OCR_ANS(ocr_jpg_path,ocr_tool)
    print(ocr_ans)
    if len(ocr_ans) == 0:
        return None
    main_id = get_main_id(ocr_ans)
    if main_id == None:
        return None
    ext_id = get_ext_id(ocr_ans)
    if ext_id == None:
        return main_id
    else:
        return main_id + '_' + ext_id
    


if __name__ == '__main__':
    # 传入参数
    OCR_JPG_DIR = r'C:\Users\24683\Desktop\ocr_jpg_dir'
    # 创建OCR对象

    ocr_tool = PaddleOCR(use_angle_cls=True, lang="ch")
    ocr_jpg_list = []
    ocr_jpg_paths = [os.path.join(OCR_JPG_DIR,ocr_jpg) for ocr_jpg in os.listdir(OCR_JPG_DIR)]
    for index,ocr_jpg_path in tqdm.tqdm(enumerate(ocr_jpg_paths)):
        new_name = rename_one(ocr_tool,ocr_jpg_path)
        if new_name == None:
            new_name = 'error'
        basename = os.path.basename(ocr_jpg_path).replace('.jpg','')
        new_basename = basename+'#'+new_name+'.jpg'
        new_path = os.path.join(OCR_JPG_DIR,new_basename)
        print(f'{ocr_jpg_path} \033[32m--->\033[0m {new_path}')
        os.rename(ocr_jpg_path,new_path)

        
