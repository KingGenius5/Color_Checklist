checklist = list()

#create
def create(item):#create item code here
    checklist.append(item)

#read
def read(index):#read code here
    return checklist[index]

#update
def update(index, item):#update code here
    checklist[index] = item

#destroy
def destroy(index):#destroy code here
    checklist.pop(index)

def test():#add testing code here
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(read(1))

test()
