# 第十八周工作总结  

## 本周工作内容  
### 改进mugen中DNF_INSTALL错误信息打印  
- 加入在log中打印缺失软件包信息的功能 [commit](https://github.com/brsf11/mugen-riscv/commit/9520e6381a552e6753840a589d98f1740f9afce7)  
### 尝试在Anolis上运行anolis-pkg-tests测试框架  
- 成功运行avocado框架，但anolis-pkg-tests部分测试用例存在一些问题，并没有完全运行  
### 在Anolis上运行一次完整的mugen测试并整理结果  
- mugen-riscv中加入anolis上运行mugen的依赖安装支持 [commit](https://github.com/brsf11/mugen-riscv/commit/b969180df696f810d7e38f11ddac3235a1715795)  
- 测试了os-basic和systemd两个测试套  