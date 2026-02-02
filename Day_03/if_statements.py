is_male = True
is_tall = False

# 1st Check
if is_male and is_tall:
    print("You are a tall male")

# 2nd Check (only happens if the 1st one failed)
elif is_male and not(is_tall):
    print("You are a short male")

# 3rd Check (only happens if the 1st and 2nd failed)
elif not(is_male) and is_tall:
    print("You are not a male but are tall")

# The "Fallback" (if none of the above are true)
else:
    print("You are not a male and not tall")