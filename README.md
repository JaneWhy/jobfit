# JobFit 简历-JD 匹配分析系统

JobFit 是一个面向实习投递场景的简历-JD 智能匹配与优化系统。用户可以上传 PDF / DOCX 简历并粘贴岗位 JD，系统会解析简历内容、抽取岗位技能要求、计算技能匹配度，并结合 LangChain 多阶段分析流程生成投递分析报告。

项目重点面向大模型 Agent、Prompt Engineering、Python 工程能力相关岗位，适合作为算法实习、AI 应用开发实习、LLM Agent 实习方向的项目展示。

## 功能特性

- 支持 PDF / DOCX 简历解析
- 支持岗位 JD 文本输入
- 支持技能关键词抽取与分类展示
- 支持整体匹配度和分类匹配度计算
- 支持 JD 结构化分析
- 支持简历结构化分析
- 支持岗位要求与简历能力差距分析
- 支持大模型生成实习投递分析报告
- 支持 LLM API 失败时切换到本地基础分析报告
- 支持基础单元测试和 LLM Chain Mock 测试
- 提供问题排查文档，覆盖 API、依赖、JSON、文件解析和编码问题

## 技术栈

- Python
- Streamlit
- LangChain
- OpenAI-compatible API
- pypdf
- python-docx
- unittest
- unittest.mock
- uv

## 项目结构

```text
jobfit/
  app.py                         # Streamlit 页面入口
  jd_parser.py                   # JD / 简历技能关键词抽取
  matcher.py                     # 技能匹配与分类匹配度计算
  resume_parser.py               # PDF / DOCX 简历解析
  prompts.py                     # 最终报告 Prompt 构建
  llm_utils.py                   # LangChain 模型初始化与 LLM 调用
  fallback_report.py             # LLM 失败时的本地基础分析报告
  development_plan.md            # 项目开发优先级与能力补强计划
  pyproject.toml                 # 项目依赖配置

  chains/
    jd_analysis_chain.py         # JD 结构化分析 Chain
    resume_analysis_chain.py     # 简历结构化分析 Chain
    gap_analysis_chain.py        # 岗位-简历差距分析 Chain

  tests/
    test_matcher.py              # 匹配逻辑测试
    test_jd_parser.py            # 技能抽取测试
    test_fallback_report.py      # 本地报告测试
    test_chains.py               # LLM Chain Mock 测试

  docs/
    troubleshooting.md           # 问题排查文档
```

## 核心流程

```text
上传简历 + 输入 JD
-> 解析简历文本
-> 规则抽取 JD / 简历技能
-> 计算整体匹配度和分类匹配度
-> JD 结构化分析
-> 简历结构化分析
-> 岗位-简历差距分析
-> 生成最终投递分析报告
-> 如果 LLM 不可用，切换本地基础分析报告
```

## LangChain 多阶段分析

项目使用 LangChain 将分析流程拆成多个阶段：

- `jd_analysis_chain.py`：从岗位 JD 中抽取核心要求、岗位职责、工程化要求和加分项
- `resume_analysis_chain.py`：从简历中抽取教育背景、项目经历、技术能力、Agent 相关经历和薄弱点
- `gap_analysis_chain.py`：综合 JD 分析、简历分析和规则匹配结果，输出优势、缺失项、弱表达和修改动作

这些 Chain 使用：

- `ChatPromptTemplate`
- `JsonOutputParser`
- OpenAI-compatible Chat Model

这样可以把一次性大 Prompt 拆成更清晰的多阶段任务，便于调试、测试和后续 Agent 化。

## 匹配分类

当前技能匹配按以下分类展示：

- 编程语言
- 后端开发
- 数据库
- AI/大模型
- 开发工具
- 工程基础
- 测试能力

其中 AI/大模型方向覆盖：

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

使用 `uv`：

```bash
uv sync
```

或使用 `pip`：

```bash
pip install -U streamlit openai pypdf python-docx langchain langchain-core langchain-openai
```

### 2. 配置环境变量

项目使用 OpenAI-compatible API：

```bash
API_KEY=你的 API Key
BASE_URL=你的模型服务 Base URL
MODEL_NAME=deepseek-v4-pro
```

PowerShell 示例：

```powershell
$env:API_KEY="your_api_key"
$env:BASE_URL="your_base_url"
$env:MODEL_NAME="deepseek-v4-pro"
```

`MODEL_NAME` 可选，不配置时使用项目默认值。

### 3. 启动应用

```bash
streamlit run app.py
```

## 使用流程

1. 上传 PDF 或 DOCX 格式简历。
2. 粘贴目标岗位 JD。
3. 点击“开始分析”。
4. 查看 JD 结构化分析。
5. 查看简历结构化分析。
6. 查看规则匹配结果。
7. 查看差距分析和最终投递分析报告。

## 测试

运行全部测试：

```bash
python -m unittest discover -s tests -v
```

当前测试覆盖：

- 技能关键词抽取
- 分类匹配分数计算
- 空 JD 技能场景
- 本地基础分析报告生成
- LLM Chain Mock 测试

`test_chains.py` 使用 `unittest.mock.patch` 替换真实模型调用，避免测试依赖 API Key、网络和账户余额。

如果当前 Python 环境没有安装 `langchain-core`，Chain 测试会被自动跳过；安装依赖后会正常执行。

## 问题排查

常见问题详见：[docs/troubleshooting.md](docs/troubleshooting.md)

文档覆盖：

- LLM API 余额不足
- 缺少 `API_KEY`
- LangChain 依赖缺失
- JSON 解析失败
- 简历解析为空
- 文件格式不支持
- 中文乱码
- Chain 测试被跳过

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

- 岗位核心要求
- 简历已匹配能力
- 简历缺失或表达不充分的能力
- 分类匹配度
- 差距分析结果
- 简历修改建议
- 可能的面试问题

## 当前进展

已完成：

- 简历文件解析
- JD 文本输入
- 技能关键词抽取
- 整体匹配度和分类匹配度计算
- JD 结构化分析 Chain
- 简历结构化分析 Chain
- 差距分析 Chain
- LLM 分析报告生成
- LLM 失败本地兜底报告
- 基础异常处理
- 单元测试
- LLM Chain Mock 测试
- 问题排查文档

待完善：

- 把 Chain 进一步封装成 LangChain Tools
- 构建 JobFit Agent 工作流
- 增加日志记录
- 增加更细粒度的错误重试机制
- 补充界面截图和示例报告

## 简历项目描述参考

项目名称：

> JobFit Agent：基于 LangChain 的简历-JD 智能匹配与优化系统

项目描述：

> 基于 Python、Streamlit、LangChain 和大模型 API 构建求职分析系统，支持 PDF/DOCX 简历解析、JD 结构化分析、简历结构化分析、技能匹配评分、岗位-简历差距分析、简历优化建议和面试题生成。系统按编程语言、AI/大模型、开发工具、工程基础等维度展示匹配结果，并在 LLM API 调用失败时自动切换为本地基础分析报告。

技术亮点：

> 使用 LangChain 的 ChatPromptTemplate 和 JsonOutputParser 构建多阶段结构化分析流程；使用 unittest 和 mock 隔离真实 LLM API，对技能抽取、匹配评分、兜底报告和 LLM Chain 流程进行测试；编写问题排查文档，覆盖 API 余额、依赖缺失、JSON 解析失败、简历解析为空和中文乱码等常见问题。
