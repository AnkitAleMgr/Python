
def program(s1, s2, s3):
    temp_variable = ""
    for i in range(max(len(s1), len(s2))):
            temp_variable += s1[i]
            temp_variable += s2[i]
        


    return s3 == temp_variable







if __name__ == "__main__":
    s1 = "abc"
    s2 = "cdf5g"
    s3 = "acbdcf"

    result = program(s1,s2,s3)
    print(result)


