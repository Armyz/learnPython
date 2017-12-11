# 1.git初始使用教程 

## 1.安装git
```shell
sudo apt-get install git-core
```

##2.进行ssh认证：
	a.终端执行：
```shell
ssh-keygen -C “your_email@example.com” -f ~/.ssh/github
```
	将会在～/.shh文件夹中生成两个文件github和github.pub，共钥和私钥。
	b.复制～/.ssh/github.pub中的内容，复制到自己的github账户上的
	Settings –> SSH and GPG keys –> New SSH key，填上适当的 Title，
	并复制github.pub 文件的内容粘贴在 Key 文本框里。
	c.在终端执行：
```shell
git -T git@github.com
```
输出Hi userNmae! You've successfully authenticated,
but GitHub does not provide shell access.

##3.保存github账号信息
```shell
git config --global user.name <userName>
git config --global user.email <your@email.com>
```
##4.在github账户上新建一个仓库
	如：https://github.com/userName/test.git

##5.在本地创建新的新的仓库
```shell
echo "#test" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/userName/test.git
git push -u origin master
```
##6.上传已经存在的仓库至github
 	切换到已存在仓库的目录下
```shell
git remote add origin https://github.com/userName/test.git
git push -u origin master
```

##7.登录不需要密码
	每次更新长传至仓库都需要输入用户名和密码，不用输入密码的步骤如下：
	a.终端执行：
```shell
git config --global credential.helper store
```
	b.上述命令会在.gitconfig文件中添加credential字段，
	下次上传输入密码后将会被记住，以后不用再输入密码
