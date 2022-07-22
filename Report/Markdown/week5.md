# 第五周工作总结

## 本周工作内容
### mugen测试例可用性测试  
- 详细的结果还在整理中  
- 整合上周的os-basic测试用例  
    ```
    oe_test_who
    oe_test_versioninfo
    oe_test_uname
    oe_test_timedatectl
    oe_test_system_monitor_process
    oe_test_system_log_security
    oe_test_system_log_recorded
    oe_test_system_log_process
    oe_test_system_log_device
    oe_test_system_log_basic
    oe_test_server_vsftpd_restart
    oe_test_server_postgresql
    oe_test_server_openssh_restart
    oe_test_server_mysql
    oe_test_server_mariadb_stop
    oe_test_server_mariadb_onlinebackup
    oe_test_server_mariadb_loadfile
    oe_test_server_mariadb_dumpMulDB
    oe_test_server_mariadb_dump
    oe_test_server_mariadb_copy
    oe_test_server_mariadb_backuptable
    oe_test_server_mariadb_backupDB
    oe_test_server_mariadb_backup
    oe_test_server_httpd_restart
    oe_test_server_httpd_recover
    oe_test_server_httpd_port
    oe_test_password_blank
    oe_test_ProcMgmt_vmstat
    oe_test_ProcMgmt_top
    oe_test_ProcMgmt_start_kill
    oe_test_ProcMgmt_ps
    oe_test_ProcMgmt_pgrep
    oe_test_IOaccess_500Mfile
    oe_test_group_access
    oe_test_kernel_sysctl
    oe_test_IOaccess_100Mfile
    oe_test_IOaccess_1Gfile
    oe_test_kernel_module_operation
    oe_test_man
    oe_test_net_cmd_ping
    oe_test_net_cmd_telnet
    ```
- 测试最小软件安装列表中可用的测试套  
    ```
    net-tools
    openssh
    NetworkManager
    git
    hostname
    osc
    iputils
    cpio
    ```