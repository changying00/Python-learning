import rsa

public_key,private_key = rsa.newkeys(2048)

with open("./public.pem", "wt") as f:
    f.write(public_key)