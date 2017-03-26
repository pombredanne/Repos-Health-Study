# Repos-Health-Study

# System Description
Repos-Health-Study looks into analyzing potential risk factors on a Github repository. Factors that this project examines include percentages of licensing/copyright information used throughout the repository and whether or not a project has published vulnerabilites. On vulnerabilities specifically, the program will connect to the National Institute of Standards and Technology (NIST) (https://www.nist.gov) to identify whether or not a project has a published risk record(s) within NIST's database using a Common Platform Enumeration (CPE) on the repository.

When a user would like to analyze potential risks on a Github repository, our Python program will run. This program will gather the repository's associated .zip file and send it through doSOCSv2, a Github project that takes a look at managing SPDX 2.0 documents and data. doSOCSv2 will then gather licensing information and the CPE of a repo. This CPE is then fed into NIST's database which will then try to find any published vulnerabilites, if they exist. The results of all preceding activity will then be documented into a JSON script and gives said script back to the user.

# Copyright Declarations/Licensing Information
Repos-Health-Study is free software: you can redistribute it and/or modify it under the terms of the MIT License as published by the Open Source Initiative. See the file LICENSE for more details.

All associated documentation is licensed under the terms of the Creative Commons Attribution Share-Alike 4.0 license. See the file CC-BY-SA-4.0 for more details.

# Maintainers: 
Dreizan Moore and Matthew Schuette

# Development Environment:
Operating Systems: Macintosh and Windows
    
Programming Languages: Python 3.4.x
    
Frameworks: N/A
    
Programming Environment: Terminal/Sublime Text/Notepad++
    
Deployment Environment - 

Windows Computer Specs: 64-bit OS, i5-660k processor, 8GB ram

Mac Computer Specs: 64-bit macOS Sierra, 2.5 GHz Intel Core i5 processor, 16GB RAM

# Repository Management: 
When a contributor wishes to edit/add to the repository's code, contributors will fork the repository. Once code has been written, before committing, the maintainers will meet to go over additions/changes. Then, pull and merge requests will be made.

# DFD of Repos-Health-Study
![alt tag](https://github.com/Dreizan/Repos-Health-Study/blob/dev/RepoHealthDFD.png?raw=true)

# Database Schema
Potentially, data will be stored under a MySQL database server, which will contain all risk information collected on projects that have already been analysed. When the user would like to find out risk analysis information on a specific Github repository, this server will be checked first to see whether or not analysis on said repository exists already. If analysis already exists, it will pull the JSON information directly from the MySQL database. If not, the Python program will be run to analyze potential risks on the repository, send the resulting analysis to the user, and store the resulting JSON file into the database.

For now, this task will potentially be returned to at a later date. Developing the analysis system will be of higher priority.
