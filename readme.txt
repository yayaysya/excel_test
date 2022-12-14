'''
使用说明:
0. 分解需求, 填充bss_type 要求dev_type bss0 bss1 都写标准  我们的dev_type要和系统的相同
1. 修改config配置文件中的文件名称
2. 把对应的文件都挪到当前目录下. 编译服务器上执行python3.6 main.py
3. 会生成dev_cfg_*_new文件.
'''

'''
-----------
更新日志:22-11-26,
1. 完善初步的版本
just test
2. 增加校验机制, 我们使用的dev_type系统层一定要有;校验ipp的表里面, 是否存在相同的两个dev_type, 但是bss_type却不同;
'''


'''
-----------
TODO:
1. 支持根据ped_type fd_type ... 自动生成bss_type, 并且进行填充.
'''