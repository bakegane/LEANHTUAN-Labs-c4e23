def remove_dollar_sign(s):
    new = s.replace("$", "")
    return new
string_with_no_dollars = remove_dollar_sign("80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Correct")
else:
    print("Buggggggg")