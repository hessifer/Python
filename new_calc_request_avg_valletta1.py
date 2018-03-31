"""Something wonderful here."""
import datetime
import sys

# parse logfile entries and return id, status, milestone, date_time_stamp
def calc_avg_task_time(file_handle):
    """Something cool here."""
    # separate each line by spaces and capture id, status, milestone,
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

        # capture date/time stamp for milestone start
        date_time_stamp = entry[0]

        # if status is 200
        if status == '200':
            if id not in data_dict and milestone == 'start':
                # capture report_id and store in data_dict with
                # appropriate key/values
                data_dict[id] = {}
                data_dict[id].update(time_start=date_time_stamp)
            elif id in data_dict and milestone == 'end':
                # just update stop milestone data
                data_dict[id].update(time_end=date_time_stamp)


                t_start = datetime.datetime.strptime(data_dict[id].get('time_start'), "%Y-%m-%dT%H:%M:%S.%fZ")

                t_stop = datetime.datetime.strptime(data_dict[id].get(
                   'time_end'), "%Y-%m-%dT%H:%M:%S.%fZ")

                td = t_stop - t_start
                ts = td.total_seconds()
                # no need to store this if we do not keep it around.
                # data_dict[key].update(td=ts)
                td_total += ts
            else:
                pass

    return td_total / len(data_dict.keys())


# TODO: -Charles add argparse functionality so that user can
# specify log file.
# TODO: What do we do with edge case where we have an end with no
# starts as well as a start with no end (log this)
# TODO: are there any cases for exception handling?

def is_supported(file_handle):

    template = ['customer_id','task','report_id','milestone','result']
    for line in file_handle:
	    # Get tags for each field
        line_list = [x.split("=")[0] for x in line.split(" ")]     
        try:
		    # First item should be a datetime - fail if not
            datetime.datetime.strptime(line_list[0], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            return False
        # Ensure tags match file layout - fail if they don't
        if not line_list[1:] == template:
            return False
    return True

# main function
def main():
    """Show your awesome skillzs."""
    msg = "Average time to complete a successful operation: {} seconds."

    # read each line of the file into a buffer
    with open('logfile.txt', 'r') as fh:
        data = fh.readlines()
    # only run if the file is supported
    if is_supported(data):
        print(msg.format(calc_avg_task_time(data)))
    else:
        print('Unsupported Filetype')

if __name__ == '__main__':
    main()

