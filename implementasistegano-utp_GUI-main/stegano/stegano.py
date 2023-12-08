from stegano import lsb

secret = lsb.hide("panda.jpg", "universitan pelita bangsa")

secret.save("sat-sec.png")

print(lsb.reveal("panda-sec.png"))