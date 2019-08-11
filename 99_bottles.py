bottles = 99

while bottles:
    print(
        f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
    bottles -= 1
    print(
        f"Take one down, pass it around, {bottles} bottles of beer on the wall.\n")
    if bottles == 1:
        print(
            f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
        bottles -= 1
        print(
            f"Take one down, pass it around, {bottles} bottles of beer on the wall.")
