# 第一周工作总结
## 本周工作内容
### 研究了openEuler/release-tools仓库结构和release-assistant
- 是什么：release-assistant的主体是javcra，而Javcra 是一款基于Python的辅助社区开发者和版本发布人员快速发布openEuler版本的自动化发布工具。
- 怎么用：依托gitee的issue平台，通过在issue中评论相应命令，实现自动触发发布流程、修改发布列表以及监控版本issue和自动验证功能。
- test/下未基于Python unittest库实现的针对javcra程序本身的单元测试代码,用于测试javcra程序的功能正确性
### 了解了Python模块和unittest库
- Python unittest库：
- 单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
- 基本使用方法：在继承unittest.TestCase的类中针对每项测试编写名称开头为test的方法。
### 解决了javcra和相应测试代码的依赖并成功运行了测试代码
- 环境：openEuler 22.03 LTS x86_64
- 最小安装 勾选所有组件
- release-assistant所需软件包：git python3 pip（安装后自带）
- 安装：git clone https://gitee.com/brsf11/release-tools.git
- javcra测试代码运行需要的python库依赖（需额外安装）：
- pip install coverage concurrent_log_handler marshmallow -gevent python-jenkins retrying pandas huawei-obs
 
- 运行前的改动1：
    - python自带的test库会导致无法识别test.base
    - 解决办法：暂时把自带的test移除
    - sudo mv /usr/lib64/python3.9/test usr/lib64/python3.9/test_temp

- 运行前的改动2（brsf11/release-tools仓库中的版本已修改）：
    - 添加./release-assistant/javcra/libs/config/__init__.py文件以解决无法识别javcra.libs.config模块的问题
    - 在./release-assistant/test/coverage_count.py中添加sys.path.append(os.path.abspath('.'))

- 运行测试：
    - 在release-tools/release-assistant目录下执行
    - python3 test/coverage_count.py