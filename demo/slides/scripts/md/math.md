title: 数学之美
class: big nobackground
build_lists: true

数学中充满着美的因素，数学美是数学科学的本质力量的感性和理性的呈现，它不是什么虚无飘渺、不可捉摸的东西，而是有其确定的客观内容。

数学美有别与其它的美，它没有鲜艳的色彩，没有美妙的声音，没有动感的画面，它却是一种独特的美。德国数学家克莱因曾对数学美作过这样的描述：音乐能激发或抚慰情怀，绘画使人赏心悦目，诗歌能动人心弦，哲学使人获得智慧，科技可以改善物质生活，但数学却能提供以上一切。

数学美是自然美的客观反映，是科学美的核心。简言之数学美就是数学中奇妙的有规律的让人愉悦的美的东西。

- 伽利略：数学是上帝用来书写宇宙的文字。
- 罗素：数学，如果正确地看，不但拥有真理，而且也具有至高的美。
- 爱因斯坦：这个世界可以由音乐的音符组成，也可以由数学的公式组成。

---

title: 数学之美
subtitle: 数字陷阱
class: segue dark nobackground

---

title: 数字陷阱
class: big nobackground
build_lists: true

有三个人同去餐厅吃饭，每人各出十元钱，餐厅找回五元钱，让服务员转交给这三个人。服务员有点贪小便宜，他一想，三个人分五元钱，怎么也不能做到平均分，于是就自己拿出二元，剩下的三元钱正好退给每人一元。 

每人事先出了10元钱，共计30元。后又每人找回1元，相当于每人各出了9元钱，计27元，加上服务员拿走的2元，计29元。

<span class="red3">那剩下那1元去哪了？</span>

---

title: 数学之美
subtitle: 角谷猜想
class: segue dark nobackground

---

title: 角谷猜想
class: nobackground fill
build_lists: true


考拉兹猜想，又称为 3n+1 猜想、角谷猜想、哈塞猜想、乌拉姆猜想或叙拉古猜想，日本数学家角谷静夫发现：

<span class="green3">对於每一个正整数，如果它是奇数，则对它乘3再加1，如果它是偶数，则对它除以2，如此循环，最终都能够得到1。</span>

例如数字 7

![考拉兹猜想](assets/collatz_conjecture1.png)


<footer class="source">Math</footer>

---

title: 角谷猜想
class: nobackground fill
build_lists: true

考拉兹猜想，又称为 3n+1 猜想、角谷猜想、哈塞猜想、乌拉姆猜想或叙拉古猜想，日本数学家角谷静夫发现：

<span class="green3">对於每一个正整数，如果它是奇数，则对它乘3再加1，如果它是偶数，则对它除以2，如此循环，最终都能够得到1。</span>

再如数字 10

![考拉兹猜想](assets/collatz_conjecture2.png)


<footer class="source">Math</footer>


---

title: 数学之美
subtitle: 折纸中的学问
class: segue dark nobackground

---

title: 折纸中的学问
class: nobackground fill
build_lists: true

一张报纸，不断对折，折30次后，纸叠得有多厚？


![折纸](assets/paper.png)


<footer class="source">Math</footer>

---

title: 数学之美
subtitle: 梵塔中的学问
class: segue dark nobackground

---

title: 梵塔中的学问
class: nobackground fill
build_lists: true

一个关于世界末日的传说。

这个传说出自古代的印度，历史学家鲍尔是这样描述的：

在世界中心贝拿勒斯的圣庙里，安放着一块黄铜板，黄铜板上插着三根宝石针。每根针高约1腕尺，象韭菜叶那样粗细。

印度教的主神梵天在创造世界的时候，在其中的一根针上从下到上穿好了由大到小的64片金片，这就是所谓的梵塔，又称汉诺塔。

不论白天黑夜，都有一个僧侣按照梵天不渝的法则，在三根针上移动这些金片：一次只能移动一片，并且要求不管在哪一根针上，小片永远在大片上面。

当所有的64片金片都从梵天穿好的那根针上移到另外一根针上时，世界就将在一声霹雳中灰飞烟灭，而梵塔、庙宇和众生也都将同归于尽。 

---

title: 梵塔中的学问
class: nobackground fill
build_lists: true

推导公式

- S(1) = 1

- S(2) = 2S(1)+1 = 2*1+1=3 = 2^2-1

- S(3) = 2S(2)+1 = 2*3+1 = 7=2^3-1

- S(4) = 2S(3)+1 = 2*7+1 = 15=2^4-1

- ……

- S(64) = 2S(63)+1 = 2^64-1

---

title: 梵塔中的学问
class: nobackground fill
build_lists: true

最后这个式子告诉我们：僧侣们把金片移动

2^64-1 = 18,446,744,073,709,551,615

次后，梵天所预言的世界末日就会来临。

这大约需要多长时间呢？

一年大约有365.2422天，这折合31,556,926秒。

假设僧侣们每秒钟就可以移动金片一次，那么也得5845亿多年才能移完所有的64片金片。

不过根据现代科学的推测，地球的寿命不会超过200亿年，那么不等僧侣们完成他们的任务，梵塔、庙宇和众生早就同归于尽了。

<footer class="source">Math</footer>


---

title: 梵塔中的学问 

JavaScript 算法示例

<pre class="prettyprint" data-lang="javascript">
var hanoi = function (disc, src, aux, dst) {
    if (disc > 0) {
        hanoi(disc - 1, src, dst, aux);
        console.log('Move disc ' + disc +' from ' + src + ' to ' + dst);
        hanoi(disc - 1, aux, src, dst);
    }
};

hanoi(5, 'Src', 'Aux', 'Dst');
</pre>

---

title: 梵塔中的学问 

Python 算法示例

<pre class="prettyprint" data-lang="python">

def hanoi(disc, src, aux, dst):
    if (disc > 0):
        hanoi(disc - 1, src, dst, aux)
        print('Move disc %d from %s to %s'%(disc,src,dst))
        hanoi(disc - 1, aux, src, dst)

hanoi(3, 'Src', 'Aux', 'Dst')

</pre>

---

title: 数学之美
subtitle: 你能想到吗
class: segue dark nobackground

---

title: 你能想到吗
class: nobackground fill
build_lists: true

有一根很长很长的绳子，恰好可以绕地球赤道一周，如果把绳子再接长15米后，绳子就会绕着地球一周悬在空中。

你能想到吗？

<span class="red3">在赤道的任何一个地方，一个身高2米39以下的人，都可以从绳子下面自由穿过。 </span>


<footer class="source">Math</footer>

---

title: 你能想到吗
class: nobackground fill
build_lists: true

其实你小学的时候，已经会计算了！

设地球半径为 R 米，则绳子的原长为 2πR，当绳子长为 2πR + 15 时：

绳子所围半径为

(2πR + 15) ÷ 2π = R + 2.39 


<footer class="source">Math</footer>


---

title: 数学之美
subtitle: 回文诗
class: segue dark nobackground


---

title: 回文诗
class: nobackground fill
build_lists: true

### 晚秋即景


- 正读

	烟霞映水碧迢迢，暮色秋声一雁遥。

	前岑落辉残照晚，边城古树冷萧萧。 

- 反念

	萧萧冷树古城边，晚照残辉落岑前。

	遥雁一声秋色暮，迢迢碧水映霞烟。 

---

title: 回文质数
class: nobackground fill
build_lists: true

所谓回文质数就是指某数为质数，把该数的各个数字倒过来写，所得到的数仍是质数。

如 13 倒过来是 31 ，13 和 31 都是质数，它们就是一对回文质数，17 和 71 也是。 

还能想到哪些？

- 113 和 311

- 347 和 743

- 769 和 967

---

title: 数学之美
subtitle: 圆周率
class: segue dark nobackground

---

title: 圆周率
class: nobackground fill
build_lists: true

瑞士数学家欧拉是最早倡导用希腊字母 π 来表示这个数。

1761年法国数学家兰伯特证明了 <span class="green3">π 不是有理数</span>。

东汉初年的数学专著《周髀算经》中，已有<span class="green">周三径一</span>的记载，这是最早的圆周率，现在将它称为<span class="green3">古率</span>。 

南北朝的祖冲之在《缀术》一书中，用割圆法给出了 <span class="red3">22/7</span> (约率)和 <span class="red3">355/113</span> (密率)两个用分数表示的圆周率，它们被称为<span class="green">祖率</span>。

- 22/7 = 3.14285714285...
- π = 3.14159265358...
- 355/113 = 3.14159292035...

---

title: 圆周率
class: nobackground fill
build_lists: true

叶维塔（Yeavita）用割圆法算至圆内接393216边形，得到π的十位小数；

荷兰数学家鲁道夫（C.Rudolff）花了毕生的精力算到π的第35位小数；

美国天文学家纽科布说：

如果把地球想像为绝对的球体，π 的10位小数就足以使计算地球的周界精确到一英寸之内，若用 π 的30位小数能使可观宇宙的四周计算精确到连最强大的显微镜也不可能分辨的一个数量级。

---

title: 圆周率
class: nobackground fill
build_lists: true

如今计算 π 的位数，已成为检验计算机性能包括它的软件（即计算方法）的一种手段。 

![计算 π](assets/calpi.png)

---

title: 圆周率
class: nobackground fill
build_lists: true

π 计算到小数点后第 710100 位时，连续出现七个数字 3：

π = 3.141592…353733333338638…；

π 的前两位数字 31，前六位数字 314159 组成的数是两个回文质数：

- 13 与 31

- 314159 与 951413 

---

title: 数学之美
subtitle: 神奇的 0.618 ...
class: segue dark nobackground

---

title: 神奇的 0.618 ...
class: nobackground fill
build_lists: true

黄金比例，又称黄金比，是一种数学上的比例关系。黄金分割具有严格的比例性、艺术性、和谐性，蕴藏着丰富的美学价值。应用时一般取0.618或1.618，就像圆周率在应用时取3.14一样。黄金分割早存在于大自然中，呈现于不少动物和植物外观。现今很多工业产品、电子产品、建筑物或艺术品均普遍应用黄金分割，呈现其功能性与美观性。

![黄金比](assets/golden_ratio.png)

---

title: 神奇的 0.618 ...
class: nobackground fill
build_lists: true

精确的五角星，任意一条线段上的比必须等于黄金分割点。


![五角星](assets/pentagram.png)

---

title: 神奇的 0.618 ...
class: nobackground fill
build_lists: true

图解：


![五角星黄金分割](assets/pentagram-gold.png)

---

title: 神奇的 0.618 ...
class: nobackground fill
build_lists: true


0.618… 这是被中世纪学者、艺术家达芬奇誉为黄金数的重要数值，因而中外比分割亦被誉为黄金分割。它也曾被德国天文、物理、
数学家开普勒赞为几何学中两大瑰宝之一。

顾名思义，黄金数当有着黄金一样的价值，人们喜欢它。

黄金比值一直统治着古代中东、中世纪西方建筑艺术，这些世人瞩目的建筑中都蕴藏着0.618…这一黄金数。

- 古埃及金字塔

- 古希腊帕特农神殿

- 印度泰姬陵

- 法国巴黎圣母院

---

title: 神奇的 0.618 ...
class: nobackground fill
build_lists: true

动物和昆虫中也是这样，像犬、马、狮、虎、蝴蝶等看上去形体都很优美，其原因也是它们的比例大体上接近黄金分割。

在我们人类中也是一样，凡是看上去体态优美的人，其身体各部分的比例也与黄金比率相近。晚会上的报幕员，一般都不会站在舞台的正中间，而是站在舞台一侧的0.618处，这样看起来，才会显得更加和谐、悦目。

在许多植物中，它们所生长的形状一般都接近黄金分割的比例。在植物的茎干上，两个相邻的叶片夹角一般都是137°30′，而这个角度恰好又是圆的黄金分割比。研究发现，这种夹角对植物的通风和采光效果最佳。

另外在向日葵上，也包含有许多黄金比例的结构和原理。在向日葵花盘上的瓜籽布局通常为左21条和右13条的两种螺旋，而13与21的比值正好与黄金分割的比值0.618非常接近。通过计算得知，向日葵籽的螺旋排列可在最小的面积上得到最大的数量。


---

title: 数学之美
content_class: flexbox vcenter

对美好的东西，你要有心动的感觉！

---

title: 不努力就会变成 IE 浏览器
content_class: flexbox vcenter

Q & A
