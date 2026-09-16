# AI Job Intelligence

An AI-powered job analysis tool built with Python and Gemini.

The project analyzes a job description, compares its requirements with a candidate's skills, calculates a match score, identifies missing or related skills, and generates an AI-powered recommendation.

## Current Features

* Analyze job descriptions using Gemini AI
* Extract required technical skills
* Perform semantic skill matching
* Identify matched, related, and missing skills
* Calculate a job match percentage
* Generate personalized recommendations
* Scrape text from publicly accessible job pages
* Accept job descriptions directly from the terminal

## Tech Stack

* Python
* Google Gemini API
* Google GenAI SDK
* Requests
* BeautifulSoup
* python-dotenv
* Git & GitHub

## Project Flow

```text
Job URL / Job Description
          ↓
     Web Scraping
          ↓
       AI Analysis
          ↓
    Skill Extraction
          ↓
 Semantic Skill Matching
          ↓
   Match Score + Gaps
          ↓
    AI Recommendation
```

## Example

The system can identify:

```text
Matched Skills:
- Webflow
- HTML
- CSS
- JavaScript
- n8n automation

Related Skills:
- API integration

Missing Skills:
- React

Match Score:
79%
```

## Project Structure

```text
ai-job-intelligence/
│
├── .venv/
├── .env
├── .gitignore
├── main.py
├── test_scraper.py
└── README.md
```

> `.env` contains API credentials and should never be committed to GitHub.

## Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd ai-job-intelligence
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install google-genai python-dotenv requests beautifulsoup4
```

### 5. Configure the API key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### 6. Run the project

```bash
python main.py
```

## Learning Goals

This project is part of my practical journey into AI automation and application development.

The main concepts I'm learning through this project are:

* Python
* APIs
* LLM integration
* Structured JSON responses
* Prompt engineering
* Semantic matching
* Web scraping
* Data processing
* Git & GitHub
* AI-powered automation

## Roadmap

* [x] Connect Python with Gemini
* [x] Generate structured JSON
* [x] Extract job skills
* [x] Implement semantic skill matching
* [x] Calculate match score
* [x] Generate recommendations
* [x] Basic job-page scraping
* [ ] Connect scraper with AI analyzer
* [ ] Improve job description extraction
* [ ] Add database storage
* [ ] Add job history
* [ ] Add Telegram notifications
* [ ] Build a web dashboard
* [ ] Automate job discovery and analysis

## Disclaimer

This is a learning project and is continuously evolving. Job-page scraping depends on the structure and accessibility of individual websites.