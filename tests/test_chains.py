import unittest
from importlib.util import find_spec
from unittest.mock import patch

if find_spec("langchain_core") is None:
    raise unittest.SkipTest("需要安装 langchain-core 后才能运行 Chain 测试")

from langchain_core.runnables import RunnableLambda  # noqa: E402

from chains.gap_analysis_chain import analyze_gap  # noqa: E402
from chains.jd_analysis_chain import analyze_jd  # noqa: E402
from chains.resume_analysis_chain import analyze_resume  # noqa: E402


def fake_llm(json_text: str) -> RunnableLambda:
    return RunnableLambda(lambda _: json_text)


class TestChains(unittest.TestCase):
    @patch("chains.jd_analysis_chain.get_client")
    def test_analyze_jd_returns_structured_dict(self, mock_get_client):
        mock_get_client.return_value = fake_llm(
            """
            {
              "core_requirements": ["Python", "LangChain", "Agent"],
              "responsibilities": ["参与 Agent 业务场景落地"],
              "engineering_requirements": ["Git", "单元测试"],
              "bonus_points": ["大模型 API 调用经验"]
            }
            """
        )

        result = analyze_jd("要求熟悉 Python、LangChain 和 Agent。")

        self.assertEqual(result["core_requirements"], ["Python", "LangChain", "Agent"])
        self.assertEqual(result["engineering_requirements"], ["Git", "单元测试"])
        mock_get_client.assert_called_once()

    @patch("chains.resume_analysis_chain.get_client")
    def test_analyze_resume_returns_structured_dict(self, mock_get_client):
        mock_get_client.return_value = fake_llm(
            """
            {
              "education": ["计算机相关专业研一"],
              "projects": ["JobFit 简历-JD 匹配系统"],
              "technical_skills": ["Python", "Streamlit"],
              "agent_related_experience": ["了解 LangChain"],
              "engineering_experience": ["Git", "异常处理"],
              "weak_points": ["缺少 Agent 工具调用实践"]
            }
            """
        )

        result = analyze_resume("计算机研一，做过 JobFit 项目，熟悉 Python。")

        self.assertIn("JobFit 简历-JD 匹配系统", result["projects"])
        self.assertIn("Python", result["technical_skills"])
        self.assertIn("缺少 Agent 工具调用实践", result["weak_points"])
        mock_get_client.assert_called_once()

    @patch("chains.gap_analysis_chain.get_client")
    def test_analyze_gap_returns_structured_dict(self, mock_get_client):
        mock_get_client.return_value = fake_llm(
            """
            {
              "matched_strengths": ["具备 Python 和 Git 基础"],
              "missing_requirements": ["缺少 LangChain Agent 项目证据"],
              "weak_expressions": ["Python 能力缺少具体项目结果"],
              "resume_improvement_actions": ["补充 Agent 工具调用和多轮对话设计"]
            }
            """
        )
        jd_analysis = {
            "core_requirements": ["Python", "LangChain", "Agent"],
            "engineering_requirements": ["Git"],
        }
        resume_analysis = {
            "technical_skills": ["Python", "Git"],
            "agent_related_experience": [],
        }
        match_result = {
            "score": 50,
            "matched_skills": ["Python", "Git"],
            "missing_skills": ["LangChain", "Agent"],
        }

        result = analyze_gap(jd_analysis, resume_analysis, match_result)

        self.assertIn("具备 Python 和 Git 基础", result["matched_strengths"])
        self.assertIn("缺少 LangChain Agent 项目证据", result["missing_requirements"])
        self.assertIn("补充 Agent 工具调用和多轮对话设计", result["resume_improvement_actions"])
        mock_get_client.assert_called_once()


if __name__ == "__main__":
    unittest.main()
