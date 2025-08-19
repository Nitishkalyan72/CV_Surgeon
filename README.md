# 🩺 CV Surgeon

[Live App Link](https://cv-surgeon.streamlit.app/)

**CV Surgeon** is an AI-powered web app that helps you **analyze, roast, and improve your CV**.  
It acts like a professional "CV doctor," providing **sharp, witty, and constructive feedback** to make your resume stand out.

---

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [License](#license)

---

## Features
- Upload CVs in **PDF** or **TXT** formats.
- Enter your **target job role** for personalized feedback.
- AI-generated **brutally honest roast** with actionable suggestions.
- Download the **detailed prescription** as a text file.
- Clean, user-friendly interface with medical-themed CV diagnosis.

---

## Demo
**Live Demo:** [CV Surgeon on Streamlit](https://cv-surgeon.streamlit.app/)  

**Interface Highlights:**
- **Sidebar Upload & Configuration:** Upload CV, specify job role, and start diagnosis.  
- **Main Panel:** Spinner shows scanning progress; AI outputs feedback once complete.  
- **Download Option:** Export AI’s CV prescription as a text file.

---

## Technologies Used
- **Python 3.13**
- **Streamlit** – Web app framework
- **PyPDF2** – PDF text extraction
- **python-dotenv** – Manage environment variables
- **Google Gemini API** – AI for resume roasting and feedback
- **Git & GitHub** – Version control and deployment
- **Streamlit Community Cloud** – Hosting

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/CV_Surgeon.git
cd CV_Surgeon
```
Create and activate a virtual environment:

```bash
python -m venv .venv
```
# Windows
```bash
.venv\Scripts\activate
```
# macOS/Linux
```bash
source .venv/bin/activate
```
Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

1. Set your **Gemini API key**:
   - Locally: Create a `.env` file in the project root with the following content:
     ```env
     GEMINI_API_KEY="your_api_key_here"
     ```
   - Streamlit Cloud: Add your API key in **Secrets** (accessible via `st.secrets["GEMINI_API_KEY"]`).

2. Run the app locally:

```bash
python -m streamlit run main.py
```
3. Open the local URL displayed in the terminal (usually `http://localhost:8501`) or use the live app link: [CV Surgeon](https://cv-surgeon.streamlit.app/).

4. Upload your CV (PDF/TXT), enter the target job role, and click **🔬 Start Diagnosis**.

5. View AI-generated roast and feedback, and download the **detailed prescription** as a text file.

---

## Deployment 

1. Push your project to GitHub (ensure `.venv` and `.env` are included in `.gitignore`).

2. Go to [Streamlit Community Cloud](https://share.streamlit.io/) → **New App** → Connect your GitHub repo.

3. Add your **GEMINI_API_KEY** in the **Secrets** section.

4. Deploy and access your live app at the provided URL.

---

## Project Structure
```env
CV_Surgeon/
│
├─ .venv/ # Virtual environment (ignored in Git)
├─ .env # Environment variables (ignored in Git)
├─ main.py # Streamlit app code
├─ requirements.txt # Python dependencies
├─ pyproject.toml # Project metadata
├─ README.md # Project documentation
├─ uv.lock # Project lock file (ignored in Git)
└─ .gitignore # Git ignore rules
```
---

## License
This project is open-source and available under the **MIT License**.

---
