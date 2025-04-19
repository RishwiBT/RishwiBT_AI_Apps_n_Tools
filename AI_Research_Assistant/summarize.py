import os
import fitz
import openai
import re

openai.api_key = os.getenv("OPENAI_API_KEY")

SECTION_TITLES = ["abstract", "introduction", "methods", "results", "discussion", "conclusion"]

def extract_text_from_pdf(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    return "\n".join(page.get_text() for page in doc)

def extract_sections(text: str) -> dict:
    sections = {}
    text = text.lower()
    for title in SECTION_TITLES:
        pattern = rf"\n{title}\s*\n"
        matches = list(re.finditer(pattern, text))
        if not matches:
            continue
        start = matches[0].end()
        end = matches[1].start() if len(matches) > 1 else len(text)
        content = text[start:end].strip()
        sections[title.title()] = content
    return sections

from openai import OpenAI

client = OpenAI()

def summarize_text(text, section="Section"):
    prompt = f"Summarize the following {section} from a research paper:\n\n{text}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=500
    )
    return response.choices[0].message.content

def summarize_sections(pdf_path: str) -> dict:
    raw_text = extract_text_from_pdf(pdf_path)
    sections = extract_sections(raw_text)

    summaries = {}
    for title, content in sections.items():
        if len(content) < 100:
            continue
        try:
            summaries[title] = summarize_text(content, section=title)
        except Exception as e:
            summaries[title] = f"[Error summarizing]: {e}"
    return summaries
