---
layout: post
title: "Choice is More Important than Hard Work"
description: "<p>两个星期之前，我下载了一本书 C 语言的电子书，《Leaning C on the Mac》，仿照书上的例子，写了一段代码，计算高斯数学。今天，又分别用 Node Go Python 和 Ruby 写了相同的逻辑，主要是为了复习他们的循环写法。</p><p>完成同样的任务，耗时相差很远，不是这些语言的解释器不努力，关键取决于我们的选择。</p><p>选择比努力重要。</p>"
category: program
tags: [c, go, python, node, ruby]
---
{% include JB/setup %}

两个星期之前，我下载了一本书 C 语言的电子书，《Leaning C on the Mac》，仿照书上的例子，写了一段代码：

#### Gauß

```c
#include <stdio.h>

int main (int argc, const char * argv[])
{
	long long number, sum;
	sum = 0;
	for ( number = 1; number <= 1000000000; number++ )
	   sum += number;
	printf("C: The sum of the numbers is %lld.\n", sum );
	return 0;
}
```
今天上午在家，百无聊奈，又用其它几种语言写了相同的程序：

#### Node

```javascript
var number, sum;
sum = 0;
for ( number = 1; number <= 1000000000; number++ )
   sum += number;

console.log("Node: The sum of the numbers is " + sum );
```

#### Go

```go
package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i <= 1000000000; i++ {
		sum += i
	}
	fmt.Println("Go: The sum of the numbers is", sum)
}
```

#### Python

```python
r = range(1, 10000 + 1)

sum = 0

for i in r:
	sum += i

print 'Python: The sum of the numbers is %d' % sum
```

#### Ruby

```ruby
r = 1..10000

sum = 0

for i in r
	sum += i
end

puts "Ruby: The sum of the numbers is #{sum}"
```

然后增加尾数的大小，考验他们的运算速度：

- Node 的效率高得惊人，感觉逆天了，比 C 还快？还是因为 C 中 sum 越界了？

- Go 的速度也很快，直逼 C，不过我暂不会使用 BigInt，求和也越界；

- Ruby 1.9.3 的性能，要比 Python 2.7.2 好；

- 不要轻易把 Python 的 range 尾数改得太大，会耗尽内存，我的 21G 的可用空间都被虚拟内存占满；

前面说了，这是一个很无聊的测试，它们都是伟大的语言，现在生活中，也鲜有这样的需求，我不过是在虐语言。

每一门语言，都有自己显著的特征，有它所擅长的领域，精通一门，了解相关的几门，就算是一名合格的程序员。

完成同样的任务，耗时相差很远，不是这些语言的解释器不努力，关键取决于我们的选择。

选择比努力重要。








