import os

from openai import OpenAI


def get_client() -> OpenAI:
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL")

    if not api_key:
        raise ValueError("缺少环境变量 API_KEY，请先配置大模型 API Key。")

    return OpenAI(api_key=api_key, base_url=base_url)


def call_llm(prompt: str) -> str:
    client = get_client()
    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME", "deepseek-v4-pro"),
        messages=[
            {"role": "system", "content": "你是一个专业的求职简历优化助手。"},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()
