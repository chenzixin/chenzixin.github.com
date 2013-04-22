---
layout: post
title: "Jekyll 按年归档插件"
description: "<p>Jekyll Bootstrap 默认提供了按年归档，但是它又细化为月，比如我想知道2012年一共发了多少文章，并不能一目了然的看出来。</p><p>借助 <a href='https://github.com/brucebot/brucebot.com.site'>brucebot</a> 和 <a href='https://github.com/tswicegood/tswicegood-jekyll-extensions'>tswicegood</a> 两位大侠的帮助，终于实现了这一功能，并且在此基础上进一步增强了我的 Jekyll 模版。</p>"
category: program
tags: [jekyll]
---
{% include JB/setup %}

Jekyll Bootstrap 默认提供了按年归档，但是它又细化为月，比如我想知道2012年一共发了多少文章，并不能一目了然的看出来。

借助 [brucebot](https://github.com/brucebot/brucebot.com.site) 和 [tswicegood](https://github.com/tswicegood/tswicegood-jekyll-extensions) 两位大侠的帮助，终于实现了这一功能，并且在此基础上进一步增强了我的 Jekyll 模版。

### 代码

- [_plugins/base_archive_generator.rb](https://github.com/tswicegood/tswicegood-jekyll-extensions/blob/master/_plugins/base_archive_generator.rb)

- [_plugins/yearly_archive_generator.rb](https://github.com/tswicegood/tswicegood-jekyll-extensions/blob/master/_plugins/yearly_archive_generator.rb)

- [_layouts/yearly_archive.html](https://github.com/brucebot/brucebot.com.site/blob/master/_layouts/yearly_archive.html)

### 安装

以上三个文件就位之后，本地运行 Jekyll，会在 _sites 目录下，生成和年份对应的文件夹。

但是，上传之后，访问 http://www.yoursite.com/2013/ 却报 404 错误，心情非常沮丧，曾怀疑插件过时，怀疑模块命名不规范，甚至怀疑自己的人品，但这些都无法解释本地的成功。

后来听说要修改 _config.yml 配置 safe 属性，然而不管是 true 还是 false，反正上传之后，GitHub 是铁板一块，不予睬理。

Google 一下，发现了[这条](https://twitter.com/Dingpeixuan/statuses/295575521960525824)Twitter：

>Github 不支持Jekyll的用户自定义插件，让我很烦恼。

接下来，我又找到几篇博客，印证了这个观点，GitHub 这么做，是出于安全的考虑，以 `-- safe` 启动，限制使用第三方插件：

- [Jekyll + Plugins + Github + You](http://charliepark.org/jekyll-with-plugins/)

- [GitHub Pages and Jekyll plugins](http://arademaker.github.io/blog/2011/12/01/github-pages-jekyll-plugins.html)

- [Gist Tag For Jekyll](http://hackfisher.info/blog/2012/03/gist-tag-for-jekyll/)

各位大神也都提出了绕过限制的方案，但是其复杂程度，都超出了我所能承受的范围，在犹豫着要不要放弃，毕竟目前这一需求不太迫切。

在追查的过程中，还了解到 Jekyll Bootstrap 的一个缺陷：

[Analytics provider google not working](https://github.com/plusjade/jekyll-bootstrap/issues/53)

### 灵光

瞅着本地睡得好好的：

```
+ _site
  + 2011
    - index.html
  + 2012
    - index.html
  + 2013
    - index.html
```

恨得牙痒，却无能为力。

然后，还是印证了那句话：办法总比困难多，脑子里突然蹦出一个点子：

直接把这三个文件夹上传，不就接了！

问题就这么简单！

需要注意的是，这个插件可能存在 Bug，上传之前，要检查有没有重复生成条目。

### 收获

1. 适当的执著，可能会有意外的惊喜；

2. 发现 GitHub 一个不错的工具 [Gist](https://gist.github.com/chenzixin/5429063)；

	有了这个，[PasteBin](http://www.chenzixin.com/program/2013/03/24/found-pastebin/) 的优势，只剩下匿名分享了。

3. 效果预览

	<http://www.chenzixin.com/2011/>

	<http://www.chenzixin.com/2012/>
	
	<http://www.chenzixin.com/2013/>









