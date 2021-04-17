# 一、`monkey`测试流程

#### 1.打开`wifi`，打开`wifi`调试![wifi](/home/steed/PycharmProjects/cherry_testing/test_recorder/wifi.png)

#### 2.打开电脑进入`terminal`

输入命令链接设备：`$ adb connect 192.168.50.141`

#### 3.查看已经链接的设备

![adb_devices](/home/steed/PycharmProjects/cherry_testing/test_recorder/adb_devices.png)

#### 4.进入脚本`monkey_test.py`所在目录

运行脚本`python monkey_test.py`![statup](/home/steed/PycharmProjects/cherry_testing/test_recorder/statup.png)

#### 5.同目录下查看日志

![log](/home/steed/PycharmProjects/cherry_testing/test_recorder/log.png)

# 二、`log`检查

```bash
// CRASH: com.amwin.iap2.service:remote (pid 14338)
// Short Msg: Native crash
// Long Msg: Native crash: Segmentation fault
// Build Label: Chery/t1a_navi/t1a_navi:4.4.3/2.0.1-rc2/eng.citos-android.20200215.123056:user/dev-keys
// Build Changelist: eng.citos-android.20200215.123056
// Build Time: 1581741082000
// *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
// Build fingerprint: 'Chery/t1a_navi/t1a_navi:4.4.3/2.0.1-rc2/eng.citos-android.20200215.123056:user/dev-keys'
// Revision: '0'
// pid: 14338, tid: 14338, name: .service:remote  >>> com.amwin.iap2.service:remote <<<
// signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 00000003
//     r0 00004fd9  r1 00003fd0  r2 00003fd0  r3 ffffffff
//     r4 00001008  r5 40165fd8  r6 6a593000  r7 00000008
//     r8 00000400  r9 bea18e74  sl 0000302d  fp 00000000
//     ip 00004fd8  sp bea18db8  lr 4012bed7  pc 4012c35c  cpsr a00d0030
//     d0  0000000000000000  d1  0000000000000000
//     d2  0000000000000000  d3  0000000000000000
//     d4  8000000000000000  d5  0000000000000000
//     d6  3f00000000000000  d7  3f8000003f4ccccd
//     d8  0000000000000000  d9  0000000000000000
//     d10 0000000000000000  d11 0000000000000000
//     d12 0000000000000000  d13 0000000000000000
//     d14 0000000000000000  d15 0000000000000000
//     d16 3fe8000000000000  d17 3fc999999999999a
//     d18 41c8c2abe3000000  d19 0000000000000000
//     d20 0000000000000000  d21 0000000000000000
//     d22 0000000000000000  d23 0000000000000000
//     d24 0000000000000000  d25 0000000000000000
//     d26 0000000000000000  d27 0000000000000000
//     d28 0000000000000000  d29 0000000000000000
//     d30 0000000000000000  d31 0000000000000000
//     scr 60000010
// 
// backtrace:
//     #00  pc 0001035c  /system/lib/libc.so (dlmalloc+1207)
//     #01  pc 0000dccf  /system/lib/libc.so (malloc+10)
//     #02  pc 00014dff  /system/lib/libc.so (__smakebuf+34)
//     #03  pc 00026727  /system/lib/libc.so (__srefill+154)
//     #04  pc 00025e0f  /system/lib/libc.so (fread+358)
//     #05  pc 000026ab  /system/lib/libdevice_manager_jni.so (uDevFilter::listDir(char const*, int, char*)+202)
//     #06  pc 000027a9  /system/lib/libdevice_manager_jni.so (uDevFilter::enumBus(char*, char*)+64)
//     #07  pc 00002849  /system/lib/libdevice_manager_jni.so (DeviceManager::init()+48)
//     #08  pc 00003915  /system/lib/libdevice_manager_jni.so
//     #09  pc 0001dbcc  /system/lib/libdvm.so (dvmPlatformInvoke+112)
//     #10  pc 0004e123  /system/lib/libdvm.so (dvmCallJNIMethod(unsigned int const*, JValue*, Method const*, Thread*)+398)
//     #11  pc 00026fe0  /system/lib/libdvm.so
//     #12  pc 0002dfa0  /system/lib/libdvm.so (dvmMterpStd(Thread*)+76)
//     #13  pc 0002b638  /system/lib/libdvm.so (dvmInterpret(Thread*, Method const*, JValue*)+184)
//     #14  pc 00060861  /system/lib/libdvm.so (dvmInvokeMethod(Object*, Method const*, ArrayObject*, ArrayObject*, ClassObject*, bool)+392)
//     #15  pc 000687c3  /system/lib/libdvm.so
//     #16  pc 00026fe0  /system/lib/libdvm.so
//     #17  pc 0002dfa0  /system/lib/libdvm.so (dvmMterpStd(Thread*)+76)
//     #18  pc 0002b638  /system/lib/libdvm.so (dvmInterpret(Thread*, Method const*, JValue*)+184)
//     #19  pc 0006057d  /system/lib/libdvm.so (dvmCallMethodV(Thread*, Method const*, Object*, bool, JValue*, std::__va_list)+336)
//     #20  pc 00049d0b  /system/lib/libdvm.so
//     #21  pc 0004d383  /system/lib/libandroid_runtime.so
//     #22  pc 0004e0a7  /system/lib/libandroid_runtime.so (android::AndroidRuntime::start(char const*, char const*)+354)
//     #23  pc 000010b7  /system/bin/app_process
//     #24  pc 0000e423  /system/lib/libc.so (__libc_init+50)
//     #25  pc 00000db0  /system/bin/app_process
// 
// code around pc:
//     4012c33c fa220340 eb0cf603 f8df0003 19823740  
//     4012c34c 2600324c f853447b e0103022 e00e461e  
//     4012c35c f0206858 ebc40c07 428a020c 460abf28  
//     4012c36c bf386919 b901461e 460b6959 2b004611  
//     4012c37c 2e00d1ee 8123f000 0704f8df 68824478  
//     4012c38c 42991b13 811bf080 8010f8d0 d3114546  
//     4012c39c 429e1933 68f2d20e 42b269b0 68b7d00e  
//     4012c3ac d3074547 42b568fd 85ccf000 60fae002  
//     4012c3bc e01d6097 06ccf8df e69b4478 f1066972  
//     4012c3cc b93a0c14 f1066932 b91a0c10 f8d9e010  
//     4012c3dc 46cc2000 f1026957 2f000914 6917d1f7  
//     4012c3ec 0910f102 d1f22f00 d3e345c4 7000f8cc  
//     4012c3fc d0332800 801cf8d6 768cf8df 094cf108  
//     4012c40c f857447f 42ae5029 f847d110 b1322029  
//     4012c41c 5678f8df 692d447d d21242aa 2201e7ca  
//     4012c42c f808fa02 0508ea2a e017607d 42a8693d  
// 
// code around lr:
//     4012beb4 fd42f7ff 1b94f8df f8d14479 079321bc  
//     4012bec4 2cf4d402 e1a6d909 70e0f501 f7fe2600  
//     4012bed4 2800ecf0 806ff041 2c0ae7f3 340bd903  
//     4012bee4 0407f024 2410e000 3b68f8df 447b08e2  
//     4012bef4 fa206818 9001f102 d021078e 0401f001  
//     4012bf04 0601f084 eb0318b1 342804c1 68b268a6  
//     4012bf14 d1064294 fa022201 ea20fc01 6018000c  
//     4012bf24 6918e00c d3054282 42b368d3 60d4d102  
//     4012bf34 e00360a2 0b20f8df e0df4478 e35800c8  
//     4012bf44 42ac689d 833ff240 d0742900 0001f04f  
//     4012bf54 f602fa00 f202fa01 f600fa06 ea474277  
//     4012bf64 ea0c0c06 42710602 0706ea01 0b161e7a  
//     4012bf74 0110f006 f201fa22 f0070957 fa220c08  
//     4012bf84 4461f60c f00208b2 fa260c04 eb01f60c  
//     4012bf94 fa26070c f001f100 fa260202 eb07f602  
//     4012bfa4 f3c60c02 fa260140 eb0cf201 18bf0701  
// 
** Monkey aborted due to error.
Events injected: 3756
:Sending rotation degree=0, persist=false
:Dropped: keys=0 pointers=0 trackballs=0 flips=0 rotations=0
## Network stats: elapsed time=146175ms (0ms mobile, 0ms wifi, 146175ms not connected)
** System appears to have crashed at event 3756 of 10000 using seed 945004553687
```

搜索`crash`、  `exception`、 `anr`字样查看具体情况