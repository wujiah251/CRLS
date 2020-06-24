第8章习题答案
=
#### 8.1-1 比较排序算法的**决策树**，叶节点可能的最小深度是？  
n-1  

#### 8.2-1 记数排序在A=⟨6,0,2,0,1,3,4,6,1,3,2⟩的过程  
操作过程见下图：  
![](https://github.com/zhuxiuwei/CLRS/blob/master/Images/8.2-1.jpg)  

#### 8.2-2 证明记数排序是稳定的。  
以8.2-1为例，任何出现两次的数，都是先把在A中靠后的数，放在B中也相对靠后的位置。  
例如B数组的第一次赋值2，是把A[11]赋值给B[6]。后来，在第(i)次赋值的2的时候，是把A[3]赋值给B[5]，**两次的2，在A、B中相对位置不变**。  

#### 8.2-3 把第10行循环改成* for j = 1 to A.length *，算法依然正确，但是还稳定吗？  
不稳定。举一个反例，依然用8.2-1的例子。第一次赋值，A[1]=6, c[6]=11，故把B[11]赋值成A[1]=6。  
而对于6这个出现2次数，如果想保持稳定，**应该把A[8]=6赋值给B[11]，A[1]=6赋值给B[10]**。  
依据以上反例，不稳定.  

#### 8.2-4 Describe an algorithm that, given n integers in the range 0 to k, preprocesses its input and then answers any query about how many of the n integers fall into a range [a..b] in O(1) time. Your algorithm should use Θ(n+k) preprocessing time.  
代码见[CountNumberInRange](https://github.com/zhuxiuwei/CLRS/blob/master/src/chap08_SortInLinerTime/CountNumberInRange.java)。  

#### 8.3-2 下面哪些排序算法是稳定的？给出一个能使任何排序算法都稳定的方法，这个方法的时间和空间开销是？  
稳定：插入排序 归并排序  
不稳定：堆排序 快速排序  
[方法](http://clrs.skanev.com/08/03/02.html)：We can make any algorithm stable by mapping the array to an array of pairs, where the first element in each pair is the original element and the second is its index. Then we sort lexicographically. This scheme takes additional   

#### 8.3-4 如何在O(n)时间内，对0到n^3-1区间内的n个整数进行排序？  
就是采用基数排序。设n^3-1的位数是d，按照d/3划分一组。每组内正好可以进行记数排序。总体进行基数排序。时间复杂度是O(d/3*n)=O(d*n)=O(n)  

#### 8.4-1 桶排序在A=⟨.79,.13,.16,.64,.39,.20,.89,.53,.71,.42⟩.过程  
操作过程见下图：  
![](https://github.com/zhuxiuwei/CLRS/blob/master/Images/8.4-1.png)  

### -------- 思考题 ----------  
#### 8-2 数组n个元素，都是0或1。对这样的数组排序算法可能有以下三种特性的一部分：  
1. 时间复杂度O(n)。   
2. 算法是稳定的。  
3. 算法是原地排序。除了输入数组外，算法只需要固定的额外存储空间。  
a.给出满足1,2的算法。  
代码见[SortArrayOfZeroOne](https://github.com/zhuxiuwei/CLRS/blob/master/src/chap08_SortInLinerTime/SortArrayOfZeroOne.java)的sortA  
b 给出满足1,3的算法。  
代码见[SortArrayOfZeroOne](https://github.com/zhuxiuwei/CLRS/blob/master/src/chap08_SortInLinerTime/SortArrayOfZeroOne.java)的sortB   
c.给出满足2,3的算法。  
代码见[SortArrayOfZeroOne](https://github.com/zhuxiuwei/CLRS/blob/master/src/chap08_SortInLinerTime/SortArrayOfZeroOne.java)的sortC  
d. 上面的算法，那个能用到基数排序中？  
算法a可以，即稳定又是O(n)的。bc不行，一个不稳定，一个不是O(n)  
e. 就地排序的counting sort。你的算法是稳定的吗？  
代码见[CountingSort](https://github.com/zhuxiuwei/CLRS/blob/master/src/chap08_SortInLinerTime/CountingSort.java)的sort_in_place方法。不稳定。  

#### 8-3 变长数据项的排序  
a. 给一个整数数组，不同整数包含的数字位数可能不同，但是所有整数总共的位数是n，设计算法在O(n)排序。  
代码见[ChangebleLengthDataSort](https://github.com/zhuxiuwei/CLRS/blob/master/src/chap08_SortInLinerTime/ChangebleLengthDataSort.java)的sortIntArray  

#### 8-4 红蓝水壶配对儿  
其实本质是基于比较的排序问题。  
a. 两层循环依次遍历，代码略。  
b. 和证明基于比较的排序比较次数下界，估计是一个套路。（决策树）  
c. 没什么思路。知道应该用快速排序类似的思想。笨办法是，用Map记录红罐的初始位置，然后用快速排序随机版排序红罐（O(nlgn)），
然后对蓝罐的数，依次从红罐进行二分查找，查找总的时间复杂度是nO(lgN)=O(nlgn)，在红罐里找到后，在从Map里O(1)红罐原始位置，和蓝罐当前位置即可配对。
排序和查找加起来2个O(nlgn)，还是O(nlgn)。 只是这个方法比较蠢。  
