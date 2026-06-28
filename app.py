import streamlit as st

from fallback_report import build_fallback_report
from jd_parser import extract_skills_by_category
from llm_utils import call_llm
from matcher import calculate_match
from prompts import build_analysis_prompt
from resume_parser import extract_resume_text


st.set_page_config(page_title="JobFit 简历-JD 匹配分析系统", layout="wide")

st.title("JobFit 简历-JD 匹配分析系统")

left, right = st.columns(2)

with left:
    st.subheader("上传简历")
    uploaded_file = st.file_uploader("选择一个简历文件，支持 PDF / DOCX", type=["pdf", "docx"])

    st.subheader("粘贴岗位 JD")
    jd_text = st.text_area("此处输入岗位描述", height=300)
    analyze_button = st.button("开始分析")

with right:
    st.subheader("分析结果")

    if analyze_button:
        if uploaded_file is None:
            st.error("请上传简历文件")
            st.stop()

        if not jd_text.strip():
            st.error("请粘贴岗位 JD")
            st.stop()

        try:
            resume_text = extract_resume_text(uploaded_file)
        except ValueError as error:
            st.error(str(error))
            st.stop()
        except Exception as error:
            st.error(f"简历解析失败：{error}")
            st.stop()

        if not resume_text.strip():
            st.error("简历解析结果为空，请检查文件内容是否可复制，或尝试上传 DOCX 格式。")
            st.stop()

        jd_skills = extract_skills_by_category(jd_text)
        resume_skills = extract_skills_by_category(resume_text)
        match_result = calculate_match(jd_skills, resume_skills)

        st.write("简历解析结果预览：")
        st.text(resume_text[:1000])

        st.subheader("规则匹配结果")
        st.metric("基础匹配度", f"{match_result['score']}%")

        for category, result in match_result["categories"].items():
            with st.expander(f"{category}：{result['score']}%", expanded=True):
                jd_skill_text = ", ".join(result["jd_skills"]) or "未识别到岗位要求"
                matched_skill_text = ", ".join(result["matched_skills"]) or "暂无"
                missing_skill_text = ", ".join(result["missing_skills"]) or "暂无"

                st.write(f"岗位要求：{jd_skill_text}")
                st.write(f"已匹配：{matched_skill_text}")
                st.write(f"待补强：{missing_skill_text}")

        prompt = build_analysis_prompt(resume_text, jd_text, match_result)
        try:
            with st.spinner("正在生成大模型分析报告..."):
                report = call_llm(prompt)
        except ValueError as error:
            st.warning(f"{error} 已切换为本地基础分析报告。")
            report = build_fallback_report(match_result)
        except Exception as error:
            st.warning(f"LLM API 调用失败：{error} 已切换为本地基础分析报告。")
            report = build_fallback_report(match_result)

        if not report.strip():
            st.warning("LLM 未返回有效分析报告，已切换为本地基础分析报告。")
            report = build_fallback_report(match_result)

        st.markdown(report)
