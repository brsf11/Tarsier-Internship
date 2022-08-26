# 第九周工作总结  

## 本周工作内容  
### 实现QEMU测试环境复原自动化和多线程测试  
- [commit](https://github.com/brsf11/mugen-riscv/commit/6f5a6efe59a5ad360d1c4d84511807edc917214a)  
- 目前实现的功能：  
    - 指定线程数和测试套列表，脚本自动启动QEMU虚拟机并分配测试套  
    - 每运行一个测试套后还原测试环境，保证每个测试套之间隔离  
    - 脚本将运行结果传回工作目录（包括打印信息、日志和生成的测试套描述文件）  
- 脚本能自动分配可用端口、检测虚拟机开启后何时可用，以及回收虚拟机销毁后的端口资源  
- 运行示例见[日志](https://github.com/brsf11/Tarsier-Internship/blob/main/Report/Misc/week10.log)  