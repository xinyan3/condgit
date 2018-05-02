这是我第一个git文件
git add README.MD后加入仓库
git commit -m "这里写注释"关联
//这里是第二次提交修改测试
git 笔记：
step1 git 仓库安装(sudo apt-get install git)
step2 git 仓库配置（git config --global user.name "xinyan3"
		    git confgi --global user.email "sky831202@gmail.com")
step3 git 仓库初始化（mkdir 目录
			cd 目录  git init（创建本目录为仓库empty git repository）
			以看到.git文件为创建成功）
step4 git 文件添加 （复制或者创建git仓库目录下的文件后 git add 文件名 完成文件添加
		  				       git commit -m "提交tags")
				$ git add file1.txt
				$ git add file2.txt file3.txt
				$ git commit -m "add 3 files.
			以上意思：可以多次add 一次commit+tags
step5 git 版本回退控制 git log 显示所有版本信息 --pretty=oneline（参数只显示一行版本号）
		       git reset --hard HEAD  最初版本
		       git reset --hard 版本号7位 
		       git reflog  显示所有版本变更命令
现在总结一下：

    HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令git reset --hard commit_id。

    穿梭前，用git log可以查看提交历史，以便确定要回退到哪个版本。

    要重返未来，用git reflog查看命令历史，以便确定要回到未来的哪个版本。

github关联

创建sshkey $ ssh-keygen -t rsa -C "youremail@example.com"
如果一切顺利的话，可以在用户主目录里找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件，这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以放心地告诉任何人。

第2步：登陆GitHub，打开“Account settings”，“SSH Keys”页面：

然后，点“Add SSH Key”，填上任意Title，在Key文本框里粘贴id_rsa.pub文件的内容：



现在的情景是，你已经在本地创建了一个Git仓库后，又想在GitHub创建一个Git仓库，并且让这两个仓库进行远程同步，这样，GitHub上的仓库既可以作为备份，又可以让其他人通过该仓库来协作，真是一举多得。

首先，登陆GitHub，然后，在右上角找到“Create a new repo”按钮，创建一个新的仓库：

名称最好很本地仓库根目录名称一样

git remote add origin git@github.com:xinyan3/condgit.git
然后绑定本地与远程仓库
git push -u origin master
最后push同步
以后只要 git push origin master




Git鼓励大量使用分支：

查看分支：git branch

创建分支：git branch <name>

切换分支：git checkout <name>

创建+切换分支：git checkout -b <name>

合并某分支到当前分支：git merge <name>

删除分支：git branch -d <name>


测试测试




		       

