test_str =input()
print("The original string is : " + str(test_str))
res = sum(1 for c in test_str if c.isalpha())
print("Count of Alphabets : " + str(res))
