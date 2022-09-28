
### 在仓库A中移动文件B.pdf到文件夹C
```
git clone <Github HTTPs URL>
git pull origin main(master)
git mv B.pdf C
git add .
git commit -m <将文件B.pdf移动到C文件夹>
git push -u origin main(master) // 不建议使用 git push --force origin master
```

### 生成密码token
```
Settings  --->  Developer settings  --->  Personal access tokends  ---> Generate new token  --->  repo打对勾   --->  Generate token
```

### 其他命令
```
查看用户名  git config user.name
查看邮箱    git config user.email
查看密码   git config user.password
```

### 设置用户名、密码
```
git config user.name "freedom"
git config user.password "123456"
git config user.email "1548429568@qq.com"
# 全局配置
git config --global user.name <用户名>
git config --global user.password <密码>
git config --global user.email <邮箱>
```
