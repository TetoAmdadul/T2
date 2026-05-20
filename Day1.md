>keyboard ShortCuts  
>for copy paste (using command + shift + c,x,v)
>for Screenshot (using Cmd + shift + 4)
 for(Option (⌥) + 8  → {
     Option (⌥) + 9  → }
>for [ (Option (⌥) + 8 → [
      Option (⌥) + 9  → ])
>for screenshot (cmd + shift + 3 +   4 +     5)
                               Fsc snip wholesc                
> for the end of the tab (cmd + arrows)
> for undo (cmd + z)
> for redo (cmd + shift + z)
>for ~ (option + ¨¨¨)
>for save(cmd + s)
>for quit (cmd + q)

Commad in Terminal
>keyboard ShortCuts  
>for copy paste (using command + shift + c,x,v)
>for Screenshot (using Cmd + shift + 4)
 for(Option (⌥) + 8  → {
     Option (⌥) + 9  → }
>for [ (Option (⌥) + 8 → [
      Option (⌥) + 9  → ])
>for screenshot (cmd + shift + 3 +   4 +     5)
                               Fsc snip wholesc                
> for the end of the tab (cmd + arrows)
> for undo (cmd + z)
> for redo (cmd + shift + z)
>for ~ (option + ¨¨¨)

New Commad in Terminal

>sudo useradd -m username
-m will create home directory

>sudo userdel -r username
-r will remove the home directory 

> sudo usermod -d 'username' directory path username

>sudo passwd -S username
 To check if the user have password or not, -P means user has usable password 

>sudo wc -l /etc/passwd
To find how many user in the directory. Because -l means number of lines, pass is one line for each

>ls -ld for finding directory
 Ls -ld directory name or path for finding the list



>sudo passwd username
To set password

>sudo grep -w 'username' /etc/passwd
For verifying is the user home directory or user shell has changed or not

> sudo usermod -s /bin/bash username 
To change from bin to bash

>sudo passwd -l username
For locking the user

>sudo passwd -u joker
For unlocking the user

>sudo ls -ld directory

>uname -m (For finding apple type/ os version)

>cp mv rm
cp for duplicating files and directories, mv for both moving and renaming them, and rm for removing them when they are no longer needed

>ln 
>ln -s
Soft Links (Symbolic Links): Created using ln -s. These are essentially shortcuts. If you delete the original file, the link becomes "broken" because it just points to the path of the original.
Hard Links: Created using just ln. These act as an exact mirror of the file. Even if you delete the original filename, the data persists as long as at least one hard link to it remains.


How to create default setting:
> defaults write com.apple.screencapture location ~/Desktop/RidhomTeto/Git/SC (for setting default location)
> killall SystemUIServer( macOS does NOT apply it instantly. So have run this command)

>hdiutil attach Command_Line_Tools_26.5_Apple_Silicon.dmg
  Mount the .dmg as a virtual disk
Show it in Finder (like a USB drive)
Print a path in Terminal (e.g. /Volumes/...)
>ls /Volumes 
 
It will:

Mount the .dmg as a virtual disk
Show it in Finder (like a USB drive)
Print a path in Terminal (e.g. /Volumes/...)

>sudo installer -pkg "Command Line Tools.pkg" -target /

It will install the git command line

>xcode-select -p
Check CLT path (most important)
What it means:

✅ If you see something like:

/Library/Developer/CommandLineTools

→ CLT is installed and referenced

❌ If you see:

xcode-select: error: unable to get active developer directory

→ CLT is missing or broken

problems:
01.  ![image](/Users/asibulhasan/Desktop/RidhomTeto/Git/SC/Screenshot 2026-05-20 at 1.48.14.png)
    I want to run git command line in terminal but it says I need to install developer command lines
    THEN I Install commandline_tools.dmv file
    I had to mount the file for .pkg file as I can Install it my mac but it didn't work as well.
Then I had to install it manually from the developer website

https://developer.apple.com/download/all/?q=Command%20Line%20Tools

Bingo! 

Git command

Problem o2
I accidentally use git init in my root directory	

> for removing accidental git tracking
  rm -rf .git
n theory, running rm -rf .git means you are completely erasing the "brain" and memory of your Git repository, turning a tracked project back into a regular, ordinary folder.

To understand exactly what it does, it helps to break it down into two parts: what .git actually is, and what the rm -rf command tells your computer to do.

1. What is .git?
Whenever you type git init inside a folder, Git creates a hidden folder named .git.

This hidden folder is the entire database for your project. It stores:

Every single commit and save point you've ever made.

Your entire version history (what the code looked like last week vs. today).

All of your branches and configuration settings.

The actual files you see and edit (like your code, images, or documents) are just a reflection of what is inside this database.

2. What does rm -rf mean?
This is a standard, highly powerful Unix/macOS command line instruction used to delete things permanently.

rm: Short for Remove. It is the basic command to delete files.

-r: Short for Recursive. By default, rm can only delete individual files, not folders. The -r flag tells it to dig down into a folder and delete everything inside it—folders within folders, all the way down to the bottom.

-f: Short for Force. This tells your computer, "Don't ask me 'Are you sure?' for every file. Just delete it all immediately without prompting me."

Putting it together: The Theoretical Result
When you combine them into rm -rf .git, you are forcefully and recursively deleting the hidden Git database.

The theoretical impact of this is twofold:

Your project files are completely untouched: Because you only targeted the hidden .git folder, your actual documents, desktops, or code files remain exactly as they are right now.

The "Time Machine" is destroyed: Your folder completely forgets that Git ever existed. It loses all tracking, all history, and all past versions. It becomes a plain, normal folder on your Mac again.


>uname -m (For finding apple type/ os version)

>cp mv rm
cp for duplicating files and directories, mv for both moving and renaming them, and rm for removing them when they are no longer needed

>ln 
>ln -s
Soft Links (Symbolic Links): Created using ln -s. These are essentially shortcuts. If you delete the original file, the link becomes "broken" because it just points to the path of the original.
Hard Links: Created using just ln. These act as an exact mirror of the file. Even if you delete the original filename, the data persists as long as at least one hard link to it remains.


How to create default setting:
> defaults write com.apple.screencapture location ~/Desktop/RidhomTeto/Git/SC (for setting default location)
> killall SystemUIServer( macOS does NOT apply it instantly. So have run this command)

>hdiutil attach Command_Line_Tools_26.5_Apple_Silicon.dmg
  Mount the .dmg as a virtual disk
Show it in Finder (like a USB drive)
Print a path in Terminal (e.g. /Volumes/...)
>ls /Volumes 
 
It will:

Mount the .dmg as a virtual disk
Show it in Finder (like a USB drive)
Print a path in Terminal (e.g. /Volumes/...)

>sudo installer -pkg "Command Line Tools.pkg" -target /

It will install the git command line

>xcode-select -p
Check CLT path (most important)
What it means:

✅ If you see something like:

/Library/Developer/CommandLineTools

→ CLT is installed and referenced

❌ If you see:

xcode-select: error: unable to get active developer directory

→ CLT is missing or broken

problems:
01.  ![image](/Users/asibulhasan/Desktop/RidhomTeto/Git/SC/Screenshot 2026-05-20 at 1.48.14.png)
    I want to run git command line in terminal but it says I need to install developer command lines
    THEN I Install commandline_tools.dmv file
    I had to mount the file for .pkg file as I can Install it my mac but it didn't work as well.
Then I had to install it manually from the developer website

https://developer.apple.com/download/all/?q=Command%20Line%20Tools

Bingo! 

Git command

Problem o2
I accidentally use git init in my root directory	

> for removing accidental git tracking
  rm -rf .git
n theory, running rm -rf .git means you are completely erasing the "brain" and memory of your Git repository, turning a tracked project back into a regular, ordinary folder.

To understand exactly what it does, it helps to break it down into two parts: what .git actually is, and what the rm -rf command tells your computer to do.

1. What is .git?
Whenever you type git init inside a folder, Git creates a hidden folder named .git.

This hidden folder is the entire database for your project. It stores:

Every single commit and save point you've ever made.

Your entire version history (what the code looked like last week vs. today).

All of your branches and configuration settings.

The actual files you see and edit (like your code, images, or documents) are just a reflection of what is inside this database.

2. What does rm -rf mean?
This is a standard, highly powerful Unix/macOS command line instruction used to delete things permanently.

rm: Short for Remove. It is the basic command to delete files.

-r: Short for Recursive. By default, rm can only delete individual files, not folders. The -r flag tells it to dig down into a folder and delete everything inside it—folders within folders, all the way down to the bottom.

-f: Short for Force. This tells your computer, "Don't ask me 'Are you sure?' for every file. Just delete it all immediately without prompting me."

Putting it together: The Theoretical Result
When you combine them into rm -rf .git, you are forcefully and recursively deleting the hidden Git database.

The theoretical impact of this is twofold:

Your project files are completely untouched: Because you only targeted the hidden .git folder, your actual documents, desktops, or code files remain exactly as they are right now.

The "Time Machine" is destroyed: Your folder completely forgets that Git ever existed. It loses all tracking, all history, and all past versions. It becomes a plain, normal folder on your Mac again.
