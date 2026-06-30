# JobFit 问题排查文档

本文档记录 JobFit 项目开发和运行过程中常见问题、可能原因和处理方式，用于提升系统调试效率和项目工程化完整度。

## 1. LLM API 余额不足

### 现象

页面提示：

```text
LLM API 调用失败：Error code: 402 - Insufficient Balance
```

### 可能原因

当前 `API_KEY` 对应的模型服务账户余额不足，或免费额度已用完。

### 处理方式

1. 登录模型服务平台检查账户余额。
2. 更换有可用额度的 `API_KEY`。
3. 给当前账户充值或领取免费额度。
4. 暂时使用项目内置的本地基础分析报告。

### 当前项目兜底

JobFit 已接入 `fallback_report.py`。当 LLM API 调用失败时，系统会自动切换为本地基础分析报告，保证页面仍然可以展示规则匹配结果、待补强技能和简历优化建议。

## 2. 缺少 API_KEY

### 现象

页面提示：

```text
缺少环境变量 API_KEY，请先配置大模型 API Key。
```

### 可能原因

运行 Streamlit 前没有配置模型服务密钥。

### 处理方式

PowerShell 示例：

```powershell
$env:API_KEY="your_api_key"
$env:BASE_URL="your_base_url"
$env:MODEL_NAME="deepseek-v4-pro"
```

其中：

- `API_KEY`：模型服务密钥
- `BASE_URL`：OpenAI-compatible API 地址
- `MODEL_NAME`：模型名称，不配置时使用项目默认值

## 3. LangChain 依赖缺失

### 现象

运行测试或启动项目时报错：

```text
ModuleNotFoundError: No module named 'langchain_core'
```

### 可能原因

当前 Python 环境没有安装 LangChain 相关依赖，或者运行命令时使用的不是项目虚拟环境。

### 处理方式

如果使用 `uv`：

```bash
uv sync
```

如果使用 `pip`：

```bash
pip install -U langchain langchain-core langchain-openai
```

检查当前 Python 解释器：

```bash
python -c "import sys; print(sys.executable)"
```

确保输出路径来自项目虚拟环境。

## 4. JSON 解析失败

### 现象

`JsonOutputParser` 报错，或页面提示：

```text
JD 结构化分析失败
简历结构化分析失败
差距分析失败
```

### 可能原因

模型没有严格返回 JSON，例如返回了 Markdown 代码块：

```text
```json
{...}
```
```

或在 JSON 前后添加了解释文本。

### 处理方式

1. 在 Prompt 中明确要求“只输出 JSON，不要 Markdown，不要解释”。
2. 使用 `JsonOutputParser().get_format_instructions()` 注入格式要求。
3. 对结构化 Chain 增加异常捕获，失败时不影响主流程。
4. 后续可以增加输出清洗或重试机制。

### 当前项目策略

`jd_analysis_chain.py`、`resume_analysis_chain.py` 和 `gap_analysis_chain.py` 已使用 `JsonOutputParser` 约束输出格式。`app.py` 中应对每个结构化 Chain 使用 `try/except`，避免单个 Chain 失败导致页面整体中断。

## 5. 简历解析结果为空

### 现象

页面提示：

```text
简历解析结果为空，请检查文件内容是否可复制，或尝试上传 DOCX 格式。
```

### 可能原因

1. PDF 是扫描件，本身没有可提取文本。
2. PDF 中文本被加密或不可复制。
3. 文件格式异常。
4. 简历内容主要由图片组成。

### 处理方式

1. 优先上传 DOCX 格式简历。
2. 确认 PDF 中的文字可以被复制。
3. 如果是扫描件，后续可接入 OCR 能力。

## 6. 文件格式不支持

### 现象

页面提示：

```text
暂不支持该文件格式，请上传 PDF 或 DOCX 文件。
```

### 可能原因

上传了非 PDF / DOCX 文件，例如 `.txt`、`.jpg`、`.png`。

### 处理方式

将简历转换为 PDF 或 DOCX 后重新上传。

## 7. 中文乱码

### 现象

代码或页面出现类似内容：

```text
绠€鍘?JD 鍖归厤
```

### 可能原因

文件编码不统一。常见情况是 Windows 环境中编辑器用 GBK 或系统默认编码保存文件，而运行环境按 UTF-8 读取。

### 处理方式

1. 在编辑器中将文件保存为 UTF-8。
2. VS Code / Cursor 可点击右下角编码，选择 `Save with Encoding`，再选择 `UTF-8`。
3. 避免在不同编码工具之间反复保存同一个文件。
4. 建议新增 `.editorconfig` 统一项目编码。

推荐配置：

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

[*.py]
indent_style = space
indent_size = 4

[*.md]
trim_trailing_whitespace = false
```

## 8. 测试中 Chain 被跳过

### 现象

运行测试时看到：

```text
skipped '需要安装 langchain-core 后才能运行 Chain 测试'
```

### 可能原因

当前 Python 环境没有安装 `langchain-core`。

### 处理方式

安装依赖后重新运行测试：

```bash
uv sync
```

或：

```bash
pip install -U langchain langchain-core langchain-openai
```

然后执行：

```bash
python -m unittest discover -s tests -v
```

## 9. 测试命令

运行全部测试：

```bash
python -m unittest discover -s tests -v
```

当前测试覆盖：

- 技能关键词抽取
- 分类匹配分数计算
- 本地基础分析报告生成
- LLM Chain 的 Mock 测试

## 10. 排查顺序建议

当系统运行异常时，建议按以下顺序排查：

1. 确认 Python 环境是否正确。
2. 确认依赖是否安装完整。
3. 确认环境变量 `API_KEY`、`BASE_URL`、`MODEL_NAME` 是否正确。
4. 单独运行测试确认基础模块是否正常。
5. 检查上传简历是否能被正常解析。
6. 检查结构化 Chain 是否返回合法 JSON。
7. 如果 LLM 不可用，确认本地基础分析报告是否正常展示。
