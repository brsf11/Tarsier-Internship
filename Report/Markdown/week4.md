# 第四周工作总结

## 本周工作内容

### mugen的使用和开发报告  
- [报告文档](https://github.com/brsf11/mugen-presentation/blob/master/Markdown/report.md)  
- [报告ppt](https://github.com/brsf11/mugen-presentation/blob/master/ppt/report.odp)  

### mugen测试套os-basic移植  
- part1共41条测试例  
- success 26条  
    ```
    oe_test_server_httpd_port            oe_test_server_openssh_key
    oe_test_server_httpd_recover         oe_test_server_openssh_restart
    oe_test_server_httpd_restart         oe_test_server_postgresql
    oe_test_server_mariadb_backup        oe_test_server_vsftpd_restart
    oe_test_server_mariadb_backupDB      oe_test_system_log_basic
    oe_test_server_mariadb_backuptable   oe_test_system_log_device
    oe_test_server_mariadb_copy          oe_test_system_log_process
    oe_test_server_mariadb_dump          oe_test_system_log_recorded
    oe_test_server_mariadb_dumpMulDB     oe_test_system_log_security
    oe_test_server_mariadb_loadfile      oe_test_system_monitor_process
    oe_test_server_mariadb_onlinebackup  oe_test_timedatectl
    oe_test_server_mariadb_stop          oe_test_versioninfo
    oe_test_server_mysql                 oe_test_who
    ```
- failed 15条  
    ```
    oe_test_server_httpd_checkfirewall   oe_test_server_vsftpd_NKdelay
    oe_test_server_httpd_tls             oe_test_server_vsftpd_transfer
    oe_test_server_mariadb_compatibilty  oe_test_system_log_dmesg
    oe_test_server_openssh_secure        oe_test_system_log_view
    oe_test_server_openssh_verifykey     oe_test_system_monitor_login
    oe_test_server_squid_blacklist       oe_test_system_monitor_reboot
    oe_test_server_squid_ip              oe_test_uname
    oe_test_server_squid_proxy
    ```
- mugen环境问题 需要多个节点  
    - oe_test_system_monitor_reboot  
    - oe_test_system_monitor_login  
    - oe_test_server_vsftpd_transfer  
    - oe_test_server_vsftpd_NKdelay  
    - oe_test_server_mariadb_compatibilty  
    - oe_test_server_openssh_key（测试成功，但疑似测试例有问题）  
- 缺少squid包  
    - oe_test_server_squid_blacklist  
    - oe_test_server_squid_ip  
    - oe_test_server_squid_proxy  
- 其他  
    - oe_test_uname ```uname -m | grep -E "aarch64|x86_64"``` -> ```uname -m | grep -E "aarch64|x86_64|riscv64"```  
    - oe_test_system_log_view 系统缺少/var/log/messages  
    - oe_test_system_log_dmesg 类似oe_test_uname  
    - 其余failed测试例还待研究  

