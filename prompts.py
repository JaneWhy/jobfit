def build_analysis_prompt(resume_text: str, jd_text: str, match_result: dict, jd_analysis:dict, resume_analysis:dict, gap_analysis:dict) -> str:
    return f"""
你是一个专业的求职简历优化助手，请根据用户的简历和岗位 JD，生成一份实习投递分析报告。

要求：
1. 分析岗位核心要求
2. 总结简历中已经匹配的能力
3. 指出简历中缺失或表达不充分的部分
4. 给出具体的简历修改建议
5. 给出 5 个可能的面试问题
6. 语言要具体，不要空泛

岗位 JD：
{jd_text}

JD结构化分析：
{jd_analysis}

简历结构化分析：
{resume_analysis}

简历原文：
{resume_text}

规则匹配结果：
{match_result}

差距分析结果：
{gap_analysis}
"""
