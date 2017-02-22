# Repos-Health-Study

# System Description
Repos-Health-Study will be using Core Infrastructure Initiative's (CII) Census Project to determine risk factor for repos. The CII Census Project takes a look at OSS Debian projects "to help identify the ones that should be tested to see if they need some help" (The Linux Foundation, https://www.coreinfrastructure.org/programs/census-project). To identify these projects, they have developed a risk scoring system using parameters like the number of CVEs a project has, popularity, number of contributors over a 12-month period, etc. For more information, visit the link above and/or their Github repository for the project: https://github.com/linuxfoundation/cii-census

For our project, we will be using a similar risk scoring system using a plethora of parameters to help identify whether a repo is at a health risk, in regards to community involvement and sustainability.

# Copyright Declarations/Licensing Information
Repos-Health-Study is free software: you can redistribute it and/or modify it under the terms of the MIT License as published by the Open Source Initiative. See the file LICENSE for more details.

All associated documentation is licensed under the terms of the Creative Commons Attribution Share-Alike 4.0 license. See the file CC-BY-SA-4.0 for more details.

# Contributors: 
Dreizan Moore and Matthew Schuette

# Development Environment:
Operating Systems: Macintosh and Windows
    
Programming Languages: Python 3.4.x
    
Frameworks: 
    
Programming Environment: Terminal/Sublime Text/Notepad++
    
Deployment Environment: 
Windows Computer Specs: 64bit OS, i5-660k processor, 8GB ram
Mac Computer Specs:

# Repository Management: 
When a contributor wishes to edit/add to the repository's code, contributors will fork the repository. Once code has been written, before committing, the contributors will meet to go over additions/changes. Then, pull and merge requests will be made.

# DFD of Repos-Health-Study
https://github.com/Dreizan/Repos-Health-Study/blob/dev/RepoHealthDFD.PNG

# Database Schema
Data will be stored under a MySQL database server, which will contain all risk information collected on projects that have already been analysed. When the user would like to find out risk analysis information on a specific Github repository, this server will be checked first to see whether or not analysis on said repository exists already. If analysis already exists, it will pull this information directly from the MySQL database. If not, the Python program will be run to analyze potential risks on the repository, send the resulting analysis to the user, and store the result into the database.
