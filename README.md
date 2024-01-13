# Badge generation script

This is a simple python script that allows for generating identification badges for participants of an event.

The program requires several files to be placed in the execution directory, in order to run:
 - A list of names and titles, separated by a newline character. The entries should look as follows `Paweł Zaręba Event coordinator`. The file should be named `names.txt`, alternatively the `NAMES_FILE` variable can be modified to reflect the actual file name.
 - A background for the generated badges. The script assumes that it is called `background.jpg`, however this can be changed by modifying the `BACKGROUND_FILE` variable. The format of the background file shouldn't make a difference (however I have only tested this script with jpg files).
 - A specific font in `.ttf` format. This example uses `UnicaOne-Regular.ttf`, but any valid ttf file will work. To use a different file, modify the `FONT_FILE` variable.


To run this code, first install the dependencies via:
```shell
pip install -r requirements.txt
```

Then just execute the script:
```shell
python3 main,py
```




Please note that this code was not meant to be pretty or serve as a good example of how to interact with Python or the Reportlab library. It was written over 2 years ago at 3AM to solve a spefific issue, and I'm only sharing it here, since I've been asked for it n-th time :D.