def build_fallback_report(match_result: dict) -> str:
    matched_skills = ", ".join(match_result["matched_skills"]) or "暂无"
    missing_skills = ", ".join(match_result["missing_skills"]) or "暂无"

    category_lines = []
    for category, result in match_result["categories"].items():
        matched = ", ".join(result["matched_skills"]) or "暂无"
        missing = ", ".join(result["missing_skills"]) or "暂无"
        category_lines.append(
            f"### {category}\n\n"
            f"- 分类匹配度：{result['score']}%\n"
            f"- 已匹配：{matched}\n"
            f"- 待补强：{missing}\n"
        )

    category_report = "\n".join(category_lines)

    return f"""
## 基础分析报告

当前大模型分析暂不可用，以下报告基于规则匹配结果自动生成。

### 整体匹配情况

- 基础匹配度：{match_result["score"]}%
- 已匹配技能：{matched_skills}
- 待补强技能：{missing_skills}

## 分类匹配情况

{category_report}

## 简历优化建议

1. 优先补充待补强技能相关的项目经历，尤其是岗位 JD 中反复出现的能力要求。
2. 对已掌握技能补充具体使用场景，例如项目背景、技术方案、个人职责和最终结果。
3. 如果缺少某项关键技能，可以在简历中补充学习实践、课程项目或小型 Demo。
4. 对 AI/大模型相关岗位，建议突出 Python、LangChain、Agent、Prompt Engineering、工具调用和测试经验。
5. 每段项目经历尽量使用“做了什么、用了什么技术、解决了什么问题、结果如何”的结构表达。

## 面试准备方向

1. 解释项目中技能匹配分数的计算方式。
2. 说明如何从 JD 和简历中抽取技能关键词。
3. 说明如何处理空简历、空 JD、文件解析失败和 API 调用失败。
4. 准备介绍一个与待补强技能相关的实践案例。
5. 如果目标岗位涉及 Agent，准备说明任务拆解、工具调用和多轮对话流程设计。
"""
