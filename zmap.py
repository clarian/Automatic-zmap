import subprocess
import os
import sys
   
print("\x1b[0;32m**********************************\x1b[0m")    
print("\x1b[0;32m*Coded by Clarian :)*\x1b[0m")
print("\x1b[0;32m**********************************\x1b[0m")
 
def run(cmd):
    subprocess.call(cmd, shell=True)
   
 
print("\x1b[0;32mDo you wish to install all the dependencies?\x1b[0m")
faggot = raw_input("Ready to scan them ranges nigga?  Y/n: ")
if faggot.lower() == "y":
    print("Installing all the dependencies...")
    run("yum install perl -y")
    run("yum update -y")
    run("yum install gcc cmake gmp gmp-devel libpcap-devel gengetopt byacc flex -y")
    run("yum install json-c-doc.noarch json-c.i686 json-c.x86_64 json-c-devel.i686 json-c-devel.x86_64 -y")
    run("yum install epel-release -y")
    run("yum install gengetopt -y")
 
print("\x1b[0;32mDo you wish to download, unzip and compile all the files? \x1b[0m")        
nig = raw_input("Y or N, how hard is it to understand?  Y/n: ")
if nig.lower() == "y":
    run("wget https://github.com/zmap/zmap/archive/v2.1.0.tar.gz")
    run("tar -xvf v2.1.0.tar.gz")
    run("clear")
    run("cd zmap-2.1.0")
    run("clear")
    run('flex -o "src'+ 'lexer.c" --header-file="src/lexer.h" "src/lexer.l"')
    run("clear")
    run("byacc -d -o " + "src" + "parser.c" + "src/parser.y")
    run("clear")
    run("mkdir /etc/zmap")
    run("clear")
    run("cp conf/* /etc/zmap")
    run("clear")
    run("cmake -DENABLE_HARDENING=ON")
    run("clear")
    run("make")
    run("make install")
    run("clear")
if nig.lower() == "n":
   print("Do it yourself then you ungrateful skid.");
 
if nig.lower() == "y":
    run("clear")
    print("\x1b[;031mNow you have ZMAP, you can scan some dank ranges now!")
    print("\x1b[;031mRemember to get a blacklist so your server doesn't get rekt by honeypots")
    print("\x1b[;031mTutorial that explains how to find IP-Ranges coming soon!")
    print("\x1b[;031m| Code created by Clarian. |x1b[0m")
