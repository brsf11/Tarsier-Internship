# 第十三周工作总结  

## 本周工作内容  
### 完成mugen测试例的第一步筛选工作  
- 目前已完成以8月18日22.09测试镜像为基准的mugen测试例筛选工作，筛选的对象包括os-basic和源中有的314个软件包，只有systemd由于环境原因还未完成  
- [commit1](https://github.com/brsf11/mugen-riscv/commit/5d0aca796e9380f696226835dc7f5498e4efd718)  
- [commit2](https://github.com/brsf11/mugen-riscv/commit/46e954117d8af8a72fa049526ad004954a955b6e)  
- 存在的问题  
    - 以什么作为参考？（22.03 x86 oE？）  
- 后续会将log上传，以及需要修复的测试套提交issue  
### 后续测试例修复工作  
- 简称修复但实际上包括查找未通过的测试例问题到底出在哪，以及是否需要修改和之后的修改的工作  
- 从os-basic开始，计划两周完成  
- 可能会遇到的情况  
    - 测试用例本身有问题（x86上也无法通过）  
    - 测试例本身在x86上无问题  
        - 环境问题（需要多节点以及挂载硬盘和网络接口，现阶段跳过）  
        - 测试例未适配RISC-V（因为oE RISC-V和oE X86本身在功能上的一些不同导致测试例未通过，在测试例中加入相应适配可解决）（如oe_test_uname）  
        - 被测对象的问题（被测的oE RISC-V镜像本身的问题，以X86作为参考）  