import fitz  # PyMuPDF
import re
import json

def extract_data_from_pdf(pdf_path):
    # Step 1: Extract all text
    pdf = fitz.open(pdf_path)
    text = ""
    for page in pdf:
        text += page.get_text()
    pdf.close()

    # Step 2: Extract fields using regex
    data = {
        "registration_number": re.search(r"Registration Number\s*[:：]?\s*(\S+)", text),
        "legal_name": re.search(r"1\.\s*Legal Name\s*(.*?)\n", text),
        "trade_name": re.search(r"2\.\s*Trade Name.*?\s*(.*?)\n", text),
        "additional_trade_names": re.search(r"3\.\s*Additional trade names.*?\s*(.*?)\n", text),
        "constitution_of_business": re.search(r"4\.\s*Constitution of Business\s*(.*?)\n", text),
        "address": re.search(r"5\.\s*Address of.*?\s*(.*?)\n", text),
        "date_of_validity_from": re.search(r"From\s*(\d{2}/\d{2}/\d{4})", text),
        "date_of_validity_to": re.search(r"To\s*(Not Applicable|\d{2}/\d{2}/\d{4})", text),
        "type_of_registration": re.search(r"8\.\s*Type of Registration\s*(\w+)", text),
    }

    # Step 3: Clean the result
    for key, match in data.items():
        data[key] = match.group(1).strip() if match else None

    return data

# Example usage
if __name__ == "__main__":
    pdf_path = "sample.pdf"  # Replace with your actual PDF file path
    result = extract_data_from_pdf(pdf_path)
    print(json.dumps(result, indent=2))
