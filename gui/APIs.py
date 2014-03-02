# My APIs that I like to use in programs. These are imported by
# 'import APIs' (to import all) or 'from APIs import example', where
# example is the function name.
# Alex Potter


def shell_command_OLD(command): # depricated
    import subprocess
    process = subprocess.Popen([command],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(process.stdout.readline, b'')

def shell_command(command, loadingtext): # works with UNIX commands
    import subprocess

    
    print(loadingtext)
    
    try:
        s = subprocess.getstatusoutput(command)
    except(KeyboardInterrupt, SystemExit):
        raise
    except:
        print("An error occurred whilst executing the shell command!\nNote that this only executes on Linux (apt).")
    else:
        output = s[1].split("\n")
        print(output)


def system_path(): # returns system PATH environment variable
    import sys
    print(sys.path)

def pinger(ip): # pings ip address
    import subprocess

    global ping_first
    ping_first = str("Pinging %s, please wait..." % ip)

    process = subprocess.Popen(["ping", "-v", "-c 3", "%s" % ip], stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    out, error = process.communicate()
    out = out.strip()
    error = error.strip()
    global output
    output = out.decode('utf-8')
    global errorout
    errorout = error.decode('utf-8')
            

        
            
            


            
                
                
