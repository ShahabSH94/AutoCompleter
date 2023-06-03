# AutoCompleter
 Auto Complete anything using a ggml model
 
 
a simple script that lets you auto-complete anything anywhere using your favorite ggml model

example for prompt generation in Stable Diffusion web UI in clipboard mode:



![ezgif-4-57adb8e040](https://github.com/ShahabSH94/AutoCompleter/assets/121495598/da8d9e62-3f5f-40e7-9ff1-c3d504f771b6)

the example prompt is based on this: https://civitai.com/images/882671?modelVersionId=78164&prioritizedUserIds=53515&period=AllTime&sort=Most+Reactions&limit=20

the model that was used for fastest inference and decent quality (q4_0): https://huggingface.co/TheBloke/Wizard-Vicuna-7B-Uncensored-GGML

symbol document mode:
in this mode enter the absolute path to your document for example C:\Users\file.txt in .env file
then on wherever you want completion just put the symbol(default=$$) on there then for example:
def helloworld()
    print$$
then press shift+ctrl hopefully you will get something like ("Hello, world!") then remove the symbol if you dont want any more completions on that line

if you didnt like what you got just ctrl+z to undo

some programs lock the file while the file is opened in that program so currently they're not supported in this mode also some other programs might not support undo
if file was edited from another program in that case you might want to use clipboard mode

clipboard mode:
in this mode copy the text you want completion for then press shift+ctrl to get completion if autopaste in .env file is set to true
then the completion will get pasted at your cursor onto whatever field its on if not you will hear a beep indicating that your completion is ready then just press ctrl+v to paste it whereever you want.

how to use:
clone the repo , install the requirements using pip, edit the .env file to your needs then run the script
tested on windows for linux you might have to run the script as sudo

if you dont have a ggml model get one from here https://huggingface.co/TheBloke


Credits:

https://github.com/ggerganov/llama.cpp

https://github.com/abetlen/llama-cpp-python
