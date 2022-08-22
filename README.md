# YouTube-Caption-Bot
Simple tool to find the words most used by a YouTube channel. Tool is written in Python with GUI implemented using TkInter. If you're in a hurry, just download the executable included and start using. If you prefer to build yourself, follow the steps below.

# Usage
1. Clone the repository to your local system.

  `git clone https://github.com/arpmay/YouTube-Caption-Bot.git`
  
2. cd to the repository on your local system and run main.py

  `python main.py`
  
3. The following gui window should show up:

![image](https://user-images.githubusercontent.com/19332781/185915148-e55eed05-a2fd-4b17-a164-0e075544f24b.png)

  
4. Enter the link to the channel that you want to scan in the Channel link box. The number of videos you want to scan in No. of videos to scan box, and the number of words you want in result in No. of results box.

5. Click Start button to start the program.

6. Depending on the number of vidoes, it may take some time.

7. The results are shown in the textbox below.

# Building stand-alone GUI app
1. Clone the repository to your local system.

  `git clone https://github.com/arpmay/YouTube-Caption-Bot.git`
 
2. Install Pyinstaller to your system.

  `pip install pyinstaller`
  
3. cd to the local directory where you downloaded this repository.

4. Run pyinstaller to create executable.
  `pyinstaller --onefile main.py`

5. After pyinstaller is done, you should get an executable in the same directory.
