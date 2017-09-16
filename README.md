﻿# GPU-Viewer
A front-end to glxinfo and Vulkaninfo. 

This project aims to capture all the required/important details of glxinfo and vulkaninfo in a GUI. The project is being developed using python 3 with tkinter (python3-tk). All the required/Important details were extracted using glxinfo/vulkaninfo with the combination of grep, CAT , AWK commands and displayed in the front-end. There is no hard OpenGL Programming involved, until glxinfo and vulkaninfo works the GPU-viewer will also work

[GitHub](https://ibb.co/hE9QTk)

## INSTALLATION STEPS

1. Before Downloading the files please ensure python3-tk is installed(sudo apt-get install python3-tk).
2. Download the file and Extract to a folder
3. Double click GPU Viewer to launch the Application or You can go to Files and then open terminal and run/type python3 GPU_Viewer.py
4. For Vulkan Tab to work Install Vulkan-Utils (sudo apt-get install vulkan-utils),also Vulkan enabled drivers should be installed.


## What's developed and available?

1. OpenGL Tab - OpenGL Information, OpenGL ES Information, OpenGL hardware limits and Extensions displayed as per different Vendors,GLX Frame Buffer Configuration
2. Vulkan Tab - Device Features, Device Limits, Device Extensions,Formats,Memory Types & Heaps, Partial Queue Families implemented, Instance and Layers


## UNDERDEVELOPMENT

1. OpenGL - Minor Bug fixes, OpenGL SPIRV support (low priority)
2. Vulkan - Looking into VkSurfaceCapabilities Tab, Development yet to start

## IMPORTANT

1. Requires Python 3 and python3-tk to run this Application, works only on linux Operating system
2. Tested on Intel and Nvidia hardware
3. For Vulkaninfo to work, nvidia, Mesa and AMD vulkan enabled drivers should be installed along with vulkan-utils
4. Vulkan Tab should work fine on 2 way and 3 way SLI/crossfire.

## KNOWN ISSUES

1. 4 Way SLI/crossfire will not work for Vulkan Tab.
2. Minor UI issues.
3. Not tested on hardware other than Intel and Nvidia
4. GLX Frame Buffer Configuration should work almost fine If there are any Blank values in the report the alignment   goes out(mainly in GLXFBConfigs). Yet to figure out a fix.
5. Devices which are not supporting OpenGL ES will experience few data/UI issues.

## DEVELOPMENT ENVIRONMENT

1. Operating System : Linux Mint 18.2 (Sonya)
2. Desktop : Cinnamon 3.4.6
3. Kernel : 4.10.0-33
4. IDE : SublimeText 3.0

## SYSTEM SETUP

1. ASUS G551JK ROG Laptop
2. Quad Core Intel Core i7-4710HQ
3. Nvidia Geforce GTX 850m (Discrete GPU) , Drivers - Nvidia (propriatery) 
4. Intel Haswel Mobile (Integrated GPU) , Drivers - MESA (Open Source)
5. 8 GB RAM

If you like/use this Application and think i deserve a cup of chai, do a Paypal donation: https://www.paypal.me/ArunSivaraman
