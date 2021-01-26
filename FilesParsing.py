import re
import DictionaryClass
import subprocess


# A function that pastes disk IDs into command
# 'symaccess list -type stor -dev DISKID -sid 723'
def paste_disk_ids(d_id):
    subprocess.call('symaccess list -type stor -dev ' + d_id +
                    ' -sid 723', shell=True)


# A function that helps with dictionary pretty printing
def dict_pretty_print(d, i):
    return 'Date - ' + i + \
           ' \nTotal number of messages happened on that date - ' + \
           str(d[i]) + '\n\n'


# 1. From messages.txt we get all the lines
# that contain <err> using regular expression;

# 2. After that from these lines we extract dates in format yyyy-mm-dd
# and count number of messages happened on each
# unique date we found;

# 3. We create a dictionary (date is a key and number of messages is a value)
# using custom type (NewDictionary);

# 3. We count number of messages that contain <err> and write it to output.txt;

# 4. We write created dictionary to output.txt
# using custom function dict_pretty_print.
def task_one():
    regex_for_err = re.compile('<err>')
    regex_for_date = re.compile(r'\d{4}-\d{2}-\d{2}')
    msgs_with_err = []
    dates = []
    # Dictionary of custom type (NewDictionary) with ADD operation
    events_on_date = DictionaryClass.NewDictionary()
    # Value for counting number of messages happened on particular date
    events_count = 1
    with open("./messages.txt", "r") as message_file:
        for msg in message_file:
            if re.search(regex_for_err, msg) is not None:
                msgs_with_err.append(re.search(regex_for_err, msg))
                dates.append(re.search(regex_for_date, msg).group(0))
    for i in range(0, len(dates) - 1):
        if dates[i] == dates[i + 1]:
            events_count = events_count + 1
        else:
            events_on_date.add(dates[i], events_count)
            events_count = 1
    with open("./output.txt", 'a') as output_file:
        if len(msgs_with_err) != 0:
            output_file.write("There are " + str(len(msgs_with_err)) +
                              " messages with <err>" + "\n\n")
            for item in events_on_date:
                output_file.write(dict_pretty_print(events_on_date, item))
        else:
            output_file.write("There are no messages with <err>")


# 1. From vmax.txt we extract disk IDs using regular expression;

# 2. Then we pass that IDs to custom function paste_disk_ids;

# 3. That function pastes IDs into command
# 'symaccess list -type stor -dev DISKID -sid 723'.
def task_two():
    regex_for_disk_ids = re.compile(r'([0-9A-Z]{5}) ')
    with open("./vmax.txt", "r") as vmax_file:
        for line in vmax_file:
            disk_id = re.search(regex_for_disk_ids, line)
            if disk_id is not None:
                paste_disk_ids(disk_id[1])


def main():
    task_one()
    task_two()


if __name__ == '__main__':
    main()
