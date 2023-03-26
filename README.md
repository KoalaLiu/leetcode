# leetcode

## 第一次刷
跟随教程：https://www.bilibili.com/video/BV1sy4y1q79M

1. 数组: 
485, 283, 27

2. 链表: 
203, 206

3. 队列
933, 239

4. 堆栈
20, 496

5. Hash
217, 389, 496

6. Set
217, 705

7. Tree
144, 94, 145



## 刷题心得
### 1. 链表心得
1. 多用头节点(dummyHead)
2. 多利用快慢指针，一般 slow -> fast 2个快慢指针，可以完成3个node的操作
2.1 用快慢指针的时候，提前设置好指针的相对位置。可以有效的减少循环时特殊情况的判断。例如
``` python
# head为链表第一个node
dummyHead = ListNode()  # 链表虚拟头结点
dummyHead.next = head

# 提前设置好 slow、fast的相对位置
slow = dummyHead
fast = slow.next # == head
```
3. 注意问题转化，很多问题都可以转化为操作2、3个node
4. 想好边界条件
4.1 例如1：什么时候退出循环
   - head is None 和 head.next is None，退出循环后head的位置不同，循环次数不同
``` python
while head is not None:
    head = head.next
    
while head.next is not None:
    head = head.next
```

### 2. 二叉树心得
1. 前中后序遍历模板
``` python
if root is None:
    return []

res = []
stack = deque()

stack.append(root)
while stack:
    top = stack.pop()
    if top:
        # 前序: 遍历方式，中左右 -> 对应stack进栈顺序: 右左中
        if top.right:
            stack.append(top.right)
        if top.left:
            stack.append(top.left)
        stack.append(top)
        stack.append(None)

        # 中序: 遍历方式，左中右 -> 对应stack进栈顺序: 右中左
        if top.right:
            stack.append(top.right)
        stack.append(top)
        stack.append(None)
        if top.left:
            stack.append(top.left)

        # 后序：遍历方式，左右中 -> 对应stack进栈顺序：中右左
        stack.append(top)
        stack.append(None)
        if top.right:
            stack.append(top.right)
        if top.left:
            stack.append(top.left)

    else:
        top = stack.pop()
        res.append(top.val)

return res
```
