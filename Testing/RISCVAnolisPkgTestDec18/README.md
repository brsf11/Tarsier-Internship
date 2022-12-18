# RISC-V 龙蜥软件包 mugen自动化测试结果说明  
## 测试说明  
### 测试范围  
- 本次测试范围涵盖所有在RISCV龙蜥软件源中有对应包的mugen测试套（测试套说明见下节关于mugen的详细说明）  
- 共230个测试套(230个软件包)，957个测试用例  
### 测试框架和测试方法  
- 测试框架：mugen-riscv  
- 测试框架仓库：https://github.com/brsf11/mugen-riscv  
- 关于mugen：[详细说明](https://github.com/brsf11/Tarsier-Internship/blob/main/Presentation/RISC-V-oE-Autotest-Dev/Markdown/report.md)  
- mugen-riscv是由PLCT Tarsier下属第三测试小队维护的一个mugen分支，用于RedHat系RISC-V发行版的自动化测试。分支相对于mugen增加了一些用于qemu镜像自动化测试的脚本，以及测试脚本针对RISC-V架构适配的修改，但绝大部分测试用例和测试套与上游保持一致。  
- 测试方式：测试环境自动复原，测试套间隔离以及自动分配硬盘外设资源的自动化测试  
    使用qemu_test.py，利用qemu qcow2快照实现在测试每个测试套时单独建立qemu虚拟机进行测试，保证了测试套间不会相互干扰。测试程序运行时会根据测试套文件中"add disk"字段的信息，自动创建硬盘资源并分配给对应的虚拟机。  
- 测试用例代码位置：https://github.com/brsf11/mugen-riscv/tree/riscv/testcases/cli-test/对应测试套名/对应测试用例名.sh  

### 测试环境  
- 本次测试使用镜像：https://mirrors.openanolis.cn/alt/risc-v/images/  
- 软件源：见AnolisOS-riscv.repo文件  
- CPU核数：8  
- 内存大小：8G  
- qemu启动参数：  
    ```shell
    qemu-system-riscv64 \
    -nographic -machine virt  \
    -smp 8 -m 8G \
    -audiodev pa,id=snd0 \
    -kernel u-boot.bin \
    -bios fw_dynamic.bin \
    -drive file=anolisos-disk-new.qcow2,format=qcow2,id=hd0 \
    -object rng-random,filename=/dev/urandom,id=rng0 \
    -device virtio-rng-device,rng=rng0 \
    -device virtio-blk-device,drive=hd0 \
    -device virtio-net-device,netdev=usernet \
    -netdev user,id=usernet,hostfwd=tcp::"ssh_port"-:22 \
    -device qemu-xhci -usb -device usb-kbd -device usb-tablet -device usb-audio,audiodev=snd0 \
    -append 'root=/dev/vda1 rw console=ttyS0 swiotlb=1 loglevel=3 systemd.default_timeout_start_sec=600 selinux=0 highres=off mem=8192M earlycon' 
    ```
- 附加硬盘qemu参数：
    ```shell
    -drive file=disk"self.id-i".qcow2,format=qcow2,id=hd"i" -device virtio-blk-pci,drive=hd"i"
    ```
    self.id：测试时为对应虚拟机的id  
    i：测试时为某一虚拟机的硬盘序号  
- anolisos-disk-new.qcow2处理  
    anolisos-disk-new.qcow2由原始镜像anolisos-disk-minimal-an8-Rawhide-sda.raw扩容至22G后转为qcow2格式而来  
## 测试结果说明  
### 测试结果文件结构  
- [logs文件夹](https://github.com/brsf11/Tarsier-Internship/tree/main/Testing/RISCVAnolisPkgTestDec18/logs)：所有测试用例的日志文件  
- [logs_failed文件夹](https://github.com/brsf11/Tarsier-Internship/tree/main/Testing/RISCVAnolisPkgTestDec18/logs_failed)：所有未通过测试用例的日志文件  
- [suite2cases_failed文件夹](https://github.com/brsf11/Tarsier-Internship/tree/main/Testing/RISCVAnolisPkgTestDec18/suite2cases_failed):每个测试套中未通过的测试用例，以测试套描述文件的形式  
- [suite2cases_passed文件夹](https://github.com/brsf11/Tarsier-Internship/tree/main/Testing/RISCVAnolisPkgTestDec18/suite2cases_passed)：每个测试套中通过的测试用例，以测试套描述文件的形式  
- [Dec18Test.ods](https://github.com/brsf11/Tarsier-Internship/blob/main/Testing/RISCVAnolisPkgTestDec18/Dec18Test.ods):测试结果的详细数据统计  
### 测试日志说明  
- 测试日志中包含测试运行时执行的命令和命令的打印信息，以+（一个或多个）开头的行为执行的命令，不以+开头的行为命令的打印信息  
- 例如fio/oe_test_fio_002日志67~87行  
    ```
    + fio-dedupe -c 1 /dev/
    + grep 'items processed'
    + CHECK_RESULT 1 0 0 'fio-dedupe -c option failed'
    + actual_result=1
    + expect_result=0
    + mode=0
    + error_log='fio-dedupe -c option failed'
    + '[' -z 1 ']'
    + '[' 0 -eq 0 ']'
    + test 1x '!=' 0x
    + test -n 'fio-dedupe -c option failed'
    + LOG_ERROR 'fio-dedupe -c option failed'
    + message='fio-dedupe -c option failed'
    + python3 /root/mugen-riscv/libs/locallibs/mugen_log.py --level error --message 'fio-dedupe -c option failed'
    Wed Dec  7 01:12:07 2022 - ERROR - fio-dedupe -c option failed
    + (( exec_result++ ))
    + LOG_ERROR 'oe_test_fio_002.sh line 33'
    + message='oe_test_fio_002.sh line 33'
    + python3 /root/mugen-riscv/libs/locallibs/mugen_log.py --level error --message 'oe_test_fio_002.sh line 33'
    Wed Dec  7 01:12:08 2022 - ERROR - oe_test_fio_002.sh line 33
    + return 0
    ```
    对应测试用例fio/oe_test_fio_002.sh中32~33行  
    ```
    fio-dedupe -c 1 /dev/${local_disk1} | grep "items processed"
    CHECK_RESULT $? 0 0 "fio-dedupe -c option failed"
    ```
    测试用例先执行```fio-dedupe -c 1 /dev/${local_disk1} | grep "items processed"```  
    后执行```CHECK_RESULT $? 0 0 "fio-dedupe -c option failed"```比较返回值是否等于0  
    日志```Wed Dec  7 01:12:08 2022 - ERROR - oe_test_fio_002.sh line 33```中提示出错代码对应的用例代码文件为oe_test_fio_002.sh，行数为33行  
## 测试结果  
- 测试中有大量软件包在安装时遇到依赖缺失的问题（大部分全部未通过的测试套为此问题）。其余的测试套测试正常，测试用例未通过可能是由软件包bug造成，详细结果见未通过测试用例日志[logs_failed](https://github.com/brsf11/Tarsier-Internship/tree/main/Testing/RISCVAnolisPkgTestDec18/logs_failed)。
- 详细结果统计见[Dec18Test.ods](https://github.com/brsf11/Tarsier-Internship/blob/main/Testing/RISCVAnolisPkgTestDec18/Dec18Test.ods)  
