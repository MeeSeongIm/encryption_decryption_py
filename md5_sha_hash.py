 
import hashlib
my_string = input("Enter a string to be hashed: ")     # Assumes the default UTF-8, user-input needed.
hash_object = hashlib.md5(my_string.encode())
hash_object_two = hashlib.sha1(my_string.encode())
hash_object_three = hashlib.sha224(my_string.encode())
hash_object_four = hashlib.sha256(my_string.encode())

print("in md5: %s" % hash_object.hexdigest())
print("in sha1: %s" % hash_object_two.hexdigest())
print("in sha224: %s " % hash_object_three.hexdigest())
print("in sha256: %s " % hash_object_four.hexdigest())

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)



"""
Output: 

Enter a string to be hashed: this is a string
in md5: b37e16c620c055cf8207b999e3270e9b
in sha1: 517592df8fec3ad146a79a9af153db2a4d784ec5
in sha224: 2b3540d8c2ad0351fd4fd9c49767d68466f54c4a134b519461e5c03b 
in sha256: bc7e8a24e2911a5827c9b33d618531ef094937f2b3803a591c625d0ede1fffc6 
{'sha1', 'dsaEncryption', 'SHA1', 'ecdsa-with-SHA1', 'md4', 'MD5', 'SHA384', 'SHA512', 'md5', 'ripemd160', 'RIPEMD160', 'sha224', 'DSA', 'DSA-SHA', 'MD4', 'SHA', 'SHA256', 'sha256', 'sha384', 'sha', 'SHA224', 'whirlpool', 'sha512', 'dsaWithSHA'}
{'sha1', 'sha224', 'sha256', 'md5', 'sha384', 'sha512'}
"""


