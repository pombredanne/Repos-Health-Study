# Repos-Health-Study

# System Description
Repos-Health-Study looks into analyzing potential risk factors on a Github repository. The main factor that this project examines is licensing/copyright information used throughout the target repository. The user passes a GitHub repository URL to our Python program, and it downloads, decompresses, and examines the target repository's zip file. To examine the repository for licensing/copyright information, we are implementing open-source project **scancode_toolkit**, developed by nexB (Source: "https://github.com/nexB/scancode-toolkit"), which is able to extract licensing and copyright claims from a file/directory. 

# System Requirements
Python 2.7.x (Link to Python Language: https://www.python.org)

Pip (included in Python 2.7.9 & up, Link: https://pip.pypa.io/en/stable/installing/  ) (sudo may be needed for installations)

Python Requests Module (http://docs.python-requests.org/en/master/user/install/) (sudo may be needed for installations)

Pytest 3.0.x (For testing purposes, https://docs.pytest.org/en/latest/)

# Installation Instructions
**Step 1: Download this repository**

Either download and decompress the Repos-Health-Study zip file (Download Link: https://github.com/Dreizan/Repos-Health-Study/archive/master.zip) from GitHub or in your Terminal session, run the following command:

    $ git clone https://github.com/Dreizan/Repos-Health-Study.git


# Usage
To run the program, run the following command:

    $ python riskAnalysis.py <URL_of_GitHub_Repository>
    
\<URL_of_GitHub_Repository\> - The URL of the main page for a GitHub repository (ex. For this repo, Repos-Health-Study, the URL would be "https://github.com/Dreizan/Repos-Health-Study".)
    
This will find the passed repository link's associated zip file (assuming the URL of the repository exists), download the file, and decompress it. Then, scancode_toolkit will be executed, creating a JSON file containing licensing and copyright information on every file contained in the target zip file. riskAnalysis.py will then look at the JSON file and parse out any licenses or copyrights found in the repository's files and output them out onto the console. Finally, the zip file and decompressed directory will be deleted from your system.

    $ python riskAnalysis.py https://github.com/Dreizan/Repos-Health-Study
    Checking if the URL passed exists:
    URL exists!
    Gathering the zip file and decompressing it.
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
      0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
    100 31204  100 31204    0     0  44464      0 --:--:-- --:--:-- --:--:-- 94844
    Attemptiing to collect licensing and copyright information on the following GitHub project - Repos-Health-Study.zi:
    (This may take awhile, depending on how big the zip file is)

    Finsihed scanning. Parsing through JSON results now:
    There are licenses included!
    Licenses:
    * - MIT License
    There are copyrights included!
    Copyrights:
    * - "Copyright (c) 2017 Dreizan Moore & Matthew Schuette"
    Parsing complete. Removing downloaded files:
    Process complete. Thank you!

# Testing Usage
After installing Pytest using the aforementioned link in the installation instructions, navigate to the main directory that holds test_riskAnalysis.py. Then run the command:

    $ pytest test_riskAnalysis.py 

You should then see the test results output.

# Copyright Declarations/Licensing Information
Repos-Health-Study is free software: you can redistribute it and/or modify it under the terms of the MIT License as published by the Open Source Initiative. See the file LICENSE for more details.

All associated documentation is licensed under the terms of the Creative Commons Attribution Share-Alike 4.0 license. See the file CC-BY-SA-4.0 for more details.

# Maintainers: 
Dreizan Moore and Matthew Schuette

# Development Environment:
Operating Systems: macOS/OSX or Unix-based system & Ubuntu 16+
    
Programming Languages: Python 2.7.x
        
Programming Environment: Terminal/Sublime Text/Notepad++

Mac Computer Specs: 64-bit macOS Sierra, 2.5 GHz Intel Core i5 processor, 16GB RAM

# Repository Management: 
When a contributor wishes to edit/add to the repository's code, contributors will fork the repository. Once code has been written, before committing, the maintainers will meet to go over additions/changes. Then, pull and merge requests will be made.

# DFD of Repos-Health-Study
![alt tag](https://github.com/Dreizan/Repos-Health-Study/blob/master/RepoHealthDFD.PNG?raw=true)

# Future Development Tasks
* Implementing DoSOCSv2 as our licensing information ananlyzer (Link: "https://github.com/DoSOCSv2/DoSOCSv2/blob/master/README.md") as well as giving us a SHA-1 value on the repository. We would use the SHA-1 value to search the NIST Database (Link: "https://www.nist.gov") for existing CPEs on the target repository.
* Implementing MongoDB server 
* Have program store JSON licensing/copyright and CPE data into the MongoDB server

# Use Case
* Title: Determine License and Copyright Information
* Primary Actor: User of an open source project
* Goal in Context: The user is able to determine license and copyright information from the provided project info
* Stakeholders:  OSS Health Community members: To receive clear license and copyright information
* Preconditions: Python 2.7.x, Download of the /Dreizan/Repos-Health-Study, Download of scan code tool, proper GitHub url has been provided
* Main Success Scenario: License and Copyright information is stored in a .json file and output to the console for the user
* Failed End Conditions: License and Copyright information is not provided, nothing is output to the console
* Trigger: Executing riskAnalysis.py
