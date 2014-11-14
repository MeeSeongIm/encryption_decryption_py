
# if one wants to use openSSL algorithms available on one's computer. 
 
import hashlib
hash_ob = hashlib.new('DSA')
hash_ob.update(b'Testing!')
print("Testing! in DSA: " + hash_ob.hexdigest())

hash_ob_SHA = hashlib.new('SHA')
hash_ob_SHA.update(b'Testing!')
print("Testing! in SHA: " + hash_ob_SHA.hexdigest())

hash_ob_SHA_letter = hashlib.new('SHA')
hash_ob_SHA_letter.update(b'T')
print("T in SHA: " + hash_ob_SHA_letter.hexdigest())

print("\n")

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)


"""
Testing! in DSA: 913bd7710451e36b15dd3c1a41fcc43bf4bf92de
Testing! in SHA: e811be3d6357cebf4508d4ff107c92a66c49eeae
T in SHA: cf53b69f03bece9be0c792ac340f179c49a1ec05


{'dsaWithSHA', 'SHA384', 'SHA', 'SHA1', 'dsaEncryption', 'RIPEMD160', 'DSA', 'sha1', 'ripemd160', 'SHA256', 'sha384', 'whirlpool', 'ecdsa-with-SHA1', 'sha', 'MD5', 'sha224', 'MD4', 'md5', 'DSA-SHA', 'SHA512', 'md4', 'sha512', 'SHA224', 'sha256'}
{'sha224', 'md5', 'sha1', 'sha512', 'sha384', 'sha256'}
""" 



