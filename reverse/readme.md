### ADB 安装 APK
- 模拟器 / 真机
- 查看设备是否连接
    - adb devices
    - adb install app_name.apk
- 安装过程:

    `复制 APK 安装包到 /data/app 目录下`
    
    `解压并扫描安装包`
    
    `把 dex(Dalvik字节码) 文件保存到 /data/dalvik-cache 目录, 并在 /data/data 目录下创建对应的应用数据目录`
- 文件目录
    - /system/data
    
        `系统自带应用程序, 获取 root 权限才能删除`
        
    - /data/app
    
        `用户程序安装的目录`
        
    - /data/data
    
        `存放应用程序数据`
    - /data/dalvik-cache
    
        `将 APK 中的 dex 文件安装到 dalvik-cache 目录下`
        
- 卸载过程

    - 删除安装过程中的(以上)三个目录下创建的文件及目录
    

- 导出 APK

