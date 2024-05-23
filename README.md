# urlbrute
This is a command line tool for finding possible paths of a given URL using either word list, random or common paths.

This tool is primarily to generate a list of paths for sites with no/limited sitemaps.

The code is designed to take full advantage of the hardware available as it has the ability to run in multi-threaded mode.

The main (default) wordlist can be edited in a standard text editor and is named "wordlist.txt".

## Requirements:
- requests (python module)
- threading (python module)

## Useage:

| Argument | Expanded argument | Details | Default |
| -------- | ----------------- | ------- | ------- |
| -h | --help | Displays help dialouge | n |
| -C | --common_mode | A pre-defined list of common URL paths are tried, path of file can be specified | n/common paths.txt |
| -R | --rand_mode | A random string will be tried as a path, number of attempts must be specified | n |
| -D | --dict_mode | Every word in the English dictionary will be tried as a path, path of file can be specified | n/wordlist.txt |
| -t | --multi_threading | Enables the multi-threading, number of threads must be specified if argument is used | n/26
| -g | --guided | Enables guided mode which is a menu with extra information about this tool | n |
| -u | --url | This is the root URL that will be used for the testing | - |
| -v | --verbose_output | Debug info will be given including thread info | n |
| -w | --wait | The scheduled delay between attempts | 0 |
| -e | --exclude | It will specify the response type that will be counted as a miss | 404,403 |
| -s | --save | It will save the output in a file, path and file name must be specified | n |

## Examples:
This example will try common paths on the site w3.org, with no wait time between attempts.
```
python urlbrute.py -u "https://w3.org" -C y -w 0
```
The output looks like this:
```
------------------------------RESULTS------------------------------
There were 9 results:

https://w3.org/about returned <Response [200]>
https://w3.org/contact returned <Response [200]>
https://w3.org/info returned <Response [200]>
https://w3.org/robots.txt returned <Response [200]>
https://w3.org/home returned <Response [300]>
https://w3.org/account returned <Response [200]>
https://w3.org/search returned <Response [200]>
https://w3.org/help returned <Response [200]>
https://w3.org/support returned <Response [200]>
-------------------------------------------------------------------
```
However, this example will try all words in the English dictionary as paths on the site google.com, with a wait time of 1 second.
```
python urlbrute.py -u "https://google.com" -D y -w 1
```
The output looks like this:
```
Took too long, I am lazy.
```
This example will try all words in the English dictionary as paths on the site youtube.com, with no wait time and 26 threads (the only available number of threads for this mode).
```
python urlbrute.py -u "https://youtube.com" -D y -w 0 -t 26
```
This example will try all words in the English dictionary as paths on the site google.com, with a wait time of 1 second, 26 threads, debug (verbose) output and file saving.
```
python urlbrute.py -u "https://google.com" -D y -w 1 -v y -s out.txt -t 26
```
It outputted a whole lot of debug info and finally:
```
All searches SUCCESS.
------------------------------RESULTS------------------------------
There were 57 results:

https://google.com/m returned <Response [200]>
https://google.com/s returned <Response [400]>
https://google.com/racing returned <Response [200]>
https://google.com/earth returned <Response [200]>
https://google.com/wallet returned <Response [200]>
https://google.com/ideas returned <Response [200]>
https://google.com/made returned <Response [200]>
https://google.com/keep returned <Response [200]>
https://google.com/takeout returned <Response [200]>
https://google.com/ie returned <Response [200]>
https://google.com/games returned <Response [200]>
https://google.com/about returned <Response [200]>
https://google.com/talk returned <Response [200]>
https://google.com/ramadan returned <Response [200]>
https://google.com/calendar returned <Response [200]>
https://google.com/dashboard returned <Response [200]>
https://google.com/navigation returned <Response [200]>
https://google.com/jigsaw returned <Response [200]>
https://google.com/mail returned <Response [200]>
https://google.com/education returned <Response [200]>
https://google.com/jobs returned <Response [200]>
https://google.com/wave returned <Response [200]>
https://google.com/images returned <Response [200]>
https://google.com/jump returned <Response [200]>
https://google.com/federal returned <Response [200]>
https://google.com/save returned <Response [200]>
https://google.com/saved returned <Response [200]>
https://google.com/video returned <Response [200]>
https://google.com/recovery returned <Response [200]>
https://google.com/views returned <Response [200]>
https://google.com/fiber returned <Response [200]>
https://google.com/scholar returned <Response [200]>
https://google.com/finance returned <Response [200]>
https://google.com/firebase returned <Response [200]>
https://google.com/registry returned <Response [200]>
https://google.com/voice returned <Response [200]>
https://google.com/fit returned <Response [200]>
https://google.com/related returned <Response [200]>
https://google.com/script returned <Response [200]>
https://google.com/vr returned <Response [200]>
https://google.com/search returned <Response [200]>
https://google.com/security returned <Response [200]>
https://google.com/research returned <Response [200]>
https://google.com/local returned <Response [200]>
https://google.com/retail returned <Response [200]>
https://google.com/logos returned <Response [200]>
https://google.com/forms returned <Response [200]>
https://google.com/loon returned <Response [200]>
https://google.com/services returned <Response [200]>
https://google.com/friends returned <Response [200]>
https://google.com/sheets returned <Response [200]>
https://google.com/romance returned <Response [200]>
https://google.com/investor returned <Response [200]>
https://google.com/io returned <Response [200]>
https://google.com/shopping returned <Response [200]>
https://google.com/sky returned <Response [200]>
https://google.com/spaces returned <Response [200]>
-------------------------------------------------------------------
File saved successfuly
```


## Credits:
- Two wordlists have been included in this repo, they are "google-10000-english.txt" and "20k.txt".
  
  They both belong to https://github.com/first20hours/google-10000-english/tree/master.
