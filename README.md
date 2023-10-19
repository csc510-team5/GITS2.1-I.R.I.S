# GITS2.1 - I.R.I.S

![GitHub](https://img.shields.io/github/license/csc510-team5/GITS2.1-I.R.I.S)
[![codecov](https://codecov.io/gh/csc510-team5/GITS2.1-I.R.I.S/branch/master/graph/badge.svg)](https://codecov.io/gh/csc510-team5/GITS2.1-I.R.I.S)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10023393.svg)](https://doi.org/10.5281/zenodo.10023393)
[![GitHub issues](https://img.shields.io/github/issues/csc510-team5/GITS2.1-I.R.I.S)](https://github.com/csc510-team5/GITS2.1-I.R.I.S/issues?q=is%3Aissue+is%3Aopen+)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/csc510-team5/GITS2.1-I.R.I.S)](https://github.com/csc510-team5/GITS2.1-I.R.I.S/issues?q=is%3Aissue+is%3Aclosed+)
![Github pull requests](https://img.shields.io/github/issues-pr/csc510-team5/GITS2.1-I.R.I.S)
[![GitHub stars](https://badgen.net/github/stars/csc510-team5/GITS2.1-I.R.I.S)](https://badgen.net/github/stars/csc510-team5/GITS2.1-I.R.I.S)
![version](https://img.shields.io/github/v/release/csc510-team5/GITS2.1-I.R.I.S)
![GitHub contributors](https://img.shields.io/github/contributors/csc510-team5/GITS2.1-I.R.I.S)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/csc510-team5/GITS2.1-I.R.I.S)


# Recent Additions

Recently we added automatic merge conflict detection using ```gits check_conflicts```. This allows you to preview merge conflicts before they happen. This feature is powered by GitHub CLI which is now required (found here: https://cli.github.com/). We have provided a Dockerfile which includes GitHub CLI and Python3 so you can build an image using GITS (Docker installation instructions below).


# About 

"Your repo is your resume. But what is a good looking repo?"

So you want to start a Project on Github. Ever wondered what makes a project repository good?
What makes your project stand apart when collaborating with multiple developers?
What would ensure that your project is well documented and readable to other developers who might try to work on this in the future?

    bash requirements.sh

Worry not. I.R.I.S is here.

I.R.I.S (Ideal ReposItory for Software projects) is a tool which can help developers align their repos as per the standards defined in Software Engineering.

You don't have to worry about missing a test case, or scratch your head on what more files or functionalities are needed to make your repository look good.

I.R.I.S streamlines your repository as per the Software Engineering Standards, so that your repository has all the necessary Structure to be called a "Good Repo".

I.R.I.S can be thought of a base repo to make sure your project repo fits the bill.


## On Linux/MacOS Machines

1. Clone GITS Repo
2. From the root directory run the following command
   ```
   pip install -r requirements.txt
   ```
3. Go to configurations directory and run the following command:

   If you are working on Linux system with a bash terminal or a Windows system using Windows subsystem for linux:

   ```
   bash project_init.sh
   ```

   If you are working on Linux system with a fish terminal:

   ```
   fish project_init.fish
   ```

4. Source the bashrc file

   ```
   source ~/.bashrc
   ```

   Note: Open the .bashrc file in User home directory to make sure that the alias command does not have any white spaces in the path. If so, rename the directory to remove the white spaces and re-run the setup.

   ##

## Installation for Windows

1.  Clone GITS Repo
2.  From the root directory run the following command
    ```
    pip install -r requirements.txt
    ```
3.  Run "windows_setup.bat" from configurations folder to setup environment.
4.  Run "autoRun.bat" as administrator.
5.  Now gits command is accessible all over the system.

## Installation Using Docker

We have provided a Dockerfile to build an image containing GITS

1.  Clone GITS Repo
2.  Enter repo directory
3.  With Docker installed and the Docker daemon running run the following command
    ```
    docker build -t image_name .
    ```
4.  Now run a container with the following command
    ```
    docker run -d -it image_name /bin/bash
    ```
5.  Now the container is running with Python3, GitHub CLI and GITS

# How to Contribute?

Please take a look at our CONTRIBUTING.md where we provide instructions on contributing to the repo and help us in enhancing the current video conferencing platforms.

# Documentation

## Functionalities Implemented

0. Use custom commands to work with Git from your command line.
1. Create Default files on startup according to the Stucture.
2. Files will be auto generated with template to give the developers an idea on what needs to be filled. Also, the user is given a choice to add license in his repo from the list provided.
3. Score Calculation to see how much the repo matches with the ideal repo structure.
4. Created commands to show version of Git, count commits, list all custom created commands.
5. Create a custom command to work with Git and make development fun.





# Team Members

This repository is made for CSC-510 Software Engineering Course at NC State University for Fall 2023.

<table>
  <tr>
    <td align="center"><a href="https://github.com/tackyunicorn"><img src="https://avatars.githubusercontent.com/u/26558907?v=4" width="75px;" alt=""/><br /><sub><b>Joshua Joseph</b></sub></a></td>
    <td align="center"><a href="https://github.com/jwgerlach00"><img src="https://avatars.githubusercontent.com/u/57069011?v=4" width="75px;" alt=""/><br /><sub><b>Jacob Gerlach
</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Uchswas"><img src="https://avatars.githubusercontent.com/u/19565049?v=4" width="75px;" alt=""/><br /><sub><b>Uchswas Paul</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Sana-Ma"><img src="https://avatars.githubusercontent.com/u/70275715?v=4" width="75px;" alt=""/><br /><sub><b>Sana Mahmoud</b></sub></a><br /></td>

  </tr>
</table>

## Contact Us:

For any questions and contribution please contact: jjoseph6@ncsu.edu

Made with ❤️ on GitHub.
