# JobFit 简历-JD 匹配分析系统

JobFit 是一个面向实习投递场景的简历-JD 智能匹配与优化工具。用户可以上传 PDF / DOCX 简历并粘贴岗位 JD，系统会解析简历内容、抽取岗位技能要求、计算技能匹配度，并调用大模型生成简历优化建议和面试准备问题。

当前项目重点面向大模型 Agent、Prompt Engineering、Python 工程能力相关岗位进行打磨，适合作为算法实习、AI 应用开发实习、LLM Agent 实习方向的项目展示。

## 功能特性

- 支持上传 PDF / DOCX 简历
- 支持粘贴岗位 JD 文本
- 自动抽取简历和 JD 中的技能关键词
- 按技能分类展示匹配结果
- 计算整体匹配度和分类匹配度
- 展示已匹配技能与待补强技能
- 调用大模型生成实习投递分析报告
- 输出简历优化建议和面试问题
- 对空输入、文件格式错误、简历解析失败、LLM API 调用失败等情况提供友好提示

## 技术栈

- Python
- Streamlit
- OpenAI-compatible API
- pypdf
- python-docx
- uv

后续计划引入：

- LangChain
- Agent Tools
- pytest
- 结构化 Prompt 输出
- 日志与问题排查文档

## 项目结构

```text
jobfit/
  app.py                # Streamlit 页面入口
  jd_parser.py          # JD / 简历技能关键词抽取
  matcher.py            # 技能匹配与分类匹配度计算
  resume_parser.py      # PDF / DOCX 简历解析
  prompts.py            # 大模型 Prompt 构建
  llm_utils.py          # 大模型 API 调用封装
  development_plan.md   # 项目开发优先级与能力补强计划
  pyproject.toml        # 项目依赖配置
  README.md             # 项目说明文档
```

## 匹配分类

当前技能匹配按以下分类展示：

- 编程语言
- 后端开发
- 数据库
- AI/大模型
- 开发工具
- 工程基础
- 测试能力

其中 AI/大模型方向重点覆盖：

- 大模型
- LLM
- Agent
- LangChain
- RAG
- Prompt Engineering
- 工具调用
- 任务拆解
- 多轮对话
- OpenAI API
- 通义千问
- 文心一言
- 智谱清言
- DeepSeek

## 运行方式

### 1. 安装依赖

如果使用 `uv`：

```bash
uv sync
```

如果使用 `pip`：

```bash
pip install streamlit openai pypdf python-docx
```

### 2. 配置环境变量

项目使用 OpenAI-compatible API，需要配置：

```bash
API_KEY=你的 API Key
BASE_URL=你的模型服务 Base URL
MODEL_NAME=deepseek-v4-pro
```

`MODEL_NAME` 可选，不配置时默认使用 `deepseek-v4-pro`。

PowerShell 示例：

```powershell
$env:API_KEY="your_api_key"
$env:BASE_URL="your_base_url"
$env:MODEL_NAME="deepseek-v4-pro"
```

### 3. 启动应用

```bash
streamlit run app.py
```

启动后在浏览器中打开 Streamlit 提供的本地地址。

## 使用流程

1. 上传 PDF 或 DOCX 格式简历。
2. 粘贴目标岗位 JD。
3. 点击“开始分析”。
4. 查看简历解析预览。
5. 查看按分类展示的技能匹配结果。
6. 查看大模型生成的简历优化报告。

## 示例岗位展示

可以使用“剪映数据与智能团队 Agent 实习 JD”作为展示案例。

示例 JD 重点要求：

- Python 编程能力
- LangChain 框架使用
- 大模型 Agent 业务场景落地
- 任务拆解
- 工具调用
- 多轮对话流程设计
- Prompt Engineering
- 大模型 API 调用与参数调优
- 单元测试与集成测试
- Git 和基础工程化能力

系统会围绕这些要求输出：

- 岗位核心技能
- 简历已匹配能力
- 简历缺失或表达不充分的能力
- 分类匹配度
- 简历修改建议
- 可能的面试问题

## 当前进展

已完成：

- 简历文件解析
- JD 文本输入
- 技能关键词抽取
- 整体匹配度计算
- 分类匹配结果展示
- LLM 分析报告生成
- 基础异常处理
- 项目开发计划文档

待完善：

- 引入 LangChain Chain
- 构建 Agent 工具调用流程
- 使用结构化 Prompt 输出 JSON
- 增加 pytest 单元测试
- 增加日志和问题排查文档
- 补充界面截图和示例报告

## 后续规划

### LangChain 改造

将当前一次性 LLM 调用拆分为多个 Chain：

- JD 分析 Chain
- 简历分析 Chain
- 匹配分析 Chain
- 报告生成 Chain

### Agent 工作流

计划将求职分析流程拆分为多个工具：

- `JDAnalysisTool`
- `ResumeAnalysisTool`
- `MatchTool`
- `SuggestionTool`
- `InterviewTool`

通过 Agent 编排完成任务拆解、工具调用和结果汇总。

### 测试体系

计划使用 `pytest` 增加测试：

- JD 技能抽取测试
- 简历技能抽取测试
- 匹配分数计算测试
- 空输入测试
- LLM API 异常测试

## 简历项目描述参考

项目名称：

> JobFit Agent：基于 LangChain 的简历-JD 智能匹配与优化系统

项目描述：

> 基于 Python、Streamlit 和大模型 API 构建求职分析系统，支持 PDF/DOCX 简历解析、JD 能力抽取、技能匹配评分、简历优化建议和面试题生成。系统按编程语言、AI/大模型、开发工具、工程基础等维度展示匹配结果，并对空输入、文件解析失败和 LLM API 调用失败等场景进行异常处理。

后续升级描述：

> 基于 LangChain Tools 构建求职分析 Agent，将 JD 分析、简历解析、能力匹配、建议生成和面试题生成拆解为多个工具模块，通过 Agent 编排完成自动化分析；设计结构化 Prompt 约束模型输出，并使用 pytest 对核心匹配逻辑进行测试。
