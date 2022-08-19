# 第九周工作总结  

## 本周工作内容  
### 继续完善自动化测试工具  
- [修复](https://github.com/brsf11/mugen-riscv/commit/123eebb1f44aeeed8641122bd134c3ebd9f91798)了[issue4](https://github.com/brsf11/mugen-riscv/issues/4)（运行测试会清空原来的log）  
- 完成issue模板的修改和合并  
### 尝试改进测试效率  
- 研究测试环境复原的方案  
    - 直接复制？  
    - btrfs下snapper  
    - rsync和rsnapshot  