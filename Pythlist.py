### 两个列表随机同步打乱顺序
```python
import random

aa = [1, 2, 3, 4, 5, 6]
bb = [1, 2, 3, 4, 5, 6]

cc = list(zip(aa, bb))
random.shuffle(cc)
aa[:], bb[:] = zip(*cc)
print(aa, bb)
# 输出为：[1, 3, 5, 2, 4, 6] [1, 3, 5, 2, 4, 6]

```
