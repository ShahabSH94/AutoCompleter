import keyboard
from llama_cpp import Llama
from dotenv import dotenv_values
import pyperclip
import winsound
env_vars = dotenv_values('.env')
while True:
    print("""autocomplete Anything
Select mode
1.symbol document mode
2.clipboard mode
3.help
    """)
    usrcmd = input(">>")
    if usrcmd in ["1","2","3"]:
        usrselection = usrcmd
        if usrselection == "1":
            try:
                documentpath = env_vars['document-path']
            except Exception as e:
                print(f"{e}")
            break
        if usrselection == "2":
            break
        if usrselection == "3":
            with open("README.md","r") as f:
                print(f.read())  
    else:
        print("wrong entry")

modelpath = env_vars['Model-path']
CTX_MAX = int(env_vars['Max-Context'])
n_threads = int(env_vars['n_threads'])
autopaste = False if (env_vars['autopaste']).lower() == 'false' else True
maxtokens = int(env_vars['max_tokens'])
try:
    symbol = env_vars['symbol']
except:
    symbol = "$$"
temperature = float(env_vars['temperature'])
repeat_penalty=float(env_vars['repeat_penalty'])
llm = Llama(model_path=modelpath,n_ctx=CTX_MAX,n_threads=n_threads)
promptslice = int(CTX_MAX - CTX_MAX/3)
if usrselection == "1":
    file = documentpath
print("waiting for key press")
def GetCompleterResponse(prompt:str):
    output = llm(prompt=prompt,temperature=temperature,repeat_penalty=repeat_penalty,max_tokens=maxtokens)
    return output['choices'][0]['text'].strip()#,top_p=top_p,top_k=top_k)
def get_lines_within_max_length(lines, max_length):
    total_length= 0
    if usrselection == "1":
        lines = [line.split(symbol)[0] for i, line in enumerate(lines) if symbol in line for line in lines[:i+1]]
    for i in range(len(lines)-1, -1, -1):
        total_length += len(lines[i])
        if total_length > max_length:
            return lines[i+1:]
    return lines
def get_prediction():
    print('get_prediction Key was pressed.')
    if usrselection == "1":
        with open(file, "r") as f:
            lines = f.read().split("\n")
        symbolcount =0
        for i in lines:
            if symbol in i:
                symbolcount+=1
            if symbolcount > 1:
                print("symbol in multiple lines make sure only one symbol is in the document")
                break
        if symbolcount == 1:
            prevlines = get_lines_within_max_length(lines,promptslice)
            prompt = (lambda lines: "\n".join([line for line in lines]))(prevlines).replace(symbol,"")
            response = GetCompleterResponse(prompt)
            new_content = '\n'.join([(line[:line.index(symbol)] + response + line[line.index(symbol):]) if symbol in line else line for line in lines])
            with open(file,'w') as f:
                f.write(new_content)
    else:
        clipboard_data = pyperclip.paste()
        prompt = get_lines_within_max_length(clipboard_data,promptslice)
        response = GetCompleterResponse(prompt)
        pyperclip.copy(response)
        if autopaste:
            keyboard.press_and_release("ctrl+v")
        else:
            winsound.Beep(450, 200)
    print("auto-completion was successful")

keyboard.add_hotkey('shift+ctrl', get_prediction)
keyboard.wait()