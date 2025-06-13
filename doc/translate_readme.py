import os
import re
import requests
from time import sleep

# ==== 配置区域 ====
API_URL = "https://api.deepseek.com/v1/chat/completions"
API_KEY = os.getenv('API_KEY')  # 请确保你设置了环境变量或直接替换为 API Key 字符串
MODEL = "deepseek-chat"  # 或 deepseek-reasoner
TRANSLATED_FILE = "README_cn.md" # 相对于github根目录
ORIGINAL_FILE = "README.md"
SLEEP_BETWEEN_REQUESTS = 2  # 避免频率限制，可适当调整
MAX_TOKENS = 4096
TEMPERATURE = 0.2

# ==== Step 1: 按标题分块 ====
def split_markdown_sections(content):
    pattern = r"(?=^#{1,6} )"  # 匹配以1-6个#开头的行（标题）
    sections = re.split(pattern, content, flags=re.MULTILINE)
    # 保留标题
    result = []
    for i in range(1, len(sections), 2):
        chunk = sections[i - 1].strip() + '\n' + sections[i].strip()
        result.append(chunk.strip())
    if len(sections) % 2 == 1:
        result.append(sections[-1].strip())
    return result

# ==== Step 2: 调用大模型翻译 ====
def translate_block(text):
    prompt = f"""
请将我提供的文本翻译成中文，规则如下：
1.无需输出解释，只需输出翻译后的文本
2.专业名词（如：Android、UI、Fastbot、Kea2）、人名、论文引用（如：An Empirical Study of Functional Bugs in Android Apps. ISSTA 2023. ）、邮箱、链接、markdown代码（如：`@precondition`）、代码块（如：```python
python3 quicktest.py
```）中的内容无需翻译；
3.术语表如下：
```
property-based testing: 基于性质的测试
property: 性质
```
4.如果无需翻译，返回原内容即可

待翻译的markdown文本：
{text}
"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]
        return content.strip()
    except Exception as e:
        print(f"❌ Error during translation: {e}")
        return f"<!-- Translation failed for block -->\n{text}"

# ==== Step 3: 主流程 ====
def main():
    if not os.path.exists(ORIGINAL_FILE):
        print(f"❌ File {ORIGINAL_FILE} not found.")
        return

    with open(ORIGINAL_FILE, "r", encoding="utf-8") as f:
        md_content = f.read()

    sections = split_markdown_sections(md_content)
    print(f"🔍 Detected {len(sections)} sections for translation.")

    translated_sections = []
    for idx, sec in enumerate(sections, 1):
        print(f"🌐 Translating section {idx}/{len(sections)}...")
        translation = translate_block(sec)
        translated_sections.append(translation)
        sleep(SLEEP_BETWEEN_REQUESTS)  # 防止请求过快被限速

    final_result = "\n\n".join(translated_sections)

    with open(TRANSLATED_FILE, "w", encoding="utf-8") as f:
        f.write(final_result)

    print(f"✅ Translation completed. Output written to: {TRANSLATED_FILE}")



if __name__ == "__main__":
    main()
