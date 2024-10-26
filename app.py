import os
os.system(f'pip install google.generativeai python-dotenv streamlit')
os.system('cls' if os.name == 'nt' else 'clear')
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-1.0-pro")
convo = model.start_chat(history=[])

# Universal variable
final_program =''

if os.path.exists("C:\\UniversalProgram"):
     pass
else:
     os.mkdir("C:\\UniversalProgram")
basefile = 'C:\\UniversalProgram\\basefile.py'

# Methods
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def requirements(program):
    convo.send_message("write only requirements file code  without any description not even single other word for below program:\n"+program)
    requirement = str(convo.last.text).replace("```","")
    with open("requirements.txt",'w') as f:
          f.write(requirement)
    os.system(f'pip install -r requirements.txt')

def modified_program(prompt):
    convo.send_message("write only program including driver code in python without any additional text.\n"+prompt)
    updated_program=str(convo.last.text).replace("```",'')
    updated_program = updated_program.replace("python",'')
    requirements(updated_program)
    return updated_program


def admin():
        try:
            with open(basefile, 'r') as f:
                original_content = f.read()
                #print("Original code:\n",original_content)
        except:
            with open(basefile,'w') as f:
                 f.write("# File Created")
            with open(basefile, 'r') as f:
                original_content = f.read()
                print("Original code:\n",original_content)

        # Reading the prompt to modify base block
        prompt = input("Explain your Program :\n")
        global updated_program
        updated_program = modified_program(prompt)
        final_program = updated_program

            # Checking format of programs
            #print("Base Block :\n",tuned_block)
            #print("Updated Base Block:\n",updated_program)

        original_content = original_content.replace(original_content,updated_program)

        with open(basefile, 'w') as f:
                f.write(original_content)
                print("Successfully Modified")

def base():
    print("Exucuting Program:")
    print(updated_program)
    if "streamlit" in updated_program :
         print("streamlit Command")
         os.system(f'streamlit run {basefile}')
    else:
        print("Python command")
        os.system(f'python {basefile}')


if __name__ =="__main__":
    admin()
    clear()
    base()
    