def sayhelo(nama):
    return (f"helo{nama}")


def total(*list):
    hasil=0
    for data in list:
        hasil = hasil+data
    return hasil