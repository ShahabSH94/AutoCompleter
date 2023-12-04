# AutoCompleter
 Auto Complete anything using a gguf model
 
 
a simple script that lets you auto-complete anything anywhere using your favorite gguf model

New Changes:


-you can now get completion token by token  instead of waiting for it to finish

-folder mode , now you can specify a folder and filetypes and you can use the symbol on files inside the folder(only one symbol at at a time)

example for code completion in vscode:


![ezgif-4-57adb8e040](https://github.com/ShahabSH94/AutoCompleter/blob/c03688b8caf3eab6d4eca1668264c3b2b521c19d/example.gif)


symbol document mode:
in this mode enter the absolute path to your document for example C:\Users\file.txt in .env file
then on wherever you want completion just put the symbol(default=$$) on there then for example:
def helloworld()
    print$$
then press shift+ctrl hopefully you will get something like 
def helloworld()
    print("Hello, world!")



folder symbol mode:
set a folder in .env and specify file types program will scan all those files and and you will get predictions on the file where the symbol is.

some programs lock the file while the file is opened in that program so currently they're not supported in these mode
if file is locked from another program in that case you might want to use clipboard mode.


clipboard mode:
in this mode copy the text you want completion for then press shift+ctrl to get completion then the completion will get pasted at your cursor onto whatever field its on

-you can press shift+ctrl again in any mode to stop the completion while its happening

how to use:
clone the repo , install the requirements using pip, edit the .env file to your needs then run the script
tested on windows for linux you might have to run the script as sudo

if you dont have a gguf model get one from here https://huggingface.co/TheBloke


Credits:

https://github.com/ggerganov/llama.cpp

https://github.com/abetlen/llama-cpp-python
