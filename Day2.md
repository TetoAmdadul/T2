> git config --global user.email "ridhomteto@gmail.com"
for config github new device


>git config --global user.name "Your Name"



> git config --global --list
for seeing the changes

>rm ~/.gitconfig
for removing git config if there is eror

****** for sending or
started writing code or notes locally first. Since the files already exist on your Mac, you must initialize the folder and link it manually:
bash
git init
git remote add origin <URL>
git push -u origin main
********

******
You start with an empty project (Future projects)
Next time, create the repository on the GitHub website first. Then, download it to your Mac immediately before adding any files:
bash
git clone <URL>
cd <repo-name
********'

git commit is like hitting Save on a file on your desktop.
git push is like uploading that saved file to the Cloud.
git pull is like downloading the latest version of that file from the Cloud to your desktop.
Would you like to try running git status right now to see if your Mac is currently ahead or behind your GitHub repository?

********

Git commands do not auto-complete by default because Git is an external program, and your terminal shell (like Bash or Zsh) does not automatically know Git's internal commands, branches, or options. You need to enable a specific autocomplete script to bridge this gap. 
How to Fix It
Select the section below that matches your operating system and terminal shell.
macOS (Using Zsh - Default)
Open your terminal.
Open your configuration file by running: nano ~/.zshrc
Add the following lines to the bottom of the file:
zsh
autoload -Uz compinit && compinit
zstyle ':completion:*:*:git:*' script ~/.zsh-git-completion.zsh
Use code with caution.
Press Ctrl + O then Enter to save, and Ctrl + X to exit.
Reload your shell by running: source ~/.zshrc 

**********

> echo ".name" > .gitignore
 