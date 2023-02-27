# FFIAC - FUZZ FOR IMPROPER ACCESS CONTROLS
### A script to fuzz for Improper Access Controls.
Latest Implementations and Improvements:
1. The script now accepts command line arguments using the argparse module.
2. The script now uses multithreading to test files concurrently.
3. The script now allows for the user to specify the file extensions to test for, instead of hardcoding them.
4. The script now handles errors when reading the wordlist file, instead of crashing. 

### Description:
This script is designed to test for improper access control vulnerabilities on a given target website by performing brute force attacks on the URL paths of the website. The script takes in a target URL, a wordlist file for brute forcing, a list of file extensions to test for, and the number of threads to use for brute forcing.

The script generates a list of file paths by combining each word in the wordlist with each file extension provided, and then uses multithreading to test each file path for improper access control. If a file is found to be accessible (i.e., the HTTP response code is 200), the script prints a message indicating that the file is vulnerable.

In summary, the script is a security testing tool designed to check for improper access control vulnerabilities by brute-forcing file paths on a website.
