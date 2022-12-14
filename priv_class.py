import logging
import os


# 私有类
class CTRL:
    sys_dev_cfg_filename = 'dev_cfg_h8.xlsx'
    ipp_bss_cfg_filename = 'dsp需求分解.xlsx'
    sys_dev_cfg_excel = 0
    ipp_bss_cfg_excel= 0
    sys_dev_cfg_sheet = 0
    ipp_bss_cfg_sheet = 0
    sys_dev_type_cell = 0
    sys_bss0_cell = 0
    ipp_dev_type_cell = 0
    ipp_bss_cell = 0

# 私有方法
def init_log(path):
    if os.path.exists(path):
        mode = 'w'
    else:
        mode = 'w'
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] <%(filename)s>[%(lineno)d] %(message)s',
        #filename='log.txt',
        #filemode=mode,
    )

    return logging