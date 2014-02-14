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

class PING:
    def pinger(ip): # pings ip address
        import subprocess
        import re   
        __builtins__.output1 = "Pinging %s" % ip
        ret = subprocess.call("ping -c 1 %s" % ip, shell=True, # checks whether site is up
                                  stdout=open('/dev/null', 'w'),
                                  stderr=subprocess.STDOUT)
        if ret == 0:
            CMD = ['ping', '-c', '1', '%s' % ip]
            result = str(subprocess.check_output(CMD)) # gets 3 ping times
            __builtins__.output2 = "%s is up! (%s)" % (ip, result)
            
                 
        else:
            __builtins__.output3 = "%s didn't respond." % ip # these need to be displayed by print/labelVariable.set()
            

        
            
            


            
                
                
