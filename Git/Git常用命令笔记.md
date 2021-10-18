[TOC]

### 在仓库A中移动文件B.pdf到文件夹C
```
git clone <Github HTTPs URL>
git pull origin master
git mv B.pdf C
git add .
git commit -m <将文件B.pdf移动到C文件夹>
git push -u origin master
```

### 生成密码token
```
Settings  --->  Developer settings  --->  Personal access tokends  ---> Generate new token  --->  repo打对勾   --->  Generate token
```

### 其他命令
```
查看用户名  git config user.name
查看邮箱    git config user.email
```