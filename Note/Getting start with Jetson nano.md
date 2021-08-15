# Getting Started With NVIDIA Jetson Nano Developer Kit

by Gilbert Tanner on Jun 15, 2020 · 9 min read

![Getting Started With NVIDIA Jetson Nano Developer Kit](https://cms.gilberttanner.com/content/images/size/w1000/2020/08/thumbnail-1.jpeg)

The NVIDIA Jetson Nano Developer Kit is a small edge computer for AI development.

In this article, you'll learn how to get started with the Jetson Nano, including:

- Jetson Nano Overview
- Requirements
- Setup
- Installing prerequisites and configuring your Python environment
- Installing deep learning libraries
- Compiling and installing Jetson Inference
- Running the Jetson Inference demos

## Overview

![ Jetson Nano Interfaces](https://cms.gilberttanner.com/content/images/size/w1000/2020/08/developer_kit_interfaces.PNG)Figure 1: Jetson Nano Interfaces

The Jetson Nano Developer Kit packs a Quad-core ARM A57 CPU with a clock rate of 1.43GHz and 4GB of low-power DDR4 memory. For the connectors, it has 4x USB 3.0, 1xUSB2.0 Micro-B for powering with 5V, a HDMI and Display Port connector for connecting displays as well as one or two camera connectors that allow you to connect a Raspberry Pi Camera.

| GPU           | 128-core Maxwell                                             |
| :------------ | ------------------------------------------------------------ |
| CPU           | Quad-core ARM A57 @ 1.43 GHz                                 |
| MEMORY        | 4 GB 64-bit LPDDR4 25.6 GB/s                                 |
| STORAGE       | microSD (not included)                                       |
| VIDEO ENCODER | 4K @ 30 \| 4x 1080p @ 30 \| 9x 720p @ 30 (H.264/H.265)       |
| VIDEO DECODER | 4K @ 60 \| 2x 4K @ 30 \| 8x 1080p @ 30 \| 18x 720p @ 30 (H.264/H.265) |
| CAMERA        | 2x MIPI CSI-2 DPHY lanes                                     |
| CONNECTIVITY  | Gigabit Ethernet, M.2 Key E                                  |
| DISPLAY       | HDMI and display port                                        |
| USB           | 4x USB 3.0, USB 2.0 Micro-B                                  |
| OTHERS        | GPIO, I2C, I2S, SPI, UART                                    |
| MECHANICAL    | 69 mm x 45 mm, 260-pin edge connector                        |

For further information and a comparison between the different Jetson devices, you can visit the [Jetson Hardware section](https://developer.nvidia.com/embedded/develop/hardware).

## Requirements

Besides the Jetson Nano Developer Kit you'll also need **a microSD card**, a power Supply (5V 2A), and an **ethernet cable or WiFi adapter**.

### microSD card

The Jetson Nano uses a microSD card as a boot device and primary storage. The minimum size for the microSD card is 16GB, but I would strongly recommend getting at least 32GB. It's also essential to get a fast microSD as this will make working on the Jetson Nano a lot more fluent.

### Power Supply

The Jetson Nano can be powered in three different ways: over <u>USB Micro-B, Barrel Jack connector, or through the GPIO Header.</u>

To power the Jetson Nano over USB Micro-B, the power supply needs to supply 5V 2A. Not every power supply is capable of providing this. NVIDIA specifically recommends a [5V 2.5A power supply from Adafruit](https://www.adafruit.com/product/1995), but I use a Raspberry Pi power supply, and it works just fine.

If you want to get the full performance out of the Jetson Nano, I'd recommend using the Barrel Jack instead of powering over USB because you can supply 5V 4A over the Barrel Jack.

Before connecting the Barrel Jack, you need to place a jumper on J48. The power jumper location can vary depending on if you have the [older A02 model or the newer B01 model](https://www.arducam.com/nvidia-jetson-nano-b01-update-dual-camera/).

![img](https://cms.gilberttanner.com/content/images/size/w1000/2021/04/nvidia-jetson-nano-a02-pinout.jpg)

![img](https://cms.gilberttanner.com/content/images/size/w1000/2021/04/nvidia-jetson-nano-b01-pinout-1.png)

Figure 2: Jetson Nano A02 Pinout (left), Jetson Nano B01 Pinout (right)

### Ethernet cable or WiFi Adapter

Lastly, you'll need an ethernet cable or a WiFi Adapter since the Jetson Nano doesn't come with one.  For the WiFi Adapter, you can either use one that connects through USB, or you can use a PCIe WiFi Card like the [Intel® Dual Band Wireless-AC 8265](https://www.intel.com/content/www/us/en/products/wireless/wireless-products/dual-band-wireless-ac-8265.html).

## Setup

Before we can get started setting up a Python environment and running some deep learning demos, we have to download the [Jetson Nano Developer Kit SD Card Image](https://developer.nvidia.com/jetson-nano-sd-card-image) and [flash it to the microSD card](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write).

After that is done you need to insert the microSD card into the microSD slot as shown in the following image:

![Insert microSD card](https://cms.gilberttanner.com/content/images/size/w1000/2020/08/insert_sd_card.png)Figure 3: Insert microSD card ([Source](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#setup))

After inserting the microSD card, you can connect the power supply, which will automatically boot up the system.

When you boot the system for the first time, you'll be taken through some initial setup, including:

- Review and accept NVIDIA Jetson software EULA
- Select system language, keyboard layout, and time zone
- Create username, password, and computer name
- Log in

After the initial setup, you should see the following screen:

![Jetson Nano Desktop](https://cms.gilberttanner.com/content/images/size/w1000/2020/08/initial_screen.png)Figure 4: Desktop

## Increasing swap memory

Recent releases of JetPack enable swap memory as part of the default distribution using the [zram module](https://en.wikipedia.org/wiki/Zram). By default, 2GB of swap memory is enabled. To change the amount of swap memory, you can either edit the /etc/systemd/nvzramconfig.sh file directly, or you can use the [resizeSwapMemory repository](https://github.com/JetsonHacksNano/resizeSwapMemory) from [JetsonNanoHacks](https://www.jetsonhacks.com/2019/11/28/jetson-nano-even-more-swap/).

```bash
git clone https://github.com/JetsonHacksNano/resizeSwapMemory
cd resizeSwapMemory
 ./setSwapMemorySize.sh -g 4
```

After executing the above command, you'll have to restart the Jetson Nano for the changes to take effect.

## Installing prerequisites and configuring your Python environment

Now, that the Jetson Nano is ready to go we will go through creating a deep learning environment. We will start of by installing all prerequsites and configuring a Python environment as well as how to code remote using VSCode Remote SSH.

### Installing prerequisites

```bash
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install git cmake python3-dev nano

sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev
```

### Configuring your Python environment

Next we will configure our Python environment. This includes downloading pip3 and virtualenv.

Install pip:

```bash
sudo apt-get install python3-pip
sudo pip3 install -U pip testresources setuptools
```

For managing virtual environments we'll be using [virtualenv](https://virtualenv.readthedocs.io/en/latest/), which can be installed like below:

```bash
sudo pip install virtualenv virtualenvwrapper
```

To get virtualenv to work we need to add the following lines to the *~/.bashrc* file:

```bash
# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

To activate the changes the following command must be executed:

```bash
source ~/.bashrc
```

Now we can create a virtual environment using the *mkvirtualenv* command.

```bash
mkvirtualenv ml -p python3
workon ml
```

### Coding remote with Visual Studio Code (optional)

If you are like me and hate writing long scripts in nano or vim, the VSCode remote development plugin is for you. It allows you to develop remotely inside VSCode by establishing an SSH remote connection.

To use VSCode remote development, you'll first have to install the remote development plugin. After that, you need to create an SSH-Key on your local machine and then copy it over to the Jetson Nano.

```bash
# Create Key
ssh-keygen -t rsa
# Copy key to jetson nano
cat ~/.ssh/id_rsa.pub | ssh user@hostname 'cat >> .ssh/authorized_keys'
```

Now you only need to add the SSH Host. Ctrl + Shift + P -> Remote SSH: Connect to Host.

![img](https://cms.gilberttanner.com/content/images/size/w1000/2020/03/grafik-5.png)Figure 5: Added new host.

![img](https://cms.gilberttanner.com/content/images/size/w1000/2020/08/vscode_remote_control.PNG)Figure 6: VSCode Remote Controll

## Installing deep learning libraries

Now that we have our development and python environments set up, we can start installing some deep learning libraries. NVIDIA provides [a guide on how to install deep learning libraries on the Jetson Nano](https://elinux.org/Jetson_Zoo). I simply put the commands for some installations below.

### [TensorFlow](https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html)

```bash
# install prerequisites
$ sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran

# install and upgrade pip3
$ sudo apt-get install python3-pip
$ sudo pip3 install -U pip testresources setuptools==49.6.0 

# install the following python packages
$ sudo pip3 install -U numpy==1.16.1 future==0.18.2 mock==3.0.5 h5py==2.10.0 keras_preprocessing==1.1.1 keras_applications==1.0.8 gast==0.2.2 futures protobuf pybind11

# to install TensorFlow 1.15 for JetPack 4.4:
$ sudo pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v44 ‘tensorflow<2’

# or install the latest version of TensorFlow (2.3) for JetPack 4.4:
$ sudo pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v44 tensorflow
```

### Keras

```bash
# beforehand, install TensorFlow (https://eLinux.org/Jetson_Zoo#TensorFlow)
$ sudo apt-get install -y build-essential libatlas-base-dev gfortran
$ sudo pip3 install keras
```

### [PyTorch](https://forums.developer.nvidia.com/t/pytorch-for-jetson-nano-version-1-5-0-now-available/72048)

```bash
# install OpenBLAS and OpenMPI
$ sudo apt-get install libopenblas-base libopenmpi-dev

# Python 2.7
$ wget https://nvidia.box.com/shared/static/yhlmaie35hu8jv2xzvtxsh0rrpcu97yj.whl -O torch-1.4.0-cp27-cp27mu-linux_aarch64.whl
$ pip install future torch-1.4.0-cp27-cp27mu-linux_aarch64.whl

# Python 3.6
$ sudo apt-get install python3-pip
$ pip3 install Cython
$ wget https://nvidia.box.com/shared/static/9eptse6jyly1ggt9axbja2yrmj6pbarc.whl -O torch-1.6.0-cp36-cp36m-linux_aarch64.whl
$ pip3 install numpy torch-1.6.0-cp36-cp36m-linux_aarch64.whl
```

### Torchvision

Select the version of torchvision to download depending on the version of PyTorch that you have installed:

- PyTorch v1.0 - torchvision v0.2.2
- PyTorch v1.1 - torchvision v0.3.0
- PyTorch v1.2 - torchvision v0.4.0
- PyTorch v1.3 - torchvision v0.4.2
- PyTorch v1.4 - torchvision v0.5.0
- PyTorch v1.5 - torchvision v0.6.0
- PyTorch v1.5.1 - torchvision v0.6.1
- PyTorch v1.6 - torchvision v0.7.0
- PyTorch v1.7 - torchvision v0.8.0

```bash
$ sudo apt-get install libjpeg-dev zlib1g-dev
$ git clone --branch <version> https://github.com/pytorch/vision torchvision   # see below for version of torchvision to download
$ cd torchvision
$ sudo python3 setup.py install
$ cd ../  # attempting to load torchvision from build dir will result in import error
$ sudo pip install 'pillow<7' # always needed for Python 2.7, not needed torchvision v0.5.0+ with Python 3.6
```

### OpenCV

Installing OpenCV on the Jetson Nano can be a bit more complicated, but frankly, [JetsonHacks.com](https://www.jetsonhacks.com/) has a [great guide](https://www.jetsonhacks.com/2019/11/22/opencv-4-cuda-on-jetson-nano/).

## Compiling and installing Jetson Inference

NVIDIA's Jetson Inference repository includes lots of great scripts that allow you to perform image classification, object detection, and semantic segmentation on both images and a live video stream. In this article, we will go through how to compile and install the Jetson Inference repository and how to run some of the provided demos. Maybe I will go through the repository in more detail in an upcoming article.

To install Jetson Inference, you need to run the following commands:

```bash
# download the repo
$ git clone --recursive https://github.com/dusty-nv/jetson-inference
$ cd jetson-inference

# configure build tree
$ mkdir build
$ cd build
$ cmake ../

# build and install
$ make -j$(nproc)
$ sudo make install
$ sudo ldconfig
```

## Running the Jetson Inference demos

After [building](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md) the project, you can go to the *jetson-inference/build/aarch64/bin* directory. Inside you'll find multiple C++ and Python scripts. Below we'll go through how to run image classification, object detection, and semantic segmentation.

### Image Classification

Inside the folder there are two imagenet examples. One for a image and one for a camera. Both are available in C++ and Python.

- [imagenet-console.cpp](https://github.com/dusty-nv/jetson-inference/blob/master/examples/imagenet-console/imagenet-console.cpp) (C++)
- [imagenet-console.py](https://github.com/dusty-nv/jetson-inference/blob/master/python/examples/imagenet-console.py) (C++)
- [imagenet-camera.cpp](https://github.com/dusty-nv/jetson-inference/blob/master/examples/imagenet-camera/imagenet-camera.cpp) (C++)
- [imagenet-camera.py](https://github.com/dusty-nv/jetson-inference/blob/master/python/examples/imagenet-camera.py) (C++)

```bash
# C++
$ ./imagenet-console --network=resnet-18 images/jellyfish.jpg output_jellyfish.jpg

# Python
$ ./imagenet-console.py --network=resnet-18 images/jellyfish.jpg output_jellyfish.jpg
```

![Image Classification Example](https://cms.gilberttanner.com/content/images/size/w1000/2020/08/imagenet_jellyfish.jpg)Figure 7: Image Classification Example

### Object Detection

- [detectnet-console.cpp](https://github.com/dusty-nv/jetson-inference/blob/master/examples/detectnet-console/detectnet-console.cpp) (C++)
- [detectnet-console.py](https://github.com/dusty-nv/jetson-inference/blob/master/python/examples/detectnet-console.py) (Python)
- [detectnet-camera.cpp](https://github.com/dusty-nv/jetson-inference/blob/master/examples/detectnet-camera/detectnet-camera.cpp) (C++)
- [detectnet-camera.py](https://github.com/dusty-nv/jetson-inference/blob/master/python/examples/detectnet-camera.py) (Python)

```bash
# C++
$ ./detectnet-console --network=ssd-mobilenet-v2 images/peds_0.jpg output.jpg     # --network flag is optional

# Python
$ ./detectnet-console.py --network=ssd-mobilenet-v2 images/peds_0.jpg output.jpg  # --network flag is optional
```

![Object Detection Example](https://cms.gilberttanner.com/content/images/size/w1000/2021/04/detectnet-ssd-peds-0.jpg)Figure 8: Object Detection Example

### Semantic Segmentation

- [segnet-console.cpp](https://github.com/dusty-nv/jetson-inference/blob/master/examples/segnet-console/segnet-console.cpp) (C++)
- [segnet-console.py](https://github.com/dusty-nv/jetson-inference/blob/master/python/examples/segnet-console.py) (Python)
- [segnet-camera.cpp](https://github.com/dusty-nv/jetson-inference/blob/master/examples/segnet-camera/segnet-camera.cpp) (C++)
- [segnet-camera.py](https://github.com/dusty-nv/jetson-inference/blob/master/python/examples/segnet-camera.py) (Python)

```bash
# C++
$ ./segnet-console --network=fcn-resnet18-cityscapes images/city_0.jpg output.jpg

# Python
$ ./segnet-console.py --network=fcn-resnet18-cityscapes images/city_0.jpg output.jpg
```

![Semantic Segmentation](https://cms.gilberttanner.com/content/images/size/w1000/2020/08/output_segmentation.jpg)Figure 9: Semantic Segmentation

## JetPack 4.5.1 CUDA and VisionWorks samples

JetPack 4.5.1 includes multiple CUDA and VisionWork demos.

### CUDA samples

Installation:

```bash
./usr/local/cuda/bin/cuda-install-samples-10.2.sh ~
cd ~/NVIDIA_CUDA-10.2_Samples/
make
cd bin/aarch64/linux/release
```

After compiling, you can find multiple examples inside the bin/aarch64/linux/release directory.

oceanFFT sample:

```bash
./oceanFFT
```

<iframe width="200" height="150" src="https://www.youtube.com/embed/EiM85VNrbAk?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" style="vertical-align: middle; border: 0px; width: 881px; height: 60vh;"></iframe>

Figure 10: oceanFFT sample

particles sample:

```bash
./particles
```

<iframe width="200" height="150" src="https://www.youtube.com/embed/5nh1ya8pRJo?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" style="vertical-align: middle; border: 0px; width: 881px; height: 60vh;"></iframe>

Figure 11: particles sample

smokeParticles sample:

```bash
./smokeParticles
```

<iframe width="200" height="150" src="https://www.youtube.com/embed/usovVzxaHV4?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" style="vertical-align: middle; border: 0px; width: 881px; height: 60vh;"></iframe>

Figure 12: smoke particles sample

### VisionWorks samples

Installation:

```bash
./usr/share/visionworks/sources/install-samples.sh
cd ~/VisionWorks-1.6-Samples
make
cd bin/aarch64/linux/release
```

After compiling, you can find multiple examples inside the bin/aarch64/linux/release directory.

Feature Tracker sample:

```bash
./nvx_demo_feature_tracker
```

<iframe width="200" height="113" src="https://www.youtube.com/embed/u3OOYDR7I6w?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" style="vertical-align: middle; border: 0px; width: 881px; height: 60vh;"></iframe>

Figure 13: Feature tracker sample

Motion Detection sample:

```bash
./nvx_demo_motion_estimation
```

<iframe width="200" height="113" src="https://www.youtube.com/embed/lgRKUS3YwfI?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" style="vertical-align: middle; border: 0px; width: 881px; height: 60vh;"></iframe>

Figure 14: Motion Detection sample

Object Tracker sample:

```bash
./nvx_sample_object_tracker_nvxcu
```

<iframe width="200" height="113" src="https://www.youtube.com/embed/cG9m6wVgLrs?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" style="vertical-align: middle; border: 0px; width: 881px; height: 60vh;"></iframe>

Figure 15: Object Tracker sample

## Conclusion

That's it from this article. In follow-up articles, I will go further into developing Artificial Intelligence on the Jetson Nano, including:

- Deploying custom models on the Jetson Nano
- [NVIDIA Jetbot](https://github.com/NVIDIA-AI-IOT/jetbot)

If you have any questions or just want to chat with me, feel free to leave a comment below or contact me on social media. If you want to get  continuous updates about my blog make sure to [join my newsletter](http://eepurl.com/gq-u4X)