# 第二十四周工作总结  

## 本周工作内容  
### RISCV龙蜥自动化测试  
- 本次测试使用镜像[来源](https://mirrors.openanolis.cn/alt/risc-v/images/)  
- 软件源  
    ```
    [anolisos]
    name=anolisos
    baseurl=http://build.openanolis.cn/kojifiles/rsync/alt/risc-v/riscv64/
    enabled=1
    gpgcheck=0

    [an8]
    name=an8
    baseurl=http://build.openanolis.cn/kojifiles/repos/anolis-riscv64-repo-external/an8/riscv64/
    enabled=1
    gpgcheck=0

    [an8dev]
    name=an8dev
    baseurl=http://build.openanolis.cn/kojifiles/repos/anolis-riscv64-repo-external/an8dev/riscv64/ 
    enabled=1
    gpgcheck=0

    [an8extra]
    name=an8extra
    baseurl=http://build.openanolis.cn/kojifiles/repos/anolis-riscv64-repo-external/an8extra/riscv64/ 
    enabled=1
    gpgcheck=0

    [an8others]
    name=an8others
    baseurl=http://build.openanolis.cn/kojifiles/repos/anolis-riscv64-repo-external/an8others/riscv64/ 
    enabled=1
    gpgcheck=0

    [an8-tmp-extra]
    name=an8-tmp-extra
    baseurl=http://build.openanolis.cn/kojifiles/repos/anolis-riscv64-repo-external/an8-tmp-extra/
    enabled=1
    gpgcheck=0

    [gcc]
    name=gcc
    baseurl=http://build.openanolis.cn/kojifiles/repos/anolis23-riscv64-repo-external/gcc/
    enabled=1
    gpgcheck=0

    [an8-perl-modules]
    name=an8-perl-modules
    baseurl=http://build.openanolis.cn/kojifiles/repos/anolis-riscv64-repo-external/an8-perl-modules/riscv64/
    enabled=1
    gpgcheck=0
    ```
- 测试范围：233个测试套所有除涉及到网络的测试例  