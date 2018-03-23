# -------------------- Imports -------------------- #
import os, sys, argparse, requests


# -------------------- Globals -------------------- #
payload = dict()
payload["datatype"] = "csv"
payload["symbol"] = ''


# -------------------- Command Line Arguements -------------------- #
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('symbols', type=str, nargs='*',
                    help='symbols to retrieve historical data from API')
parser.add_argument('--sfile', type=str,
                    help='Get symbols from file. Command line symbols are ignored.')
parser.add_argument('--all', action="store_true",
                    help='Get all data, not compact')
parser.add_argument('--key', type=str,
                    help='AlphaVantage API Key')
parser.add_argument('--save', action="store_true",
                    help='Save whatever data was retrieved!')                    

parser.add_argument('--prompt', action="store_true",
                    help='Prompt whether to store data for each symbol. Default action is to store.')

parser.add_argument('-v', action="store_true",
                    help='Verbosity')
parser.add_argument('-vv', action="store_true",
                    help='More verbosity')

args = parser.parse_args()
if args.vv :
    args.v = True


if args.key:
    api_key = args.key
else:
    try:
        path_to = os.getenv('HOME') + '/Desktop/misc/Alpha Vantage API Key.txt'
        with open(path_to) as file :
            api_key = file.read()
    except:
        print("API KEY required! Please enter valid alphavantage API key!")
        exit(0)


# API URL
url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED"

# API Key
payload["apikey"] = api_key

# Data to retrieve
if args.all:
    payload["outputsize"] = "full"
else:
    payload["outputsize"] = "compact"

if args.sfile:
    with open(args.sfile) as file:
        args.symbols = [ x.strip() for x in file.readlines() ]

# Verbose output
if args.v:
    print("API Key :", api_key)
    print("API URL :", url)
    print("Payload without symbol :", payload)
    print("Symbols :", args.symbols)


# -------------------- Requests to API -------------------- #

for s in args.symbols:
    payload["symbol"] = s
    r = requests.get(url, params = payload)

    if args.v :
        print("Symbol :", s, "Request code :", r.status_code)
        if args.vv :
            print("Data :", r.text)

    if "Error Message" in r.text:
        print("Error for", s, "!!")

    if payload["outputsize"] == "full" or args.save:
        if args.prompt:
            opt = input("Store", s, "? (y/n")
            if opt.casefold() == 'n':
                continue
        
        with open(os.path.abspath('../data/' + s + '.csv'), 'w') as file:
            print(file.write(r.text), "written")
    print(s, "DONE!")
