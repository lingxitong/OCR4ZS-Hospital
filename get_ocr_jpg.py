import opensdpc
import os
import tqdm
import psutil


def get_memory_usage_percentage():
    memory_info = psutil.virtual_memory()
    memory_usage_percentage = (memory_info.used / memory_info.total) * 100
    return memory_usage_percentage


if __name__ == '__main__':
    # 传入参数
    SDPC_DIR = '/mnt/net_sda/SDPC'
    OCR_JPG_DIR = '/mnt/net_sda/SDPC/ocr_jpg_dir'
    wsi_list = [os.path.join(SDPC_DIR, wsi) for wsi in os.listdir(SDPC_DIR) if wsi.endswith('.sdpc')]
    for wsi_path in tqdm.tqdm(wsi_list):
        m_per = get_memory_usage_percentage()
        if m_per > 80:
            print('内存占用过高，退出程序')
            break 
        basename = os.path.basename(wsi_path).replace('.sdpc','jpg')
        ocr_jpg_path = os.path.join(OCR_JPG_DIR,basename)
        if os.path.exists(ocr_jpg_path):
            continue
        wsi = opensdpc.OpenSdpc(wsi_path)
        wsi.saveLabelImg(ocr_jpg_path)