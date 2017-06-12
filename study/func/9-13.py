def self_service(n):
    if(n>5):
        return
    print("self_service %d"%n)
    self_service(n+1)

a=1
self_service(a)
