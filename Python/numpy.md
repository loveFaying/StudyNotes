### python中实现matlab左除右除

- **以下A的行和B的行相等**
- 左除（\）：如果Ax=B，则x=A\B，称为左除
```
x = np.dot(np.linalg.inv(A), B)
x = np.linalg.solve(A, B)
```
- 右除（/）：如果xA=B，则x=B/A，称为右除
```
x = np.dot(np.linalg.pinv(A),B)
x = np.linalg.lstsq(A, B, rcond=None)[0]
```



