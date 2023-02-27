import requests
import argparse

# define command line arguments
parser = argparse.ArgumentParser(description='Test for improper access control vulnerabilities')
parser.add_argument('url', type=str, help='The target URL to test')
parser.add_argument('-w', '--wordlist', type=str, default='wordlist.txt', help='The wordlist file to use for brute forcing (default: wordlist.txt)')
parser.add_argument('-e', '--extensions', type=str, default='php,txt,html', help='The file extensions to test for (default: php,txt,html)')
parser.add_argument('-t', '--threads', type=int, default=10, help='The number of threads to use for brute forcing (default: 10)')
args = parser.parse_args()

# load wordlist file into a list
try:
    with open(args.wordlist, 'r') as f:
        wordlist = f.read().splitlines()
except:
    print(f"Error: could not read wordlist file {args.wordlist}")
    exit()

# generate list of files to test
extensions = args.extensions.split(',')
files = [f"{word}.{ext}" for word in wordlist for ext in extensions]

# function to test each file for improper access control
def test_file(file):
    url = f"{args.url}/{file}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Vulnerable: {url}")

# use multithreading to test files concurrently
import concurrent.futures

with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
    executor.map(test_file, files)

print("Done.")
