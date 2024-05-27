# QtRvSim Setup 文档
### 构建依赖

- Qt 5（测试的最低版本是5.9.5），实验性支持Qt 6
- elfutils（可选；libelf也可以，但可能会有一些问题）

### 在Linux上快速编译

在Linux上，可以使用一个包装Makefile并在项目根目录运行`make`。它将创建一个构建目录并在其中运行CMake。可用的目标是：`release`（默认）和`debug`。

打包者注意：当创建源码归档时，CMake会删除这个Makefile以避免任何歧义。包应该直接调用CMake。

### 通用编译

```shell
cmake -DCMAKE_BUILD_TYPE=Release /path/to/qtrvsim
make
```

其中，`/path/to/qtrvsim`是项目根目录的路径。构建的二进制文件将在构建目录中的`target`目录下（即调用cmake的目录）。

使用`-DCMAKE_BUILD_TYPE=Debug`编译开发版本，包括检测工具。

如果没有提供构建类型，默认是`Debug`。

### 在macOS上从源码构建

从App Store安装最新版本的**Xcode**。然后打开终端并执行`xcode-select --install`以安装命令行工具。然后打开Xcode，接受许可协议并等待它安装任何附加组件。最终看到"Welcome to Xcode"屏幕后，从顶部栏选择`Xcode -> Preferences -> Locations -> Command Line Tools`并选择一个SDK版本。

安装[Homebrew](https://brew.sh/)并使用它安装Qt。（macOS构建必须使用捆绑的libelf）

```shell
brew install qt
```

现在按照通用编译（[上面](#general-compilation)）的方法构建项目。

### 下载二进制包

- [https://github.com/cvut/qtrvsim/releases](https://github.com/cvut/qtrvsim/releases)
    - 包含Windows和通用GNU/Linux二进制文件的归档
- [https://build.opensuse.org/repositories/home:jdupak/qtrvsim](https://build.opensuse.org/repositories/home:jdupak/qtrvsim)
- [https://software.opensuse.org/download.html?project=home%3Ajdupak&package=qtrvsim](https://software.opensuse.org/download.html?project=home%3Ajdupak&package=qtrvsim)
    - Open Build Service二进制包
- [https://launchpad.net/~qtrvsimteam/+archive/ubuntu/ppa](https://launchpad.net/~qtrvsimteam/+archive/ubuntu/ppa)
    - Ubuntu PPA归档

```bash
sudo add-apt-repository ppa:qtrvsimteam/ppa
sudo apt-get update
sudo apt-get install qtrvsim
```

### Nix包

QtRVSim提供了一个Nix包作为仓库的一部分。你可以使用以下命令来构建和安装它。更新必须通过检出git手动完成。NIXPKGS包处于PR阶段。

```shell
nix-env -if .
```

### 测试

测试由CTest（CMake的一部分）管理。要构建和运行所有测试，使用以下命令：

```bash
cmake -DCMAKE_BUILD_TYPE=Release /path/to/QtRVSim
make
ctest
```

## 文档

主要文档在这个README文件以及子目录[`docs/user`](docs/user)和[`docs/developer`](docs/developer)中提供。

该项目由Karel Kočí、Jakub Dupak和Max Hollmann的论文开发和扩展。有关链接和参考，请参见[资源和出版物](#resources-and-publications)部分。

## 接受的二进制格式

模拟器接受为RISC-V目标编译的ELF静态链接可执行文件（`--march=rv64g`）。模拟器将根据ELF文件头自动选择字节序。
仿真将根据ELF文件头以XLEN=32或XLEN=64执行。

- 支持64位RISC-V ISA RV64IM和32位RV32IM ELF可执行文件。
- 暂不支持压缩指令。

你可以使用专门的RISC-V GCC/Binutils工具链（`riscv32-elf`）或使用带有[LLD](https://lld.llvm.org/)的统一Clang/LLVM工具链来编译代码进行仿真。如果安装了Clang，你不需要任何额外的工具。Clang可以在Linux、Windows、macOS等系统上使用。

### 使用LLVM工具链

```shell
clang --target=riscv32 -march=rv32g -nostdlib -static -fuse-ld=lld test.S -o test
llvm-objdump -S test
```

### 使用GNU工具链

```shell
riscv32-elf-as test.S -o test.o
riscv32-elf-ld test.o -o test
riscv32-elf-objdump -S test
```

或

```shell
riscv32-elf-gcc test.S -o test
riscv32-elf-objdump -S test
```

### 使用GNU 64位工具链用于RV32I目标

支持多库的64位嵌入式工具链可以用于构建可执行文件

```shell
riscv64-unknown-elf-gcc -march=rv32i -mabi=ilp32 -nostdlib -o test test.c crt0local.S -lgcc
```

必须设置全局指针和堆栈以建立符合运行时C代码的环境。如果没有使用其他C库，可以使用下一个简单的`crt0local.S`。


```asm
/* minimal replacement of crt0.o which is else provided by C library */

.globl main
.globl _start
.globl __start

.option norelax

.text

__start:
_start:
        .option push
        .option norelax
        la gp, __global_pointer$
        .option pop
        la      sp, __stack_end
        addi    a0, zero, 0
        addi    a1, zero, 0
        jal     main
quit:
        addi    a0, zero, 0
        addi    a7, zero, 93  /* SYS_exit */
        ecall

loop:   ebreak
        beq     zero, zero, loop

.bss

__stack_start:
        .skip   4096
__stack_end:

.end _start
```

## 集成汇编器

模拟器包含基本的集成汇编器。也识别[GNU汇编器](https://sourceware.org/binutils/docs/as/)指令集的一小部分。识别以下指令：`.word`、`.orig`、`.set`/`.equ`、`.ascii`和`.asciz`。某些其他指令则被简单忽略：`.data`、`.text`、`.globl`、`.end`和`.ent`。这允许编写的代码可以被集成和全功能汇编器编译。地址分配给标签/符号，存储在符号表中。识别加、减、乘、除和按位与或运算。

## 支持调用外部make工具

动作"由外部make构建可执行文件"调用"make"程序。如果动作被调用，并且主窗口选项卡中选择了一些源代码编辑器，则在相应的目录中启动"make"。否则，选择最后选择的编辑器目录。如果没有打开编辑器，则使用最后加载的ELF可执行文件的目录作为"make"启动路径。如果连这也不是选项，则使用启动仿真器时的默认目录。
