# 第七周工作总结  

## 本周工作内容  
### 文档  
- [mugen-riscv测试用例筛选规范](https://github.com/brsf11/mugen-riscv/blob/riscv/doc_riscv/Markdown/mugen-riscv%E6%B5%8B%E8%AF%95%E7%94%A8%E4%BE%8B%E7%AD%9B%E9%80%89%E8%A7%84%E8%8C%83.md)  
- [RISC-V-oE自动化测试脚本的使用](https://github.com/brsf11/mugen-riscv/blob/riscv/doc_riscv/Markdown/RISC-V-oE%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E8%84%9A%E6%9C%AC%E4%BD%BF%E7%94%A8.md)  
### mugen-riscv开发工作流程探索  
- [报告文档](https://github.com/brsf11/Tarsier-Internship/blob/main/Presentation/RISC-V-mugen-Workflow/Markdown/report.md)  
### mugen-riscv开发工作  
- 建立了mugen-riscv仓库 https://github.com/brsf11/mugen-riscv  
- runtest.py（RISC-V-oE自动化测试脚本）增添了一系列功能  
    - 测试套分类功能（mugen原生和riscv测试套）  
    - riscv测试套优先运行功能  
    - 原生模式（默认运行mugen原生测试套）  
    - 引入argparse  
    - 改善了代码鲁棒性  