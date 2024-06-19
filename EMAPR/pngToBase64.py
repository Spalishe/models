import base64

Files = [
    "drip_fall.png",
]

for n in Files:
    with open(n,"rb") as f:
        string = base64.b64encode(f.read())
        with open(n.replace(".png","B64.txt"),"wb") as f1:
            f1.write(string)