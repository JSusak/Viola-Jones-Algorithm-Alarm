# Viola Jones Algorithm Alarm

This project was made in a few hours, stemming from an idea which came to me as I woke up :)  
The **Viola Jones Algorithm Alarm** makes use of the OpenCV library (discussed below) in order to capture real time footage of a computer webcam, providing alerts whenever a face appears.

Footage is consistently recorded and played back for the user, while also detecting the prescence of any defining facial features. A periodic timer occurs to process a single frame captured at that moment - If a rough outline of a face IS detected in the frame, an external JSON file is updated as well as tables in a database created with SQLite3 with the time of detection, the image is saved to an external folder to view later and a blaring alarm plays >:)

Making this fun program was an introductory gateway into **object detection frameworks** and **computer vision** alongside the brushing up of my Python skills which I haven't done for a while (due to learning Java for my CS classes and JavaScript for my Discord bot).

# Prerequisites

- A webcam (self-explanatory :D)
- Installation of the OpenCV library
- A recent version of Python (I used `3.7.0`)

# How to build

This program was implemented using _Visual Studio Code_, any instructions here are under the assumption that you also used this IDE.

- Install the [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) in your environment, allowing you to run code just by right clicking a desired .py file.
- Fork the project OR clone it by running `git clone https://github.com/JSusak/Viola-Jones-Algorithm-Alarm.git`

# Connecting your Android Device

This program does have the ability to render the algorithm through an Android phone, working in the same manner as if a webcam was attached to your PC. However, if you already have a webcam I would personally not follow these instructions as I have found the algorithm to be quite inaccurate while taking video footage from your phone - this is probably due to your phone camera being able to move so quickly whereas a webcam is in one place all the time.
FURTHERMORE, I have noticed that the specific site that you have to use is considered insecure - I have tested the site and it does work but a further check has to be uncommented in the code, which you will have to do yourself if you want to access the footage which will be used in the code. Nevertheless, here are the steps to take if you wish to do it:

- Download the [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en&gl=US) app from the play store.
- Open it and modify the settings to your liking - I chose to turn the sound off on my version, I would recommend you do it too.
- When the camera starts you should notice two links under the IPv4 header - Copy that link into a browser. It should have the structure: "https://abc.def.g.hij:klmn"
- On the site, under "Video Renderer" click "Javascript".
- When you run the code AND have uncommented the right line in algo.py (verify=False) the footage from your phone should appear if you type 'phone' on the main menu!

I haven't found an implementation for iOS devices (sorry Apple users :( )

# Contributions

The implementation still has lots of room for improvement to become more refined. I am currently attempting to:

- Make asynchronous code, in order to display JSON statistics at certain intervals WITHOUT affecting code performance.
- Find some more Haar Cascade files for other features (maybe ears, nose, perhaps even full body eventually) OR create my own (which may be excruciatingly arduous!)

# What is the Viola-Jones Algorithm?

In VERY simple terms, the Viola-Jones algorithm is a method of object detection mainly concerned with distinguishing facial features. It was proposed in 2001 and can work on both images and real-time video. It is best performed on greyscale images.
It works based on **Haar Features** which essentially gets the pixel intensity of each region. To speed up detection, images can be converted to an **integral image** - it can be generated through the equation shown below - For each pixel in the original image, the value in the integral imagine is the value from the original image + all values above and to the left of the value.

<img src="./resources/int_eq1.svg">
[wip]

# OpenCV

[OpenCV](https://opencv.org/about/) is a very popular library aimed extensively for features relating to computer vision and machine learning. I would recommend you to check it out and see the powerful features it is capable of! (If you have the time of course :))

I hope you enjoy looking at this project - Feel free to contribute to anything you would like.
~ Josh
