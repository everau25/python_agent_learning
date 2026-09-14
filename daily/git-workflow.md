# 每日学习内容归档与 Git 提交流程

本文件规定如何把每天学习的 Python、大模型 API、Prompt、RAG 和 Agent 内容整理进本仓库。

## 1. 先确认仓库根目录

本仓库的实际根目录是：

~~~text
D:\learning\python-agent-learning
~~~

D:\learning 只是父目录，不能作为本项目的工作目录。判断当前目录是不是仓库根目录：

~~~powershell
Set-Location 'D:\learning\python-agent-learning'
git rev-parse --show-toplevel
git remote -v
~~~

应看到仓库根目录和下面的远程地址：

~~~text
https://github.com/greed5883/python-agent-learning.git
~~~

以后所有 Git 命令都从 D:\learning\python-agent-learning 执行。

## 2. Git 仓库里应该保存什么

Git 不是视频网盘。每天看完课程后，只保存自己整理出的、能够复查和验证的内容：

| 学习内容 | 放入仓库的位置 | 最低要求 |
| --- | --- | --- |
| 当天总结 | daily/dayXX-主题.md | 用自己的话写概念、代码、问题和结果 |
| 知识点实验 | notes/dayXX-主题/ | 每个实验能单独运行 |
| 完整项目 | projects/项目名/ | 有源码、README 和测试或手工验收 |
| 视频和文档来源 | 当天 Markdown 的“学习资料”部分 | 写链接、集数或章节，不下载视频 |
| 报错和解决方式 | 当天 Markdown 的“问题记录”部分 | 写现象、原因、排查和修复 |
| 周总结 | daily/weekXX-review.md | 总结掌握程度和下一周计划 |

不要提交这些内容：

- 课程视频、压缩包、PDF 原文件和重复截图；
- .venv、__pycache__、IDE 配置和日志；
- .env、API Key、密码、Cookie、Token；
- 真实联系人、真实业务数据和含隐私的聊天记录；
- 可以从依赖安装得到的大文件或本地模型。

## 3. 推荐目录和命名

保留现在的 daily、notes、projects 三个目录，并统一命名规则：

~~~text
python-agent-learning/
├── README.md                    # 仓库总说明和进度入口
├── roadmap.md                  # 六个月路线
├── daily/                      # 每日记录和周复盘
│   ├── README.md
│   ├── git-workflow.md
│   ├── day09-oop.md
│   └── week02-review.md
├── notes/                      # 知识点实验和专题笔记
│   ├── README.md
│   ├── day09-oop/
│   │   ├── 01-class-basics.py
│   │   └── 02-dataclass.py
│   └── day10-decorators/
└── projects/                   # 可独立运行的阶段项目
    ├── README.md
    └── week01-python-contacts/
~~~

命名规则只有三条：

1. 每天使用两位数字：day01、day09，不要混用 day1、Day09 和 第9天。
2. Markdown 和目录名使用小写英文加短横线：day09-oop.md、week01-python-contacts/。
3. Python 文件和函数遵循 Python 习惯，使用下划线：dataclass_demo.py、load_contacts()。

一个知识点固定归档三层：

~~~text
daily/day09-oop.md                         # 今天学了什么
notes/day09-oop/01-class-basics.py         # 能不能单独写出来
projects/week01-python-contacts/           # 能不能用于项目
~~~

不要把所有内容都塞进一个“学习笔记.md”，也不要把一个完整项目拆散到 daily 和 notes 的多个目录中。

## 4. 第 1～8 天的历史内容怎么补录

你已经完成第 1～8 天，可以补建这些每日记录：

~~~text
daily/day01-python-basics.md
daily/day02-containers.md
daily/day03-functions.md
daily/day04-files-exceptions.md
daily/day05-ollama-api.md
daily/day06-streamlit.md
daily/day07-review.md
daily/day08-mini-project.md
~~~

补录时只写你确实学过或重新验证过的内容。记不清的地方写“回溯时未独立复现”，不要编造视频集数、运行结果或掌握程度。

历史内容建议一次性提交：

~~~powershell
Set-Location 'D:\learning\python-agent-learning'
git status
git add daily notes projects
git diff --cached --stat
git diff --cached
git commit -m 'docs: archive learning progress from day01 to day08'
git push origin main
~~~

从第 9 天开始，每天单独提交，便于回看学习曲线。

## 5. 每天开始前的操作

每天打开电脑后先执行：

~~~powershell
Set-Location 'D:\learning\python-agent-learning'
git status
git log --oneline --max-count=5
git pull --ff-only
~~~

解释：

- git status：查看昨天是否有未提交修改；
- git log：回顾最近完成了什么；
- git pull --ff-only：从 GitHub 获取自己的最新版本，不自动制造复杂合并。

如果 git status 显示有未提交内容，先执行 git diff 看清楚。不要直接 git pull，也不要删除这些文件。若确认是昨天留下的半成品，继续完成后再提交。

## 6. 看视频时如何转成仓库内容

不要一边播放一边复制字幕。每看 20～30 分钟，暂停并完成下面四步：

1. 用一句话写出这个概念解决的问题。
2. 合上视频，用自己的话写三条结论。
3. 把教程例子改成不同题材，再敲一遍代码。
4. 运行代码，保存真实输出或测试结果。

例如今天学 class，不要只写“类是对象的模板”。应当写：

~~~text
我用 Book 类保存书名和价格。创建对象时 __init__ 给实例设置属性，
summary() 读取实例属性返回简介。教程中的例子我改成了图书，代码见
notes/day09-oop/01-class-basics.py。
~~~

视频和文档只记录来源，不把视频文件放入仓库：

~~~markdown
## 学习资料

- 主视频：黑马程序员 Python 语言进阶，观看 P6～P10、P14～P15
- 官方文档：Python 类，阅读 9.1～9.5
~~~

## 7. 每日记录模板

每天复制这个模板，新建 daily/dayXX-主题.md：

~~~~markdown
# Day XX：主题名称

- 日期：2026-09-XX
- 学习时长：X 小时
- 主视频：名称、链接、集数或时间范围
- 补充文档：名称、链接、章节
- 对应项目：projects/项目目录/

## 今天要解决的问题

我今天要解决的具体问题是什么？不要写“学习 Python”。

## 核心知识

### 概念一

用自己的话解释：它解决什么问题，什么时候使用。

### 概念二

写一个最小例子，以及一个容易犯错的地方。

## 我写的代码

- 文件：notes/dayXX-主题/文件名.py
- 运行命令：python notes/dayXX-主题/文件名.py
- 运行结果：写真实结果，不写“运行成功”四个字带过。

## 项目改动

- 新增或修改了哪个文件？
- 新增了什么功能？
- 为什么这样设计？

## 验收结果

- [ ] 示例代码可以运行
- [ ] 项目正常场景通过
- [ ] 至少一个边界场景通过
- [ ] 测试通过，或已记录手工验收结果

测试命令和结果：

~~~text
python -m pytest -q
X passed
~~~

## 问题记录

- 现象：
- 完整报错最后一行：
- 我的判断：
- 我做的排查：
- 根本原因：
- 最终修复：

## 明天第一步

写一个明天打开电脑后马上执行的动作，例如“先为重复电话号码写失败测试”。
~~~~

## 8. 第 9 天完整示例

第 9 天主题是面向对象。目录和文件如下：

~~~text
daily/day09-oop.md
notes/day09-oop/01-class-basics.py
notes/day09-oop/02-dataclass.py
projects/week01-python-contacts/contacts/models.py
projects/week01-python-contacts/tests/test_models.py
~~~

### 8.1 先写知识点实验

notes/day09-oop/01-class-basics.py 可以写一个和教程不同的 Book 类：

~~~python
class Book:
    def __init__(self, title: str, price: float) -> None:
        self.title = title
        self.price = price

    def summary(self) -> str:
        return f'{self.title}: {self.price:.2f} 元'


book = Book('Python 入门', 49.9)
print(book.summary())
~~~

从仓库根目录运行：

~~~powershell
Set-Location 'D:\learning\python-agent-learning'
python notes/day09-oop/01-class-basics.py
~~~

然后在 02-dataclass.py 中练习 @dataclass，并把每个实验的实际输出写入当天笔记。

### 8.2 再把知识接入项目

项目里的 Contact 模型负责表示联系人，不能把所有逻辑继续堆在 main.py：

~~~python
from dataclasses import asdict, dataclass


@dataclass(slots=True)
class Contact:
    name: str
    phone: str
    email: str = ''

    def to_dict(self) -> dict[str, str]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> 'Contact':
        return cls(**data)
~~~

对应测试至少包括一个正常对象和一个无效对象：

~~~python
import pytest

from contacts.models import Contact


def test_contact_can_convert_to_dict() -> None:
    contact = Contact('张三', '13800000000', 'zhang@example.com')

    assert contact.to_dict() == {
        'name': '张三',
        'phone': '13800000000',
        'email': 'zhang@example.com',
    }


def test_empty_name_is_rejected() -> None:
    with pytest.raises(ValueError):
        Contact('', '13800000000')
~~~

你需要把项目中其他模块的字典访问改为对象属性访问，例如把 contact['name'] 改成 contact.name。存储 JSON 时再使用 to_dict()，读取 JSON 后使用 from_dict()。

### 8.3 第 9 天提交

下面命令假设项目使用仓库根目录的 .venv；如果你的虚拟环境位置不同，只调整激活命令：

~~~powershell
Set-Location 'D:\learning\python-agent-learning'
.venv\Scripts\Activate.ps1
python -m pytest -q projects/week01-python-contacts/tests
git diff --check
git status
git add daily/day09-oop.md notes/day09-oop projects/week01-python-contacts
git diff --cached --stat
git diff --cached
git commit -m 'day09: learn classes and convert contact model'
git push origin main
git status
~~~

这次提交表达的是“第 9 天学会类，并把联系人模型改成对象”，比“今天学习”“修改代码”更有用。

## 9. 提交信息命名

统一格式：

~~~text
<类型>: <dayXX 或模块> <完成的事情>
~~~

| 类型 | 使用场景 | 示例 |
| --- | --- | --- |
| learn | 知识点示例 | learn: practice generators |
| feat | 新功能 | feat: add json contact storage |
| test | 测试 | test: cover invalid phone numbers |
| docs | 笔记、README、路线 | docs: record day09 oop notes |
| refactor | 不改变功能的重构 | refactor: split cli and service layers |
| fix | 修复错误 | fix: handle corrupted contact json |
| chore | 依赖和仓库配置 | chore: add pytest dependency |

一天可以有多个小提交：

~~~text
learn: add class basics example
feat: introduce Contact dataclass
test: cover Contact serialization
docs: record day09 oop notes
~~~

不要使用 update、final、修改一下、今天学习这种无法检索的名称。

## 10. 每天结束的固定检查

~~~powershell
Set-Location 'D:\learning\python-agent-learning'
python -m pytest -q
git diff --check
git status
git log --oneline --max-count=3
~~~

确认以下内容后再提交：

- 当天笔记文件是 daily/dayXX-主题.md；
- 至少有一个示例或项目功能实际运行过；
- 有正常输入和边界输入的验收结果；
- 测试通过，或笔记中记录了手工验收；
- 没有 .env、Key、Token、真实数据、日志和虚拟环境；
- 提交信息能说明完成了什么；
- 最后执行 git push origin main，并再次查看 git status。

## 11. 常见 Git 操作

### 误把文件放进暂存区

还没有 commit 时，取消暂存但保留文件：

~~~powershell
git restore --staged .
git status
~~~

然后按文件路径重新 git add。

### 查看某一天的变化

~~~powershell
git log --oneline --all
git show --stat <commit-id>
git show <commit-id>
~~~

### 暂存区没问题，但想再确认一次

~~~powershell
git diff --cached
~~~

只要看到密钥、私人文件或与当天无关的大量变化，就先停止提交。

### 错误已经推送到 GitHub

如果推送了 API Key、密码或 Token，先到对应平台撤销或轮换它，再从仓库删除文件并提交修复。仅仅删除当前文件不能让已经暴露的密钥失效。

## 12. 每周复盘

每 7 天新建 daily/weekXX-review.md，回答：

1. 哪三个知识点可以不看资料写出来？
2. 哪个知识点只能照抄，还不能独立实现？
3. 本周最典型的一个报错是什么，根因是什么？
4. 本周项目新增了哪些可演示功能？
5. 测试数量和通过情况是什么？
6. 下周第一个要补的薄弱点是什么？

这样 Git 历史就不只是代码备份，而是你的学习证据：能看到每天学了什么、何时开始独立编程、哪些问题反复出现，以及项目能力怎样逐步增加。
