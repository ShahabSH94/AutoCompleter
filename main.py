from keyboard import press_and_release ,add_hotkey ,wait
from llama_cpp import Llama
from dotenv import dotenv_values
from pyperclip import copy,paste
from utils import slicePromptIfExceedsWarningCtx
from threading import Thread, active_count , enumerate
from os import listdir , path
env_vars = dotenv_values('.env')
try:
    symbol = env_vars['symbol']
except:
    symbol = "$$"
usrselection = ''
class Completer():
    def __init__(self) -> None:
        self.docFolder = env_vars["doc_folder"] if 'doc_folder' in env_vars.keys() else ''
        self.file = env_vars["document_path"] if 'document_path' in env_vars.keys() else ''
        self.fileTypes = env_vars['file_types'].split(',') if 'file_types' in env_vars.keys() else ''
        self.modelpath = env_vars['Model_path'] if env_vars['Model_path'] != '' else ''
        self.CTX_MAX = int(env_vars['Max_Context'])
        self.n_threads = int(env_vars['n_threads'])
        self.maxtokens = int(env_vars['max_tokens'])
        self.temperature = float(env_vars['temperature'])
        self.repeat_penalty=float(env_vars['repeat_penalty'])
        self.llm = Llama(model_path=self.modelpath,n_ctx=self.CTX_MAX,n_threads=self.n_threads)  if self.modelpath != '' else print("no model set in .env")
        self.warningCtx = self.CTX_MAX // 30
        self.promptslice = self.CTX_MAX- self.warningCtx
        self.stop = False
    def GetCompleterResponse(self,prompt:str):
        output = self.llm(stream=True,prompt=prompt,temperature=self.temperature,repeat_penalty=self.repeat_penalty,max_tokens=self.maxtokens)
        return output
    def stopPrediction(self):
        self.stop = True
    def get_prediction(self):
        print('get_prediction Key was pressed.')
        symbolcount =0
        if usrselection == "1" or usrselection == '3':
            if usrselection == "1":
                if self.file != '':
                    with open(self.file, "r",encoding="utf-8") as f:
                        doc= f.read()
                        lines = doc.split("\n")
                    for i in lines:
                        if symbol in i:
                            symbolcount+=1
                        if symbolcount > 1:
                            print("symbol in multiple lines make sure only one symbol is in the document")
                            break
                    if symbolcount == 0:
                        print("no symbol found")
                else:
                    print('no document_path set in .env')
            if usrselection == "3":
                if self.docFolder != '':
                    doc , self.file = self.getDocWithSymbol()
                else:
                    print("no doc_folder set in .env")
            if symbolcount == 1 or usrselection == "3":
                prompt = slicePromptIfExceedsWarningCtx(symbol,usrselection,doc,self.promptslice,self.warningCtx,self.CTX_MAX)
                response = self.GetCompleterResponse(prompt)
                new_content = ''
                splitdoc = doc.split(symbol)
                beforeSymbol = splitdoc[0]
                afterSymbol = splitdoc[1]
                completion =''
                for i in response:
                    completion +=i['choices'][0]['text']
                    new_content= beforeSymbol + completion + afterSymbol    
                    with open(self.file,'w',encoding="utf-8") as f:
                        f.write(new_content)
                    if self.stop:
                        break

        else:
            clipboard_data = paste()
            prompt = slicePromptIfExceedsWarningCtx(symbol,usrselection,clipboard_data,self.promptslice,self.warningCtx,self.CTX_MAX)
            response = self.GetCompleterResponse(prompt)
            completion = ''
            for i in response:
                completion+=i['choices'][0]['text']
                copy(completion)
                press_and_release("ctrl+v")
                completion = ''
                if self.stop:
                    break
        print("auto-completion is Done.")
        self.stop = False

    def getDocWithSymbol(self):
        docNames = []
        if self.fileTypes != []:
            if path.exists(self.docFolder):
                for docName in listdir(self.docFolder):

                    for fileType in self.fileTypes:
                        if docName.endswith(fileType):
                            docNames.append(docName)
            for docName in docNames:
                docPath = f'{self.docFolder}\{docName}'
                with open(docPath,'r',encoding="utf-8") as f:
                    doc = f.read()
                    if symbol in doc:
                        return doc , docPath
        else:
            print("no file types specified in .env")


documentpath = ''
while True:
    print("""autocomplete Anything
Select mode
1.symbol document mode
2.clipboard mode
3.symbol folder mode         
4.help
    """)
    usrcmd = input(">>")
    if usrcmd in ["1","2","3",'4']:
        usrselection = usrcmd
        if usrselection == "4":
            with open("README.md","r") as f:
                print(f.read())
          
        
    else:
        print("WRONG ENTRY!")
        continue
    print("waiting for key press")
    break

completer = Completer()

def getPrediction():
    global completer
    print(active_count())
    print(enumerate())
    listofTs =[thread.name for thread in enumerate()]
    if 'get_prediction' not in str(listofTs):
        getpredT = Thread(target=completer.get_prediction)
        getpredT.start()
    else:
        stoppredT = Thread(target=completer.stopPrediction)
        stoppredT.start()

add_hotkey('shift+ctrl', getPrediction)
wait()