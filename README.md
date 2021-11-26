# OpenVSLAM-Python-bindings
Python bindings for [OpenVSLAM](https://github.com/OpenVSLAM-Community/openvslam), an ORB based visual SLAM similar to ORB-SLAM2.

By compiling the provided cpp file, you get the module **openvslam** that let you control openvslam'system from Python.  OpenVSlam must be already installed in your system.  You'll be able to run openvslam, load & save maps, feed images and get the pose matrix.

Right now no bindings for viewers are provided, so do not expect to see the 3D map nor the features over the image.

## Building the bindings
In order to get a **openvslam** module you can import from Python, you need to:

* install [OpenVSLAM](https://github.com/OpenVSLAM-Community/openvslam)
* install [PyBind11](https://github.com/pybind/pybind11)
  * like ```pip install pybind11```
* compile _openvslam-bindings.cpp_ 

This is an example of command line compilation in Linux:

    /usr/bin/g++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) -I/usr/local/include/openvslam/3rd/json/include -DUSE_DBOW2 /home/user/OpenVSLAM-Python-bindings/openvslam_bindings.cpp -o openvslam$(python3-config --extension-suffix) -lopenvslam

In this command line you can remove -DUSE_DBOW2 if you don't want to use DBoW2, and use fbow instead.

The result is a module in a form of a shared library, like

    openvslam.cpython-38-x86_64-linux-gnu.so

You can import this module in your Python code simply like

    import openvslam
    
provided the module file is reachable, for example being in the working directory.

## Testing the module

In order to run openvslam you always need a configuration file and a vocabulary file.  You can get the vocabulary [orb_vocab.dbow2 file from openvslam](https://github.com/OpenVSLAM-Community/DBoW2_orb_vocab).

Two tests are available in Python.

_test1.py_ is a minimal proof of operation, it starts and shuts down openvslam.  A random _config.yaml_ file is provided in this project to facilitate this test.  Don't rest until you get this test running without errors.

_test2.py_ is a more complete demo, inspired in [run_video_slam](https://github.com/OpenVSLAM-Community/openvslam/blob/main/example/run_video_slam.cc) example.  You'll need a video with the right config.yaml.  You can download them from the [datasets openvslam made public](https://openvslam-community.readthedocs.io/en/latest/simple_tutorial.html#equirectangular-datasets).  Here are the direct links:

* [omnidirectional camera dataset (equirectanulgar)](https://drive.google.com/drive/folders/1A_gq8LYuENePhNHsuscLZQPhbJJwzAq4)
* [fisheye camera dataset](https://drive.google.com/drive/folders/1SVDsgz-ydm1pAbrdmhRQTmWhJnUl_xr8)

Each zip contains a video and the appropiate _config.yaml_.

## What is in the module
_openvslam_ module contains two clases: _config_ and _system_.  The former is only used to pass config.yaml to _system_ initialization.  You do all the work with a _system_ object.

At the end of _openvslam_binding.cpp_ you'll find the list of bound functions accessible from Python.  Tests serve as example of use.


## License
3-clause BSD license (see LICENSE)

This project uses code from the following third party libraries:

* NDArrayConverter from [edmBernard/pybind11_opencv_numpy](https://github.com/edmBernard/pybind11_opencv_numpy), Apache License 2.0
* NDArrayConverter uses code from [OpenCV 3.1.0](https://github.com/opencv/opencv/tree/3.1.0), 3-clause BSD license
* NDArrayConverter is based on the work of [yati-sagade/opencv-ndarray-conversion](https://github.com/yati-sagade/opencv-ndarray-conversion), MIT license

## Thanks
Many thanks to [Jack Cai](https://github.com/JackCai1206/openvslam/blob/master/python/bindings.cc) whose non appropiable code inspired this project.

## Help needed
All help is welcome to facilitate installation with cmake.  From cmakelists.txt to the documentation with examples of use.
We can communicate through Dicussions.
