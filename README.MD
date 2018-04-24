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



		       

