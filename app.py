import streamlit as st
from scanner import scan

st.set_page_config(page_title="Simple Web Vulnerability Scanner", layout="centered")

st.title(" Web Vulnerability Scanner")
st.write("Enter a website URL to check for basic vulnerabilities (SQL Injection, XSS).")

url = st.text_input("Enter Website URL (e.g., https://example.com)")

if st.button("Scan"):
    if url.strip() == "":
        st.error(" Please enter a valid URL.")
    else:
        with st.spinner("Scanning... Please wait ⏳"):
            results = scan(url)
        st.success(" Scan Completed!")
        for vuln, status in results.items():
            if status:
                st.error(f" Vulnerable to {vuln}")
            else:
                st.success(f" Not Vulnerable to {vuln}")
