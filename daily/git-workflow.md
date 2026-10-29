# 每日学习操作手册

仓库位置：

```powershell
Set-Location D:\learning\python_agent_learning
```

每天按下面的顺序操作即可。

## 1. 开始学习前

先确认仓库状态，并获取 GitHub 上自己的最新内容：

```powershell
git status
git pull --ff-only
```

如果 `git status` 显示有昨天留下的修改，先看清楚这些修改，再继续学习。

## 2. 写当天总结

正式课程日使用：

```text
daily/YYYY-MM-DD-DayXX.md
```

例如：

```text
daily/2026-10-30-Day04.md
```

自习日单独使用：

```text
daily/2026-10-30-自习日.md
```

新建总结时，可以复制模板：

```powershell
Copy-Item daily/daily-template.md daily/2026-10-30-Day04.md
```

当天总结填写四部分：

```text
今天学了什么
我实际写了什么
遇到的问题
明天继续
```

自习日可以记录预习、补作业、复习、环境配置、服务器操作或 GitHub 学习。

## 3. 保存作业和练习

老师布置的课程作业放在：

```text
Assignments/day_XX_work/
```

自己额外写的练习放在：

```text
practice/day_XX/
```

例如 Day04：

```text
Assignments/day_04_work/
practice/day_04/
```

作业和练习至少运行一次，把运行结果、报错和解决方法写入当天总结。

## 4. 更新每日记录列表

在 [`daily/README.md`](README.md) 中增加当天记录的链接，例如：

```markdown
- [2026-10-30-Day04](2026-10-30-Day04.md)：今天的主题
```

## 5. 学习结束前检查

```powershell
git status
git diff --check
git diff
```

确认改动内容正确，并确认没有把密钥、个人隐私、虚拟环境或无关文件放进提交。

## 6. 提交并推送

```powershell
git add daily Assignments practice
git diff --cached
git commit -m "study: record day04"
git push
```

如果当天是自习日，提交信息可以写成：

```powershell
git commit -m "study: record self-study 2026-10-30"
git push
```

## 每天记住这几件事

```text
总结放 daily
作业放 Assignments
练习放 practice
代码运行一次
问题写进总结
检查 Git
提交并推送
```

`notes/` 和 `projects/` 暂时不用操作。只有开始整理独立专题或完整项目时，才使用这两个目录。
