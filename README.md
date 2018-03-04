# PasswordChecker
A Python wrapper that utilizes Troy Hunt's Pwned Passwords V2 API. 

This script uses the range service which implements the k-Anonymity mathematical property that allows a password to be searched for by its partial hash.

As stated by Troy Hunt on his post at https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/

> Using this model, someone searching the data set just gets back the hash suffixes and counts (everything in bold after the first 5 chars) and they can then see if everything after the first 5 chars of their hash matches any of the returned strings. Now keep in mind that as far as I'm concerned, the partial hash I was sent could be any one of 475 different possible values. Or it could be something totally different, I simply don't know and therein lies the anonymity value.




