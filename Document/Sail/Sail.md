RISCV Sail模型
================

什么是Sail?
-------------

[Sail](https://github.com/rems-project/sail)是一种描述处理器指令集架构（ISA）语义的语言：机器指令行为的架构规范。Sail是一种对工程师友好的语言，非常类似于早期的供应商伪代码，但定义更为精确，并具有支持广泛用例的工具。

给定Sail规范，工具可以对其进行类型检查，生成文档片段（以LaTeX或AsciiDoc格式），生成可执行的模拟器（以C或OCaml编写），显示规范覆盖率，为放松内存模型工具生成ISA版本，支持自动指令序列测试生成，为交互证明生成定理证明器定义（在Isabelle、HOL4和Coq中），支持关于二进制代码的证明（在Islaris中），并（正在进行中）生成可用于形式硬件验证的SystemVerilog参考ISA模型。

  <img width="800" src="https://www.cl.cam.ac.uk/~pes20/sail/overview-sail.png?">

Sail用于多种ISA描述，包括基本完整的Arm-A顺序行为版本（自动从权威的Arm内部规范导出，并在Arm的许可下以BSD Clear许可证发布）、RISC-V、CHERI-RISC-V、CHERIoT、MIPS和CHERI-MIPS；所有这些都足以启动各种操作系统。此外，还存在针对IBM POWER和x86的小片段Sail模型，包括从ACL2 x86模型自动翻译的版本。

RISC-V指令规范示例
----------------------------------

以下是包含基本指令的模型文件[riscv_insts_base.sail](https://github.com/riscv/sail-riscv/blob/master/model/riscv_insts_base.sail)中的逐字摘录，添加了一些注释。

### ITYPE（或ADDI）

```sail
/* ITYPE指令的汇编抽象语法树（AST）子句 */

union clause ast = ITYPE : (bits(12), regbits, regbits, iop)

/* AST元素和32位字之间的编码/解码映射 */

mapping encdec_iop : iop <-> bits(3) = {
  RISCV_ADDI  <-> 0b000,
  RISCV_SLTI  <-> 0b010,
  RISCV_SLTIU <-> 0b011,
  RISCV_ANDI  <-> 0b111,
  RISCV_ORI   <-> 0b110,
  RISCV_XORI  <-> 0b100
}

mapping clause encdec = ITYPE(imm, rs1, rd, op) <-> imm @ rs1 @ encdec_iop(op) @ rd @ 0b0010011

/* ITYPE指令的执行语义 */

function clause execute (ITYPE (imm, rs1, rd, op)) = {
  let rs1_val = X(rs1);
  let immext : xlenbits = EXTS(imm);
  let result : xlenbits = match op {
    RISCV_ADDI  => rs1_val + immext,
    RISCV_SLTI  => EXTZ(rs1_val <_s immext),
    RISCV_SLTIU => EXTZ(rs1_val <_u immext),
    RISCV_ANDI  => rs1_val & immext,
    RISCV_ORI   => rs1_val | immext,
    RISCV_XORI  => rs1_val ^ immext
  };
  X(rd) = result;
  true
}

/* AST元素和字符串之间的汇编/反汇编映射 */

mapping itype_mnemonic : iop <-> string = {
  RISCV_ADDI  <-> "addi",
  RISCV_SLTI  <-> "slti",
  RISCV_SLTIU <-> "sltiu",
  RISCV_XORI  <-> "xori",
  RISCV_ORI   <-> "ori",
  RISCV_ANDI  <-> "andi"
}

mapping clause assembly = ITYPE(imm, rs1, rd, op)
                      <-> itype_mnemonic(op) ^ spc() ^ reg_name(rd) ^ sep() ^ reg_name(rs1) ^ sep() ^ hex_bits_12(imm)
```

### SRET

```sail
union clause ast = SRET : unit

mapping clause encdec = SRET() <-> 0b0001000 @ 0b00010 @ 0b00000 @ 0b000 @ 0b00000 @ 0b1110011

function clause execute SRET() = {
  match cur_privilege {
    User       => handle_illegal(),
    Supervisor => if   mstatus.TSR() == true
                  then handle_illegal()
                  else nextPC = handle_exception(cur_privilege, CTL_SRET(), PC),
    Machine    => nextPC = handle_exception(cur_privilege, CTL_SRET(), PC)
  };
  false
}

mapping clause assembly = SRET() <-> "sret"
```

顺序执行
----------

该模型构建OCaml和C模拟器，可以执行RISC-V ELF文件，且两个模拟器都提供足够的平台支持来启动Linux、FreeBSD和seL4。OCaml模拟器可以生成自己的平台设备树描述，而C模拟器目前需要手动提供一致的描述。C模拟器可以链接到Spike模拟器以进行每条指令的联检验证。

对于Linux启动，C模拟器目前在Intel i7-7700上大约运行300 KIPS（当详细的每条指令跟踪被禁用时），并且未来有很多优化的机会（Sail MIPS模型大约运行1 MIPS）。这使得能够在大约4分钟内启动Linux，在大约2分钟内启动FreeBSD。启动Linux时C模拟器的内存使用量大约为140MB。

OCaml和C模拟器目录中的文件实现ELF加载和平台设备，定义物理内存映射，并使用命令行选项来选择特定实现的ISA选择。

### 在测试中用于规范覆盖率测量

Sail生成的C模拟器可以测量任何执行测试的规范分支覆盖率，以每个文件的表格和html标注版本的模型源代码显示结果。

### 用作联检验证中的测试Oracle

对于随机指令流的联检验证，工具支持[TestRIG](https://github.com/CTSRD-CHERI/TestRIG)中使用的协议直接将指令注入C模拟器，并以RVFI格式生成跟踪信息。这已用于与Spike和用Bluespec SystemVerilog编写的[RVBS](https://github.com/CTSRD-CHERI/RVBS)规范进行交叉测试。

C模拟器也可以直接链接到Spike，这在ELF二进制文件（包括OS启动）上提供联检验证。当模型中的OS启动问题在Spike上已知正常工作时，这通常在调试时很有用。它还可以检测Spike中未由ISA规范强制的特定平台实现选择。

并发执行
--------------------

ISA模型与RISC-V的放松内存模型RVWMO的操作模型集成（如[RISC-V用户级规范](https://github.com/riscv/riscv-isa-manual/releases/tag/draft-20181227-c6741cb)附录中所述），这是RISC-V并发架构开发中使用的参考模型之一；这是[RMEM](http://www.cl.cam.ac.uk/users/pes20/rmem)工具的一部分。它还与作为[isla-axiomatic](https://isla-axiomatic.cl.cam.ac.uk/)工具一部分的RISC-V公理并发模型集成。

### 并发测试

作为剑桥大学/INRIA并发架构工作的一个部分，这些小组制作并发布了大约7000个[litmus测试](https://github.com/litmus-tests/litmus-tests-riscv)。操作和公理RISC-V并发模型在这些测试中同步，并且它们与对应的ARM架构行为在共同测试中的表现一致。

这些测试也在RISC-V硬件上运行过，使用的是SiFive RISC-V FU540多核原型板（Freedom Unleashed），该板由Imperas慷慨借出。迄今为止，只观察到了顺序一致的行为。

在测试生成中的使用
----------------------

Sail OCaml后端可以为Sail规范中的类型生成QuickCheck风格的随机生成器，这些生成器已被用于生成随机指令序列进行测试。开发者可以覆盖单个类型的生成，以例如移除特定实现的指令或引入寄存器偏向。

生成定理证明器定义
----------------------

Sail旨在支持跨多个工具生成惯用的定理证明器定义。目前它支持Isabelle、HOL4和Coq，并且`prover_snapshots`目录提供了生成的定理证明器定义的快照。

这些定理证明器的转换可以针对多种单子进行，以实现不同的目的。首先是一个具有不确定性和异常的状态单子，适合在顺序环境中进行推理，假设有影响的表达式在没有中断的情况下执行并且独占访问状态。

对于并发推理，其中指令乱序执行、推测执行和非原子执行，有一个基于内存操作数据类型的自由单子。这个单子也是通过上述RMEM工具支持并发的一部分。

`handwritten_support`目录下的文件为Coq、Isabelle和HOL4提供了库定义。

目录结构
-------------------

```
sail-riscv
- model                   // Sail规范模块
- generated_definitions   // 由Sail生成的文件，在RV32和RV64子目录中
  -  c
  -  ocaml
  -  lem
  -  isabelle
  -  coq
  -  hol4
  -  latex
- prover_snapshots        // 生成的定理证明器定义的快照
- handwritten_support     // 定理证明器支持文件
- c_emulator              // C模拟器的支持平台文件
- ocaml_emulator          // OCaml模拟器的支持平台文件
- doc                     // 文档，包括阅读指南
- test                    // 测试文件
  - riscv-tests           // 来自riscv/riscv-tests github仓库的测试快照
- os-boot                 // 引导操作系统映像的信息和示例文件
```

入门
---------------

### 构建模型

使用[opam安装](https://github.com/rems-project/sail/blob/sail2/INSTALL.md) [Sail](https://github.com/rems-project/sail/)，然后：

```
$ make
```

将在`ocaml_emulator/riscv_ocaml_sim_RV64`中构建64位OCaml模拟器，在`c_emulator/riscv_sim_RV64`中构建C模拟器，在`generated_definitions/isabelle/RV64/Riscv.thy`中构建Isabelle模型，在`generated_definitions/coq/RV64/riscv.v`中构建Coq模型，以及在`generated_definitions/hol4/RV64/riscvScript.sml`中构建HOL4模型。

可以通过在`make`命令行中指定`ARCH=RV32`或`ARCH=RV64`来构建RV32或RV64模型，并使用匹配的目标后缀。默认构建RV64模型，但可以使用以下命令构建RV32模型：

```
$ ARCH=RV32 make
```

这将在`ocaml_emulator/riscv_ocaml_sim_RV32`中创建32位OCaml模拟器，在`c_emulator/riscv_sim_RV32`中创建C模拟器，并在相应的`RV32`子目录中创建定理证明器模型。

Makefile目标`riscv_isa_build`、`riscv_coq_build`和`riscv_hol_build`调用相应的定理证明器来处理定义。我们测试了Isabelle 2018、Coq 8.8.1和HOL4 Kananaskis-12。在构建这些目标时，请确保Sail目录（`$SAIL_DIR/lib/$prover`）中的相应定理证明器库是最新的并且已构建，例如通过在这些目录中运行`make`。

### 执行测试二进制文件

可以使用C和OCaml模拟器执行小型测试二进制文件。OCaml模拟器依赖于设备树编译器包，可以在Ubuntu中安装：

```
$ sudo apt-get install device-tree-compiler
```

然后，你可以运行测试二进制文件：

```
$ ./ocaml_emulator/riscv_ocaml_sim_<arch>  <elf-file>
$ ./c_emulator/riscv_sim_<arch> <elf-file>
```

一个由[`riscv-tests`](https://github.com/riscv/riscv-tests)测试套件派生的RV32和RV64测试程序套件包含在[test/riscv-tests/](test/riscv-tests/)下。测试套件可以使用`test/run_tests.sh`运行。

### 配置平台选项

每个模拟器的额外配置选项信息可以从`./ocaml_emulator/riscv_ocaml_sim_<arch> -h`和`./c_emulator/riscv_sim_<arch> -h`获得。

一些有用的选项包括：配置未对齐访问是否触发陷阱（C使用`--enable-misaligned`，OCaml使用`-enable-misaligned`），以及页表遍历是否更新PTE位（C使用`--enable-dirty-update`，OCaml使用`-enable-dirty-update`）。