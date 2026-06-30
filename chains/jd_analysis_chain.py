import os 
from llm_utils import get_client
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

def build_jd_analysis_prompt(jd_text: str) -> str:
    return f"""
    你是一个专业的实习岗位 JD 分析助手，请从下面的岗位 JD 中抽取结构化信息。

    请严格按照要求输出 JSON（不要 Markdown，不要解释，不要多余文本）。

    JSON 结构必须为：
    {{
     "core_requirements": [],
     "responsibilities": [],
    "engineering_requirements": [],
    "bonus_points": []
    }}

    字段说明：
    - core_requirements：核心技能（如 Python、LangChain、Agent、Prompt Engineering）
    - responsibilities：岗位职责
    - engineering_requirements：工程化要求（Git、测试、代码规范等）
    - bonus_points：加分项

    岗位 JD：
    {jd_text}
"""


def analyze_jd(jd_text: str) -> dict:
    llm = get_client()
    parser = JsonOutputParser()
    #让parser把格式要求自动注入prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个专业的JD分析助手，必须输出严格JSON结构。\n{format_instructions}"),
        ("human","{input}")
    ]).partial(
        format_instructions = parser.get_format_instructions()
    )
    print(parser.get_format_instructions())
    chain = prompt | llm | parser
    result = chain.invoke({
        "input":build_jd_analysis_prompt(jd_text)
    })

    return result