# 数据类型
## 变量 Variable
- 不可变：Number, String, Tuple
- 可变：Bool, List, Set, Dictionary

### 布尔 Bool
True or False

|   and   | True | False |
| --- | --- | --- |
|True | True | False |
|False | False | False |

|   or   | True | False |
| --- | --- | --- |
|True | True | True |
|False | True | False |

|   not   | True | False |
| --- | --- | --- |
| | False | True |

### 数字 Number
> int, long, float, complex

- `//` **向下取整**：返回商的整数部分
```
365 // 10 # 36
5 // 3 # 1
-5 // 3 # -2
```

- 负数零取整 int()
```
int(-5//3) # -1
```

- `%` 取模 - 返回除法的余数
```
365 % 10 # 5  --> (365 - (365//10)*10 = 5)
5 % 3    # 2  --> (5 - (5//3)*3 = 2)
-5 % 3   # 1  --> (-5 - (-5//3)*3 = 1)
5 % -3   # -1 --> (5 - (5//-3)*(-3) = -1)
# 奇数
num % 2 != 0
# 偶数
num % 2 == 0

# 移位操作
nums % 2^n = nums & (2^n - 1)
nums % 2 = nums & 1
```

### 字符串 String

- f -> format
```
first_name = "Ross"
last_name = "MatNoble"
full_name = f"{first_name} {last_name}" # Ross MatNoble
```
- 特殊符号

|操作|说明|
|-|-|
| \ | 转义符|
|\n| 换行符|
|\t|制表符|

`r` 避免转义
`print(r"\\\t\\") # \\\t\\`

|操作|说明|
|-|-|
|.title()|首字母大写|
|.upper()|大写|
|.lower()|小写|
|.strip()|消除空格|

### 列表 List[]
|操作|说明|
|-|-|
|.insert(index, value)|增|
|.append(value)|增|
|.remove(value)|删|
|del list[index]|删|
|.pop()|删|

#### 直接赋值 & 浅拷贝(copy) & 深拷贝(deepcopy)

- **直接赋值**：其实就是对象的引用（别名）。
- **浅拷贝(copy)**：拷贝父对象，不会拷贝对象的内部的子对象。
- **深拷贝(deepcopy)**： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。

<img src="https://cdn.jsdelivr.net/gh/MatNoble/Images/copy.png" width="600"/>

```
import copy
a = [1, 2, 3, 4, ['a', 'b']] #原始对象
 
b = a                #赋值，传对象的引用
c = copy.copy(a)        #对象拷贝，浅拷贝
d = copy.deepcopy(a)    #对象拷贝，深拷贝
 
a.append(5)               #修改对象a
a[4].append('c')          #修改对象a中的['a', 'b']数组对象
 
print( 'a = ', a )
print( 'b = ', b )
print( 'c = ', c )
print( 'd = ', d )

>>> ('a = ', [1, 2, 3, 4, ['a', 'b', 'c'], 5])
>>> ('b = ', [1, 2, 3, 4, ['a', 'b', 'c'], 5])
>>> ('c = ', [1, 2, 3, 4, ['a', 'b', 'c']])
>>> ('d = ', [1, 2, 3, 4, ['a', 'b']])
```

#### 其他函数

|操作|说明|
|-|-|
|.sort()|排序|
|.reverse()|逆序|

### 元组 Tuple()

**不可修改**

### 字典 Dictionary{:}
`dict = {key1:value1, key2:value2, key3:value3}`

- 增
`dict['key'] = value`
- 删 
`del dict['key']`

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1TUA3v4K_zdZzSUjCtoO-0tbA_9sAvFQe?usp=sharing)

### 集合 Set{}

**唯一性**

|操作|说明|
|-|-|
|.add(value)|增|
|.update(value)|增, 列表、元组、字典|
|.remove(value)|删|
|.discard(value)|删，不报错|