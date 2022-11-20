---
layout: post
title:  "Azure ML"
date:   2022-02-20 19:51 +1200
categories: machine-learning azure python
---

What does a hacker have to go through these days to lay hands on a GPU?

Azure ML is one route you might go, if your corporate overlords drank some of that Redmond kool-aid. Hosted Jupyter notebooks are packaged up fairly nicely.

Conda provides environments. As of now, `conda activate azureml_py38_PT_TF` gives you the latest stable pytorch-1.10.2. They could update to Python 3.9

Doing the following buys us a little insurance against totally hosing the environment at the cost of some waiting around.

```sh
conda create --name azureml_py38_bacs --clone azureml_py38_PT_TF
```

Conda, is this something I need to waste 20 minutes on?

```sh
failed with initial frozen solve. Retrying with flexible solve.
Solving environment: | 
Found conflicts! Looking for incompatible packages.
This can take several minutes.  Press CTRL-C to abort.
Examining conflict for opencv torchvision torchaudio mkl_random mkl_fft numpy pytorch:  75%|█████████▋   | 59/79 [15:09<04:11, 12.56s/| ]
```

(azureml_py38_bacs) azureuser@jcb-cpu:~/cloudfiles/code/Users/christopher.bare/bacs$ sudo chmod 700 secrets.json 
(azureml_py38_bacs) azureuser@jcb-cpu:~/cloudfiles/code/Users/christopher.bare/bacs$ ls -alph secrets.json 
-rwxrwxrwx 1 root root 73 Feb 20 07:50 secrets.json


To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code PA6LWD8MG to authenticate.

