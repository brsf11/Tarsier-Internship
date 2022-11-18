# 第二十一周工作总结  

## 本周工作内容  
### 0926镜像回归自动化测试  
- 经过一次os-basic-riscv完整测试和对之前出错的新产生问题的用例单独测试，排除了所有用例的问题  
- [issue评论](https://gitee.com/openeuler/RISC-V/issues/I5UQ31?from=project-issue#note_14440971_link)  
### RISC-V龙蜥mugen测试  
- 软件源中大概只有300+软件包，手动解决了mugen依赖和配置（使用了oE RISC-V 的tcl和expect）  
- 完整地测试了os-basic测试套138个测试例  
- 通过36个测试例，失败102个，其中41个为qemu环境造成  
- 剩余61个未通过测试例大致分为3类  
    - 软件缺失（包括因为paramiko依赖没有解决无法安装和没有预装）48个  
    - 可能为系统bug，需要进一步分析 12个  
    - 其他，和openEuler行为不一致 1个  
- [测试结果](https://github.com/brsf11/Tarsier-Internship/tree/main/Testing/RISCVAnolis8.6)  