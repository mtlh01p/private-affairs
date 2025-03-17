slicedup = "Jangan tinggalkan barang Anda tanpa diawasi."
print(slicedup[1:7])
print(slicedup[11:1:-2])

additional = slicedup[0:25] + "saya" + slicedup[29:len(slicedup)]
print(additional)
print("Location of d is", slicedup.find('d'))
sliceddown = slicedup * 3
print(sliceddown)