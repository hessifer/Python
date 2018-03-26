import datetime

# parse logfile entries and return id, status, milestone, date_time_stamp
def calc_avg_task_time(file_handle):
    # separate each line by spaces and capture id, status, milestone
    # and date_time_stamp and return avg seconds for tasks
    data_dict = {}

    # td_total (time delta)
    td_total = 0

    for line in file_handle:
        # split line by spaces
        entry = line.strip().split(' ')

        # capture id
        id = entry[3].split('=')[1]

        # capture status
        status = entry[-1].split('=')[1]

        # capture milestone
        milestone = entry[4].split('=')[1]

        # capture date/time stamp for log entry
        date_time_stamp = entry[0]

        # if status is 200 process data
        if status == '200':
            if id not in data_dict and milestone == 'start':
                # capture report_id and store in data_dict with
                # appropriate key/values
                data_dict[id] = {}
                data_dict[id].update(time_start=date_time_stamp)
            elif id in data_dict and milestone == 'end':
                # just update end milestone data in data_dict
                data_dict[id].update(time_end=date_time_stamp)

                t_start = datetime.datetime.strptime(data_dict[id].get(
                    'time_start'), "%Y-%m-%dT%H:%M:%S.%fZ")
                t_stop = datetime.datetime.strptime(data_dict[id].get(
                    'time_end'), "%Y-%m-%dT%H:%M:%S.%fZ")
                td = t_stop - t_start
                ts = td.total_seconds()
                td_total += ts
            else:
                pass
        return td_total / len(data_dict.keys())

# TODO: add argparse functionality so that user can
# specify logfile.
# TODO: make sure we support the log file

# main function
def main():
    msg = "Average time to complete a successful operation: {} seconds."

    # read each line of the file into a buffer
    with open('logfile.txt', 'r') as fh:
        data = fh.readlines()

    print(msg.format(calc_avg_task_time(data)))


if __name__ == '__main__':
    main()
