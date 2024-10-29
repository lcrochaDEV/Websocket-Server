from subprocess import check_output 

class LinuxCLI:
    @staticmethod
    def raspberry(cli):
        check_output(cli)


'''
uname -m = armv6l
uname -n = raspberrypi
uname -o = GNU/Linux
'''