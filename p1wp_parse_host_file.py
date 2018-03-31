"""
    FileName: p1wp_parse_host_file.py
    Author: Charles A. Hessifer
    Date: 03/28/2018
    Version: 0.01
"""
import os.path as op
import sys

# program begins here
def main():
    parse_host_file()

# function to parse data from host file
def parse_host_file(hostfile='/etc/hosts'):
    if op.isfile(hostfile):
        # here we will store IPADDR, FQDN, HOST info
        data = []

        # open the file and get its contents
        with open(hostfile, 'r') as fh:
            file_info = fh.readlines()

        # loop over file contents and if
        # line is not blank and does
        # not start with a '#', print
        # the line
        for line in file_info:
            if not line[0] == '#':
                if line.strip():
                    ipaddr = line.strip().split()[0]
                    print("IPADDR: {}".format(ipaddr))
                    # print FQDN: value
                    # if there is a host value, print HOST: value
    else:
        sys.exit("ERROR: Could not access hostfile: {}".format(hostfile))


if __name__ == '__main__':
    main()
