# 第二十三周工作总结  

## 本周工作内容  
### 解决自动化测试riscv龙蜥镜像的问题  
- 自动化测试需要解决网络和复原两方面问题  
    - 网络方面需要知道guest的ip和guest何时就绪  
    - 复原可以使用qcow2快照或者强行复制的方法  
- ssh/sftp root连接  
    sshd_config配置文件中禁用了root登录  
- 网络自动配置  
    使用systemd unit，开机时自动配置网络，通过查询host上libvirtd的log获得ip  
- 硬盘容量  
    - 本次使用的镜像没有使用lvm，无法使用常见的lvm动态扩容方法  
    - 在host上创建新raw磁盘后将原来的数据拷贝，启动卡住  
    - 使用qemu-img resize + growpart + resize2fs最终解决  
- 自动复原  
    - 建立qcow2快照无法启动  