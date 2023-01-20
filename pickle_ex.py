import pickle
mylist = [1,2,3,4]
int = "dax"
ser = pickle.dumps(mylist)
name = pickle.dumps(int)
print("num : ", name)
print("mylist : ", ser)

print("mylist: ",pickle.loads(ser),"dumps: ", pickle.dumps(mylist))
print("name: ", pickle.loads(name))

#in the output at starting b indicates the output is in bytes