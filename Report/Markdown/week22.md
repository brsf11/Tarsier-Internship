# 第二十二周工作总结  

## 本周工作内容  
### 对RISC-V 龙蜥的测试  
- 本次测试使用镜像[来源](https://mirrors.openanolis.cn/alt/risc-v/images/)，软件源：[an8](http://build.openanolis.cn/kojifiles/repos/anolis-riscv64-repo-external/an8/riscv64/) [gcc](http://build.openanolis.cn/kojifiles/repos/anolis23-riscv64-repo-external/gcc/) [an8extra](http://build.openanolis.cn/kojifiles/repos/anolis-riscv64-repo-external/an8extra/riscv64/) [anolis-riscv](http://build.openanolis.cn/kojifiles/rsync/alt/risc-v/riscv64/)  
- 为保证测试结果有效性，本次测试了筛选过后的mugen os-basic测试套中的56个测试用例  
- 测试结果：46个用例通过，10个用例失败  
- 测试用例代码可在[此处](https://github.com/brsf11/mugen-riscv/tree/riscv/testcases/system-test/system-integration/os-basic)找到  
- 10个测试失败用例的日志文件在此目录的logs/os-basic中  
- 通过的46个用例列表为passed_tests  