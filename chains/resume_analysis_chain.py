from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

from llm_utils import get_client


def build_resume_analysis_prompt(resume_text: str) -> str:
    return f"""
你是一个专业的实习简历分析助手，请从下面的简历文本中抽取结构化信息。

请严格按照要求输出 JSON，不要输出 Markdown，不要解释，不要添加多余文本。

JSON 结构必须为：
{{
  "education": [],
  "projects": [],
  "technical_skills": [],
  "agent_related_experience": [],
  "engineering_experience": [],
  "weak_points": []
}}

字段说明：
- education：教育背景，例如学校、专业、学历、年级等
- projects：项目经历，提取项目名称、项目内容、个人职责、技术栈和结果
- technical_skills：简历中体现出的技术能力，例如 Python、LangChain、RAG、数据库、后端开发等
- agent_related_experience：与大模型、Agent、Prompt Engineering、工具调用、多轮对话相关的经历
- engineering_experience：工程化能力，例如 Git、测试、代码规范、异常处理、模块化设计等
- weak_points：从简历文本看表达不充分或缺失的能力点

要求：
1. 只基于简历原文抽取，不要编造经历
2. 如果某个字段没有相关内容，返回空数组
3. 项目经历要尽量保留具体技术和个人贡献
4. weak_points 可以基于简历中没有明显体现的岗位相关能力进行判断

简历文本：
{resume_text}
"""


def analyze_resume(resume_text: str) -> dict:
    llm = get_client()
    parser = JsonOutputParser()

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "你是一个专业的简历分析助手，必须输出严格 JSON 结构。\n{format_instructions}",
            ),
            ("human", "{input}"),
        ]
    ).partial(format_instructions=parser.get_format_instructions())

    chain = prompt | llm | parser
    return chain.invoke({"input": build_resume_analysis_prompt(resume_text)})
