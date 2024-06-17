import base64

Files = [
    "soul_fire_flame.png",
    "smoke_atlas.png",
    "Lava.png",
    "flash.png",
    "flame.png",
    "falling_obsidian_tear_atlas.png",
    "explosion_atlas.png",
    "end_rod_atlas.png",
    "electric_spark.png",
    "campfire_smoke_atlas.png",
]

for n in Files:
    with open(n,"rb") as f:
        string = base64.b64encode(f.read())
        with open(n.replace(".png","B64.txt"),"wb") as f1:
            f1.write(string)