import streamlit as st
from dotenv import load_dotenv
import io
import os
import PyPDF2
import google.generativeai as genai

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# --- Page Config ---
st.set_page_config(page_title="CV Surgeon", page_icon="🩺", layout="wide")

# --- Header ---
st.title("🩺 CV Surgeon")
st.markdown("**Upload your CV & let the Surgeon diagnose, roast, and prescribe improvements 💉📄**")
st.divider()

# --- Sidebar ---
with st.sidebar:
    st.header("🩻 CV Checkup")
    st.caption("Upload your CV for diagnosis")
    file_uploaded = st.file_uploader("📂 Upload CV", type=["pdf", "txt"])
    job_role = st.text_input("🎯 Target Job Role")
    analyze = st.button("🔬 Start Diagnosis", use_container_width=True)
    st.info("💡 Tip: Use a clean, updated CV for the best results!")

# --- Helper Functions ---
def extract_text_from_pdf(file_bytes):
    reader = PyPDF2.PdfReader(file_bytes)
    return "\n".join(page.extract_text() or '' for page in reader.pages)

def extract_text(file_uploaded):
    """Extract text from a text or PDF"""
    file_type = file_uploaded.type
    if file_type == 'application/pdf':
        with io.BytesIO(file_uploaded.read()) as file_bytes:
            return extract_text_from_pdf(file_bytes)
    elif file_type == 'text/plain':
        return file_uploaded.read().decode("utf-8")

# --- Main Section ---
if analyze and file_uploaded:
    with st.spinner("🩻 Scanning your CV... This may take a few seconds ⏳"):
        try:
            content = extract_text(file_uploaded)
            if not content.strip():
                st.error("❌ The file seems empty. Please upload a valid CV.")
                st.stop()

            # AI Prompt
            prompt = f"""You are a brutally honest, no-nonsense HR expert who has been reviewing resumes for decades.
            Roast this CV like you’re diagnosing a patient—be sharp, witty, and brutally honest where needed.
            Don’t hold back, but also deliver genuinely useful feedback and practical improvements.
            The goal is to transform this CV so it could actually land a job in {job_role} at a good company.

            Here’s the CV:\n{content}\n
            Keep it stinging, sharp, and constructive—around 150 words max."""

            model = genai.GenerativeModel("models/gemini-1.5-flash")
            response = model.generate_content(prompt)

            # Display Result
            st.success("✅ Diagnosis complete!")
            st.subheader("💬 Doctor’s Notes (Roast & Feedback)")
            st.write(response.text)

            # Download Option
            st.download_button(
                label="💾 Download Prescription",
                data=response.text,
                file_name="cv_diagnosis.txt",
                mime="text/plain",
                use_container_width=True
            )

        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")

else:
    st.info(" Upload a CV (PDF/TXT) and enter target role in the sidebar to begin.", icon="🧾")
