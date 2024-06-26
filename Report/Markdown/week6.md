# 第六周工作总结

## 本周工作内容
### RISC-V oE自动化测试脚本开发报告  
### 整合可用的mugen测试，形成可见产出  
- 已将此前跑通的测试例整合  
    - os-basic-riscv  
    - cpio  
    - git  
    - net-tools  
    - NetworkManager  
    - openslp  
    - util-linux  
- systemd测试套(121个测试例通过)  
    ```
    oe_test_service_console-getty
    oe_test_service_dbus-org.freedesktop.hostname1
    oe_test_service_dbus-org.freedesktop.locale1
    oe_test_service_dbus-org.freedesktop.login1
    oe_test_service_dbus-org.freedesktop.machine1
    oe_test_service_dbus-org.freedesktop.timedate1
    oe_test_service_debug-shell
    oe_test_service_hwclock-save
    oe_test_service_initrd-cleanup
    oe_test_service_initrd-parse-etc
    oe_test_service_initrd-switch-root
    oe_test_service_initrd-udevadm-cleanup-db
    oe_test_service_ldconfig
    oe_test_service_rc-local
    oe_test_service_rescue
    oe_test_service_systemd-ask-password-console
    oe_test_service_systemd-binfmt
    oe_test_service_systemd-bless-boot
    oe_test_service_systemd-boot-system-token
    oe_test_service_systemd-exit
    oe_test_service_systemd-firstboot
    oe_test_service_systemd-halt
    oe_test_service_systemd-hibernate
    oe_test_service_systemd-hostnamed
    oe_test_service_systemd-hwdb-update
    oe_test_service_systemd-hybrid-sleep
    oe_test_service_systemd-initctl
    oe_test_service_systemd-journal-catalog-update
    oe_test_service_systemd-journal-flush
    oe_test_service_systemd-kexec
    oe_test_service_systemd-localed
    oe_test_service_systemd-logind
    oe_test_service_systemd-machined
    oe_test_service_systemd-machine-id-commit
    oe_test_service_systemd-modules-load
    oe_test_service_systemd-poweroff
    oe_test_service_systemd-pstore
    oe_test_service_systemd-random-seed
    oe_test_service_systemd-reboot
    oe_test_service_systemd-remount-fs
    oe_test_service_systemd-rfkill
    oe_test_service_systemd-suspend
    oe_test_service_systemd-suspend-then-hibernate
    oe_test_service_systemd-sysctl
    oe_test_service_systemd-sysusers
    oe_test_service_systemd-timedated
    oe_test_service_systemd-timesyncd
    oe_test_service_systemd-tmpfiles-clean
    oe_test_service_systemd-tmpfiles-setup-dev
    oe_test_service_systemd-tmpfiles-setup
    oe_test_service_systemd-udev-settle
    oe_test_service_systemd-update-done
    oe_test_service_systemd-update-utmp-runlevel
    oe_test_service_systemd-update-utmp
    oe_test_service_systemd-user-sessions
    oe_test_service_systemd-vconsole-setup
    oe_test_service_systemd-volatile-root
    oe_test_socket_systemd-coredump
    oe_test_socket_systemd-initctl
    oe_test_socket_systemd-journald-dev-log
    oe_test_socket_systemd-journald
    oe_test_socket_systemd-udevd-control
    oe_test_socket_systemd-udevd-kernel
    oe_test_target_basic
    oe_test_target_boot-complete
    oe_test_target_ctrl-alt-del
    oe_test_target_default
    oe_test_target_exit
    oe_test_target_final
    oe_test_target_getty-pre
    oe_test_target_getty
    oe_test_target_graphical
    oe_test_target_halt
    oe_test_target_hibernate
    oe_test_target_hybrid-sleep
    oe_test_target_initrd-fs
    oe_test_target_initrd-root-device
    oe_test_target_initrd-root-fs
    oe_test_target_initrd
    oe_test_target_initrd-switch-root
    oe_test_target_kexec
    oe_test_target_local-fs-pre
    oe_test_target_local-fs
    oe_test_target_multi-user
    oe_test_target_network-online
    oe_test_target_network-pre
    oe_test_target_network
    oe_test_target_nss-lookup
    oe_test_target_nss-user-lookup
    oe_test_target_paths
    oe_test_target_poweroff
    oe_test_target_reboot
    oe_test_target_remote-fs-pre
    oe_test_target_remote-fs
    oe_test_target_rescue
    oe_test_target_rpcbind
    oe_test_target_runlevel0
    oe_test_target_runlevel1
    oe_test_target_runlevel2
    oe_test_target_runlevel3
    oe_test_target_runlevel4
    oe_test_target_runlevel5
    oe_test_target_runlevel6
    oe_test_target_shutdown
    oe_test_target_sigpwr
    oe_test_target_sleep
    oe_test_target_slices
    oe_test_target_sockets
    oe_test_target_suspend
    oe_test_target_suspend-then-hibernate
    oe_test_target_swap
    oe_test_target_sysinit
    oe_test_target_system-update-pre
    oe_test_target_system-update
    oe_test_target_timers
    oe_test_target_time-set
    oe_test_target_time-sync
    oe_test_target_umount
    oe_test_service_emergency
    oe_test_target_emergency
    oe_test_target_first-boot-complete
    ```
- osc测试套结果整理中  
    