# algorithm头文件下的常用函数
> 常用函数有以下几种：
> - 
> - **`max(x,y)`** **求两个数之中较大的那个**
> - **`min(x,y)`** **求两个数中较小的那个**
> - **`abs(x)`** **返回一个整数的绝对值**
> - **`swap(x,y)`** **交换两个变量的值**
> - **reverse(it,it2)** **reverse(it,it2)  可以将数组指针之间的元素进行反转。**
> - **`next-permutation()`** **给出一个序列在全排列下的下一个序列**

```C
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int arr[5] = {1,2,3,4,5};
    do{
        printf("%d %d %d\n",arr[0],arr[1],arr[2]);
    }while(next_permutation(arr,arr+3)); //将数组前三位赋值成了全排列中的下一列
    return 0 ;
}
```
> 输出结果为：
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1


> - **`fill()`** **可以把数组或容器中的某一段区域赋为一个相同的值**

```C
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int arr[5];
    fill(arr,arr+5,250); //将所有值都赋为250
    for(int i = 0;i < 5;i++){
        printf("%d\n",arr[i]);
    }
}
```
> 输出结果为：
> 250
250
250
250
250

> - **`sort()`** **给一个数组继续排序**
> - **`lower_bound(frist,last,val)`** **用来寻找在数组或容器[frist,last)范围内第一个值大于等于** **val** **的元素的位置**
> - **`upper_bound(frist,last,val)`** **用来寻找在数组或容器[frist,last)范围内第一个值大于** **val** **的元素的位置**


