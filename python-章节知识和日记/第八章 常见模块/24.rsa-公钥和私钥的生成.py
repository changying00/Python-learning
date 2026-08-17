





import rsa

public_key,private_key = rsa.newkeys(2048)


public_bytes = public_key.save_pkcs1()

with open("./public.pem","wb") as file:
    file.write(public_bytes)

private_bytes  = private_key.save_pkcs1()
with open("./private.pem","wb")as file:
    file.write(private_bytes)