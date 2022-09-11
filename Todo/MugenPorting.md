## Mugen RISC-V移植计划  
1. 完成[list_pkglist](https://github.com/brsf11/mugen-riscv/blob/riscv/lists/list_pkglist)中所有测试套的初步筛选（通过的测试例） 计划2022年9月17日前  
2. 完成未通过测试例的鉴别和修复工作，计划如下  
    - os-basic 计划两周完成  
    - system-integration(os-basic + os-storage) (system-test所有？) 视os-storage在qemu上测试可行性决定，也可能跳过  
    - ORSP005系统基本可用性中[预装包](https://gitee.com/openeuler/RISC-V/blob/master/proposal/ORSP005/openEulerRISC-V%E7%9A%84%E7%B3%BB%E7%BB%9F%E9%95%9C%E5%83%8F%E5%92%8C%E6%BA%90%E7%9A%84%E5%9F%BA%E6%9C%AC%E5%8F%AF%E7%94%A8%E6%80%A7%E5%AE%9A%E4%B9%89.md) ([list_minimal](https://github.com/brsf11/mugen-riscv/blob/riscv/lists/list_minimal))在mugen中有的测试套 计划一个月左右  
    - oE RISC-V软件源中所有在mugen中有对应测试套的 ([list_pkglist](https://github.com/brsf11/mugen-riscv/blob/riscv/lists/list_pkglist)) 长期工作    
3. 缺失测试例/测试套的开发工作  
    - ORSP005系统基本可用性中[预装包](https://gitee.com/openeuler/RISC-V/blob/master/proposal/ORSP005/openEulerRISC-V%E7%9A%84%E7%B3%BB%E7%BB%9F%E9%95%9C%E5%83%8F%E5%92%8C%E6%BA%90%E7%9A%84%E5%9F%BA%E6%9C%AC%E5%8F%AF%E7%94%A8%E6%80%A7%E5%AE%9A%E4%B9%89.md) ([list_minimal](https://github.com/brsf11/mugen-riscv/blob/riscv/lists/list_minimal))缺失的  
    - 其他可用mugen测试的包  