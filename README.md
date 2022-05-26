# Viola Jones Algorithm Alarm

This project was made in a few hours, stemming from an idea which came to me as I woke up :)  
The **Viola Jones Algorithm Alarm** makes use of the OpenCV library (discussed below) in order to capture real time footage of a computer webcam, providing alerts whenever a face appears.

Footage is consistently recorded and played back for the user, while also detecting the prescence of any defining facial features. A periodic timer occurs to process a single frame captured at that moment - If a rough outline of a face IS detected in the frame, an external JSON file is updated with the time of detection, the image is saved to an external folder to view later and a blaring alarm plays >:)

Making this fun program was an introductory gateway into **object detection frameworks** and **computer vision** alongside the brushing up of my Python skills which I haven't done for a while (due to learning Java for my CS classes and JavaScript for my Discord bot).

# Prerequisites

- A webcam (self-explanatory :D)
- Installation of the OpenCV library
- A recent version of Python (I used `3.7.0`)

# How to build

This program was implemented using _Visual Studio Code_, any instructions here are under the assumption that you also used this IDE.

- Install the [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) in your environment, allowing you to run code just by right clicking a desired .py file.
- Fork the project OR clone it by running `git clone https://github.com/JSusak/Viola-Jones-Algorithm-Alarm.git`

# Contributions

The implementation still has lots of room for improvement to become more refined. I am currently attempting to:

- Make asynchronous code, in order to display JSON statistics at certain intervals WITHOUT affecting code performance.
- Find some more Haar Cascade files for other features (maybe ears, nose, perhaps even full body eventually) OR create my own (which may be excruciatingly arduous!)

# What is the Viola-Jones Algorithm?

In VERY simple terms, the Viola-Jones algorithm is a method of object detection mainly concerned with distinguishing facial features. It was proposed in 2001 and can work on both images and real-time video. It is best performed on greyscale images.
It works based on **Haar Features** which essentially gets the pixel intensity of each region. To speed up detection, images can be converted to an **integral image** - it can be generated through the equation shown here:

![image][./resources/int_eq1.svg]

# OpenCV

[OpenCV](https://opencv.org/about/) is a very popular library aimed extensively for features relating to computer vision and machine learning. I would recommend you to check it out and see the powerful features it is capable of! (If you have the time of course :))

I hope you enjoy looking at this project - Feel free to contribute to anything you would like.
~ Josh
