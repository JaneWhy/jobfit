COMMON_SKILLS = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "SQL",
    "Linux",
    "Git",
    "Docker",
    "MySQL",
    "Redis",
    "MongoDB",
    "Flask",
    "Django",
    "Streamlit",
    "FastAPI",
    "机器学习",
    "深度学习",
    "大模型",
    "LLM",
    "Agent",
    "RAG",
    "LangChain",
    "Prompt Engineering",
    "工具调用",
    "任务拆解",
    "多轮对话",
    "OpenAI API",
    "通义千问",
    "文心一言",
    "智谱清言",
    "DeepSeek",
    "ChromaDB",
    "向量数据库",
    "数据结构",
    "算法",
    "操作系统",
    "计算机网络",
    "数据库",
    "软件工程",
    "后端开发",
    "前端开发",
    "单元测试",
    "集成测试",
    "pytest",
]


def extract_skills(text: str) -> list[str]:
    found_skills = []
    lower_text = text.lower()
    for skill in COMMON_SKILLS:
        if skill.lower() in lower_text:
            found_skills.append(skill)
    return found_skills


SKILL_CATEGORIES = {
    "编程语言": ["Python", "Java", "C++", "JavaScript", "SQL"],
    "后端开发": ["Flask", "Django", "FastAPI"],
    "数据库": ["MySQL", "Redis", "MongoDB", "向量数据库", "ChromaDB"],
    "AI/大模型": [
        "机器学习",
        "深度学习",
        "大模型",
        "LLM",
        "RAG",
        "LangChain",
        "Agent",
        "Prompt Engineering",
        "工具调用",
        "任务拆解",
        "多轮对话",
        "OpenAI API",
        "通义千问",
        "文心一言",
        "智谱清言",
        "DeepSeek",
    ],
    "开发工具": ["Linux", "Git", "Docker"],
    "工程基础": ["数据结构", "算法", "操作系统", "计算机网络", "软件工程"],
    "测试能力": ["单元测试", "集成测试", "pytest"],
}


def extract_skills_by_category(text: str) -> dict[str, list[str]]:
    result = {}
    lower_text = text.lower()
    for category, skills in SKILL_CATEGORIES.items():
        found_skills = []
        for skill in skills:
            if skill.lower() in lower_text:
                found_skills.append(skill)
        result[category] = found_skills
    return result
