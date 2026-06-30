import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def get_client() -> ChatOpenAI:
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL")
    model_name = os.getenv("MODEL_NAME", "deepseek-v4-pro")

    if not api_key:
        raise ValueError("缺少环境变量 API_KEY，请先配置大模型 API Key。")

    return ChatOpenAI(
        api_key=api_key,
        base_url=base_url,
        model=model_name,
        temperature=0.3
    )


def call_llm(prompt: str) -> str:
    client = get_client()
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "你是一个专业的求职简历优化助手。"),
        ("human", "{input}")
    ])
    chain = prompt_template | client | StrOutputParser()
    return chain.invoke({"input": prompt})

