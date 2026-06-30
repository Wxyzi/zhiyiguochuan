# 智译国传智能体技术文档

本文件夹是一套可在 Oxygen XML Editor 28.1 中打开、编辑、验证和发布的 DITA 技术文档，描述运行在扣子（coze.cn）平台上的「智译国传」中文科技新闻英译智能体。

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

## 在 Oxygen XML Editor 28.1 中打开

1. 打开 Oxygen XML Editor 28.1。
2. 选择 `Window > Open Perspective > DITA`。
3. 打开 `Window > Show View > DITA Maps Manager`。
4. 在 DITA Maps Manager 中打开 `maps/zhiya-guochuan-agent.ditamap`。
5. 使用 DITA Maps Manager 工具栏中的 `Validate and Check for Completeness` 检查完整性。
6. 使用 `Configure Transformation Scenario(s)` 选择 WebHelp Responsive 或 PDF 发布场景。

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

## GitHub Actions CI/CD

本仓库配置了 `.github/workflows/docs.yml`，用于实现 Docs-as-Code 流程：

- **CI**：当 `main` 或 `master` 分支收到 push，或创建 pull request 时，自动使用 DITA-OT 校验 `maps/zhiya-guochuan-agent.ditamap`。
- **构建**：校验通过后，自动构建 HTML5 文档站点，并将构建结果作为 Actions artifact 保存。
- **CD**：当变更合入 `main` 或 `master` 分支后，自动把 HTML5 文档发布到 GitHub Pages。

云端 CI/CD 使用开源 DITA-OT 的 `html5` 转换类型。当前精排 PDF 使用 Oxygen XML Editor 28.1 的 `pdf-css-html5` 和 Oxygen PDF Chemistry，本地可生成；GitHub 托管 runner 默认没有 Oxygen PDF Chemistry，因此不在云端直接生成精排 PDF。

## 命令行验证与发布

如果需要在 Oxygen 外部复现验证和发布流程，可以使用 Oxygen 自带的 Java 与 DITA-OT：

```powershell
$env:JAVA_HOME='C:\Program Files\Oxygen XML Editor 28\jre'
$env:PATH="$env:JAVA_HOME\bin;$env:PATH"
& 'C:\Program Files\Oxygen XML Editor 28\frameworks\dita\DITA-OT\bin\dita.bat' validate -i 'maps\zhiya-guochuan-agent.ditamap' --outer.control=quiet
```

生成 PDF 时建议增加 `outer.control=quiet` 参数。当前主 map 位于 `maps` 目录，topic 位于同级 `topics` 目录，DITA-OT 会把这些 topic 识别为输入 map 目录之外的资源；该参数用于避免重复显示不影响发布结果的目录范围提示。

`--args.css` 必须使用相对路径（不要使用 `file:/` URI），且是相对于输出目录 `build/pdf-css-html5/` 的路径。从输出目录回退两级到达项目根，再进入 `styles/`：

```powershell
$env:JAVA_HOME='C:\Program Files\Oxygen XML Editor 28\jre'
$env:PATH="$env:JAVA_HOME\bin;$env:PATH"
& 'C:\Program Files\Oxygen XML Editor 28\frameworks\dita\DITA-OT\bin\dita.bat' -i 'maps\zhiya-guochuan-agent.ditamap' -f pdf-css-html5 -o 'build\pdf-css-html5' --args.output.base='zhiya-guochuan-agent' --args.css='..\..\styles\zh-cn-pdf.css' --outer.control=quiet
```

> 注：上述命令需在 `zhiya-guochuan-agent-doc` 目录下运行，并按实际 Oxygen 安装路径调整。发布产物位于 `build/pdf-css-html5/zhiya-guochuan-agent.pdf`。
