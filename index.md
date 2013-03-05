---
layout: default
title: Hello World!
---


{{ page.title }}


最新文章


{% for post in site.posts %}
    {{ post.date | date_to_string }} {{ post.title }}
{% endfor %}

----

从小，就有许多梦想，现在，一个也不曾留下。我也没有了眼泪。黑沉沉的夜里总是开满黑沉沉的花。慢慢睡去，月光撒落，这个世界干燥冰凉。

