# JSON Minifier Application User Guide

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Using the Application](#using-the-application)
- [Understanding the Output](#understanding-the-output)
- [Troubleshooting](#troubleshooting)
- [Contact Information](#contact-information)

## Introduction
The JSON Minifier is a user-friendly desktop application designed to simplify and compress JSON files. It's particularly useful for creating mock data in Postman or other scenarios where compact JSON strings are needed.

### Key Features:
- Minifies JSON files by removing unnecessary whitespace
- Converts minified JSON to a string format suitable for Postman mock creation
- Saves the minified JSON to a new file
- Provides an easy-to-use graphical interface

## Getting Started

### System Requirements
- Windows 10 or later, macOS 10.12 or later, or a recent Linux distribution
- No additional software installation required

### Installation
1. Locate the `JSONMinifier.exe` (Windows), `JSONMinifier.app` (macOS), or `JSONMinifier` (Linux) file provided to you.
2. Copy this file to a location of your choice on your computer.
3. No further installation steps are required.

## Using the Application

1. Double-click the JSON Minifier application icon to launch the program.
2. In the application window, click the **"Select JSON File"** button.
3. Navigate to and select the JSON file you want to minify.
4. The application will automatically process the file and display the results.

## Understanding the Output

After processing a file, you'll see:

- A text box containing the minified JSON as a single line string.
  - This string is ready to be copied and used in Postman for mock creation.
- A message below the text box indicating where the minified JSON file has been saved.
  - The new file will have "_minified" added to its original name.

## Troubleshooting

### Common issues and solutions:
- **"Invalid JSON file" message**: Ensure your input file contains valid JSON. Check for syntax errors in the original file.
- **"Error reading or writing file" message**: Make sure you have permission to read the input file and write to the output location.
- **Application doesn't open**: Verify that you're using the correct version for your operating system.
