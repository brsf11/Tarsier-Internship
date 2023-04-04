# 0331 23.03oE自动化测试说明
- 镜像（不需要xfce，统一使用base）：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/testing/20230331_openEuler-23.03-V1-riscv64/QEMU/  
- mugen使用[gitee仓](https://gitee.com/src-oerv/mugen)最新版本(2b5c190)
- qemu_test.py运行推荐用-F加配置文件的方法，参考配置文件为oE23030331，理论上只用修改workingDir和listFile，酌情修改该threads cores memory
- mugen_ready.qcow2为克隆好mugen(到/root/mugen目录)、运行dep_install.sh和使用mugen.sh -c配置好节点后的镜像，推荐创建一个qemu的写时复制镜像来完成这件事。后续qemu_test测试时会在这个镜像的基础上再创建写时复制镜像用于每个测试套的测试
- 需要进行以下几处改动
    - 更改镜像yum源，将每个仓目录改为https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/testing/20230331_openEuler-23.03-V1-riscv64/repo/下对应的目录
    - 删除qemu_test.py 150行append参数，并在上一行末添加引号（计划后面修改添加参数的方式，因此本次测试暂时手动修改以下）
    - 将suite2cases/binutils.json中的全角逗号改为半角，删除最后一行的~（上游留的bug，后面会提pr）
    