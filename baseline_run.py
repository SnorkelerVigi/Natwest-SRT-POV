import pandas as pd
import PyPDF2
import os
from google import genai
import datetime
import re
import numpy as np
import time
from google.genai import types
from dotenv import load_dotenv
load_dotenv()
from response_types import *
from question_class_mapping import get_classes_for_question
import json


GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=GEMINI_API_KEY)

model_name="gemini-2.0-flash"

SYSTEM_PROMPT = """
You are to review a provided facility agreement in context to determine how the agreement affects the inclusion of assets in Significant Risk Transfers (SRTs).
Your purpose is to identify provisions regarding confidentiality, transferability, consents, confidentiality undertakings, approved lender lists, and any conditions that must be satisfied for including the asset in an SRT.
Your final output must be sufficiently clear, detailed, and legally accurate so that a legal team can rely on it directly.

In cases where the options for you to respond with are explicitly provided in the user prompt, you are required to respond with the most appropriate option and nothing else in your response.

Here is the full text of the facility agreement:
"""

def get_pdf_text(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PyPDF2.PdfReader(f)
        text = ''
        for page in range(len(pdf.pages)):
            text += pdf.pages[page].extract_text()
        return text
    
def get_initial_contents(text):
    contents = [
        {
            "role": "user",
            "parts": [{"text": SYSTEM_PROMPT + "\n\n" + text}]
        }
    ]
    return contents


if __name__ == "__main__":
    df = pd.read_csv('/Users/vigneshramesh/Desktop/Deals/Natwest/baseline_run_filled_2.5.csv')
    df.fillna('', inplace=True)
    df.drop(columns=['Response'], inplace=True)

    pdf_folder = '/Users/vigneshramesh/Desktop/Deals/Natwest/SRT Checklist Groundtruths'
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith('.pdf'):
            print('Processing: ', pdf_file)
            pdf_path = os.path.join(pdf_folder, pdf_file)
            column_name = pdf_file.replace('.pdf', '')
            df[column_name] = ''  # Add new column for this PDF's responses
        text = get_pdf_text(pdf_path)

        for category, group_df in df.groupby('Question Category'):
            
            contents = get_initial_contents(text)

            for index, row in group_df.iterrows():

                contents.append({
                        "role": "user",
                        "parts": [{"text": row['Question Text']}]
                    })

                response_schema, _ = get_classes_for_question(row['Question Text'])

                response = client.models.generate_content(
                    contents=contents,
                    model=model_name,
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json",
                        response_schema=response_schema if response_schema else None
                    )
                )
                match = re.search(r"```json\s*({.*?})\s*```", response.text, re.DOTALL)

                if match:
                    json_str = match.group(1)
                    data = json.loads(json_str)
                    append_text = str(data['response'])
                else:
                    data = response.text
                    append_text = response.text

                df.at[index, column_name] = data
                contents.append({
                    "role": "model",
                    "parts": [{"text": append_text}]
                })
                
            df.to_csv('/Users/vigneshramesh/Desktop/Deals/Natwest/baseline_run_filled_2.0_AllDocs.csv', index=False)
        print('Completed: ', pdf_file)