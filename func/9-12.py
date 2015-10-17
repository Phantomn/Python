i=1
def self_service():
    global i
    if(i>5):
        return
    print("self_service : %d"%i)
    i+=1
    self_service()

self_service()

