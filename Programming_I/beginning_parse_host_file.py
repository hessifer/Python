#!/usr/bin/env python3

def parse_host_file(host_file='/etc/hosts'):
    """Parse valid host file entries from host_file.

    Keyword arguments:
    host_file -- the location of the hosts file (default '/etc/hosts')

    Return values:
    data -- information structure for valid host file entries
    """
    host_file_entries = []

    with open(host_file, 'r') as fh:
        data = fh.readlines()

    for line in data:
        ls = line.strip()
        if ls and ls[0] != '#':
            host_file_entries.append(ls)
    return host_file_entries

def main():
    """Begins the program."""
    for entry in parse_host_file():
        entry_split = entry.split()
        len_entry_split = len(entry_split)

        if len_entry_split == 3:
            print("IPADDR: {:>5}\t\tDNS: {:<25}HOST: {:<15}\n".format(
                entry_split[0], entry_split[1], entry_split[2]))
        elif len_entry_split == 2:
            print("IPADDR: {:>5}\t\tDNS: {}\n".format(
                entry_split[0], entry_split[1]))
        else:
            continue

if __name__ == '__main__':
    main()
