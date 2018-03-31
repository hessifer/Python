def parse_host_file(host_file='/etc/hosts'):
    """Parse valid host file entries from host_file.
    Keyword arguments:
    host_file -- the location of the hosts file (default '/etc/hosts')
    Return values:
    data -- information structure for valid host file entries
    """
    host_file_entries = []
    # create an ignore list
    ignore_ips = ["127.0.0.1", "::1"]

    with open(host_file, 'r') as fh:
        data = fh.readlines()

    for line in data:
        ls = line.strip()
        if ls:
            ip = ls.split()[0]
            fqdn = ls.split()[1]
            host = ls.split()[2]
            print(ls.split()[0])

def main():
    """Program begins here."""
    parse_host_file()

    

if __name__ == '__main__':
    main()