#!/usr/bin/python3
"""Task: Search and update
"""


def append_after(filename="", search_string="", new_string=""):
        """inserts a line of text to a file, after each line
           containing a specific string
        Args:
            filename (str): file to searc and update
            search_string (str): string to look for
            new_string (str): what's gonna be added
        """
        with open(filename, encoding="utf-8") as my_file:
            text = my_file.read()
        text_list = text.split("\n")
        for i in range(len(text_list)):
            if search_string in text_list[i]:
                text_list[i] = text_list[i] + "\n" + new_string
            elif (i != len(text_list) - 1):
                text_list[i] = text_list[i] + "\n"
        final_txt = ''.join(text_list)
        with open(filename, encoding="utf-8", mode="w") as my_file2:
            my_file2.write(final_txt)
