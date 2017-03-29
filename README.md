# Repos-Health-Study

# System Description
Repos-Health-Study looks into analyzing potential risk factors on a Github repository. Factors that this project examines include percentages of licensing/copyright information used throughout the repository and whether or not a project has a Common Platform Enumeration(CPE). On vulnerabilities specifically, the program will connect to the National Institute of Standards and Technology (NIST) (https://www.nist.gov) to identify whether or not a project has a published risk record(s) within NIST's database using a CPE on the repository. That CPE then may have associated Common Vulnerabilities and Exposures (CVE) with it.

When a user would like to analyze potential risks on a Github repository, our Python program will run. This program will gather the repository's associated .zip file and send it through doSOCSv2(https://github.com/DoSOCSv2/DoSOCSv2), a Github project that takes a look at managing SPDX 2.0 documents and data. doSOCSv2 will then gather licensing information and the CPE of a repo. This CPE is then fed into NIST's database which will then try to find any published vulnerabilites, if they exist. The results of all preceding activity will then be documented into a JSON script and gives said script back to the user.

# System Requirements

Python 2.7.x (Link to Python Language: https://www.python.org)

# Installation Instructions

**Step 1: Download this repository**

Either download and decompress the Repos-Health-Study zip file (Download Link: https://github.com/Dreizan/Repos-Health-Study/archive/master.zip) from GitHub or in your Terminal session, run the following command:

    $ git clone https://github.com/Dreizan/Repos-Health-Study.git

**Step 2: Download the scancode_toolkit Repository**

Download the scancode_toolkit Repository's zip file (Link: https://github.com/nexB/scancode-toolkit/archive/develop.zip) and decompress the zip file inside your Repos-Health-Study directory.

# Usage

To run the program, run the following command:

    $ python riskAnalysis.py <URL_of_GitHub_Repository>
    
* \<URL_of_GitHub_Repository\> - The URL of the main page for a GitHub repository (ex. For this repo, Repos-Health-Study, the URL would be "https://github.com/Dreizan/Repos-Health-Study".)

    $ python riskAnalysis.py https://github.com/Dreizan/Repos-Health-Study
    
This will find the passed repository link's associated zip file (assuming the URL of the repository exists), download the file, and decompress it. Then, scancode_toolkit will be executed, creating a JSON file containing licensing and copyright information on every file contained in the ********

# Copyright Declarations/Licensing Information
Repos-Health-Study is free software: you can redistribute it and/or modify it under the terms of the MIT License as published by the Open Source Initiative. See the file LICENSE for more details.

All associated documentation is licensed under the terms of the Creative Commons Attribution Share-Alike 4.0 license. See the file CC-BY-SA-4.0 for more details.

# Maintainers: 
Dreizan Moore and Matthew Schuette

# Development Environment:
Operating Systems: macOS/OSX or Unix-based system
    
Programming Languages: Python 2.7.x
    
Frameworks: N/A
    
Programming Environment: Terminal/Sublime Text/Notepad++
    
Deployment Environment: (TBD)

Mac Computer Specs: 64-bit macOS Sierra, 2.5 GHz Intel Core i5 processor, 16GB RAM

Database: TBD (possibly MySQL Database)

# Repository Management: 
When a contributor wishes to edit/add to the repository's code, contributors will fork the repository. Once code has been written, before committing, the maintainers will meet to go over additions/changes. Then, pull and merge requests will be made.

# DFD of Repos-Health-Study
![alt tag](https://github.com/Dreizan/Repos-Health-Study/blob/dev/RepoHealthDFD.PNG?raw=true)

# Database Schema
Potentially, data will be stored under a MySQL database server, which will contain all risk information collected on projects that have already been analysed. When the user would like to find out risk analysis information on a specific Github repository, this server will be checked first to see whether or not analysis on said repository exists already. If analysis already exists, it will pull the JSON information directly from the MySQL database. If not, the Python program will be run to analyze potential risks on the repository, send the resulting analysis to the user, and store the resulting JSON file into the database.

For now, this task will potentially be returned to at a later date. Developing the analysis system will be of higher priority.

# To-Do's


