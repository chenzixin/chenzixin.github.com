---
layout: post
title: "使用批处理删除 Windows 临时文件"
description: "<p>马大姐日理万机，小小的 C 盘，一向不堪重负，正常情况下，不出一个月，就会空间告急。去年我曾手工帮她清理过几次，以下应用软件是占地大户，删除之后，大概有 6G 左右的可用空间：</p><p>Roaming 目录</p><ul><li><p>Apple</p></li><li><p>QQ</p></li><li><p>Foxmail</p></li></ul><blockquote class='warning'>注：都是临时文件，而非邮件附件，也不是聊天记录。</blockquote>"
category: program
tags: [bat, windows]
---
{% include JB/setup %}

马大姐日理万机，小小的 C 盘，一向不堪重负，正常情况下，不出一个月，就会空间告急。去年我曾手工帮她清理过几次，以下应用软件是占地大户，删除之后，大概有 6G 左右的可用空间：

目录：C:\Users\USERNAME\AppData\Roaming

* Apple
 
* QQ

* Foxmail

<blockquote class="warning">注：这些目录下的文件，都是临时文件，而非邮件附件，也不是聊天记录。</blockquote>

## 完成任务

这是今天写的一个清理脚本：

```bat
RD "C:\Users\USERNAME\AppData\Roaming\Apple Computer\Logs" /s /q
RD "C:\Users\USERNAME\AppData\Roaming\Apple Computer\MobileSync" /s /q
RD "C:\Users\USERNAME\AppData\Roaming\Tencent" /s /q
RD "C:\Users\USERNAME\AppData\Roaming\Foxmail" /s /q
```

RD：Remove Directory -- 删除目录

RD 命令参考：

```
RD [/s] [/q] [drive:]path
```

/s    除目录本身外，还将删除指定目录下的所有子目录和文件，用于删除目录树

/q    安静模式，带 /s 删除目录树时不要求确认

常与 `taskkill` 配合使用，如：

```bat
taskkill /f /im 360tray.exe
RD C:\Progra~1\360safe  /s /q
```

## 更进一步

来自百度知道。

删除其它临时文件，不过大多是小文件，主要是清理浏览记录等。

```bat
@echo off 
echo 正在清除系统垃圾文件，请稍等...... 
del /f /s /q %systemdrive%\*.tmp 
del /f /s /q %systemdrive%\*._mp 
del /f /s /q %systemdrive%\*.log 
del /f /s /q %systemdrive%\*.gid 
del /f /s /q %systemdrive%\*.chk 
del /f /s /q %systemdrive%\*.old 
del /f /s /q %systemdrive%\recycled\*.* 
del /f /s /q %windir%\*.bak 
del /f /s /q %windir%\prefetch\*.* 
rd /s /q %windir%\temp & md %windir%\temp 
del /f /q %userprofile%\cookies\*.* 
del /f /q %userprofile%\recent\*.* 
del /f /s /q "%userprofile%\Local Settings\Temporary Internet Files\*.*" 
del /f /s /q "%userprofile%\Local Settings\Temp\*.*" 
del /f /s /q "%userprofile%\recent\*.*" 
echo 清除系统垃圾完成! 
echo. & pause 
```

真正为系统盘腾空间，还是要先分析，到底是哪些目录在吃空间，有针对性的删除。

写批处理程序的好处：

* 固定的代码，不易出错

* 速度快，节省时间

* 使用门槛低，双击即可运行

* 我不用经常跑 18 楼了








