# AutoCompleter
 Auto Complete anything using a ggml model
 
 
a simple script that lets you auto-complete anything anywhere using your favorite ggml model

example for prompt generation:
https://github.com/ShahabSH94/AutoCompleter/assets/121495598/e7c22714-deea-43ba-a5f7-7b781ed4c5d7

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
tested on windows for linux you might have to run the script as admin

if you dont have a ggml model get one from here https://huggingface.co/TheBloke



