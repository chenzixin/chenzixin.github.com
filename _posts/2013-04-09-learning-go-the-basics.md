---
layout: post
title: "Go 语言基础"
description: "<p>我一向比较崇拜 Google 的产品，虽然现在的 Google 已经没有之前那么可爱，但是毕竟它骨子里还是一家商业公司，互相理解。</p><p>在冷落 Python 之后，Google 主推自己的 Go 语言，一直听闻在性能上相当不错，语法也很干净，上周又简单的实测了一下运算速度，真的表现优异。考虑到公司在某些领域已经开始应用，我也应该 Hello World 一下了。</p><p>在 <a href='http://coolshell.cn/'>CoolShell</a> 上找到两篇很不错的入门文章，转载学习：</p><p><a href='http://coolshell.cn/articles/8460.html'>Go 语言简介（上）— 语法</a></p><p><a href='http://coolshell.cn/articles/8489.html'>Go 语言简介（下）— 特性</a></p><p>很欣赏 CoolShell 的坚持，如果我从2009年坚持流水到现在，应该也有不错的积累了。</p>"
category: program
tags: [go]
---
{% include JB/setup %}

我一向比较崇拜 Google 的产品，虽然现在的 Google 已经没有之前那么可爱，但是毕竟它骨子里还是一家商业公司，互相理解。

在冷落 Python 之后，Google 主推自己的 Go 语言，一直听闻在性能上相当不错，语法也很干净，上周又简单的实测了一下运算速度，真的表现优异。考虑到公司在某些领域已经开始应用，我也应该 Hello World 一下了。

在 [CoolShell](http://coolshell.cn/) 上找到两篇很不错的入门文章，转载学习：

[Go 语言简介（上）— 语法](http://coolshell.cn/articles/8460.html)

[Go 语言简介（下）— 特性](http://coolshell.cn/articles/8489.html)

很欣赏 CoolShell 的坚持，如果我从2009年坚持流水到现在，应该也有不错的积累了。

----

### 前提

要对 C 语言，Unix，Python 有一点基础。

### Hello World

文件名：hello.go

```go
package main //声明本文件的package名
 
import "fmt" //import语言的fmt库——用于输出
 
func main() {
    fmt.Println("hello world")
}
```

### 运行

1. 解释执行（实际是编译成a.out再执行）

	```
	$ go run hello.go
	hello world
	```
2. 编译执行

	```
	$go build hello.go

	$ls
	hello hello.go
	 
	$./hello
	hello world
	```

3. GoSublime

	`ctrl + b` 各种 go 语言命令

### 自己的 package

你可以使用 GOPATH 环境变量，或是使用相对路径来 import 你自己的 package。

Go的规约是这样的：

1. 在import中，你可以使用相对路径，如 ./ 或 ../ 来引用你的 package；

2. 如果没有使用相对路径，那么，go 会去找 $GOPATH/src/ 目录。

使用相对路径

```
import "./haoel"  //import当前目录里haoel子目录里的所有的go文件
```

使用 GOPATH 路径

```
import "haoel"  //import 环境变量 $GOPATH/src/haoel子目录里的所有的go文件
```

### fmt 输出格式

fmt 包和 libc 里的那堆使用 printf， scanf，fprintf，fscanf 很相似。下面的东西对于 C 程序员不会陌生。

注意：Println 不支持，Printf 才支持 % 式的输出：

```go
package main

import "fmt"
import "math"

func main() {
	fmt.Println("hello world")

	fmt.Printf("%t\n", 1 == 2)
	fmt.Printf("二进制：%b\n", 255)
	fmt.Printf("八进制：%o\n", 255)
	fmt.Printf("十六进制：%X\n", 255)
	fmt.Printf("十进制：%d\n", 255)
	fmt.Printf("浮点数：%f\n", math.Pi)
	fmt.Printf("字符串：%s\n", "hello world")
}
```

当然，也可以使用如 \n \t \r 这样的和 C 语言一样的控制字符。

### 变量和常量

变量的声明很像 Javascript，使用 var 关键字。注意：go 是静态类型的语言，下面是代码：

```go
//声明初始化一个变量
var x int = 100
var str string = "hello world"
//声明初始化多个变量
var i, j, k int = 1, 2, 3

//不用指明类型，通过初始化值来推导
var b = true //bool型
```

还有一种定义变量的方式（这让我想到了Pascal语言，但完全不一样）

```go
x := 100 //等价于 var x int = 100;
```

常量很简单，使用 const 关键字：

```go
const s string = "hello world"
const pi float32 = 3.1415926
```

### 数组

直接看代码（注意其中的 for 语句，和 C 很相似吧，就是没有括号了）

```go
package main

import (
	"fmt"
)

func main() {
	var a [5]int
	fmt.Println("array a:", a)

	a[1] = 10
	a[3] = 30
	fmt.Println("assign:", a)

	fmt.Println("len:", len(a))

	b := [5]int{1, 2, 3, 4, 5}
	fmt.Println("init:", b)

	var c [2][3]int
	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			c[i][j] = i + j
		}
	}
	fmt.Println("2d: ", c)
}
```

运行结果：

```
array a: [0 0 0 0 0]
assign: [0 10 0 30 0]
len: 5
init: [1 2 3 4 5]
2d:  [[0 1 2] [1 2 3]]
```

### 数组的切片操作

这个很Python了。

```go
package main

import (
	"fmt"
)

func main() {

	a := [5]int{1, 2, 3, 4, 5}

	b := a[2:4] // a[2] 和 a[3]，但不包括a[4]
	fmt.Println(b)

	b = a[:4] // 从 a[0]到a[4]，但不包括a[4]
	fmt.Println(b)

	b = a[2:] // 从 a[2]到a[4]，且包括a[2]
	fmt.Println(b)
}
```

### 分支循环语句

if语句

注意：if 语句没有圆括号，而必需要有花括号

```go
//if 语句
if x % 2 == 0 {
    //...
}

//if - else
if x % 2 == 0 {
    //偶数...
} else {
    //奇数...
}
 
//多分支
if num < 0 {
    //负数
} else if num == 0 {
    //零
} else {
    //正数
}
```

switch 语句

注意：switch 语句没有 break，还可以使用逗号 case 多个值

```go
switch i {
    case 1:
        fmt.Println("one")
    case 2:
        fmt.Println("two")
    case 3:
        fmt.Println("three")
    case 4,5,6:
        fmt.Println("four, five, six")
    default:
        fmt.Println("invalid value!")
}
```

for 语句

前面你已见过了，下面再来看看 for 的三种形式：（注意：Go 语言中没有 while）

```go
//经典的for语句 init; condition; post
for i := 0; i<10; i++{
     fmt.Println(i)
}
 
//精简的for语句 condition
i := 1
for i<10 {
    fmt.Println(i)
    i++
}
 
//死循环的for语句 相当于for(;;)
i :=1
for {
    if i>10 {
        break
    }
    i++
}
```

### 关于分号

从上面的代码我们可以看到代码里没有分号。其实，和 C 一样，Go 的正式的语法使用分号来终止语句。和 C 不同的是，这些分号由词法分析器在扫描源代码过程中使用简单的规则自动插入分号，因此输入源代码多数时候就不需要分号了。

规则是这样的：如果在一个新行前方的最后一个标记是一个标识符（包括像 int 和 float64 这样的单词）、一个基本的如数值这样的文字、或以下标记中的一个时，会自动插入分号：

通常 Go 程序仅在 for 循环语句中使用分号，以此来分开初始化器、条件和增量单元。如果你在一行中写多个语句，也需要用分号分开。

**注意**：无论任何时候，你都不应该将一个控制结构（(if、for、switch 或 select）的左大括号放在下一行。如果这样做，将会在大括号的前方插入一个分号，这可能导致出现不想要的结果。

### map

map 在别的语言里可能叫哈希表或叫 dict，下面是和 map 的相关操作的代码，代码很容易懂。

```go
package main

import (
	"fmt"
)

func main() {
	m := make(map[string]int) //使用make创建一个空的map

	m["one"] = 1
	m["two"] = 2
	m["three"] = 3

	fmt.Println(m)      //输出 map[three:3 two:2 one:1] (顺序在运行时可能不一样)
	fmt.Println(len(m)) //输出 3

	v := m["two"]  //从map里取值
	fmt.Println(v) // 输出 2

	delete(m, "two")
	fmt.Println(m) //输出 map[three:3 one:1]

	m1 := map[string]int{"one": 1, "two": 2, "three": 3}
	fmt.Println(m1) //输出 map[two:2 three:3 one:1] (顺序在运行时可能不一样)

	for key, val := range m1 {
		fmt.Printf("%s => %d \n", key, val)
		/*输出：(顺序在运行时可能不一样)
		  three => 3
		  one => 1
		  two => 2*/
	}
}
```

### 指针

Go 语言一样有指针，看代码：

```go
package main

import (
	"fmt"
)

func main() {
	var i int = 1
	var pInt *int = &i
	//输出：i=1     pInt=0xf8400371b0       *pInt=1
	fmt.Printf("i=%d\tpInt=%p\t*pInt=%d\n", i, pInt, *pInt)

	*pInt = 2
	//输出：i=2     pInt=0xf8400371b0       *pInt=2
	fmt.Printf("i=%d\tpInt=%p\t*pInt=%d\n", i, pInt, *pInt)

	i = 3
	//输出：i=3     pInt=0xf8400371b0       *pInt=3
	fmt.Printf("i=%d\tpInt=%p\t*pInt=%d\n", i, pInt, *pInt)
}
```

Go 具有两个分配内存的机制，分别是内建的函数 new 和 make。他们所做的事不同，所应用到的类型也不同，这可能引起混淆，但规则却很简单。

### 内存分配

**new** 是一个分配内存的内建函数，但不同于其他语言中同名的new所作的工作，它只是将内存清零，而不是初始化内存。new(T) 为一个类型为T的新项目分配了值为零的存储空间并返回其地址，也就是一个类型为 *T 的值。用 Go 的术语来说，就是它返回了一个指向新分配的类型为 T 的零值的指针。

**make(T, args)** 函数的目的与 new(T) 不同。它仅用于创建切片、map 和 chan（消息管道），并返回类型 T（不是*T）的一个被初始化了的（不是零）实例。这种差别的出现是由于这三种类型实质上是对在使用前必须进行初始化的数据结构的引用。例如，切片是一个具有三项内容的描述符，包括指向数据（在一个数组内部）的指针、长度以及容量，在这三项内容被初始化之前，切片值为 nil。对于切片、映射和信道，make 初始化了其内部的数据结构并准备了将要使用的值。如：

下面的代码分配了一个整型数组，长度为10，容量为100，并返回前10个数组的切片：

```go
make([]int, 10, 100)
```

以下示例说明了new和make的不同：

```go
package main

import (
	"fmt"
)

func main() {
	// 不必要地使问题复杂化：
	var p *[]int = new([]int)
	fmt.Println(p) //输出：&[]
	*p = make([]int, 10, 10)
	fmt.Println(p)       //输出：&[0 0 0 0 0 0 0 0 0 0]
	fmt.Println((*p)[2]) //输出： 0

	// 习惯用法:
	v := make([]int, 10)
	fmt.Println(v) //输出：[0 0 0 0 0 0 0 0 0 0]
}
```

### 函数

老实说，我对 Go 语言这种反过来声明变量类型和函数返回值的做法有点不满（保持和 C 一样的不可以吗? 呵呵）

```go
package main
import "fmt"
 
func max(a int, b int) int { //注意参数和返回值是怎么声明的
 
    if a > b {
        return a
    }
    return b
}
 
func main(){
    fmt.Println(max(4, 5))
}
```
### 函数返回多个值

Go 中很多 Package 都会返回两个值，一个是正常值，一个是错误，如下所示：


```go
package main

import "fmt"

func main() {
	v, e := multi_ret("one")
	fmt.Println(v, e) //输出 1 true

	v, e = multi_ret("four")
	fmt.Println(v, e) //输出 0 false

	//通常的用法(注意分号后有e)
	if v, e = multi_ret("four"); e {
		// 正常返回
	} else {
		// 出错返回
	}
}

func multi_ret(key string) (int, bool) {
	m := map[string]int{"one": 1, "two": 2, "three": 3}

	var err bool
	var val int

	val, err = m[key]

	return val, err
}
```

### 函数不定参数

例子很清楚了，我就不多说了。

```go
package main

import "fmt"

func sum(nums ...int) {
	fmt.Print(nums, " ") //输出如 [1, 2, 3] 之类的数组
	total := 0
	for _, num := range nums { //要的是值而不是下标
		total += num
	}
	fmt.Println(total)
}
func main() {
	sum(1, 2)
	sum(1, 2, 3)

	//传数组
	nums := []int{1, 2, 3, 4}
	sum(nums...)
}
```

待续...





















