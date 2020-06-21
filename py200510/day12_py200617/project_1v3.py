# v3. Encrypting Password
# For security reasons, the password should not directly be persisted into databases in original form.
# It is recommended that every character should get right shifted for 3 steps.
# For example,
# a -> d,   b -> e,  c -> f,  …, 0 -> 3
# print out the encrypted password
# then decrypt the password and print it out to compare it with the original one