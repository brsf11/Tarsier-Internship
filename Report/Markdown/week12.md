# 第十二周工作总结  

## 本周工作内容  
### 修复qemu_test.py的bug  
- 虚拟机ssh服务坏掉后该分发线程会退出，导致分发线程越来越少的问题 [commit](https://github.com/brsf11/mugen-riscv/commit/71dcc122f8167f83eed2c181e731d8ba52bff251)  
- 分发测试不是原子操作导致的问题 [commit](https://github.com/brsf11/mugen-riscv/commit/71dcc122f8167f83eed2c181e731d8ba52bff251)  
### 修复mugen_riscv.py中的bug  
- python没有重载功能导致的问题 [commit](https://github.com/brsf11/mugen-riscv/commit/39e8cbdb67e01b9bea1db3af17688575bbe047a1)  
### 推进测试用例筛选  
- 167个测试套 [commit](https://github.com/brsf11/mugen-riscv/commit/6ebc7bed19385730b935697fe4d3a6468680691d)  
### 编写mugen_riscv.py的分步使用教程  
- [commit](https://github.com/brsf11/mugen-riscv/commit/c40e621cea327c24c319775f0599bd80c5b1c4ee)