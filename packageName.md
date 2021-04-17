- `adb shell monkey --pct-syskeys 0 --throttle 100 -v -v -v 10000 >./b.log`
获取包名：

- 详细日志`logcat *:S ActivityManager:V`
  - `.ui.MainActivity`
- 包名`adb shell am monitor`

高德导航`com.autonavi.amapauto`

-  `com.autonavi.auto.remote.fill.UsbFillActivity`

app列表`com.chery.launcher`

酷我音乐`cn.kuwo.kwmusiccar`

考拉`com.edog.car`

百度carlife `com.amwin.carlife.app`

设置`com.chery.settings`

紧急联系人`com.chery.tbox`

个人账户`com.chery.tsp`

##command
 `adb shell ls /data/data > ./info.txt`


