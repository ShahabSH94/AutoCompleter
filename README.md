# AutoCompleter
 Auto Complete anything with a ggml model
 
 
a simple script that lets you auto-complete anything anywhere using your favorite ggml model

symbol document mode:
in this mode enter the absolute path to your document for example C:\Users\file.txt in .env file
then on wherever you want completion just put the symbol(default=$$) on there then for example:
def helloworld()
    print$$
then press shift+ctrl hopefully you will get something like ("Hello, world!") then remove the symbol if you dont want any more completions on that line

if you didnt like what you got just ctrl+z to undo

some programs lock the file while the file is opened in that program so currently they're not supported also some other programs might not support undo
if file was edited from another program in that case you might want to use clipboard mode

clipboard mode:
in this mode copy the text you want completion for then press shift+ctrl to get completion if autopaste in .env file is set to true
then the completion will get pasted at your cursor onto whatever field its on if not you will hear a beep indicating that your completion is ready

how to use:
install the requirements using pip, edit the .env file to your needs then run the script
tested on windows for linux you might have to run the script as admin
