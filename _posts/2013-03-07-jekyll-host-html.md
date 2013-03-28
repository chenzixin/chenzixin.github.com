---
layout: post
title: "在 Jekyll 中展示精彩的 CSS3 效果"
description: "<p>这几天终于将 Jekyll 折腾好了，这是程序员的本性。推荐给组内同事，他问：</p><p>能不能用 HTML ？</p><p>其实本质上，GitHub Page 的运作，就是将 MarkDown 转为 HTML，所以理论上是没有问题的。</p><p>这里用 <a href='http://www.hongkiat.com/blog/' target='_blank'>HONGKIAT</a> 写的十个漂亮的 CSS3 效果作为例子，演示效果，顺便学习CSS3。以后该主题的博文，将会发表在 <a href='http://www.jsoops.com/'>JS Oops!</a> 中。</p>"
category: program
tags: [html, css3]
---
{% include JB/setup %}

这几天终于将 Jekyll 折腾好了，这是程序员的本性。推荐给组内同事，他问：

> 能不能用 HTML ？

其实本质上，GitHub Page 的运作，就是将 MarkDown 转为 HTML，所以理论上是没有问题的。

这里用 [HONGKIAT](http://www.hongkiat.com/blog/) 写的十个漂亮的 CSS3 效果作为例子，演示效果，顺便学习CSS3。以后该主题的博文，将会发表在 [JS Oops!](http://www.jsoops.com/) 中。

原文：[10 Creative Techniques Using CSS3 Box Shadow](http://www.hongkiat.com/blog/css3-box-shadows-effects/)

延伸：[20 Hottest Trends To Watch Out For In 2013](http://www.hongkiat.com/blog/web-design-trend-2013/)

### 1. 固定顶部工具栏

演示：[Fixed Top Toolbar](/demo/box-shadow/fixed-top-toolbar.html)

代码：

{%highlight css%}
#banner {
	position: fixed;
	height: 60px;
	width: 100%;
	top: 0;
	left: 0;
	border-top: 5px solid #a1cb2f;
	background: #fff;
	-moz-box-shadow: 0 2px 3px 0px rgba(0, 0, 0, 0.16);
	-webkit-box-shadow: 0 2px 3px 0px rgba(0, 0, 0, 0.16);
	box-shadow: 0 2px 3px 0px rgba(0, 0, 0, 0.16);
	z-index: 999999;
}

#banner h1 {
	line-height: 60px;
}
{%endhighlight%}



### 2. 下拉式导航菜单

演示：[Sub Navigation Dropdown](/demo/box-shadow/sub-navigation-dropdown.html)

代码：

{%highlight css%}
#bar {
	display: block;
	height: 45px;
	background: #22385a;
	padding-top: 5px;
	margin-bottom: 150px;
	position: relative;
}

#bar ul {
	margin: 0px 15px;
	font-family: Candara, Calibri, "Segoe UI", Segoe, Arial, sans-serif;
}

#bar ul li {
	background: #22385a;
	display: block;
	font-size: 1.2em;
	position: relative;
	float: left;
}

#bar ul li a {
	display: block;
	color: #fffff7;
	line-height: 45px;
	font-weight: bold;
	padding: 0px 10px;
	text-decoration: none;
	z-index: 9999;
}

#bar ul li a:hover, #bar ul li a.selected {
	color: #365977;
	background: #fff;
	border-top-left-radius: 3px;
	border-top-right-radius: 3px;
	-webkit-border-top-left-radius: 3px;
	-webkit-border-top-right-radius: 3px;
	-moz-border-radius-topleft: 3px;
	-moz-border-radius-topright: 3px;
}

#bar ul .subnav {
	display: block;
	left: 14px;
	top: 48px;
	z-index: -1;
	width: 500px;
	position: absolute;
	height: 90px;
	border: 1px solid #edf0f3;
	border-top: 0;
	padding: 10px 0 10px 10px;
	overflow: hidden;
	-moz-border-radius-bottomleft: 3px;
	-moz-border-radius-bottomleft: 3px;
	-webkit-border-bottom-left-radius: 3px;
	-webkit-border-bottom-right-radius: 3px;
	border-bottom-right-radius: 3px;
	border-bottom-right-radius: 3px;
	-moz-box-shadow: 0px 2px 7px rgba(0,0,0,0.25);
	-webkit-box-shadow: 0px 2px 7px rgba(0,0,0,0.25);
	box-shadow: 0px 2px 7px rgba(0,0,0,0.25);
	-ms-filter: "progid:DXImageTransform.Microsoft.Shadow(Strength=3, Direction=180, Color='#333333')";
	filter: progid:DXImageTransform.Microsoft.Shadow(Strength=3, Direction=180, Color='#333333');
}
{%endhighlight%}



### 3. 带光泽阴影按钮

演示：[Glossy Shadow Button](/demo/box-shadow/glossy-shadow-button.html)

代码：

{%highlight css%}
blues {
	color: #fff;
	width: 190px;
	height: 35px;
	cursor: pointer;
	font-family: Arial, Tahoma, sans-serif;
	font-size: 1.0em;
	font-weight: bold;
	-moz-border-radius: 2px;
	-webkit-border-radius: 2px;
	border-radius: 2px;
	border-width: 1px;
	border-color: #0053a6 #0053a6 #000;
	background-color: #6891e7;
	background-image: -moz-linear-gradient(top,#4495e7 0, #0053a6 100%);
	background-image: -ms-linear-gradient(top,#4495e7 0, #0053a6 100%);
	background-image: -o-linear-gradient(top,#4495e7 0, #0053a6 100%);
	background-image: -webkit-gradient(linear,left top,left bottom,color-stop(0, #4495e7),color-stop(100%, #0053a6));
	background-image: -webkit-linear-gradient(top,#4495e7 0,#0053a6 100%);
	background-image: linear-gradient(to bottom,#4495e7 0,#0053a6 100%);
	text-shadow: 1px 1px 0 rgba(0, 0, 0, .6);
	-moz-box-shadow: inset 0 1px 0 rgba(256, 256, 256, .35);
	-ms-box-shadow: inset 0 1px 0 rgba(256, 256, 256, .35);
	-webkit-box-shadow: inset 0 1px 0 rgba(256, 256, 256, .35);
	box-shadow: inset 0 1px 0 rgba(256, 256, 256, .35);
	filter: progid:DXImageTransform.Microsoft.Gradient(GradientType=0,StartColorStr=#4495e7,EndColorStr=#0053a6);
}

.blues:hover {
	border-color: #002d59 #002d59 #000;
	-moz-box-shadow: inset 0 1px 0 rgba(256, 256, 256, 0.55), 1px 1px 3px rgba(0, 0, 0, 0.25);
	-ms-box-shadow: inset 0 1px 0 rgba(256, 256, 256, 0.55), 1px 1px 3px rgba(0, 0, 0, 0.25);
	-webkit-box-shadow: inset 0 1px 0 rgba(256, 256, 256, 0.55), 1px 1px 3px rgba(0, 0, 0, 0.25);
	box-shadow: inset 0 1px 0 rgba(256, 256, 256, 0.55), 1px 1px 3px rgba(0, 0, 0, .25);
	filter: progid:DXImageTransform.Microsoft.Gradient(GradientType=0,StartColorStr=#3a8cdf ,EndColorStr=#0053a6);
	background-image: -moz-linear-gradient(top,#3a8cdf 0,#0053a6 100%);
	background-image: -ms-linear-gradient(top,#3a8cdf 0,#0053a6 100%);
	background-image: -o-linear-gradient(top,#3a8cdf 0,#0053a6 100%);
	background-image: -webkit-gradient(linear,left top,left bottom,color-stop(0,#3a8cdf),color-stop(100%,#0053a6));
	background-image: -webkit-linear-gradient(top,#3a8cdf 0,#0053a6 100%);
	background-image: linear-gradient(to bottom,#3a8cdf 0,#0053a6 100%);
}

.blues:active {
	border-color: #000 #002d59 #002d59;
	-moz-box-shadow: inset 0 1px 3px rgba(0,0,0,0.2),0 1px 0 #fff;
	-ms-box-shadow: inset 0 1px 3px rgba(0,0,0,0.2),0 1px 0 #fff;
	-webkit-box-shadow: inset 0 1px 3px rgba(0,0,0,0.2),0 1px 0 #fff;
	box-shadow: inset 0 1px 3px rgba(0,0,0,0.2),0 1px 0 #fff;
	filter: progid:DXImageTransform.Microsoft.Gradient(GradientType=0,StartColorStr=#005ab4,EndColorStr=#175ea6);
	background-image: -moz-linear-gradient(top,#005ab4 0,#175ea6 100%);
	background-image: -ms-linear-gradient(top,#005ab4 0,#175ea6 100%);
	background-image: -o-linear-gradient(top,#005ab4 0,#175ea6 100%);
	background-image: -webkit-gradient(linear,left top,left bottom,color-stop(0,#005ab4),color-stop(100%,#175ea6));
	background-image: -webkit-linear-gradient(top,#005ab4 0,#175ea6 100%);
	background-image: linear-gradient(to bottom,#005ab4 0,#175ea6 100%);
}
{%endhighlight%}



### 4. 弹出通知栏

演示：[Notifications Flyout Menu](/demo/box-shadow/notifications-flyout-menu.html)

代码：

{%highlight css%}
.flyout {
	width: 310px;
	margin-top: 10px;
	font-size: 11px;
	position: relative;
	font-family: 'Lucida Grande', Tahoma, Verdana, Arial, sans-serif;
	background-color: white;
	padding: 9px 11px;
	background: rgba(255, 255, 255, 0.9);
	border: 1px solid #c5c5c5;
	-webkit-box-shadow: 0 3px 8px rgba(0, 0, 0, .25);
	-moz-box-shadow: 0 3px 8px rgba(0, 0, 0, .25);
	box-shadow: 0 3px 8px rgba(0, 0, 0, .25);
	-webkit-border-radius: 3px;
	-moz-border-radius: 3px;
	border-radius: 3px;
}

.flyout #tip {
	background-image: url('images/tip.png');
	background-repeat: no-repeat;
	background-size: auto;
	height: 11px;
	position: absolute;
	top: -11px;
	left: 25px;
	width: 20px;
}

.flyout h2 {
	text-transform: uppercase;
	color: #666;
	font-size: 1.2em;
	padding-bottom: 5px;
	margin-bottom: 12px;
	border-bottom: 1px solid #dcdbda;
}

.flyout p {
	padding-bottom: 25px;
	font-size: 1.1em;
	color: #222;
}
{%endhighlight%}


### 5. 苹果页面包装

演示：[Apple Page Wrapper](/demo/box-shadow/apple-page-wrapper.html)

代码：

{%highlight css%}
.applewrap {
	width: 100%;
	display: block;
	height: 150px;
	background: white;
	border: 1px solid;
	border-color: #e5e5e5 #dbdbdb #d2d2d2;
	-webkit-border-radius: 4px;
	-moz-border-radius: 4px;
	border-radius: 4px;
	-webkit-box-shadow: rgba(0, 0, 0, 0.3) 0 1px 3px;
	-moz-box-shadow: rgba(0,0,0,0.3) 0 1px 3px;
	box-shadow: rgba(0, 0, 0, 0.3) 0 1px 3px;
}

.applewrap .col {
	float: left;
	box-sizing: border-box;
	width: 250px;
	height: 150px;
	padding: 16px 7px 6px 22px;
	font: 12px/18px "Lucida Grande", "Lucida Sans Unicode", Helvetica, Arial, Verdana, sans-serif;
	color: #343434;
	border-right: 1px solid #dadada;
}
{%endhighlight%}

### 6. 苹果内容框效果

演示：[Apple Content Box](/demo/box-shadow/apple-content-box.html)

代码：

{%highlight css%}
.applebox {
	width: auto;
	height: 85px;
	box-sizing: border-box;
	background: #f5f5f5;
	padding: 20px 20px 10px;
	margin: 10px 0 20px;
	border: 1px solid #ccc;
	border-radius: 4px;
	-webkit-border-radius: 4px;
	-moz-border-radius: 4px;
	-o-border-radius: 4px;
	-webkit-box-shadow: inset 0px 1px 1px rgba(0, 0, 0, .3);
	-moz-box-shadow: inset 0px 1px 1px rgba(0, 0, 0, .3);
	box-shadow: inset 0px 1px 1px rgba(0, 0, 0, .3);
}

.applebox .col {
	width: 140px;
	float: left;
	margin: 0 0 0 30px;
}
{%endhighlight%}

### 7. 精选链接

演示：[Apple Feature Links](/demo/box-shadow/apple-feature-links.html)

代码：

{%highlight css%}
.applefeature {
	height: 150px;
	margin: 8px;
	vertical-align: top;
	display: inline-block;
}

.applefeature a {
	display: block;
	width: 168px;
	height: 140px;
	border: 1px solid #ccc;
	color: #333;
	text-decoration: none;
	font-weight: bold;
	line-height: 1.3em;
	background: #f7f7f7;
	-webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, .3);
	-moz-box-shadow: inset 0 1px 2px rgba(0, 0, 0, .3);
	box-shadow: inset 0 1px 2px rgba(0, 0, 0, .3);
	-webkit-border-radius: 4px;
	-moz-border-radius: 4px;
	border-radius: 4px;
}

.applefeature a:hover {
	background: #fafafa;
	background: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#fff), to(#f7f7f7));
	background: -moz-linear-gradient(100% 100% 90deg, #f7f7f7, #fff);
	-webkit-box-shadow: inset 0 1px 2px rgba(0,0,0,.3);
	-moz-box-shadow: inset 0 1px 2px rgba(0,0,0,.3);
	box-shadow: inset 0 1px 2px rgba(0,0,0,.3);
	-webkit-border-radius: 4px;
	-moz-border-radius: 4px;
	border-radius: 4px;
}

.applefeature a img {
	display: block;
	margin: 26px auto 4px;
}

.applefeature a h4 {
	display: block;
	width: 160px;
	font-size: 1.3em;
	font-family: Arial, Tahoma, sans-serif;
	color: #646464;
	text-align: center;
}
{%endhighlight%}

### 8. 帧内图片

演示：[Framed Images](/demo/box-shadow/framed-images.html)

代码：

{%highlight css%}
.wpframe {
	background: #fff;
	border-radius: 2px;
	-webkit-border-radius: 2px;
	-moz-border-radius: 2px;
	padding: 8px;
	-webkit-box-shadow: 1px 2px 1px #d1d1d1;
	-moz-box-shadow: 1px 2px 1px #d1d1d1;
	box-shadow: 1px 2px 1px #d1d1d1;
}
{%endhighlight%}

### 9. 具有焦点亮度效果的文本框

演示：[Glowing Input Fields](/demo/box-shadow/glowing-input-fields.html)

代码：

{%highlight css%}
.formwrap {
	display: block;
	margin-bottom: 15px;
}

.formwrap label {
	display: inline-block;
	width: 80px;
	font-size: 11px;
	font-weight: bold;
	color: #444;
	font-family: Arial, Tahoma, sans-serif;
}

.formwrap .shadowfield {
	position: relative;
	width: 250px;
	font-size: 17px;
	font-family: "Helvetica Neue", Arial, sans-serif;
	font-weight: normal;
	background: #f7f8f8;
	color: #7c7c7c;
	line-height: 1.4;
	padding: 6px 12px;
	outline: none;
	transition: all 0.2s ease-in-out 0s;
	-webkit-transition: all 0.2s ease-in-out 0s;
	-moz-transition: all 0.2s ease-in-out 0s;
	border: 1px solid #ad9c9c;
	border-radius: 6px 6px 6px 6px;
	box-shadow: 0 1px rgba(34, 25, 25, 0.2) inset, 0 1px #fff;
}

.formwrap .shadowfield:focus {
	border-color: #930;
	background: #fff;
	color: #5d5d5d;
	box-shadow: inset 0 1px rgba(34, 25, 25, 0.2), 0 1px rgba(255, 255, 255, 0.6), 0 0 7px rgba(235, 82, 82, 0.5);
	-moz-box-shadow: inset 0 1px rgba(34, 25, 25, 0.2), 0 1px rgba(255, 255, 255, 0.6), 0 0 7px rgba(235, 82, 82, 0.5);
	-webkit-box-shadow: inset 0 1px rgba(34, 25, 25, 0.2), 0 1px rgba(255, 255, 255, 0.6), 0 0 7px rgba(235, 82, 82, 0.5);
}
{%endhighlight%}

### 10. 弹性阴影按钮

演示：[Elastic Shadow Buttons](/demo/box-shadow/elastic-shadow-buttons.html)

代码：

{%highlight css%}
.blu-btn {
	display: inline-block;
	-moz-border-radius: .25em;
	border-radius: .25em;
	-webkit-box-shadow: 0 2px 0 0 rgba(0,0,0,0.1), inset 0 -2px 0 0 rgba(0,0,0,0.2);
	-moz-box-shadow: 0 2px 0 0 rgba(0,0,0,0.1), inset 0 -2px 0 0 rgba(0,0,0,0.2);
	box-shadow: 0 2px 0 0 rgba(0,0,0,0.1), inset 0 -2px 0 0 rgba(0,0,0,0.2);
	background-color: #276195;
	background-image: -moz-linear-gradient(#3c88cc,#276195);
	background-image: -ms-linear-gradient(#3c88cc,#276195);
	background-image: -webkit-gradient(linear,left top,left bottom,color-stop(0%,#3c88cc),color-stop(100%,#276195));
	background-image: -webkit-linear-gradient(#3c88cc,#276195);
	background-image: -o-linear-gradient(#3c88cc,#276195);
	filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#3c88cc',endColorstr='#276195',GradientType=0);
	-ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorstr='#3c88cc', endColorstr='#276195', GradientType=0)";
	background-image: linear-gradient(#3c88cc,#276195);
	border: 0;
	cursor: pointer;
	color: #fff;
	text-decoration: none;
	text-align: center;
	font-size: 16px;
	padding: 0px 20px;
	height: 40px;
	line-height: 40px;
	min-width: 100px;
	text-shadow: 0 1px 0 rgba(0,0,0,0.35);
	font-family: Arial, Tahoma, sans-serif;
	-webkit-transition: all linear .2s;
	-moz-transition: all linear .2s;
	-o-transition: all linear .2s;
	-ms-transition: all linear .2s;
	transition: all linear .2s
}

.blu-btn:hover, .blu-btn:focus {
	-webkit-box-shadow: 0 2px 0 0 rgba(0,0,0,0.1), inset 0 -2px 0 0 rgba(0,0,0,0.3), inset 0 12px 20px 2px #3089d8;
	-moz-box-shadow: 0 2px 0 0 rgba(0,0,0,0.1), inset 0 -2px 0 0 rgba(0,0,0,0.3), inset 0 12px 20px 2px #3089d8;
	box-shadow: 0 2px 0 0 rgba(0,0,0,0.1), inset 0 -2px 0 0 rgba(0,0,0,0.3), inset 0 12px 20px 2px #3089d8;
}

.blu-btn:active {
	-webkit-box-shadow: inset 0 2px 0 0 rgba(0,0,0,0.2), inset 0 12px 20px 6px rgba(0,0,0,0.2), inset 0 0 2px 2px rgba(0,0,0,0.3);
	-moz-box-shadow: inset 0 2px 0 0 rgba(0,0,0,0.2), inset 0 12px 20px 6px rgba(0,0,0,0.2), inset 0 0 2px 2px rgba(0,0,0,0.3);
	box-shadow: inset 0 2px 0 0 rgba(0,0,0,0.2), inset 0 12px 20px 6px rgba(0,0,0,0.2), inset 0 0 2px 2px rgba(0,0,0,0.3);
}

.grn-btn {
	display: inline-block;
	-moz-border-radius: .25em;
	border-radius: .25em;
	-webkit-box-shadow: 0 2px 0 0 rgba(0,0,0,0.1), inset 0 -2px 0 0 rgba(0,0,0,0.2);
	-moz-box-shadow: 0 2px 0 0 rgba(0,0,0,0.1), inset 0 -2px 0 0 rgba(0,0,0,0.2);
	box-shadow: 0 2px 0 0 rgba(0,0,0,0.1), inset 0 -2px 0 0 rgba(0,0,0,0.2);
	background-color: #659324;
	background-image: -moz-linear-gradient(#81bc2e,#659324);
	background-image: -ms-linear-gradient(#81bc2e,#659324);
	background-image: -webkit-gradient(linear,left top,left bottom,color-stop(0%,#81bc2e),color-stop(100%,#659324));
	background-image: -webkit-linear-gradient(#81bc2e,#659324);
	background-image: -o-linear-gradient(#81bc2e,#659324);
	filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#81bc2e',endColorstr='#659324',GradientType=0);
	-ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorstr='#81bc2e', endColorstr='#659324', GradientType=0)";
	background-image: linear-gradient(#81bc2e,#659324);
	border: 0;
	cursor: pointer;
	color: #fff;
	text-decoration: none;
	text-align: center;
	font-size: 16px;
	padding: 0px 20px;
	height: 40px;
	line-height: 40px;
	min-width: 100px;
	text-shadow: 0 1px 0 rgba(0,0,0,0.35);
	font-family: Arial, Tahoma, sans-serif;
	-webkit-transition: all linear .2s;
	-moz-transition: all linear .2s;
	-o-transition: all linear .2s;
	-ms-transition: all linear .2s;
	transition: all linear .2s;
}

.grn-btn:hover, .grn-btn:focus {
	-webkit-box-shadow: 0 2px 0 0 rgba(0,0,0,0.1), inset 0 -2px 0 0 rgba(0,0,0,0.3), inset 0 12px 20px 2px #85ca26;
	-moz-box-shadow: 0 2px 0 0 rgba(0,0,0,0.1), inset 0 -2px 0 0 rgba(0,0,0,0.3), inset 0 12px 20px 2px #85ca26;
	box-shadow: 0 2px 0 0 rgba(0,0,0,0.1), inset 0 -2px 0 0 rgba(0,0,0,0.3), inset 0 12px 20px 2px #85ca26;
}

.grn-btn:active {
	-webkit-box-shadow: inset 0 2px 0 0 rgba(0,0,0,0.2), inset 0 12px 20px 6px rgba(0,0,0,0.2), inset 0 0 2px 2px rgba(0,0,0,0.3);
	-moz-box-shadow: inset 0 2px 0 0 rgba(0,0,0,0.2), inset 0 12px 20px 6px rgba(0,0,0,0.2), inset 0 0 2px 2px rgba(0,0,0,0.3);
	box-shadow: inset 0 2px 0 0 rgba(0,0,0,0.2), inset 0 12px 20px 6px rgba(0,0,0,0.2), inset 0 0 2px 2px rgba(0,0,0,0.3);
}
{%endhighlight%}


全文暂完。



