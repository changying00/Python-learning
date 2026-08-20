# GitHub 本地配置与双机协作指南

适用仓库：`git@github.com:changying00/Python-learning.git`  
方式：SSH + Git + PyCharm

---

## 一、目标说明

- 在**自己的电脑**上配置 Git，通过 SSH 连接 GitHub
- 在 **PyCharm** 里拉取、修改、提交、上传项目
- 在**两台电脑**（例如机房电脑 + 自己电脑）上协作更新同一个项目

**核心原则：**

1. 换电脑前：当前电脑先 **Push（上传）**
2. 到另一台后：先 **Update / Pull（拉最新）**，再改代码
3. 两台都使用同一个仓库地址

---

## 二、本机已完成的检查（参考）

| 项目 | 状态说明 |
|------|----------|
| Git | 已安装（如 `git version 2.54.0`） |
| SSH 密钥 | 需生成并加入 GitHub |
| SSH 测试 | 成功时显示：`Hi changying00! You've successfully authenticated...` |

---

## 三、配置 Git 身份（必做）

在 **PowerShell** 或 **PyCharm 终端** 中执行（邮箱换成你的 GitHub 邮箱）：

```powershell
git config --global user.name "changying00"
git config --global user.email "2541104422@gamil.com"
```

检查是否生效：

```powershell
git config --global --list
```

---

## 四、配置 SSH（连接 GitHub）

### 4.1 生成 SSH 密钥

```powershell
ssh-keygen -t ed25519 -C "2541104422@gamil.com"
```

操作说明：

- 提示保存路径 → **直接回车**（默认：`C:\Users\你的用户名\.ssh\id_ed25519`）
- 提示 passphrase → 可直接回车（不设密码），或设一个自己记得住的

### 4.2 启动 ssh-agent 并添加密钥

```powershell
Get-Service ssh-agent | Set-Service -StartupType Manual
Start-Service ssh-agent
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

### 4.3 复制公钥内容

```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub
```

复制整行内容（以 `ssh-ed25519` 开头）。

### 4.4 把公钥加到 GitHub

1. 打开：https://github.com/settings/keys
2. 点击 **New SSH key**
3. **Title**：随便写，例如 `家里电脑` / `自己电脑`
4. **Key**：粘贴刚才复制的公钥
5. 点击 **Add SSH key**

### 4.5 测试 SSH 是否连通

```powershell
ssh -T git@github.com
```

#### 第一次连接时的提示

若出现：

```text
The authenticity of host 'github.com ...' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

输入：

```text
yes
```

然后回车。这是**第一次连接 GitHub 的正常提示**，确认后会加入本机信任列表。

#### 成功标志

```text
Hi changying00! You've successfully authenticated, but GitHub does not provide shell access.
```

看到上面这句就说明 **SSH 配置成功**。

---

## 五、在 PyCharm 中管理项目

### 5.1 方式 A：重新克隆（推荐，干净）

1. 打开 **PyCharm**
2. **File → New → Project from Version Control**  
   （或 Welcome 界面的 **Get from VCS**）
3. URL 填写：

```text
git@github.com:changying00/Python-learning.git
```

4. Directory 选择存放路径，例如：

```text
C:\Users\Administrator\Desktop\Python-learning
```

5. 点击 **Clone**
6. 克隆完成后，用这个目录作为项目根目录

### 5.2 方式 B：使用本机已有文件夹（如 `Python-learning-main`）

1. **File → Open** → 选择已有项目目录
2. 打开底部 **Terminal**，检查远程仓库：

```powershell
git remote -v
```

3. 如果没有 remote，添加：

```powershell
git remote add origin git@github.com:changying00/Python-learning.git
```

4. 如果已有 origin 但地址不对，修改为：

```powershell
git remote set-url origin git@github.com:changying00/Python-learning.git
```

5. 拉取最新代码：

```powershell
git pull origin main
```

> 若默认分支是 `master`，把上面的 `main` 改成 `master`。

---

## 六、日常操作：拉最新 / 提交 / 上传

### 6.1 改代码前：Update（更新项目 = 拉最新）

**作用：** 从 GitHub 把最新代码拉到本机，避免和另一台电脑的改动冲突。

在 PyCharm 中任选一种方式：

| 方式 | 操作 |
|------|------|
| 快捷键 | `Ctrl + T` |
| 菜单 | **Git → Update Project...** |
| 工具栏 | 右上角 **向下箭头 ⬇**（Update Project） |

弹出窗口一般保持默认，点 **OK** 即可。

**一句话：Update Project = 从 GitHub 拉最新 = 更新本地项目。**

### 6.2 改完后：Commit and Push（提交并上传）

| 操作 | 含义 |
|------|------|
| **Commit** | 在本机“拍快照”，记录这次改了什么（需写一句说明） |
| **Push** | 把快照上传到 GitHub，另一台电脑才能拉到 |
| **Commit and Push** | 提交 + 上传一次完成 |

图形界面：

1. 左侧查看改过的文件，勾选要提交的内容
2. 填写 commit 说明（例如：`完成第3章练习`）
3. 点击 **Commit and Push**  
   或：**Git → Push**（快捷键 `Ctrl + Shift + K`）

终端命令等价写法：

```powershell
git pull
git add .
git commit -m "说明这次改了什么"
git push
```

### 6.3 推荐日常流程

```text
打开项目 → Update（拉最新）→ 改代码 → Commit and Push（上传）
```

---

## 七、两台电脑如何同时维护同一个项目

### 7.1 基本规则

| 步骤 | 做什么 |
|------|--------|
| 1 | 两台电脑都配置好 Git + SSH，并克隆**同一个仓库** |
| 2 | 在 A 电脑改完 → **Commit and Push** |
| 3 | 到 B 电脑 → 先 **Update / Pull** → 再改 → 再 **Push** |
| 4 | 再回 A 电脑 → 同样先 **Update**，再继续改 |

### 7.2 仓库地址（两台统一使用）

```text
git@github.com:changying00/Python-learning.git
```

### 7.3 注意避免冲突

- **不要**两台同时改同一文件却都不先拉最新
- 换电脑前务必 **Push**
- 到另一台务必先 **Update**
- 若出现冲突，PyCharm 会提示，按提示选择保留哪边的修改或手动合并后再提交

### 7.4 示意图

```text
机房电脑                          自己电脑
   |                                 |
 改代码                             先 Update
   |                                 |
 Commit + Push  ──上传到 GitHub──►  再改代码
   |                                 |
 先 Update  ◄──从 GitHub 拉取──    Commit + Push
   |                                 |
 继续改...                          继续改...
```

---

## 八、常用命令速查

| 目的 | 命令 |
|------|------|
| 配置用户名 | `git config --global user.name "名字"` |
| 配置邮箱 | `git config --global user.email "邮箱"` |
| 测试 SSH | `ssh -T git@github.com` |
| 克隆项目 | `git clone git@github.com:changying00/Python-learning.git` |
| 拉最新 | `git pull` |
| 查看改动 | `git status` |
| 添加改动 | `git add .` |
| 提交 | `git commit -m "说明"` |
| 上传 | `git push` |
| 查看远程地址 | `git remote -v` |
| 设置远程地址 | `git remote set-url origin git@github.com:changying00/Python-learning.git` |

---

## 九、PyCharm 操作对照表

| 你想做的事 | PyCharm 操作 | 相当于命令 |
|------------|--------------|------------|
| 拉最新 / 更新项目 | `Ctrl + T` 或 Git → Update Project | `git pull` |
| 提交 | 勾选文件 → 写说明 → Commit | `git commit` |
| 上传 | Commit and Push 或 Git → Push | `git push` |
| 提交并上传 | Commit and Push | `git commit` + `git push` |

---

## 十、配置检查清单

按顺序勾选：

- [ ] 已安装 Git
- [ ] 已设置 `user.name` 和 `user.email`
- [ ] 已生成 SSH 密钥（`id_ed25519` / `id_ed25519.pub`）
- [ ] 公钥已添加到 GitHub（Settings → SSH and GPG keys）
- [ ] `ssh -T git@github.com` 显示 `Hi changying00!`
- [ ] 已在 PyCharm 中克隆或正确关联远程仓库
- [ ] 会使用 Update（拉最新）和 Commit and Push（上传）
- [ ] 两台电脑都按「先 Push，到另一台先 Update」的规则操作

---

## 十一、常见问题

### Q1：Update 是不是就是更新项目？

是。**Update Project = 从 GitHub 拉最新代码到本机 = 更新本地项目。**

### Q2：第一次 `ssh -T` 问 yes/no 怎么办？

输入 `yes` 回车即可，属于正常安全确认。

### Q3：两台电脑怎么不打架？

始终：**离开前 Push，到达后先 Update，再改代码。**

### Q4：Push 失败 / 没权限？

- 再测一次：`ssh -T git@github.com`
- 确认公钥已加到 **当前登录的 GitHub 账号**
- 确认远程地址是：`git@github.com:changying00/Python-learning.git`

### Q5：分支是 main 还是 master？

在项目目录执行：

```powershell
git branch
```

看当前分支名；`git pull` / `git push` 时与之一致即可。

---

## 十二、一句话总结

1. **SSH 配好** → 本机能安全连上 GitHub  
2. **PyCharm 克隆同一仓库** → 本地有项目  
3. **改前 Update，改后 Commit and Push** → 两台电脑同步同一项目  

仓库地址：

```text
git@github.com:changying00/Python-learning.git
```
