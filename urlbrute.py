import requests
import string
import random
import time
import threading
from random import randint
from time import sleep
import argparse

ico = "                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@\n@@@@      @@@@    @@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@\n@@@@      @@@@    @@@@@@@@@@@@@@                                @@@@    @@@@            @@@@\n@@@@      @@@@    @@@@      @@@@                                @@@@    @@@@            @@@@\n@@@@      @@@@    @@@@  @@  @@@@                                @@@@    @@@@            @@@@\n@@@@      @@@@    @@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@    @@@@    @@@@@@@@@@@@    @@@@\n@@@@      @@@@    @@@@      @@      @@@@@@@@@@@@@@@@@@@@@@@@    @@@@    @@@@@@@@@@@@    @@@@\n@@@@      @@@@    @@@@      @@@@                        @@@@    @@@@    @@@@    @@@@    @@@@\n@@@@@@@@@@@@@@    @@@@      @@@@                        @@@@    @@@@    @@@@    @@@@    @@@@\n  @@@@@@@@@@      @@@@@@@@@@@@      @@@@@@@@@@@@@@@@    @@@@    @@@@    @@@@    @@@@    @@@@\n                                    @@@@@@@@@@@@@@@@    @@@@    @@@@    @@@@    @@@@    @@@@\n                                                        @@@@    @@@@            @@@@    @@@@\n                                                        @@@@    @@@@            @@@@    @@@@\n@@@@@@@@@@@@    @@@@@@@@@@@@    @@@@    @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@\n@@@@@@@@@@@@    @@@@@@@@@@@@    @@@@    @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@\n@@@@@@@@@@@@    @@@@@@@@@@@@    @@@@    @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@\n                @@@@    @@@@            @@@@            @@@@                            @@@@\n                @@@@    @@@@            @@@@            @@@@                            @@@@\n@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@\n@@@@                            @@@@            @@@@            @@@@    @@@@                \n@@@@                            @@@@            @@@@            @@@@    @@@@                \n@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@    @@@@\n@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@    @@@@\n@@@@    @@@@            @@@@                            @@@@                    @@@@    @@@@\n@@@@    @@@@            @@@@                            @@@@                    @@@@    @@@@\n@@@@    @@@@            @@@@                            @@@@                    @@@@    @@@@\n@@@@    @@@@    @@@@    @@@@    @@@@@@@@@@@@@@@@@@@@    @@@@    @@@@    @@@@@@@@@@@@    @@@@\n@@@@    @@@@    @@@@    @@@@    @@@@@@@@@@@@@@@@@@@@    @@@@    @@@@    @@@@@@@@@@@@    @@@@\n@@@@    @@@@    @@@@    @@@@    @@@@            @@@@    @@@@    @@@@    @@@@            @@@@\n@@@@    @@@@    @@@@    @@@@    @@@@            @@@@    @@@@    @@@@    @@@@            @@@@\n@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@\n@@@@                                    @@@@                    @@@@                    @@@@\n@@@@                                    @@@@                    @@@@                    @@@@\n@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@\n@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@\n@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@\n        @@@@    @@@@    @@@@                            @@@@                    @@@@    @@@@\n        @@@@    @@@@    @@@@                            @@@@                    @@@@    @@@@\n@@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@    @@@@@@@@@@@@@@@@@@@@    @@@@\n@@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@    @@@@@@@@@@@@@@@@@@@@    @@@@\n@@@@                            @@@@            @@@@    @@@@    @@@@                    @@@@\n@@@@                            @@@@            @@@@    @@@@    @@@@                    @@@@\n@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@\n@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@\n@@@@    @@@@                            @@@@                                    @@@@        \n@@@@    @@@@                            @@@@                                    @@@@        \n@@@@    @@@@                            @@@@                                    @@@@        \n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"

save_data = ""

alphabet_wordlist_conv = "abcdefghijklmnopqrstuvwxyz"

#arguments for tool options
parser = argparse.ArgumentParser(description='For exploring sites and their paths. This is a command line tool for finding possible paths of a given URL using either word list, random or commonpaths. This tool is primarily to generate a list of paths for sites with no/limited sitemaps.')
parser.add_argument('-C', '--common_mode', required=False, help='A pre-defined list of common URL paths, path of file must be specified', default="")
parser.add_argument('-R', '--rand_mode', required=False, help='A random string will be tried as a path, number of attempts must be specified', default=0)
parser.add_argument('-D', '--dict_mode', required=False, help='Every word in the English dictionary will be tried as a path, path of file must be specified', default="")
parser.add_argument('-t', '--multi_threading', required=False, help='Enables the multi-threading engine, number of threads must be specified', default=1)
parser.add_argument('-g', '--guided', required=False, help='A menu will be provided with extra information about this tool')
parser.add_argument('-u', '--url', required=True, help='This is the root URL that will be used for the testing', type=str)
parser.add_argument('-w', '--wait', required=True, help='The scheduled delay between attempts')
parser.add_argument('-v', '--verbose_output', required=False, help='Debug info will be given including thread info')
parser.add_argument('-e', '--exclude', required=False, help='It will specify the response type that will be counted as a miss.', default="404,403")
parser.add_argument('-s', '--save', required=False, help='It will save the output in a file, path and file name must be specified', default="")

args = parser.parse_args()

hits = []

if args.guided == True:
    #guided mode interface
    domain = input("Domain:\n")

    common_mode = input("Search for common URL paths? (y/n)\n")
    dict_mode = input("Search for all words as paths? (y/n)\n")
    rand_mode = input("Search for random strings as paths? (y/n)\n")
    verbose_mode = input("Verbose mode? (y/n)\n")
    delay = float(input("Delay for each search query: (seconds)\n"))
    save_location = input("Would you like to save the output? (path/n)\n")
else:
    #argument to variable conversion
    domain = args.url
    common_mode = args.common_mode
    dict_mode = args.dict_mode
    rand_mode = int(args.rand_mode)
    verbose_mode = args.verbose_output
    delay = float(args.wait)
    threads = int(args.multi_threading)
    search_list = eval("["+args.exclude+"]")
    save_location = args.save

#setting defaults if input is not sufficient
if common_mode == "default" or common_mode == "Default" or common_mode == "y" or common_mode == "Y":
    common_mode = "commonpaths.txt"
if dict_mode == "default" or dict_mode == "Default" or dict_mode == "y" or dict_mode == "Y":
    dict_mode = "wordlist.txt"
if ":" not in domain:
    domain = "https://"+domain

#common word search mode
def search_common():
    commonlist = open(common_mode, "r")
    common = commonlist.read().split("\n")
    commonlist.close()
    for x in range(0, len(common)):
        if verbose_mode == "y" or verbose_mode == "Y":
            print("Searching "+domain+"/"+common[x])
        r = requests.get(domain+"/"+common[x])
        if verbose_mode == "y" or verbose_mode == "Y":
            print(r)
        if str(r) != "<Response [404]>"  and "404" not in r and int(str(r).split("[")[1].split("]")[0]) not in search_list:
            if verbose_mode == "y" or verbose_mode == "Y":
                print("HIT")
            hits.append([common[x], r])
        time.sleep(delay)

#SINGLE THREADED dictionary search
def search_dict():
    wordlist = open(dict_mode, "r")
    words = wordlist.read().split("\n")
    wordlist.close()
    for x in range(0, len(words)):
        if verbose_mode == "y" or verbose_mode == "Y":
            print("Searching "+domain+"/"+words[x])
        r = requests.get(domain+"/"+words[x])
        if verbose_mode == "y" or verbose_mode == "Y":
            print(r)
        if str(r) != "<Response [404]>"  and "404" not in r and int(str(r).split("[")[1].split("]")[0]) not in search_list:
            if verbose_mode == "y" or verbose_mode == "Y":
                print("HIT")
            hits.append([words[x], r])
        time.sleep(delay)

#MULTI THREADED dictionary search
def search_dict_threaded(letter):
    wordlist = open("wordlist.txt", "r")
    words = wordlist.read().split("\n")
    wordlist.close()
    for x in range(0, len(words)):
        if words[x][0] == alphabet_wordlist_conv[letter-1].lower() or words[x][0] == alphabet_wordlist_conv[letter-1].upper():
            if verbose_mode == "y" or verbose_mode == "Y":
                print("Searching "+domain+"/"+words[x])
            r = requests.get(domain+"/"+words[x])
            if verbose_mode == "y" or verbose_mode == "Y":
                print(r)
            if str(r) != "<Response [404]>"  and "404" not in r and int(str(r).split("[")[1].split("]")[0]) not in search_list:
                if verbose_mode == "y" or verbose_mode == "Y":
                    print("HIT")
                hits.append([words[x], r])
            time.sleep(delay)

#random search
def search_rand():
    for x in range(0, rand_mode):
        rand_string = str(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(random.randint(1, 10))))
        if verbose_mode == "y" or verbose_mode == "Y":
            print("Searching "+domain+"/"+rand_string)
        r = requests.get(domain+"/"+rand_string)
        if verbose_mode == "y" or verbose_mode == "Y":
            print(r)
        if str(r) != "<Response [404]>"  and "404" not in r and int(str(r).split("[")[1].split("]")[0]) not in search_list:
            if verbose_mode == "y" or verbose_mode == "Y":
                print("HIT")
            hits.append([rand_string, r])
        time.sleep(delay)

#Using argument inputs to enable/diable each relevent mode
if common_mode != "":
    search_common()

if dict_mode != "":
    if threads > 1:
        thread_list = []
        for i in range(1, 26):
            t = threading.Thread(target=search_dict_threaded, args=(i,))
            thread_list.append(t)
            if verbose_mode == "y" or verbose_mode == "Y":
                print("Creating thread "+str(i)+"...")
        for thread in thread_list:
            thread.start()
            if verbose_mode == "y" or verbose_mode == "Y":
                print("Starting thread "+str(i)+"...")
        for thread in thread_list:
            thread.join()
            if verbose_mode == "y" or verbose_mode == "Y":
                print("Joining thread "+str(i)+"...")
    else:
        search_dict()

if rand_mode != 0:
    thread_list = []
    for i in range(1, threads):
        t = threading.Thread(target=search_rand)
        thread_list.append(t)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    search_rand()

#Simple output code
print("\n------------------------------RESULTS------------------------------")
save_data = save_data + "\n------------------------------RESULTS------------------------------\n"
print("There were "+str(len(hits))+" results:\n")
save_data = save_data + ("There were "+str(len(hits))+" results:\n")
for x in range(0, len(hits)):
    print(domain+"/"+str(hits[x][0])+" returned "+str(hits[x][1]))
    save_data = save_data + (domain+"/"+str(hits[x][0])+" returned "+str(hits[x][1])+"\n")
print("-------------------------------------------------------------------\n")
save_data = save_data + "-------------------------------------------------------------------\n"

if save_location != "":
    f = open(str(save_location), "a")
    f.write("\n"+str(save_data)+"\n")
    f.close()
    if verbose_mode == "y" or verbose_mode == "Y":
        print("File saved successfuly")
