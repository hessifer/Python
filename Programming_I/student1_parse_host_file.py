# import our modules
import os.path as op


def main():
    """Program starts here."""
    parse_host_file('/etc/hosts')


def parse_host_file(hostfile='C:\Sara\Python\Student\hosts.log'):
    if op.isfile(hostfile):
        with open(hostfile, 'r') as fh:
            file_info = fh.readlines()

        # loop over each line of text in file_info
        for line in file_info:
            # strip the line of whitspaces and create the ls list
            ls = line.strip()

            # TODO: find a way to improve the code so that we are not
            # using split() so many times. (HINT: use a variable to store the
            # results of the split() function.)

            # TODO: implement an IGNORE list so that if any IP are in the
            # IGNORE list, you do not process them. For example we do not need
            # ::1, 127.0.0.1. Implement this either as a function or directly
            # your code.

            # if we have data in the list
            if ls and not ls.split()[0][0] == '#':
                # get the number of elements in our list
                # for example do we have IP, FQDN, and HOST
                num_of_elements = len(ls.split())

                # if we have all three do this
                if num_of_elements == 3:
                    IP = ls.split()[0]
                    FQDN = ls.split()[1]
                    HOST = ls.split()[2]

                    print("IP: {}\nFQDN:{}\nHOST: {}\n".format(IP, FQDN, HOST))
                # if we have only the first two do this
                elif num_of_elements == 2:
                    IP = ls.split()[0]
                    FQDN = ls.split()[1]

                    print("IP: {}\nFQDN:{}\n".format(IP, FQDN))
                # for all other conditions just continue
                else:
                    continue

    else:
        print("ERROR: Unable to locate file: {}".format(hostfile))


if __name__ == '__main__':
        main()
