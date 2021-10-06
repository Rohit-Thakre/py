
"""
            task 
have to enter ac no. or something, 
it shoud have to satisfy the following conditions,
1. the length of characters should be 11
2. first 4 characters should uppercase 
3. 5th character should be 0.

text could look like this:
SBIN0123456

"""


def check():
    # for terminal clear and color to green
    import os
    os.system("cls")
    os.system("color a")

    text = input("enter your text here \t")
    # text = "SBIN0125456"
    # print(len(text))

    # print(str.upper(text[0]))
    if len(text) == 11:

        # print("len 11: first condiont cheaked and correct")
        if str.isupper(text[0:4]):
            # print("upper:okay second condition cheaked and correct")
            # print(text[4])

            if text[4] == "0":
                # print("0 condion cheaked and found okay")
                print("Output : acceptable", )

            else:
                print("0 missing at 5th position !")

        else:
            print("First 4 characters should be alphabet and in upper case.")

        # pass

    else:
        print("length expected 11 alphanumeric keys:\nand got:", len(text))


check()
