---
layout: post
title: "Sina SAE WordPress 搭建笔记"
description: "<p>作为程序员，我更倾向于用 Jekyll 这样的程序写笔记，但是，我们毕竟身在高墙之内，万一 GitHub 永远的被隔离在外，我们也只能用 WordPress 之类的工具了。</p><p>WordPress 也是杰出的 Blog 工具。</p><p>最初开通 Sina SAE 的时候，我安装的应用就是 WordPress for SAE，当时还可免费安装。一年之后，开通服务和实名认证赠送的云豆全部用完，我只好先删除应用，将一些相对有价值的文章，手工转录到 GitHub。</p><p>但没过多久，我就通过了开发者认证，应用免租金，而且对 SAE 的架构也熟悉了一些，于是重新搭建 Blog，作为灾备。</p>"
category: program
tags: [sina, sae, wp, wordpress]
---
{% include JB/setup %}

作为程序员，我更倾向于用 Jekyll 这样的程序写笔记，但是，我们毕竟身在高墙之内，万一 GitHub 永远的被隔离在外，我们也只能用 WordPress 之类的工具了。

WordPress 也是杰出的 Blog 工具。

最初开通 Sina SAE 的时候，我安装的应用就是 WordPress for SAE，当时还可免费安装。一年之后，开通服务和实名认证赠送的云豆全部用完，我只好先删除应用，将一些相对有价值的文章，手工转录到 GitHub。

但没过多久，我就通过了开发者认证，应用免租金，而且对 SAE 的架构也熟悉了一些，于是重新搭建 Blog，作为灾备。

同事直接下载 WordPress 最新版，参考网上的一些文章，比如：

[tahoroom.sinaapp.com](http://tahoroom.sinaapp.com/?p=2013)

也不麻烦，很快就跑起来了：[labsunwp.sinaapp.com](http://labsunwp.sinaapp.com/)

而我的台式机上，还保存着当时 check out 到本地的 源码，皮肤、插件 一应俱全，我当然选择上传这个版本，据作者的说法，专门针对 SAE 做了优化，对我而言，最重要的就是省事儿。

## 第一步：上传代码

新建应用，创建默认版本代码，并 check out 到本地：

`$ svn co https://svn.sinaapp.com/[your_app_name]`

将 WordPress 安装文件拷贝到 \[your_app_name]\\1目录下，添加到 svn 版本管理，如果是从官方下载的 WordPress，则按照上面的教程修改源文件。

`$ svn add *`

然后提交代码：

`$svn ci -m 'upload wp'`

## 第二步：配置服务

初始化 MySQL； 

初始化 Memcache 初期没有多少访问量，我只配了 5M 的空间； 

新建一个 Storage (Public) 域名，比如 `wordpress`，这个域名要和 

`wp-includes/functions.php`

第 2222 行的 wp_upload_dir 方法定义一致，比如我的：

{% highlight php%}
// for SAE
$dir = 'saestor://wordpress/uploads';
{% endhighlight %}

## 第三步：安装应用

访问 http://\[your_app_name].sinaapp.com

WordPress 会自动跳转到安装界面，For SAE 能看到醒目的提示：

**安装前请确保已经初始化 Mysql, Memcache 服务，并已在 Storage 服务中创建名为 'wordpress' 的 Domain。**

依据指示安装就行。

## 第四步：最后增强

1、安装必要的插件，比如 语法高亮，防垃圾评论等，可在后台直接搜索安装；

2、安装皮肤； 

3、管理分类； 

4、修改示例 Page，一般是站长自我介绍； 

5、设置固定链接。

WordPress固定链接设置技巧：

**1）不要让日期出现在固定链接里面**

这基于两个方面的考虑。一是如果数字出现在固定链接里面，等于提醒搜索引擎，这是很旧的内容了，没必要再爬一遍了。另外一个原因是，假如你要修改文章的日期重新发布的话，链接地址就变了，也就是意味着你的反向链接，PR 等等都没有了。

**2）不要让分类的链接出现在固定链接里面**

这一点是很多人都会忽略的地方。让分类出现在固定链接里面有两个缺陷：一是一篇文章如果选择了多个分类的话，则会出现多个链接地址，这很容易造成因为重复内容而被搜索引擎惩罚；二是有可能会造成关键词堆砌而被搜索引擎惩罚。

**3）链接不要过深**

这一点经常看到。很多 WordPress 用户的固定链接是年/月/日/分类名/文章名。这种过于深的固定链接对搜索引擎是非常不友好的。

**4）不要让中文字符出现在固定链接里面**

虽然现在的搜索引擎已经能识别 URL 地址里面的中文字符，但无论是从美观上，还是从 WordPress 优化的角度来看，都是非常差的。

参数列表：

<table class="table table-bordered table-hover table-striped"><tbody>
<tr>
<th class="confluenceTh">参数</th>
<th class="confluenceTh">意义</th>
<th class="confluenceTh">示例</th>
</tr>
<tr>
<td>%year%</td>
<td>基于文章发布的年份</td>
<td>比如 2010</td>
</tr>
<tr>
<td>%monthnum%</td>
<td>基于文章发布的月份</td>
<td>比如 01</td>
</tr>
<tr>
<td>%day%</td>
<td>基于文章发布当日</td>
<td>比如 06</td>
</tr>
<tr>
<td>%hour%</td>
<td>基于文章发布小时数</td>
<td>比如 23</td>
</tr>
<tr>
<td>%minute%</td>
<td>基于文章发布分钟数</td>
<td>比如 43</td>
</tr>
<tr>
<td>%second%</td>
<td>基于文章发布秒数</td>
<td>比如 33</td>
</tr>
<tr>
<td>%postname%</td>
<td>基于文章的postname其值为撰写时指定的缩略名，默认为文章标题</td>
<td>比如 hello-world</td>
</tr>
<tr>
<td>%post_id%</td>
<td>基于文章post_id</td>
<td>比如 48</td>
</tr>
<tr>
<td>%category%</td>
<td>基于文章分类，子分类会处理成“分类/子分类”这种形式</td>
<td>比如 code</td>
</tr>
<tr>
<td>%author%</td>
<td>基于文章作者名</td>
<td>比如 chenzixin</td>
</tr>
</tbody></table>

全文完。






