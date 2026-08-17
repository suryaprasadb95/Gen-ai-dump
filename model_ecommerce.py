from http import client

import google.generativeai as genai
from openai import api_key
from openai import api_key
import pandas as pd
import numpy as np
import json



def extract_attributes(sd, ld):
    prompt = f"""
    Based on the following item descriptions, 
    Short Description (SD): {sd}
    Long Description (LD): {ld}
    extract/predict the required  below attributes:
    Battery Type, Design, Is Portable, Weight Type.
    give the output in json format  
    """
    
    # genai.configure(api_key="")
  
    model = genai.GenerativeModel("gemini-3.5-flash-lite")


    # Call a Google Gemini model using the OpenAI format
    response = model.generate_content(prompt)
    # response = client.models.generate_content(
    # model="gemini-3.6-flash", 
    # contents="Hello!"
    # )

    print(response.text)

    return (response)


def get_parsed_response(response):
    return json.loads(response.choices[0].message.content)


if __name__ == "__main__":
    # Load your Excel or CSV file
    file_path = r"D:\Surya\github-repos\Gen-ai-dump\E-commerce Sample.csv"
    df = pd.read_csv(file_path)
    # print(df)

    # Ensure columns E to H exist (replace 'Attr_E', 'Attr_F', etc. with your column names)
    target_columns = ["Battery Type", "Design", "Is Portable", "Weight Type"]


    # Iterate through each row and fill columns E to H
    for idx, row in df.iterrows():
        sd_val = row.get("SD", "")
        ld_val = row.get("LD", "")

        extracted = extract_attributes(sd_val, ld_val)
        with open("output.txt", "a", encoding="utf-8") as file:
            file.write(extracted.text )
    # for col in target_columns:
    #     df.at[idx, col] = (extracted or {}).get(col, np.nan)

    # # Save the updated file
    # df.to_excel(r"d:/Surya/github-repos/Gen-ai-dump/updated_file.xlsx", index=False)
    # print("File successfully processed and saved!")

