### Java Appnium
- appnium 
- jdk 1.8
- [java-client](https://mvnrepository.com/artifact/io.appium/java-client)
> [启动参数](https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md)

```json
{
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "66J5T18A03002502",
    "noReset": true,
    "appPackage": "com.jingdong.app.mall",
    "appActivity": "com.jingdong.app.mall.main.MainActivity"
}
```
**获取参数**
> 方法一    
> 
> 在 cmd 中执行

```
adb devices                # 验证设备是否连接
adb logcat > appnium.log   # 写入日志

运行指定 app 任意操作几下， 就可以停止写入日志。

Notepad++ 打开 appnium.log

appPackage    | com.jingdong.app.mall

搜索 Package | 在当前文件中查找
找到 packageName  
Line 84509: 12-29 14:32:35.142   707  1570 D OemNetd : setPidForPackage: packageName=com.jingdong.app.mall, pid=11002, pid=10272


appActivity       | com.jingdong.app.mall.MainFrameActivity

GuardService: notifyChange! preName = ComponentInfo{com.jingdong.app.mall/com.jingdong.app.mall.MainFrameActivity}; curName = ComponentInfo{com.miui.home/com.miui.home.launcher.Launcher}

```

> 方法二
>
> adb shell dumpsys activity | find "jd"

---
启动 appnium | 分析界面 UI 控件

IDEA Java

```java
import io.appium.java_client.android.AndroidDriver;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.net.MalformedURLException;
import java.net.URL;


public class Automate {
    public static void main(String[] args) throws MalformedURLException, InterruptedException {
        DesiredCapabilities caps = new DesiredCapabilities();
        // 设备名称
        caps.setCapability("deviceName", "66J5T18A03002502");
        // 系统类型
        caps.setCapability("platformName", "Android");
        // 系统版本
        caps.setCapability("platformVersion", "10");
        // APP 包名
        caps.setCapability("appPackage", "com.jingdong.app.mall");
        // APP 入口(activity)
        caps.setCapability("appActivity", "com.jingdong.app.mall.main.MainActivity");
        // 不重置应用状态
        caps.setCapability("noReset", true);

        // 创建驱动  | 指定 appium 通讯地址
        AndroidDriver driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), caps);
        // 等待时间
        Thread.sleep(5000);
        driver.findElementByXPath("//android.view.View[@content-desc=\"我的\"]").click();
        Thread.sleep(3000);
        // 点击商品收藏
        driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout[1]").click();
        Thread.sleep(3000);
        // 点击收藏的第一个
        driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[1]").click();
        Thread.sleep(3000);
        // 点击立即抢购
        driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]").click();
        Thread.sleep(3000);
        driver.quit();
    }
}
```