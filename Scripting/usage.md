### Introduction:
This is the solution to the problem mentioned in the scripting section of the Blackberry QNX Technical Assignment for Software Developer in Test.

### Usage:
To use this script, first you need to install the required packages and modules.

#### Requirements:
netperf should be installed and netserver should be running before runnign this script. Requirements are given in the requirements.txt file.

To install the requirements, run the following command:

```
./install_reqs.sh
```

If the script is not running, run the following commands:

```
chmod +x install_reqs.sh
./install_reqs
```

#### Note:
If modifying the source code and adding more modules/packages to the code, and need to add them to requirements.txt file, add them at the end of the file.

To run the script, run the following command:
```
./script.py num_iters
```

Where num_iters is the number of iterations for which netperf should run

To check the usage message run the command:

```
./script.py -h
```

Output:
```
usage: script.py [-h] count

positional arguments:
  count       Number of iterations to run netperf

optional arguments:
  -h, --help  show this help message and exit
```
