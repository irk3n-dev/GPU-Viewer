﻿# GPU-Viewer
**A front-end to glxinfo, vulkaninfo and clinfo.** 


This project aims to capture all the important details of glxinfo, vulkaninfo and clinfo in a GUI. The project is being developed using python 3 pygobject with GTK3. All the important details are extracted using glxinfo/vulkaninfo/clinfo with the combination of grep, CAT , AWK commands and displayed in the front-end. There is no hard OpenGL Programming involved, until glxinfo, vulkaninfo and clinfo works the GPU-viewer will also work

![screenshot from 2018-03-21 21-01-50](https://user-images.githubusercontent.com/30646692/37719689-91039ad2-2d4b-11e8-9c97-4b314850f7a7.png)

![screenshot from 2018-03-21 21-02-08](https://user-images.githubusercontent.com/30646692/37719719-a558121a-2d4b-11e8-8a46-24299e456f85.png)

![screenshot from 2018-03-21 21-02-24](https://user-images.githubusercontent.com/30646692/37719740-b3e88b5c-2d4b-11e8-909e-3bfea6e0cde2.png)

![screenshot from 2018-03-21 21-04-44](https://user-images.githubusercontent.com/30646692/37719766-c47d228e-2d4b-11e8-96f9-c9a0b4bbaf45.png)

* Please note that the above images solely depends on the Theme being used on the system. Recommended themes are Flat-Plat and Adapta

## INSTALLATION STEPS 

1. Before Downloading the files please see the Known issues mentioned below
2. Ensure python is installed
3. **Ubuntu 18.04 (Bionic)/Ubuntu 17.10 (Artful)/Ubuntu 17.04 (Zesty)/Ubuntu 16.04 (Xenial)/Linux Mint 18.x** users should be able to install this application using the below PPA

    * sudo add-apt-repository ppa:arunsivaraman/gpuviewer
    * sudo apt-get update
    * sudo apt-get install gpu-viewer
    
    Please note all the dependencies python, vulkan-utils,clinfo will be installed, if not installed before.
    
4. **Debian based distro** users should be able to install the application by just running the .deb file https://github.com/arunsivaramanneo/GPU-Viewer/blob/master/gpu-viewer_1.8b1-1_amd64.deb
5. **Arch based distro** - 	[![AUR package](https://repology.org/badge/version-for-repo/aur/gpu-viewer.svg)](https://repology.org/metapackage/gpu-viewer) - users should be able to grab the application at https://aur.archlinux.org/packages/gpu-viewer/ or by running command **yaourt -s gpu-viewer** from the terminal . This should automatically take care of the dependencies. Thanks to Dan Johnson (strit)for maintaining the AUR Package
6. For others please follow steps 6 to 9
7. Download the file and Extract to a folder
8. Navigate to extracted folder, open terminal and enter ./install and follow on-screen instruction.
9. Once completed,Application can be accessed at menu->System/Administration/System tools->GPU Viewer
10. For **Vulkan Tab** to work Install Vulkan-Utils (sudo apt install vulkan-utils) in Ubuntu, Vulkan-extra-layers in Arch, Vulkan in Solus, also Vulkan enabled drivers should be installed.
The installer should be able to take care of this dependency in Debian based distro and Solus.
11. For **OpenCL Tab** to work install clinfo (sudo apt install clinfo) in ubuntu , clinfo in Solus (sudo eopkg install clinfo), clinfo in arch. Also, ensure you have OpenCL installed for your respective platforms, Ex. Nvidia CUDA for Nvidia hardware, beignet for Intel Graphics or pocpl for cpu or AMD openCL for AMD hardware.
12. Some distro's don't come with glxinfo installed by default, so you will need to install mesa-utils to get the OpenGL Tab displayed properly.
13. Incase of issues launching the application please see the FAQ in Wiki section

## UNINSTALL STEPS

1. Debian users should be able to uninstall in the default way i.e. sudo apt remove gpu-viewer
2. For others, Remove gpu-viewer directory in \usr\share\  or run sudo rm \usr\share\gpu-viewer -r to remove. Also you need to remove the symlink by running sudo rm \usr\bin\gpu-viewer

## What's developed and available?

1. OpenGL Tab - OpenGL Information, OpenGL ES Information, OpenGL hardware limits and Extensions displayed as per different Vendors, View GLX Frame Buffer Configuration
2. Vulkan Tab - Device Features, Device Limits, Device Extensions,Formats,Memory Types & Heaps, Partial Queue Families implemented, Instance and Layers,Surface Tab
3. OpenCL Tab - Platform Details, Device Details , Device Memory & Image Details, Device Queue and Execution capabilities, Device Vector Details, Total No. of Platforms, No. of Devices for the platform.
4. About Tab - About GPU Viewer Application, ability to report a bug,view license,view change log, Donate via paypal, GPU Viewer Github main page.


## UNDER DEVELOPMENT

1. General - Bug fixes, Code Optimizations (High Priority)

## PLANNED DEVELOPMENT

1. OpenGL SPIR Support (Provided glxinfo gets updated to show SPIRV details or any other Command line)

## IMPORTANT

1. Requires Python to run this Application, works only on linux Operating system
2. For Vulkan Tab to work, nvidia, Mesa and AMD vulkan enabled drivers should be installed along with vulkan-utils
3. For OpenCL Tab to work, install clinfo along with OpenCL drivers for your respective GPU's

## KNOWN ISSUES

1. Minor UI issues.
2. The Extensions drop down menu in OpenGL tab will not render well if there are too many items, users may see a big empty space at the start. This is a GTK issue (https://github.com/arunsivaramanneo/GPU-Viewer/issues/9)
3. The Application does not render well under dark themes.

## DEVELOPMENT ENVIRONMENT

1. Operating System : Linux Mint 18.2 (Sonya)/Solus 3/Ubuntu Budgie
2. Desktop : Cinnamon 3.6/Budgie 10.4
3. Kernel : 4.14.8
4. IDE : SublimeText 3.0,IntelliJ IDEA Community Edition


## SYSTEM SETUP

1. ASUS G551JK ROG Laptop
2. Quad Core Intel Core i7-4710HQ
3. Nvidia Geforce GTX 850m (Discrete GPU) , Drivers - Nvidia (proprietary)
4. Intel Haswel Mobile (Integrated GPU) , Drivers - MESA (Open Source)
5. 8 GB RAM

**If you like/use this Application,consider supporing us by DONATING at PayPal https://www.paypal.me/ArunSivaraman.**
