# 第十九周工作总结  

## 本周工作内容  
### qemu_test.py功能更新  
- 增加了根据软件源生成测试列表的功能 [commit](https://github.com/brsf11/mugen-riscv/commit/8d9ad2dad58fcc77ec6ad7842c05b1b8bc1049f6)  
- 增加了输入测试配置文件的功能 [commit](https://github.com/brsf11/mugen-riscv/commit/25b974ee8a39d5c83a647a30397f4cda93dc6d7f)  
### 分析上周在anolis上mugen和anolis-pkg-tests用例的未通过原因  
- anolis-pkg-tests官方更名为anolis-sys-tests  
- anolis-sys-tests因为avocado配置存在很多问题，本周未进一步研究  
- mugen测试  
    - systemd测试套 129/160 os-basic 57/138 (openEuler riscv systemd 120/160 os-basic 60/138)  
    - 本次测试所用python版本为3.6，paramiko库安装有问题  
    - os-basic未通过测试90%是由于paramiko有问题，涉及到两种情况，其一需要多节点和ssh，其二用到DNF_INSTALL，使用python3.9解决paramiko问题后预计属于第二种情况的测试用例还能通过一部分  
    - 剩下小部分用例未通过原因是anolis和openEuler行为不同  
### 其他  
- 构建了Deepin RISC-V的QEMU虚拟机  