# JobFit 项目开发优先级与能力补强计划

## 一、开发优先级

### 1. 修复现有基础问题

- 修复 `app.py`、`jd_parser.py`、`prompts.py`、`llm_utils.py` 中的中文乱码问题。
- 修复技能匹配逻辑错误：当前 `calculate_match()` 期望接收 `list[str]`，但实际传入的是按分类组织的 `dict`。
- 将匹配结果改为按技能分类展示，例如编程语言、AI/大模型、开发工具、工程基础等。
- 完善异常处理，例如空简历、空 JD、文件格式不支持、LLM API 调用失败等场景。
- 将 `pyproject.toml` 中的 Python 版本要求调整为更常见的 `>=3.10` 或 `>=3.11`。

### 2. 完善 README 和项目展示

- 补充项目背景：面向实习投递场景的简历-JD 智能匹配与优化工具。
- 补充技术栈：Python、Streamlit、LLM API、LangChain、pytest 等。
- 补充功能说明：简历解析、JD 分析、技能匹配、优化建议、面试题生成。
- 补充运行方式：依赖安装、环境变量配置、启动命令。
- 补充示例输入输出，建议使用“剪映数据与智能团队 Agent 实习 JD”作为展示案例。
- 后续加入界面截图和分析报告截图，提升简历项目可信度。

### 3. 扩展岗位相关技能库

围绕目标岗位补充关键词和分类：

- Python 编程
- 面向对象编程
- LangChain
- Agent
- 工具调用
- 任务拆解
- 多轮对话
- Prompt Engineering
- 大模型 API
- OpenAI API
- 通义千问
- 文心一言
- 智谱清言
- DeepSeek
- RAG
- 单元测试
- 集成测试
- Git
- 代码规范

### 4. 引入 LangChain Chain

将当前直接调用 LLM API 的方式逐步升级为 LangChain 风格：

- 使用 `ChatPromptTemplate` 管理 Prompt。
- 使用 Chain 拆分 JD 分析、简历分析、匹配分析、报告生成。
- 将 Prompt 输出设计为结构化 JSON，降低后续解析成本。
- 为不同任务设置不同的温度参数，例如信息抽取使用低温度，建议生成可适当提高温度。

建议模块结构：

```text
chains/
  jd_analysis_chain.py
  resume_analysis_chain.py
  report_chain.py
```

### 5. 构建 LangChain Agent 工作流

围绕岗位 JD 中的“Agent 业务场景落地开发”进行升级。

建议拆分工具：

```text
tools/
  resume_tool.py
  jd_tool.py
  match_tool.py
  interview_tool.py
```

Agent 工作流可以设计为：

1. `JDAnalysisTool`：分析 JD，抽取岗位职责、核心技能、加分项。
2. `ResumeAnalysisTool`：分析简历，抽取教育背景、项目经历、技能关键词。
3. `MatchTool`：计算技能匹配度，输出匹配项、缺失项、弱表达项。
4. `SuggestionTool`：生成简历优化建议。
5. `InterviewTool`：根据 JD 和简历生成面试问题。

最终目标是让项目能体现：

- 任务拆解
- 工具调用
- Agent 编排
- 多轮对话
- 结构化输出

### 6. 强化 Prompt Engineering

建议至少设计三类 Prompt：

- `jd_extract_prompt`：从 JD 中结构化抽取岗位要求。
- `resume_extract_prompt`：从简历中结构化抽取候选人能力。
- `gap_analysis_prompt`：结合 JD 和简历输出差距分析与补强建议。

输出格式建议使用 JSON：

```json
{
  "core_requirements": [],
  "matched_experience": [],
  "missing_skills": [],
  "resume_rewrite_suggestions": [],
  "interview_questions": []
}
```

Prompt 优化重点：

- 明确角色设定。
- 明确输出字段。
- 明确不要输出空泛建议。
- 明确结合具体 JD 和简历内容。
- 对异常输出增加重试或兜底逻辑。

### 7. 增加测试体系

使用 `pytest` 增加核心模块测试。

建议目录：

```text
tests/
  test_jd_parser.py
  test_matcher.py
  test_resume_parser.py
  test_prompt_output.py
```

重点测试：

- JD 技能是否能被正确抽取。
- 简历技能是否能被正确抽取。
- 匹配分数计算是否正确。
- 空 JD、空简历、无匹配技能等边界情况。
- LLM API 返回异常时是否能正确处理。
- Prompt 结构化输出是否能被解析。

### 8. 增加日志与问题排查能力

为了贴合岗位中的“问题排查报告”，建议加入：

- 日志模块，例如 `logging`。
- LLM 请求耗时记录。
- 输入输出摘要记录。
- 异常堆栈记录。
- Debug 模式开关。
- 简单的问题排查说明文档。

可以新增：

```text
docs/
  troubleshooting.md
```

### 9. 打磨最终展示版本

最终项目应能展示：

- 一个可运行的 Streamlit 页面。
- 一个针对目标 JD 的完整分析案例。
- 一个结构清晰的 README。
- 一组基础测试。
- 一套 Agent 工具模块。
- 一份问题排查或测试说明。

## 二、需要补强的能力

### 1. Python 工程能力

重点补强：

- 函数拆分
- 面向对象编程
- 类型标注
- 异常处理
- 文件解析
- 模块化设计
- 代码规范

建议目标：

- 能清楚解释每个模块的职责。
- 能说明为什么这样拆分代码。
- 能处理常见异常和边界情况。

### 2. LangChain

重点学习：

- `ChatPromptTemplate`
- `Runnable`
- `StrOutputParser`
- `JsonOutputParser`
- `Tool`
- `AgentExecutor`
- Memory 或会话状态管理

建议目标：

- 能把一次性 LLM 调用拆成多个 Chain。
- 能封装工具供 Agent 调用。
- 能解释 Agent 如何选择工具、如何组织执行流程。

### 3. Agent 设计

重点理解：

- 任务拆解
- 工具调用
- 多轮对话
- 中间状态维护
- 错误恢复
- 输出闭环

建议目标：

- 能讲清楚 JobFit Agent 的执行流程。
- 能说明每个 Tool 的输入、输出和作用。
- 能解释如何避免 Agent 输出不稳定。

### 4. Prompt Engineering

重点补强：

- 角色设定
- 结构化输出
- Few-shot 示例
- 输出约束
- JSON 格式校验
- 温度参数调优
- Prompt 版本迭代

建议目标：

- 能说明你如何优化 Prompt。
- 能展示 Prompt 修改前后的效果差异。
- 能解释为什么某些任务要使用低温度。

### 5. 大模型 API 集成

重点补强：

- API Key 管理
- Base URL 配置
- 模型参数设置
- 错误重试
- 超时处理
- Token 成本控制
- 多模型切换

建议目标：

- 能支持不同模型服务，例如 DeepSeek、OpenAI、通义千问等。
- 能在 API 失败时给出友好的错误提示。

### 6. 测试能力

重点补强：

- pytest 基础
- 单元测试
- 集成测试
- Mock LLM API
- 边界用例设计
- 测试报告输出

建议目标：

- 核心匹配逻辑必须有单元测试。
- LLM 调用部分通过 mock 测试。
- 能说明测试覆盖了哪些关键场景。

### 7. Git 与工程化习惯

重点补强：

- Git 基础命令
- 分支管理
- 清晰 commit message
- `.gitignore`
- README 编写
- 依赖管理

建议目标：

- 保持提交记录清晰。
- 每完成一个功能模块提交一次。
- README 能让面试官快速运行项目。

## 三、建议简历项目表述

项目名称：

> JobFit Agent：基于 LangChain 的简历-JD 智能匹配与优化系统

项目描述：

> 基于 Python、Streamlit、LangChain 和大模型 API 构建求职分析 Agent，支持 PDF/DOCX 简历解析、JD 能力抽取、技能匹配评分、简历优化建议和面试题生成。系统将求职分析流程拆解为 JD 分析、简历解析、匹配计算、建议生成等多个工具模块，通过 Agent 编排完成自动化分析。

技术亮点：

> 使用 LangChain Tools 实现任务拆解与工具调用，设计结构化 Prompt 约束模型输出，提升分析结果稳定性；使用 pytest 对技能抽取、匹配评分和异常输入进行测试，保障核心流程稳定。
