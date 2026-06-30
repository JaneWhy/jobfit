from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

from llm_utils import get_client


def build_gap_analysis_prompt(
    jd_analysis: dict,
    resume_analysis: dict,
    match_result: dict,
) -> str:
    return f"""
你是一个专业的实习投递差距分析助手，请综合岗位结构化分析、简历结构化分析和规则匹配结果，判断候选人与岗位之间的匹配差距。

请严格按照要求输出 JSON，不要输出 Markdown，不要解释，不要添加多余文本。

JSON 结构必须为：
{{
  "matched_strengths": [],
  "missing_requirements": [],
  "weak_expressions": [],
  "resume_improvement_actions": []
}}

字段说明：
- matched_strengths：候选人已经匹配岗位要求的优势，必须结合简历证据
- missing_requirements：岗位要求中简历没有体现或明显缺失的能力
- weak_expressions：简历中可能有相关能力，但表达不够具体、不够有说服力的地方
- resume_improvement_actions：具体可执行的简历修改动作

分析要求：
1. 优先参考岗位结构化分析中的核心要求和工程化要求
2. 结合简历结构化分析中的项目、技能和工程经验判断
3. 参考规则匹配结果中的 matched_skills 和 missing_skills
4. 不要编造简历中没有的经历
5. 修改建议要具体，例如补充项目背景、技术栈、个人职责、量化结果等

岗位结构化分析：
{jd_analysis}

简历结构化分析：
{resume_analysis}

规则匹配结果：
{match_result}
"""


def analyze_gap(
    jd_analysis: dict,
    resume_analysis: dict,
    match_result: dict,
) -> dict:
    llm = get_client()
    parser = JsonOutputParser()

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "你是一个专业的求职差距分析助手，必须输出严格 JSON 结构。\n{format_instructions}",
            ),
            ("human", "{input}"),
        ]
    ).partial(format_instructions=parser.get_format_instructions())

    chain = prompt | llm | parser
    return chain.invoke(
        {
            "input": build_gap_analysis_prompt(
                jd_analysis,
                resume_analysis,
                match_result,
            )
        }
    )