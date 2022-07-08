# Firefox查看测试
## 阅读模式基本测试
- 在支持阅读模式的网页在的地址栏点击阅读模式的图标进入阅读模式，进入阅读模式后图标变为蓝色
    - 部分支持阅读模式的网页在RISC-V oE上无法识别支持    
    - <https://support.mozilla.org/en-US/kb/firefox-reader-view-clutter-free-web-pages>  
    - Archlinux x86_64 firefox 102.0  
    <img src="../Img/view/oe_no_readermode.png">  
    - openEuler RISC-V firefox 97.0.1  
    <img src="../Img/view/arch_readermode.png">  
    - <https://riscv.org/technical/specifications/>  
    - Archlinux x86_64 firefox 102.0  
    <img src="../Img/view/riscv_spec_page_arch_readermode.png">  
    - openEuler RISC-V firefox 97.0.1  
    <img src="../Img/view/riscv_spec_page_readermode.png"> 
    - 使用前缀 ```about:reader?url=``` 强制进入阅读模式，可以看到进入阅读模式后图标变蓝  
    <img src="../Img/view/oe_forced_readermode.png">  

## 阅读模式测试
- 进入阅读模式时，调节布局（字体、字号、行宽、行距） 
    - 原布局  
    <img src="../Img/view/original_layout.png">  
    - 调节字体 正常  
    <img src="../Img/view/font_changed.png">  
    - 调节字号 正常  
    <img src="../Img/view/font_size_increased.png">  
    <img src="../Img/view/font_size_decreased.png">  
    - 调节行宽 正常  
    <img src="../Img/view/content_width_increased.png">  
    <img src="../Img/view/content_width_decreased.png">  
    - 调节行距 正常  
    <img src="../Img/view/line_height_increased.png">  
    <img src="../Img/view/line_height_decreased.png">  
- 进入阅读模式时，调节主题（明亮、深色、黑暗），退出，朗读  
    - 调节主题：明亮 正常    
    <img src="../Img/view/light_mode.png">  
    - 调节主题：深色 正常  
    <img src="../Img/view/sepia_mode.png">  
    - 调节主题：黑暗 正常    
    <img src="../Img/view/dark_mode.png">  
    - 退出 可以正常退出，退出后地址栏出现阅读模式按钮，重启firefox访问同一网页无阅读模式按钮，符合参考行为（Archlinux x86_64 Firefox 102.0）  
    <img src="../Img/view/exit_reader_mode.png">  
    <img src="../Img/view/restart_firefox_no_readermode.png">  
    - 朗读    
    阅读模式下无朗读按钮，可能原因是未安装TTS相关依赖  

## 全屏测试
- 点击菜单按钮，点击全屏按钮，或快捷键F11进入全屏模式  
    - 点击按钮进入全屏，并能正常退出全屏  
    <img src="../Img/view/fullscreen_button.png">  
    - 快捷键进入全屏，并能正常退出全屏  
    <img src="../Img/view/fullscreen_f11.png">  
## PDF阅读器测试
- 点击 PDF 文件的链接和在 下载面板 打开 PDF 文件时，在内置 pdf 阅读器里打开  
    - PDF文件链接打开   
    点击文件链接显示是否保存  
    <img src="../Img/view/pdf_from_link.png">  
    下载完成后不会自动打开，与参考行为不同（Archlinux x86_64 Firefox 102.0）  
    <img src="../Img/view/pdf_downloaded.png">  
    - PDF文件打开 可以正常打开浏览文件  
    <img src="../Img/view/pdf_from_download_list.png">  
