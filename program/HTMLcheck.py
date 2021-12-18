# need full path to the two files
# print diffs between these two files
def checkHTML(f1, f2):

    import filecmp

    # shallow comparison
    # NOTE: here you can't write e.g."./xyz.txt"
    result = filecmp.cmp(f1, f2)
#    print(result)
    if(result==True):
        return(result)

    #~~~~~~~~~~~~~~~~~~~~~~~~~

    if result == False:
        # deep comparison
        result = filecmp.cmp(f1, f2, shallow=False)
#        print(result)
        if(result==True):
            return(result)

    #~~~~~~~~~~~~~~~~~~~~~~~~~

    if result == False:

        # Open File in Read Mode
        # NOTE: here you can write e.g."./xyz.txt"
        file_1 = open(f1, 'r')
        file_2 = open(f2, 'r')
        file_3 = open("diffHTML.txt", "w", -1, "utf-8")

        #print("Comparing files ", " @ " + 'file1.txt', " # " + 'file2.txt', sep='\n')
        #print()

        file_1_line = file_1.readline()
        file_2_line = file_2.readline()


        # Use as a Counter
        line_no = 1

        with open(f1) as file1:
            with open(f2) as file2:
                same = set(file1).intersection(file2)


#        print("Difference Lines in Both Files")
        file_3.write("Different Lines in Both Files\n")

        while file_1_line != '' or file_2_line != '':

            # Removing whitespaces
#            file_1_line = file_1_line.rstrip()
            file_1_line = ''.join(file_1_line.split())
#            file_2_line = file_2_line.rstrip()
            file_2_line = ''.join(file_2_line.split())

            # Compare the lines from both file
            if file_1_line != file_2_line:

                # otherwise output the line on file1 and use @ sign
                if file_1_line == '':
#                    print("@", "Line-%d" % line_no, file_1_line)
                    file_3.write("@"); file_3.write("Line-%d" % line_no); file_3.write(file_1_line);file_3.write("\n")

                else:
#                    print("@-", "Line-%d" % line_no, file_1_line)
                    file_3.write("@-"); file_3.write("Line-%d" % line_no); file_3.write(file_1_line); file_3.write("\n");

                # otherwise output the line on file2 and use # sign
                if file_2_line == '':
#                    print("#", "Line-%d" % line_no, file_2_line)
                    file_3.write("#"); file_3.write("Line-%d" % line_no); file_3.write(file_2_line); file_3.write("\n")

                else:
#                    print("#+", "Line-%d" % line_no, file_2_line)
                    file_3.write("#+"); file_3.write("Line-%d" % line_no); file_3.write(file_2_line); file_3.write("\n")

                # Print an empty line
#                print()
                file_3.write("\n")

            # Read the next line from the file
            file_1_line = file_1.readline()
            file_2_line = file_2.readline()

            line_no += 1


        file_1.close()
        file_2.close()
        file_3.close()
        return (result)

# ~ I am thinking about giving here only path to the right folder and in function specify the files to compare ~

#file_no1 = "/home/kali/Desktop/projekt/logs/22_17_12_2021/HTML.txt"
#file_no2 = "/home/kali/Desktop/projekt/logs/21_17_12_2021/HTML.txt"

#checkHTML(file_no1, file_no2)

# checkHTML()
