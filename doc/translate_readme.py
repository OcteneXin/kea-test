import os
import requests

def translate_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    prompt = f"""
请将以下文档翻译成中文，规则如下：
1.无需输出解释，只需输出翻译后的文本
2.专业名词（如：Android、UI、Fastbot、Kea2）、人名、论文引用（如：An Empirical Study of Functional Bugs in Android Apps. ISSTA 2023. ）、邮箱、链接、markdown代码（如：`@precondition`）、代码块（如：```python
python3 quicktest.py
```）中的内容无需翻译；
3.术语表如下：
```
property-based testing: 基于性质的测试
property: 性质
```


{content}"""

    # DeepSeek-R1 或你接入的任何大模型 API
    response = requests.post(
        url="https://api.deepseek.com/v1/chat/completions",  # 示例 URL
        headers={
            "Authorization": f"Bearer {os.getenv('API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek-chat",  # 根据实际模型名称
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2
        }
    )

    result = response.json()
    translated = result["choices"][0]["message"]["content"]

    with open("README_cn.md", "w", encoding="utf-8") as f:
        f.write(translated)

if __name__ == "__main__":
    translate_readme()
