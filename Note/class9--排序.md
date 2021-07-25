[TOC]

# Outline:

![image-20210724151916006](img/image-20210724151916006.png)

1. 基于比较的各类排序算法

- 基于比较的排序：通过比较大小来决定元素间的相对次序。可以证明这类排序算法的时间复杂度下届为O(log(N)) – 不可能更快了的
- 非比较类排序：本质就是不通过比较元素的大小来决定排列的顺序，而是通过？？？？ 因此时间复杂度受多种因素影响，不单取决于N元素数量N

2. 其它类型的排序算法，不同排序算法的适用场景



2. 第K大的数，中位数，逆序对等应用



# 排序

## 初级排序算法：选，插，冒

- 选择排序（Slelection Sort) – “该放那个数了？” ==》 每次扫描一遍序列，找到当前的min，然后放到新的序列末尾。 ==> 或者，为了省空间，你也可以不用开一个新的数组，就swap currnet index i 和当前的min

![image-20210724154334542](img/image-20210724154334542.png)

- 插入排序(Insertion Sort) – “这个数该放哪儿？” ==》 就有点像打扑克牌，你抽牌的时候，要考虑新的一张牌应该放哪儿呢？–》 平均时间复杂度为O(N^2), 因为每一张牌都需要查询 – O(N)，和插入 – O(N)

- 冒泡排序(Bubble Sort) – 思路就是不断循环扫描，每次查看相邻的元素，如果你序列了，就交换他们的位置。Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.  ==> 你如果从前往后扫描，那最大的元素就会被带到最后，打你如果从后往前扫描，那最小的元素就会被带到前面，思路都是一样的

  **Example:** 
  ==> **First Pass:** we are starting from first to the end, so by the end of first round, the largest element will be carry to the end. 最大的数就像泡泡一样，会带到最后一位
  ( **5** **1** 4 2 8 ) –> ( **1** **5** 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1. 
  ( 1 **5** **4** 2 8 ) –> ( 1 **4** **5** 2 8 ), Swap since 5 > 4 
  ( 1 4 **5** **2** 8 ) –> ( 1 4 **2** **5** 8 ), Swap since 5 > 2 
  ( 1 4 2 **5** **8** ) –> ( 1 4 2 **5** **8** ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.
  ==> **Second Pass:** The second largest element will be carry to the end
  ( **1** **4** 2 5 8 ) –> ( **1** **4** 2 5 8 ) 
  ( 1 **4** **2** 5 8 ) –> ( 1 **2** **4** 5 8 ), Swap since 4 > 2 
  ( 1 2 **4** **5** 8 ) –> ( 1 2 **4** **5** 8 ) 
  ( 1 2 4 **5** **8** ) –> ( 1 2 4 **5** **8** ) 
  Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one **whole** pass without **any** swap to know it is sorted.
  ==> **Third Pass:** 
  ( **1** **2** 4 5 8 ) –> ( **1** **2** 4 5 8 ) 
  ( 1 **2** **4** 5 8 ) –> ( 1 **2** **4** 5 8 ) 
  ( 1 2 **4** **5** 8 ) –> ( 1 2 **4** **5** 8 ) 
  ( 1 2 4 **5** **8** ) –> ( 1 2 4 **5** **8** ) 

  ```python
  # Python program for implementation of Bubble Sort
  def bubbleSort(arr):
      n = len(arr)
      # Traverse through all array elements
      for i in range(n):
          # Last i elements are already in place
          for j in range(0, n-i-1):
              # traverse the array from 0 to n-i-1
              # Swap if the element found is greater
              # than the next element
              if arr[j] > arr[j+1] :
                  arr[j], arr[j+1] = arr[j+1], arr[j]
   
  # Driver code to test above
  arr = [64, 34, 25, 12, 22, 11, 90]
  bubbleSort(arr)
  print ("Sorted array is:")
  for i in range(len(arr)):
      print ("%d" %arr[i]),
  ```

- Reference: GeeksforGeeks, Bubble Sort， https://www.geeksforgeeks.org/bubble-sort/

  

