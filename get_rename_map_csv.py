import pandas as pd
import os

if __name__ == '__main__':
    # 传入参数
    ocr_jpg_rename_ok_dir = r'C:\Users\24683\Desktop\ocr_jpg_dir'
    csv_path = r'C:\Users\24683\Desktop\ocr_jpg_dir.csv'

    ocr_jpg_paths = [os.path.join(ocr_jpg_rename_ok_dir, ocr_jpg) for ocr_jpg in os.listdir(ocr_jpg_rename_ok_dir) if ocr_jpg.endswith('.jpg')]
    ocr_jpg_names = [os.path.basename(ocr_jpg).replace('.jpg','') for ocr_jpg in ocr_jpg_paths]

    # 分割字符串并创建DataFrame
    data = [name.split('#') for name in ocr_jpg_names]
    df = pd.DataFrame(data, columns=['ori', 'rename'])

    # 保存为CSV文件
    df.to_csv(csv_path, index=False)