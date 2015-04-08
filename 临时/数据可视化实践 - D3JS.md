## D3简介

D3是一个JavaScript库，用于创建数据可视化图形。它的全称是Data-Driven Documents（数据驱动文档）。
- GITHUB: Github：https://github/mbostock/d3/
- D3官网：http://d3js.org/
- 实例代码：https://github.com/mbostock/d3/wiki/Gallery
- API参考：https://github.com/mbostock/d3/wiki/Api%E5%8F%82%E8%80%83

**简单地说，D3是一个很不错的软件，它能帮你生成和操作带数据的文档。**

1. 把数据加载到浏览器的内存空间。
1. 把数据绑定到文档中的元素，根据需要创建新元素。
1. 解析每个元素的范围资料，并为其设置相应的可视化属性，实现元素的变换。
1. 响应用户输入实现元素状态的过渡。

学习D3的过程，就是学习那些告诉它如何加载、绑定数据，变换和过渡元素的语法的过程。

**D3不能做什么？**

1. D3不能生成预定义的或“事先处理好”的视觉图形。
1. D3不打算支持旧版浏览器。
1. D3的核心功能不处理像谷歌地图或Cloudmade等提供的那些位图格式的地图贴片。
1. D3不隐藏你的原始数据。


## 安装D3

1、下载D3

先创建一个新文件夹，保存项目文件
```
project-folder |--d3
```

2、引用D3
```
<script type="text/javascript" src="d3/d3.min.js"></script>
```


## 数据

**1、连缀方法：类似jQuery的选择器链表。**

- d3：引用D3对象，从而能够调用其方法。
- .select("body")：向select()方法传入一个CSS选择符作为输入，它就会返回一个对DOM中匹配的第一个元素的引用。如果你想取得多个元素，可以使用selectAll()方法。
- .append("p")：会创建一个指定的DOM元素，把创建的新元素的引用交给下一个方法。
- .text("New paragraph!")：text()接受一个字符串，把它插入到当前元素的开始和结束标签之间。

**2、平衡交接**

很多D3方法都返回选中的元素，正因为这样才能实现方法连缀。

*绑定数据*

- 要通过D3的selection.data()方法把数据绑定到DOM元素。但必须具备两个条件：**数据** 和 **选中的DOM元素**

- D3可以很智能地处理各种数据，能够接受任何数值、字符串或对象的数组，能够流畅地处理JSON（GeoJSON），甚至还有一个内置的方法用于加载CSV文件。

*加载CSV文件类型：*
```
d3.csv("food.csv", function(data) {
    console.log(data);
});
```
- csv()接受两个参数：表示CSV文件路径的字符串和用作回调函数的匿名函数。
- 回调函数只有在把CSV文件加载到内存之后才会执行。
- 回调在执行时，会接收到加载和解析后的CSV数据。
- d3.csv()是一个异步方法，在调用时要处理好错误和数据依赖。

*加载JSON数据*
```
d3.json("food.json", function(json) {
    console.log(json);
});
```


作出你的选择：怎么选择还不存在的元素？
```
d3.enter("body").selectAll("p")
    .data(dataset)
    .enter()
    .append("p")
    .text("New paragraph!");
```


**`.selectAll("p")`**：选择DOM中的所有段落。（可以认为这个空元素代表马上就会创建的段落）

**`.data(dataset)`**：解析并数出数据值。dataset数组中有5个值，因而此后的所有方法都将执行5遍，每次针对一个值。

**`.enter()`**：要创建新的绑定数据的元素，就必须使用enter()，类似占位元素。

**`.append("p")`**：取得由enter()创建的空占位元素，并把一个p元素追加到相应的DOM中。

**`.text("New paragraph!")`**：取得新创建的p元素，插入文本内容。

**添加属性和样式**

**`.attr()`**：添加属性

**`.style("color", "red")`**：添加样式



## 第六章 基于数据绘图


**1、绘制DIV**

绘制简单的条形图，条形图实际上就是矩形，而HTML的div元素是绘制矩形的最简单手段。对浏览器来讲一切都是矩形。

严格来说，柱形图（column chart）指的是矩形沿垂直方向试题的图形，而沿水平方向度量的矩形叫条形图。

**2、关于类（class）**

元素的类作为HTML属性存在于标记代码中，同时CSS样式规则也可以引用它。

```
.attr("class", "bar")
```

D3的另一个方法classed()，用于快速地添加或删除元素的类。如：`.classed("bar", true)`会添加一个bar的类样式，如果为false则删除一个bar的样式。

**3、示例**
```
   var dataset = [10, 15, 20, 25, 30];
   d3.select("body").selectAll("div")
       .data(dataset)
       .enter()
       .append("div")
       .attr("class", "bar");
```

**data()的魔力**
```
   var dataset = [ 25, 7, 5, 26, 11, 8, 25, 14, 23, 19,
    14, 11, 22, 29, 11, 13, 12, 17, 18, 10,
    24, 18, 25, 9, 3 ];
   d3.select("body").selectAll("div")
       .data(dataset)
       .enter()
       .append("div")
       .attr("class", "bar")
       .style("height", function(d) {
           var barHeight = d * 5;
           return barHeight + "px";
       });
```

*注意：是数据驱动可视化，而不是相反*

**随机数据**
```
   var dataset = [];
   for (var i=0; i<25; i++) {
       var newNumber = Math.random() * 30;
       dataset.push(newNumber);
   }
```

**绘制SVG**

关于SVG元素，最关键的是要记住它们的各个方面都是通过属性来设定的。换名话说，就是通过标签中的属性/值对来指定SVG元素的各方面特征。

    `<element property="value"></element>`

**创建SVG**

```
    // 创建一个SVG
    var svg = d3.select("body").append("svg");
    // 设置相关属性
    svg.attr("width", 500)
       .attr("height", 50)
       .attr("background", "#efefef");
    // 数据驱动的图形
    var dataset = [5, 10, 15, 20, 25];
    var circle = svg.selectAll("circle")
       .data(dataset)
       .enter()
       .append("circle");
    circle.attr("cx", function(d, i) {
        return (i * 50) + 25;
    })
    .attr("cy", 25)
    .attr("r", function(d) {
        return d;
    });
```


**你好，色彩**

色彩填充（fill）和描边（stroke）同样也是属性，也可以通过attr()方法来设定。
再连缀如下：
```
    .attr("fill", "yellow")
    .attr("stroke", "orange")
    .attr("stroke-width", function(d) {
        return d/2;
    })
```

**绘制条形图**

用新方法改进条形图，需要设置好条形图（SVG）的宽度和高度

通常的步骤：
1. 初始变量设置
1. 创建SVG元素
1. 生成数据集
1. 创建图形类型（如条形图、柱形图）
1. 设置图形的属性（需要考虑SVG元素特有的一些属性设置）
1. 上色的处理
1. 加标签。用.text()

```
    // 创建SVG元素
    var w=500, h=100, barPadding = 1;
    var svg = d3.select("body")
        .append("svg")
        .attr("width", w)
        .attr("height", h);

    // 生成矩形元素rect
    var dataset = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13, 11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ];
    svg.selectAll("rect")
        .data(dataset)
        .enter()
        .append("rect")
        .attr("x", function(d, i) {
            return i * (w /dataset.length);
        })
        .attr("y", 0)
        .attr("width", w / dataset.length - barPadding)
        .attr("height", 100)
        .attr("fill", function(d) {
            return "rgb(0, 0, "+ (d * 10) +")"
        })
        .attr("x", function(d, i) {
            return i * (w / dataset.length);
        })
        .attr("y", function(d) {
            return h - (d * 4);
        });

    svg.selectAll("text")
        .data(dataset)
        .enter()
        .append("text")
        .text(function(d) {
           return d;
        })
        .attr("x", function(d, i) {
            return i * (w /dataset.length) + (w / dataset.length - barPadding) /2;
        })
        .attr("y", function(d) {
            return h - (d * 4) + 14;
        })
        .attr("fill", "white")
        .attr("font-family", "Microsoft Yahei")
        .attr("font-size", "11px")
        .attr("text-anchor", "middle");
```

**6.5 **绘制散点图

散点图是在两个坐标轴上表现两组对应值的常见图表。

- 数据：数组的数组 （二维数组）

```
var dataset = [
[5, 20], [480, 90], [250, 50], [100, 33], [330, 95],
[410, 12], [475, 44], [25, 67], [85, 21], [220, 88]
];
```

- 绘制散点图：可以借鉴条形图的大部分代码

```
// 1 数据
var dataset = [
[5, 20], [480, 90], [250, 50], [100, 33], [330, 95],
[410, 12], [475, 44], [25, 67], [85, 21], [220, 88]
];

// 创建SVG元素
var w = 500, h = 100;
var svg = d3.select("body")
    .append("svg")
    .attr("width", w)
    .attr("height", h);

// 为每个数据点创建circle
svg.selectAll("circle")
    .data(dataset)
    .enter()
    .append("circle")
    // 不再设定矩形的x,y以及width和height属性
    // 而是要设定图形的cx, cy, r(rx, ry)
    .attr("cx", function(d) {
        return d[0];
    })
    .attr("cy", function(d) {
        return d[1];
    })
    .attr("r", function(d) {
        return Math.sqrt(h - d[1]);
    });
// 加标签
svg.selectAll("text")
   .data(dataset)
   .enter()
   .append("text")
   .text(function(d) {
       return d[0] + "," + d[1];
   })
   .attr("x", function(d) {
        return d[0];
   })
   .attr("y", function(d) {
       return d[1];
   });
```


## 第七章 比例尺

比例尺是一组把输入域映射为输出范围的函数。本章只讨论线性比例尺，这是一种最常用也最容易理解的比例尺。

**值域和范围**

比例尺的输入值域（input domain）指可能的输入值的范围。

比例尺的输出范围（output range）指输出值可能的范围，一般以用于显示的像素为单位。

归一化（normalization）就是根据可能的最小值和最大值，把某个数值映射为介于0-1之间的一个新值的过程。比如，一年365天，那么310天映射过来就是0.85，即85%。

**创建比例尺**

D3有一个比例尺函数生成器，通过d3.scale来访问。要生成一个比例尺，在d3.scale后面加上要创建的比例尺类型即可。

```
 var scale = d3.scale.linear();
```

 scale是一个保存函数的变量，即linear()返回的是一个函数。

 通过scale(2.5)来设置比例尺。

 设置比例尺值域需要调用domain()方法，并将值域以数组形式传给它。

```
 scale.domain([100, 500]);
```

 设定输出范围的方式类似，但需要调用range()方法：

```
 scale.range([10, 350]);
```

 这些步骤可以独立完成，也可以连缀起来。

```
 var scale = d3.scale.linear().domain([100, 500]).range([10, 350]);
```

 一般来说，我们都会在attr()或其他类似方法中调用比例尺函数，而不会像这样独立调用它。

**d3.min()和d3.max()**

既然不想给值域设置固定的值，那可以使用两个方便的数组函数：d3.min()和d3.max()，让它们帮你动态分析数据集。

```
d3.max(dataset, function(d) {
    return d[0];
});
```

设置动态缩放

设置x轴值的比例尺函数
```
var xScale = d3.scale.linear()
.domain([0, d3.max(dataset, function(d) { return
d[0]; })])
.range([0, w]);
```

设置y轴值的比例尺函数
```
var yScale = d3.scale.linear()
.domain([0, d3.max(dataset, function(d) { return d[1]; })])
.range([0, h]);
```

其他比例尺

**sprt**：平方根比例尺

**pow**：幂比例尺

**log**：对数比例尺

**quantize**：输出范围为独立的值的线性比例尺，适合想把数据分类的情形。

**quantile**： 与quantize类似，但输入值域是独立的值，适合已经对数据分类的情形。

**ordinal**：使用非定量值作为输出的序数比例尺，非常适合比较苹果和桔子。

**d3.scale.category10()**, **d3.scale.category20()**, **d3.scale.category20b()**和**d3.scale.category20c()**：能够输出10到20种类别颜色的预设数比例尺，非常方便。

**d3.time.scale()**：针对时间和日期的一个比例尺方法，可以对日期刻度作特殊处理。


## 第八章 数轴

与比例尺相似，D3的数轴实际上也是由你定义参数的函数。但与比例尺不同的是，调用数轴函数并不会返回值，而是生成数轴相关的可见元素，包括轴线、标签和刻度。

但要注意，数轴函数只适用于SVG图形，因为它们生成的都是SVG元素。同样，数轴是设计与定量比例尺（与序数比例尺相对）配合使用的。


**设定数轴**

使用d3.svg.axis()可以创建通用的数轴函数：

    var xAxis = d3.svg.axis();

要使用数轴，最起码要告诉它基于什么比例尺工作。

    xAxis.scale(xScale);

数轴的默认位置是底部，也就是标签会出现在轴线下方。水平数轴的位置可以在顶部也可以在底部。而垂直数轴则要么在左要么在右。

    xAxis.orient("bottom"); //支持 top, bottom , left, right


优化刻度线的数量：xAxis.ticks(5);

**垂直数轴**
```
// 定义y轴
var yAixs = d3.svg.axis()
    .scale(yScale)
    .orient("left")
    .ticks(5);

// 创建y轴
svg.append("g")
    .attr("class", "axis")
    .attr("transform", "translate(" + padding + ", 0)")
    .call(yAxis);
```

**为刻度标签定义样式**

```
var formatAsPercentage = d3.format(".1%");

xAxis.tickFormat(formatAsPercentage);
```


## 第九章 更新、过渡和动画

序数比例尺，序数就是有固定顺序的一些类别。

    // 定义序数比例尺：序数就是有固定顺序的一些类别。
    var xScale = d3.scale.ordinal()    // 定义一个序数比例尺，
        .domain(d3.range(dataset.length))
        .rangeRoundBands([0, w], 0.05);

**自动分档**

d3.scale.ordinal()有一个优势，它支持范围分档（banding）。序数比例尺使用的是离散范围值，也就是输出值是事先就确定好的，可以是数值，也可以不是。

映射范围时，可以使用range()，也可以使用rangeBands()。后者接收一个最小值和一个最大值，然后根据输入域的长度自动将其切分成相等的块或档。

- .rangeBands([0, w]， 0.2)：计算从0到w可以均分为几档，然后把比例尺的范围设定为这些档。
- 可以给rangeBands()传入第二个参数，指定档间距。在此，我们使用0.2,也就是档间距为每一档宽度的20%;
- .rangeRoundBands()与rangeBands()的区别只是输出的值会舍入为最接近的整数。如，12.23423 -> 12

**使用序数比例尺**

```
// 创建条形
svg.selectAll("rect")
.data(dataset)
.enter()
.append("rect")
.attr("x", function(d, i) {
return xScale(i); // <-- 设定x 坐标
});
```

**更新数据**

1、 通过事件监听实现交互：d3的selection.on()方法是添加事件监听器的简便方法，它接受两个参数：事件类型（"click"）和监听器（匿名函数）

```
d3.select("p").on("click", function()｛
    // 单击时执行任务
});
```


2、改变数据：重新绑定新值与已有元素，为此，需要选择相应的矩形，再调用一次data()方法：

```
svg.selectAll("rect")
    .data(dataset); // 新数据绑定成功
```

3、更新视觉元素：修改视觉元素的属性

```
svg.selectAll("rect")
    .data(dataset)
    .attr("y", function(d) {
        return h - yScale(d);
    })
    .attr("height", function(d) {
        return yScale(d);
    });
```

完整的更新数据的代码：
```
d3.select("p")
    .on("click", function() {
        // 新数据集
        dataset = [ 11, 12, 15, 20, 18, 17, 16, 18, 23, 25, 5, 10, 13, 19, 21, 25, 22, 18, 15, 13 ];

        // 更新所有矩形
        svg.selectAll("rect")
            .data(dataset)
            .transition() // 添加过滤动画
            .attr("y", function(d) {
                return h - yScale(d);
            })
            .attr("height", function(d) {
                return yScale(d);
            });
    });
```


**过渡动画**

要创建一个精致、流畅、动态的过渡效果，只需简单的一行代码：

```
.transition();
```

*特别要注意的是，在方法链上，要把这个调用插到选择元素之后，改变任何属性之前。*

**持续时间**

我们可以控制动画的持续时间：

```
.duration(1000);
```

*注意，必须把duration()放到transition()之后，参数的单位是毫秒。*


**缓动函数**

应用于过渡效果的这种动画品质叫做缓动。用动画术语来说，可以理解成元素缓缓就位。

在D3中使用ease()指定不同的缓动类型。默认的缓动效果是"cubic-in-out"，逐渐加速再逐渐减速。

注意，要在transition()之后，attr()之前指定ease()。事实上，ease()在duration()之前之后都没有问题。

ease()的取值：

1. circle：逐渐进入并加速，然后突然停止。
1. elastic：描述这个效果的一个最恰当的词是"有弹性"
1. bounce：像皮球落地一样反复弹跳，慢慢停下来。


**延迟时间**

delay()：用于指定过渡什么时间开始。

可以给delay()传入一个静态的值，同样以毫秒为单位。

*注意：delay()和ease()一样，建议放在duration()前面。先设定延迟时间，然后过渡动画。*


**其他数据更新方式**

- 添加值和元素

向数据集中添加一个新值
```
var maxValue = 25;
var newNumber = Math.floor(Math.random() * maxValue);
dataset.push(newNumber);
```

- 选择

select()和selectAll()取得和返回DOM元素。

- 加入

在绑定新数据后，调用enter()方法，加入数据。

```
svg.selectAll("rect")
    .data(dataset)
    .enter()
    .append("rect");
```

- 删除值和元素

要访问退出元素集，可以使用exit()方法。

退出元素是指那些该删除的元素。先取得退出元素集，然后把它们过渡到右边，最后删除它们。

```
bars.exit()
    .transition()
    .duration(500)
    .attr("x", w)
    .remove();
```

温和退出


**通过键联结数据**

在把数据绑定到DOM元素时（即调用data()时)，就会发生数据联结，默认的联结是按照索引顺序，即第一个值绑定到元素集中第一个DOM元素，第二个值绑定到元素集中第二个DOM元素。

1、准备数据
```
var dataset = [ { key: 0, value: 5 },
{ key: 1, value: 10 },
{ key: 2, value: 13 },
{ key: 3, value: 19 },
{ key: 4, value: 21 },
{ key: 5, value: 25 },
{ key: 6, value: 22 },
{ key: 7, value: 18 },
{ key: 8, value: 15 },
{ key: 9, value: 13 },
{ key: 10, value: 11 },
{ key: 11, value: 12 },
{ key: 12, value: 15 },
{ key: 13, value: 20 },
{ key: 14, value: 18 },
{ key: 15, value: 17 },
{ key: 16, value: 16 },
{ key: 17, value: 18 },
{ key: 18, value: 23 },
{ key: 19, value: 25 } ];
```

2、更新所有引用。
```
var yScale = d3.scale.linear()
.domain([0, d3.max(dataset, function(d) { return d.value;
})])
.range([0, h]);
```


3、键函数
```
var key = function(d) {
return d.key;
};
```

4、退出过渡
```
// 退出……
bars.exit()
.transition()
.duration(500)
.attr("x", -xScale.rangeBand()) // <-- 从左侧下台
.remove();
```

- 添加和删除组合拳

```
// 看看单击了哪个段落
var paragraphID = d3.select(this).attr("id");
// 确定接下来该干什么
if (paragraphID == "add") {
//Add a data value
var maxValue = 25;
var newNumber = Math.floor(Math.random() * maxValue);
var lastKeyValue = dataset[dataset.length - 1].key;
console.log(lastKeyValue);
dataset.push({
key: lastKeyValue + 1,
value: newNumber
});
} else {
// 删除一个值
dataset.shift();
}
```


## 第10章 交互式图表

**绑定事件监听器**

为了让图表具有交互能力，我们必须针对一些事件来编写代码，以便监听某些DOM元素发生的这些事件。
```
d3.select("p")
    .on("click", function() {

    });
```

为图表赋予交互能力很简单，只要两步：
1. 绑定事件监听器
1. 定义行为

```
// 部分代码：交互
svg.selectAll("rect")
        .data(dataset)
        .enter()
        .append("rect")
        .attr("x", function(d, i) {
            return xScale(i);
        })
        .attr("y", 0)
        .attr("width", w / dataset.length - barPadding)
        .attr("height", 100)
        .attr("fill", function(d) {
            return "rgb(0, 0, "+ (d * 10) +")";
        })
        .attr("x", function(d, i) {
            return i * (w / dataset.length);
        })
        .attr("y", function(d) {
            return h - (d * 4);
        })

	// 交互的代码
        .on("mouseover", function() {
            d3.select(this).attr("fill", "orange");
        })
        .on("mouseout", function(d) {
            d3.select(this)
            .transition()
            .duration(250)
            .attr("fill", "rgb(0, 0, "+ (d * 10) +")");
        });
```

**单击排序**

交互式图表真正的强大之处，体现在能够展示数据的不同视图，吸引用户从不同角度来探索数据中蕴藏的奥秘。

对数据进行排序是非常重要的一种功能。

```
.on("click", function() {
    sortBars();
});

var sortBars = function() {
 svg.selectAll("rect")
     // sort方法排序，需要知道哪个排前面。设置排序的规则
     .sort(function(a, b) {
         return d3.ascending(a, b); // asc 升序
     })
     .transition()
     .duration(1000)
     .attr("x", function(d, i) {
         return xScale(i);
     });
};
```


**提示条**

浏览器默认的提示方法：直接将title添加上去，放在属性与事件的后面

```
.append("title")
    .text(function(d) {
        return "This value is " + d;
    });
```

SVG*元素提示条：略，要控制就得多花点时间，有点复杂*

HTML的div提示条

适用情形：

1、实现的效果通过SVG不可能做到，或者支持不够好。

2、提示条要SVG图形的边界。

*注意：position属性的值是absolute，这样就可以精确控制它在页面上的位置了。*

pointer-events: none可以保证鼠标经过提示条不会触发条形的mouseout事件，从而让提示条得以继续隐身。

```
.on("mouseover", function(d) {
        d3.select(this).attr("fill", "orange");

       // 取得条形的x/y 值，增大后作为提示条的坐标
        var xPosition = parseFloat(d3.select(this).attr("x")) + xScale.rangeBand() / 2;
        var yPosition = parseFloat(d3.select(this).attr("y")) / 2 + h / 2;
        // 更新提示条的位置和值
        d3.select("#tooltip")
        .style("left", xPosition + "px")
        .style("top", yPosition + "px")
        .select("#value")
        .text(d);
         // 显示提示条
        d3.select("#tooltip").classed("hidden", false);
    })
    .on("mouseout", function(d) {
        d3.select(this)
        .transition()
        .duration(250)
        .attr("fill", "rgb(0, 0, "+ (d * 10) +")");
        // 隐藏提示条
        d3.select("#tooltip").classed("hidden", true);
    });
```

## 第11章 布局

D3 全部的布局方法如下。
- **Bundle**：把霍尔顿（Holten）• 的分层捆绑算法应用到连线（edge）。
- **Chord**：根据矩阵关系生成弦形图（chord diagram）。
- **Cluster**：聚集实体生成系统树图（dendrogram）。
- **Force**：根据物理模拟定位链接的结点。
- **Hierarchy**：派生自定义的系统（分层的）布局实现。
- **Histogram**：基于量化的分组计算数据分布。
- **Pack**：基于递归圆形填充（circle packing）产生分层布局。
- **Partition**：递归细分结点树，呈射线或冰挂状。
- **Pie**：计算饼图或圆环图中弧形的起止角度。
- **Stack**：计算一系列堆叠的条形或面积图的基线。
- **Tree**：整齐地定位树结点。
- **Treemap**：基于递归空间细分来显示结点树。

三个最常用的布局方法：饼图（Pie）、堆叠（Stack）和力导向（Force）。

#### 饼图布局

d3.layout.pie()：主要用于创建饼图。

**1、定义数据集**

```
var dataset = [ 5, 10, 20, 45, 6, 25 ];
```

**2、定义一个默认的饼图布局**

```
var pie = d3.layout.pie();
```

饼图布局方法把简单的数值数组转换成了对象的数组，每个值一个对象。每个对象又包含几个值，最重要的是startAngle和endAngle.

要绘制扇形，还得使用d3.svg.arc()，这是D3中用SVG的path元素绘制弧形的内置方法。

path是SVG用来绘制不规则图形的一个元素。任何不是矩形、圆形或其他基本形状的图形，都可以用path来绘制。


**3、用d3.svg.arc()方法生成路径就好了。**

弧形是一个自定义函数，接受内圆半径和外圆半径作为参数。

```
var w = 300, h = 300;
var outerRadius = w / 2, innerRadius = 0;
var arc = d3.svg.arc()
   .innerRadius(innerRadius)
   .outerRadius(outerRadius);
```

**4、绘制扇形，首先要创建SVG元素**

```
// 创建SVG元素
var svg = d3.select("body")
    .append("svg")
    .attr("width", w)
    .attr("height", h);
```

**5、为每个绘制的扇形创建新的分组（g）, 把用于生成饼图的数据绑定到这些元素，并把每个分组平移到图表中心。**

```
var arcs = svg.selectAll("g.arc")
        .data(pie(dataset))
        .enter()
        .append("g")
        .attr("class", "arc")
        .attr("transform", "translate(" + outerRadius + ", " + outerRadius + ")");
```

**6、最后我们在每个g元素中追加一个path元素。路径相关属性的值都保存在d中，所在这里调用arc生成器，基于绑定到这个分组的数据来生成路径信息：**

```
arcs.append("path")
   .attr("fill", function(d, i) {
       return color(i);
   })
   .attr("d", arc);
```

颜色的设置由D3随机产生

```
var color = d3.scale.category10();
```

**7、为每个扇形生成文本标签**

```
arcs.append("text")
    .attr("transform", function(d) {
    return "translate(" + arc.centroid(d) + ")";
    })
    .attr("text-anchor", "middle")
    .text(function(d) {
    return d.value;
    });
```

arc.centroid(d)：所谓圆心（centroid）就是通过计算得到的任何图形的中心点，无论是常规图形还是极为不规则的图形。

arc.centroid()是个超级有用的函数，它负责计算并返回任何弧形的中心点。然后把弧形标签元素平移到每个弧形的中心点。

innerRadius值,如果其值大于0，饼图就会变成圆环图。

#### 堆叠布局

d3.layout.stack()能够把二维数据转换成"堆叠"数据，它会计算每个数据点的基线值，以便把数据层相互堆叠起来。

这个布局方法可以用于创建堆叠条形图、堆叠面积图，河流图。

**1、数据集**

```
var dataset = [
{ apples: 5, oranges: 10, grapes: 22 },
{ apples: 4, oranges: 12, grapes: 28 },
{ apples: 2, oranges: 19, grapes: 32 },
{ apples: 7, oranges: 23, grapes: 35 },
{ apples: 23, oranges: 17, grapes: 43 }
];
```

第一步就要把这些数据重新组织成一个数组的数组，每个数组代表一个类别（apples, oranges, grapes）。

在每个类别数组中，要用对象表示每个数据值，而表示每个数据的对象本身包含x和y值。这里的x值其实就是ID，而y值才是实际的数据值。

```
var dataset = [
[
{ x: 0, y: 5 },
{ x: 1, y: 4 },
{ x: 2, y: 2 },
{ x: 3, y: 7 },
{ x: 4, y: 23 }
],
[
{ x: 0, y: 10 },
{ x: 1, y: 12 },
{ x: 2, y: 19 },
{ x: 3, y: 23 },
{ x: 4, y: 17 }
],
[
{ x: 0, y: 22 },
{ x: 1, y: 28 },
{ x: 2, y: 32 },
{ x: 3, y: 35 },
{ x: 4, y: 43 }
]
];
```

**2、初始化一个堆叠布局函数，把原始数据集传进去**

```
var stack = d3.layout.stack();
stack(dataset);
```

#### 力导向布局

力导向布局典型地要使用网状数据。在计算机科学领域，这种数据集叫做图（graph）。图由一组节点（node）和连线（edge）构成。
节点代表数据集中的实体，连线代表结点之间的关系。

**1、数据集**

```
var dataset = {
nodes: [
    { name: "Adam" },
    { name: "Bob" },
    { name: "Carrie" },
    { name: "Donovan" },
    { name: "Edward" },
    { name: "Felicity" },
    { name: "George" },
    { name: "Hannah" },
    { name: "Iris" },
    { name: "Jerry" }
    ],
    edges: [
    { source: 0, target: 1 },
    { source: 0, target: 2 },
    { source: 0, target: 3 },
    { source: 0, target: 4 },
    { source: 1, target: 5 },
    { source: 2, target: 5 },
    { source: 2, target: 5 },
    { source: 3, target: 4 },
    { source: 5, target: 8 },
    { source: 5, target: 9 },
    { source: 6, target: 7 },
    { source: 7, target: 8 },
    { source: 8, target: 9 }
    ]
};
```

**2、初始化一个力导向布局**

```
var force = d3.layout.force()
    .nodes(dataset.nodes)
    .links(dataset.edges)
    .size([w, h])
    .linkDistance([50])
    .charge([-100])
    .start();
```

**3、创建作为连线的SVG直线：**

```
var edges = svg.selectAll("line")
    .data(dataset.edges)
    .enter()
    .append("line")
    .style("stroke", "#ccc")
    .style("stroke-width", 1);
```

**4、为每个结点创建SVG圆形**

```
var nodes = svg.selectAll("circle")
    .data(dataset.nodes)
    .enter()
    .append("circle")
    .attr("r", 10)
    .style("fill", function(d, i) {
    return colors(i);
    })
	.call(force.drag);
```

## 第12章 地图

**JSON与GeoJSON**

GeoJSON是基于JSON的、为WEB应用而编码地理数据的一个标准。实际上GeoJSON并不是另一种格式，而只是JSON非常特定的一种使用方法。

1、数据：GeoJSON数据

**路径**

2、定义一个路径生成器

```
var path = d3.geo.path();
```

是一个把GeoJSON坐标转换成更乱的SVG路径代码。

然后使用d3.json() 来加载。
```
d3.json("us-states.json", function(json) {
    svg.selectAll("path")
    .data(json.features)
    .enter()
    .append("path")
    .attr("d", path);
});
```

**投影**

所谓投影，就是一种折中算法，一种把3D空间“投影”到2D平面的方法。

定义D3投影的方式：

```
var projection = d3.geo.albersUsa().translate([w/2, h/2]);
```

要明确告诉路径生成器，应该使用这个自定义的投影来生成所有路径：

```
var path = d3.geo.path().projection(projection);
```

还可以给投影添加一个scale()方法，把地图缩小一些。

```
var projection = d3.geo.albersUsa()
    .translate([w/2, h/2])
    .scale([500]);
```

**等值区域**

首先，创建一个比例尺，将数据值作为输入，返回不同的颜色。这是等值区域地图的核心所在：

```
var color = d3.scale.quantize()
.range(["rgb(237,248,233)", "rgb(186,228,179)",
"rgb(116,196,118)", "rgb(49,163,84)","rgb(0,109,44)"]);
```


**添加定位点**

1、准备数据

2、加载
```
d3.csv("us-cities.csv", function(data) {
    // 加载完数据，执行一些操作
    svg.selectAll("circle")
    .data(data)
    .enter()
    .append("circle")
    .attr("cx", function(d) {
    return projection([d.lon, d.lat])[0];
    })

    .attr("cy", function(d) {
    return projection([d.lon, d.lat])[1];
    })
    .attr("r", 5)
    .style("fill", "yellow")
    .style("opacity", 0.75);
});
```

**取得和解析地图数据**


1、查找 shapefile 文件

所谓的shapefile，是在线地图和可视化流行之前的一种文件。这种文件包含着与现在的GeoJSON中几乎相同的数据。

2、选择解析度

下载之前，要确定数据的解析度（resolution）,所有shapefile都是矢量数据，因此解析度的意思不是像素，而是地理信息的详尽程序或粒度。

Natural Earth 的数据集分三种解析度，包括最详尽的和不怎么详尽的：
```
• 1:10 000 000
• 1:50 000 000
• 1:110 000 000
```
也就是说，在最高解析度的数据中，1 个单位对应现实世界中的1000 万个这样的单
位。或者反过来说，现实世界中的1000 万个单位会简化为1 个。因此，1000 万英
寸（254 公里）在这个数据中表示为1 英寸。


3、简化数据文件

Matt Bloch 开发的MapShaper（http://mapshaper.org/）是一个非常好用的简化数据
的工具。你可以上传shapefile 文件，然后拖动滑动条上的滑块来选择解析度。

4、转换为GeoJSON

如果没有合适的软件，那么这一步会麻烦一些。我们最终的目的是要使用一个叫
ogr2ogr 的终端命令，可以在Mac、Unix 和Windows 系统中使用。主要问题是
ogr2ogr 依赖一些框架、库之类的东西，不把它们都安装好，就没办法用。
关于安装这些依赖的细节，我们就不介绍了，但本节会告诉你大致怎么做。

首先，要下载Geospatial Data Abstraction Library，即GDAL（http://www.gdal.org/）。
这个程序包里包含ogr2ogr。

还要下载GEOS（http://trac.osgeo.org/geos/），即Geometry Engine, Open Source。
然后在Windows 或Unix/Linux 计算机中，下载源代码，然后输入好玩的build、
make，以及众多其他安装命令。

实际的安装命令我不记得了，但大致过程就是这样。（郑重地跟大家说一声，如果这
一步你过不了，可以参考O’Reilly 出版的相关图书，根据里面的介绍下载和安装这
种软件包。）

如果你使用的是Mac，那很可能已经安装了Xcode 和Homebrew。那么，只要在终
端中简单地输入brew install gdal，就行了。（如果这两个工具有一个你没安
装，建议安装上。这两个工具都是免费的，但安装可能得花点时间。Xcode 本身很
大，要从App Store 下载。安装了Xcode 之后，至少从理论讲，只要在终端里使用
一个简单的命令就能安装Homebrew 了。根据我的经验，可能要解决一些小问题才
能最终安装好。）

对于使用Mac 但没有安装Xcode 或Homebrew 用户来说，还可以选择一个预编译
的GUI 安装程序，这个程序会安装GDAL、GEOS 以及其他一些你不用知道是干
什么的工具。GDAL Complete 包的最新版地址在这里：http://www.kyngchaos.com/
software/frameworks。仔细看一看GDAL ReadMe 文件吧。安装后， 还不能在终
端窗口里使用ogr2ogr。还得把GDAL 程序放到壳程序的路径中。最简单的办法
是打开终端窗口，输入nano .bash_profile，然后把export PATH=/Library/
Frameworks/GDAL.framework/Programs:$PAT 粘贴进去， 再按Control-X 和
Control-y 保存，再输入exit 退出会话。打开一个新终端窗口，输入ogr2ogr 就能
看到它可以使用了。

无论你使用什么操作系统，安装了这些工具后，打开终端窗口，进入保存所有
shapefile 文件的文件夹（比如cd ~/ocean_shapes/），然后输入如下命令：
ogr2ogr -f "GeoJSON" output.json filename.shp
这是告诉ogr2ogr 取得扩展名为.shp 的filename 文件，把它转换成GeoJSON，然
后保存为名为output.json 的文件。

以我下载的海洋文件为例，使用ogr2ogr 的命令如下：
```
ogr2ogr -f "GeoJSON" output.json ne_110m_ocean.shp
```
输入这些命令，但愿你什么也看不到。

这就完了啊？！我知道，花几个小时间才弄好了命令行工具，你希望结尾怎么也得
辉煌一些吧，就像你在《超级马里奥兄弟3》里救下公主一样。（其实我始终没玩到
那一关，但我想象着那一刻肯定非常激动人心。）
可是没有，你最好乞求什么也不会发生。当然，同一个文件夹里最好还会多一个叫
output.json 的文件。这就是我得到的结果：
```
{
"type": "FeatureCollection",
"features": [ { "type": "Feature", "properties":
{ "scalerank": 0, "featurecla": "Ocean" },
"geometry": { "type": "Polygon", "coordinates":
[ [ [ 49.110290527343778, 41.28228759765625 ],
[ 48.584472656250085, 41.80889892578125 ],
[ 47.492492675781335, 42.9866943359375 ],
[ 47.590881347656278, 43.660278320312528 ],
[ 46.682128906250028, 44.609313964843807 ],
[ 47.675903320312585, 45.641479492187557 ],
[ 48.645507812500085, 45.806274414062557 ]
...
```
嘿，最后这个结果看起来很面熟啊！


## 第13章 导出文件

1、导出位图：截屏

2、导出PDF

PDF，即Portable Document Format（便携文档格式）的文档可以包含矢量图，包括
SVG 图形。因此，导出到PDF 可以迅速得到一个可伸缩的图表

3、导出SVG：复制SVG代码重新保存为SVG文件






