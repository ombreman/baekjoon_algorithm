alphabet = input()

alphabet = alphabet.replace("c=", "a").replace("c-", "b").replace("dz=", "c").replace("d-", "d").replace("lj", "e").replace("nj", "f").replace("s=", "g").replace("z=", "h")

print(len(alphabet))
