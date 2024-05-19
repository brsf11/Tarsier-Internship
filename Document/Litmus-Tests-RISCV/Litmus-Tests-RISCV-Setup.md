# Litmus-Tests-RISCV RISC-V内存一致性石蕊测试集
## Litmus-Tests-RISCV介绍
- sail-riscv项目用于对RISC-V指令集的形式化描述。除了对RISC-V指令的行为描述外，其还包含了对RISC-V的内存一致性模型，即RVWMO的形式化描述。因此一些用于对并行执行行为进行测试或理论推导的工具也使用sail-riscv作为RISC-V的定义，如[RMEM](http://www.cl.cam.ac.uk/users/pes20/rmem)和[isla-axiomatic](https://isla-axiomatic.cl.cam.ac.uk/)等。
- 并行执行行为规范的其中一个重要组成是内存一致性模型。与内存一致性模型经常被人一起提到的是缓存一致性（Cache Coherence）。简单的来说，在拥有多个同级缓存的系统中，会存在同一地址的值在系统中有多份有效拷贝的情况，缓存一致性保证了这些有效拷贝都是最新的。缓存一致性是针对一个地址的约束，而内存一致性模型是针对多个地址的访问顺序的。由于硬件，编译器都可能对访存操作进行重排（以获得更高的性能），内存一致性模型规定了一个系统可能发生的所有访存重排或者指定所有不被允许的访存重排行为。程序编写者和编译器优化算法因此可根据内存一致性模型推断程序或编译器优化会不会造成期望外的运行行为（bug）。
- 验证系统是否满足内存一致性模型可以通过静态的形式化验证，也可以通过动态的测试，如Litmus test（石蕊测试）。每一条Litmus test都是一条短小的多线程程序，并会给出在指定内存一致性模型下允许和不允许的测试执行结果。Litmus-Tests-RISCV项目包含了约7000条Litmus test，用于验证系统是否满足RISC-V指令集所定义的RVWMO宽松内存一致性模型。
## Litmus-Tests-RISCV Setup
- 在硬件上运行测试

    - diy 工具套件中的 litmus 工具可以生成一个 C 程序，该程序将每个 litmus 测试（作为嵌入式汇编集成到 C 程序中）在一个激进的测试框架中多次运行，并在目标 RISC-V 机器上执行。该程序收集结果（每次运行每个测试的最终状态）并以可由 diy 工具套件中的其他工具处理的格式打印出来。

    - 要构建 diy 工具套件和由 litmus 生成的 C 程序，你需要一个具有 OCaml（4.02.0 或更高版本）、GNU make（3.81 或更高版本，尽管这也可能适用于其他版本的 make）和 gcc 的系统。如果这些工具在你打算运行测试的 RISC-V 机器（目标机器）上不可用，你将需要另一台机器，该机器不一定是 RISC-V，但可以提供这些工具（宿主机器）。

    - 以下部分解释了在三种场景下运行 litmus 测试的方法：

        - 1. 在同一（RISC-V）机器上构建和运行：目标 RISC-V 机器安装了 diy 工具套件、gcc 和 make。

        - 2. 在宿主机器上生成程序（在目标机器上编译）：目标 RISC-V 机器安装了 gcc 和 make，但没有安装 diy 工具套件。在这种情况下，你将需要另一台安装了 diy 工具套件的机器。

        - 3. 交叉编译：目标 RISC-V 机器未安装 gcc 或 make。在这种情况下，你将需要另一台安装了 diy 工具套件、make 和 gcc 并能为 RISC-V 进行交叉编译的机器。

    - 在第一和第三种场景中，对于某些 RISC-V 指令（例如 amoswap.w.aq.rl），`make` 将检查你的 gcc 是否支持这些指令。包含不受支持指令的 litmus 测试将被排除在测试之外。在运行如下所述的 `make run-hw-tests ...` 或 `make hw-tests ...` 之后，文件 gcc.excl 将列出所有因 gcc 不支持而被排除的 litmus 测试名称。命令 `grep "#" gcc.excl` 将显示被 gcc 检测为不支持的指令。

    - 此外，如果你遵循第二种场景，或者目标 RISC-V 机器不支持某些指令（即使 gcc 支持），你可以在文件 exclude-instructions 中列出你想要排除的指令（每行一个指令，以 # 开头的行将被忽略）。命令 `make exclude-instructions` 将生成该文件（如果它尚不存在），其中包含 litmus 测试使用的所有指令（已注释掉）。在运行第一个 `make ...` 命令之后，文件 instructions.excl 将列出所有因包含 exclude-instructions 中的指令而被排除的 litmus 测试名称。

    - 请注意，运行测试可能需要几天甚至几周时间。测试分几批进行。每批包含完整的测试集，但具有不同的框架参数，以增加观察到全范围行为的机会。第一批相对较快（几分钟）。此批的结果将保存到文件 run.test.log 中。接下来的批次将需要更长时间（每批几小时）。每批次的结果将保存到 run.<n>.log 中，其中 <n> 是批次号。

- 在同一（RISC-V）机器上构建和运行

    - 这里我们假设 litmus-tests-riscv 仓库已在你打算运行测试的 RISC-V 机器上检出，并且该机器已安装了 diy 工具套件、make 和 gcc。

    - 要生成 C 程序、构建并运行它，请执行
`make run-hw-tests CORES=<n> [GCC=<gcc>] [-j <m>]`
其中 `<n>` 是机器可以运行的硬件线程数
**（注意：这可能需要几天时间才能完成，但第一个日志文件应在几分钟内生成）**。
可选的 `GCC=<gcc>` 允许你指定非标准的 gcc 路径（默认是 `gcc`）。可选的 `-j <m>` 将使用 `<m>` 个并发进程来加快编译速度（如果没有此选项，可能需要几个小时）。

    - 生成并编译测试程序后，make 将运行它。你应该在 `hw-tests/` 中看到包含结果的日志文件。

- 在宿主机器上生成程序（在目标机器上编译）

    - 这里我们假设 litmus-tests-riscv 仓库已在安装了 diy 工具套件的宿主机器上检出，而目标 RISC-V 机器已安装了 gcc 和 make。

    - 要生成 C 程序，请执行 `make hw-tests-src.tgz CORES=<n>` 其中 `<n>` 是目标机器可以运行的硬件线程数。

    - 将 hw-tests-src.tgz 复制到目标 RISC-V 机器，然后在目标机器上执行：
    ```bash
    $ tar -zxf hw-tests-src.tgz
    $ cd hw-tests-src
    $ make [GCC=<gcc>] [-j <m>]
    ...
    $ ./run.sh
    ```

    - 其中 `<gcc>` 和 `<m>` 如前一部分所述。
**（注意：run.sh 可能需要几天时间才能完成！）**

    - 当测试完成时，run.sh 将触碰文件 "done"。将所有 `run.*.log` 文件复制回宿主机器的 `litmus-tests-riscv/hw-tests` 目录（你需要先创建它），然后在宿主机器上执行 `make merge-hw-tests`。

- 交叉编译

    - 这里我们假设 litmus-tests-riscv 仓库已在安装了 diy 工具套件、make 和 gcc 并能够为 RISC-V 进行交叉编译的宿主机器上检出。
    - 在 Ubuntu 上，你可以通过以下方式获得配置为 RISC-V 进行交叉编译的 gcc：
`sudo apt install gcc-riscv64-linux-gnu` 并按照下面的说明使用 `GCC=riscv64-linux-gnu-gcc`。

    - 要生成 C 程序并构建它，请执行
`make hw-tests CORES=<n> [GCC=<gcc>] [-j <m>]`
其中 `<n>`、`<gcc>` 和 `<m>` 如前几部分所述。注意 `<gcc>` 应该为 RISC-V 进行交叉编译。如果你安装了 Ubuntu 软件包 gcc-riscv64-linux-gnu，这将是 `riscv64-linux-gnu-gcc`。
这将生成包含两个文件（run.exe 和 run.sh）的 hw-tests 目录。将这些文件复制到目标机器，并在目标机器上运行 run.sh **（注意：run.sh 可能需要几天时间才能完成）**。
当测试完成时，run.sh 将触碰文件 "done"。将所有 `run.*.log` 文件复制回宿主机器的 hw-tests 目录，然后在宿主机器上执行 `make merge-hw-tests`。
