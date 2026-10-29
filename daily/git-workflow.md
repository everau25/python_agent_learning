# Git 日常操作

在仓库目录中操作。开始前确认有没有昨天留下的未提交内容：

```powershell
git status
git pull --ff-only
```

完成总结、作业和练习后，检查本次改动再提交：

```powershell
git status
git diff
git add .
git diff --cached
git commit -m "study: record day XX"
git push
```

如果还有未完成或不属于本次学习的改动，不要整目录暂存；把 `git add` 后面的目录替换成具体文件路径。提交前确认没有 `.env`、密钥、私人数据、虚拟环境或 IDE 配置。
