# 智译国传智能体技术文档

[在线阅读](https://wxyzi.github.io/zhiyiguochuan/) · [下载 PDF](https://wxyzi.github.io/zhiyiguochuan/pdf/zhiya-guochuan-agent.pdf) · [构建与发布状态](https://github.com/Wxyzi/zhiyiguochuan/actions)

这是“智译国传”中文科技新闻汉译英智能体的 DITA 技术文档项目，也是一套**为自己的智能体编写文档的示例**。你可以学习如何整理功能、写操作步骤、记录知识库与模型配置，并将文档发布成网页和 PDF。

智能体在扣子平台运行；Oxygen 编辑本地文档；Git 保存版本；GitHub Actions 构建文档；GitHub Pages 展示构建结果。更新本仓库不会自动修改扣子中的提示词、知识库或模型设置。

## 我应该从哪里开始

| 你的目标 | 阅读入口 |
| --- | --- |
| 使用“智译国传”完成一次翻译 | [快速开始](topics/t-quick-start.dita) |
| 学习为自己的智能体写文档 | [从零编写智能体技术文档](topics/t-write-agent-documentation.dita) |
| 查看各章节写什么、如何证明功能 | [智能体文档结构与填写模板](topics/r-agent-documentation-template.dita) |
| 直接创建自己的 DITA 文档集 | [最小示例地图](templates/agent-docs/agent.ditamap) |
| 在 Oxygen 中修改并检查文档 | [编辑、验证和发布](topics/t-author-and-validate-in-oxygen.dita) |
| 把修改同步到 GitHub 和 Pages | [同步与发布步骤](topics/t-sync-github-pages.dita) |

GitHub 上的 `.dita` 文件是 XML 源文件，排版后的阅读版本请从上方“在线阅读”进入。

## 如何为自己的智能体写文档

1. **整理事实**：记录名称、读者、任务、入口、实际功能和限制。用平台配置与运行记录核对；未验证的功能标为“待验证”。
2. **先写一次成功操作**：从准备输入、提交请求、查看结果写到保存成果。每步写明操作和可观察结果。
3. **拆分内容**：概念说明用 `concept`，操作步骤用 `task`，参数、格式和问题列表用 `reference`。每篇解决一个问题。
4. **补齐技术信息**：为提示词、知识库、模型和工具记录版本、用途及使用条件。知识库命中要有对应运行记录，挂载知识文件不等于模型训练。
5. **加入示例和问题处理**：标明真实材料来源或“教学示例”，说明预期结构、人工复核点以及输出不符时的处理方法。
6. **验证并维护**：让新用户照文档操作，修复遗漏；在 Oxygen 验证地图，预览网页和 PDF，再提交和发布。

建议先完成“概述、快速开始、输入输出、常见问题”四篇，再按实际需要扩展。完整步骤见[写作教程](topics/t-write-agent-documentation.dita)。

## 复用最小模板

`templates/agent-docs/` 包含四篇带填写提示的主题和一张地图，不依赖本项目的产品变量。

1. 将 `templates/agent-docs/` 整个文件夹复制到自己的新项目目录。
2. 在 Oxygen 中打开复制后根目录的 `agent.ditamap`，选择在 **DITA Maps Manager** 中管理。
3. 按 `topics/` 中的 `[填写...]` 提示补充实际内容，更新产品名、版本和示例。
4. 验证地图并生成 HTML5 或 PDF。

模板不会自动为新项目配置 Pages。本仓库的发布入口仍是 `maps/zhiya-guochuan-agent.ditamap`。

## 文件结构

```text
zhiya-guochuan-agent-doc/
  maps/
    zhiya-guochuan-agent.ditamap   # 主地图，组织阅读顺序、发布结构和关系表
    keys.ditamap                    # key 定义，统一管理产品名、平台名、输出部分名等变量
  topics/
    c-overview.dita                 # 智能体概述（含架构图）
    c-audience-and-scenarios.dita   # 目标用户和使用场景
    c-agent-persona-and-principles.dita  # 智能体定位与工作原则
    c-workflow-model.dita           # 六步工作流模型（含工作流图）
    c-documentation-model.dita      # 维护者说明：DITA 文档开发模型
    t-quick-start.dita              # 快速开始
    t-configure-profile.dita        # 配置翻译任务参数
    t-run-translation-workflow.dita # 运行翻译工作流
    t-review-and-export.dita        # 审校和导出结果
    t-author-and-validate-in-oxygen.dita  # 维护者说明：在 Oxygen 中编辑、验证和发布
    t-write-agent-documentation.dita     # 从零为自己的智能体写文档
    r-agent-documentation-template.dita  # 章节结构和填写模板
    t-sync-github-pages.dita             # 本地编辑后的同步与发布
    r-input-output-formats.dita     # 输入和输出格式
    r-configuration-reference.dita  # 配置项参考
    r-error-messages.dita           # 常见问题和处理方法
    r-response-format-and-rules.dita # 回复格式与质量规则（含输出结构图）
    r-style-guide.dita              # 写作风格规范
    r-quality-checklist.dita        # 文档发布前质量检查清单
    r-glossary.dita                 # 术语表
    common-reuse.dita               # 公共复用内容（conref 源，resource-only）
    images/
      agent-architecture.svg        # 智能体架构图
      workflow-six-steps.svg        # 六步工作流图
      output-five-parts.svg         # 五部分输出结构图
  styles/
    zh-cn-pdf.css                   # PDF Chemistry 中文字体定制
  templates/agent-docs/              # 可独立复制的最小 DITA 文档集
  scripts/prepare_site.py            # 整理目录、样式链接并检查站点本地引用
  ditaval/customer-release.ditaval   # 对外构建过滤规则
  .github/workflows/docs.yml         # 自动构建 HTML5/PDF 并部署 Pages
```

## 信息架构

本文档采用 DITA 三类型划分：

- **concept**（概念型）：说明「是什么」和「为什么」。
- **task**（任务型）：说明「怎么做」，按用户目标组织步骤。
- **reference**（参考型）：提供可查询的规则、表格、参数和清单。

主地图通过 `topichead` 分章节、`collection-type="sequence"` 标记有序任务流、`reltable` 建立「概念 ↔ 任务 ↔ 参考」三向关联，并在 WebHelp 中自动生成「相关主题」链接。`维护者说明` 章节面向文档维护者，用于说明 DITA 模型、Oxygen 编辑、验证和发布流程，不属于智能体终端用户的操作路径。

## 复用机制

- **conref（内容引用）**：`common-reuse.dita` 存放公共警告和规则段落（人工审校、事实核查、限定语保留、标题克制等），各 topic 通过 `conref` 引用，单源维护、改一处多处更新。
- **keyref（变量引用）**：`keys.ditamap` 定义产品名、平台名、输出部分名等 key，修改 key 定义即可全局生效，避免散落在各 topic 的硬编码变量。
- **conkeyref（基于 key 的内容引用）**：通过 key 和片段 id 定位复用文本。修改 key 影响文档引用，不会切换智能体实际运行模式。

## 在 Oxygen XML Editor 28.1 中打开

1. 在 Oxygen 中打开 `maps/zhiya-guochuan-agent.ditamap`，选择在 **DITA Maps Manager** 中打开。
2. 在地图树中双击需要修改的主题并保存；新增主题后要把引用加入地图。
3. 使用 `Validate and Check for Completeness` 检查完整性，修复无效 XML、断链和缺失资源。
4. 使用 `Configure Transformation Scenario(s)` 选择 HTML5、WebHelp 或 PDF 发布场景，再执行转换。WebHelp 和 Chemistry PDF 需要相应 Oxygen 组件。

本项目以 Oxygen 28.1 为写作环境，本机另使用 Oxygen 27 自带的 DITA-OT 验证。独立版、Eclipse 插件版和不同界面的菜单可能不同。创建主题与地图的官方说明见 [Oxygen 28.1 DITA 入门](https://www.oxygenxml.com/doc/versions/28.1/ug-editor/topics/eppo-first-dita-topic.html)。

中文界面中，重点查找以下功能名称：

- `DITA Maps Manager`：DITA 映射管理器。
- `Validate and Check for Completeness`：验证并检查完整性。
- `Configure Transformation Scenario(s)`：配置转换场景。
- `Apply Transformation Scenario(s)`：应用转换场景。

## 推荐编辑流程

1. 从 `maps/zhiya-guochuan-agent.ditamap` 打开整个文档集。
2. 先检查概念类 topic，确认产品定位、受众和工作流是否准确。
3. 再检查 task topic，确认步骤能否从快速开始走到配置、运行、审校和导出。
4. 最后检查 reference topic，确认格式、配置项、问题、回复规则和术语是否完整。
5. 如需维护 DITA 源文件，再检查 `维护者说明` 章节中的文档模型、Oxygen 操作和发布前质量清单。
6. 在发布前运行 `Validate and Check for Completeness`。
7. 发布 PDF 或 WebHelp 后，按照 `r-quality-checklist.dita` 逐项检查输出效果。

## 修改后同步到 GitHub 和 Pages

先保存并验证，在 PowerShell 中进入本地仓库：

```powershell
cd "C:\Users\Administrator\Desktop\codex project\zhiya-guochuan-agent-doc"
git status
git diff
```

按实际修改选择文件，以下示例提交地图和主题：

```powershell
git add -- maps topics
git diff --cached
git commit -m "docs: update agent documentation"
git push origin main
```

修改 README、模板、样式或工作流时，把相应路径加入 `git add --`。本地 `build/` 和生成的 PDF 不需要提交。如果提示远程有新提交，先 `git fetch origin` 并查看分支状态，保留本地修改并处理差异后再推送；不要强制覆盖远程历史。

推送后，打开 [Actions](https://github.com/Wxyzi/zhiyiguochuan/actions)，确认**对应新提交**的构建和部署成功，再查看[在线文档](https://wxyzi.github.io/zhiyiguochuan/)。页面未更新时按 `Ctrl + F5` 刷新。保存、提交、推送和在线发布是四个不同状态。完整排查见[同步与发布步骤](topics/t-sync-github-pages.dita)。

## GitHub Actions CI/CD

本仓库配置了 `.github/workflows/docs.yml`，用于实现 Docs-as-Code 流程：

- **CI**：相关文件推送到 `main`/`master`、收到拉取请求或手动运行时，检查主文档和起步模板的 XML，并构建两套 HTML5 验证引用。
- **构建**：使用 DITA-OT 4.2.4 生成主文档 HTML5 和中文 PDF，检查 PDF 字体及中文文本；构建产物 `zhiya-guochuan-agent-site` 保留 30 天。
- **CD**：主分支的推送或手动运行会部署 Pages；拉取请求只构建，不发布。

云端使用开源 DITA-OT HTML5 和 PDF/FOP 转换。本地精排 PDF 使用 Oxygen PDF Chemistry，两者排版可能不同。线上 PDF 入口是 `pdf/zhiya-guochuan-agent.pdf`。

对外构建应用 `ditaval/customer-release.ditaval`，排除 `audience="internal"` 内容。过滤只控制生成结果；公开仓库中的源文件仍可阅读。

## 命令行验证与发布

如果需要在 Oxygen 外部复现验证和发布流程，可以使用 Oxygen 自带的 Java 与 DITA-OT：

```powershell
$oxygenDir = 'C:\Program Files\Oxygen XML Editor 27'  # 改为实际安装目录
$env:JAVA_HOME = Join-Path $oxygenDir 'jre'
$env:PATH="$env:JAVA_HOME\bin;$env:PATH"
$dita = Join-Path $oxygenDir 'frameworks\dita\DITA-OT\bin\dita.bat'
& $dita validate -i 'maps\zhiya-guochuan-agent.ditamap' --outer.control=quiet
```

生成 PDF 时建议增加 `outer.control=quiet` 参数。当前主 map 位于 `maps` 目录，topic 位于同级 `topics` 目录，DITA-OT 会把这些 topic 识别为输入 map 目录之外的资源；该参数用于避免重复显示不影响发布结果的目录范围提示。

为了避免不同 Oxygen 版本对相对路径的解析差异，`--args.css` 使用原生绝对文件路径，不使用 `file:/` URI。沿用上方 `$dita` 变量，在仓库根目录执行：

```powershell
& $dita -i 'maps\zhiya-guochuan-agent.ditamap' -f pdf-css-html5 -o 'build\pdf-css-html5' --args.output.base='zhiya-guochuan-agent' --args.css="$PWD\styles\zh-cn-pdf.css" --filter='ditaval\customer-release.ditaval' --outer.control=quiet
```

> 注：上述命令需在 `zhiya-guochuan-agent-doc` 目录下运行，并按实际 Oxygen 安装路径调整。发布产物位于 `build/pdf-css-html5/zhiya-guochuan-agent.pdf`。
