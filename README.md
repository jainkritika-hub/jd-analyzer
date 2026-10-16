# JD Analyzer

A small Python tool that reads a job description, pulls out the important details as structured data, and tells you how well your skills match.

Built with LangChain, Groq and Pydantic.

## What it does

1. Reads a job description from `jd.txt`.
2. Extracts structured details: job title, company, location, employment type, minimum experience, required skills, nice-to-have skills, responsibilities and a one-line summary.
3. Compares the required skills with your own skills (`my_skills.py`).
4. Prints a match percentage, the skills you have, the skills you are missing, and a short piece of advice.
5. Saves everything to `result.json`.

## How it works

```
jd.txt  ->  LLM (fills the JobPosting form)  ->  required skills
                                                     |
my_skills.py  ----------------------------------->  LLM (fills the SkillMatch form)
                                                     |
                                           match % calculated in Python
                                                     |
                                       printed output + result.json
```

- **Structured output:** the model does not write free text. It fills in Pydantic classes (`JobPosting`, `SkillMatch`) using LangChain's `with_structured_output`, so the result can be used directly in code.
- **Judgement by the model, maths by the code:** the model decides whether a skill counts as matched (for example "REST API" and "REST APIs" are the same skill). The percentage is calculated in plain Python, because that is more reliable than asking a model to do arithmetic.
- **No guessing:** the system prompt tells the model to leave a field empty when the job description does not mention it.

## Project structure

```
jd-analyzer/
├── analyzer.py      # model calls: extract job details, match skills
├── main.py          # reads jd.txt, prints results, saves result.json
├── models.py        # Pydantic forms: JobPosting and SkillMatch
├── my_skills.py     # your skill list
├── jd.txt           # the job description to analyze
├── .env.example     # shows which key is needed
└── README.md
```

## Setup

You need Python 3.10 or newer and a free Groq API key from [console.groq.com](https://console.groq.com).

1. Clone the repository and open the folder:
   ```
   git clone https://github.com/YOUR_USERNAME/jd-analyzer.git
   cd jd-analyzer
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
   On macOS or Linux, activate with `source .venv/bin/activate` instead.

3. Install the libraries:
   ```
   pip install langchain langchain-groq python-dotenv pydantic
   ```

4. Create a file named `.env` in the project folder with your key:
   ```
   GROQ_API_KEY=your_key_here
   ```
   The `.env` file is ignored by git, so the key stays on your machine.

5. Check that `MODEL_NAME` in `analyzer.py` is a model your Groq key can use. Groq retires models from time to time. If you get a "model does not exist" error, list the models available to your key and update the line:
   ```python
   from dotenv import load_dotenv
   from groq import Groq

   load_dotenv()
   for m in Groq().models.list().data:
       print(m.id)
   ```

## Usage

1. Open `my_skills.py` and replace the list with your real skills.
2. Paste a job description into `jd.txt`.
3. Run:
   ```
   python main.py
   ```

## Example output

The values below come from a sample job description. Your results will depend on the model and your skill list.

```
Title: Python Developer - AI Applications
Company: Acme Tech
Location: Noida (Hybrid)
Type: Full-time
Min experience (years): 2

Required skills:
 - Python
 - REST APIs
 - SQL
 - LangChain

Nice to have:
 - Docker
 - AWS
 - LangGraph

Responsibilities:
 - Build REST APIs with FastAPI or Django
 - Create agents and RAG pipelines with LangChain
 - Write tests and maintain documentation

Summary: Build LLM-powered tools as a Python developer.

Skill match: 75%
You have: Python, REST APIs, SQL
You are missing: LangChain
Advice: Learn LangChain first, since it is the only required skill you lack.

Saved to result.json
```

## Limitations

- It handles one job description at a time.
- The match depends on how the model reads your skill list, so the percentage is a guide and not an exact score.
- Output quality changes with the model you choose. Smaller models fill the lists less accurately.

## Ideas for next steps

- Read a whole folder of job descriptions and rank them by match percentage.
- Fetch job descriptions from a job board instead of pasting them.
- Add a simple web page with FastAPI or Streamlit.
- Add tests with a few saved job descriptions and the results you expect.

## Tech stack

Python, LangChain, Groq, Pydantic, python-dotenv