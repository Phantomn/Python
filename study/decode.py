#-*- coding: utf-8 -*-
def encode(strs):
   returns = ""
   for i in range(len(strs)):
      returns += chr((((ord(strs[i])^10+i)<<1)^50)/2)
   return returns

print(encode("{fad-9&`~hhia jr,llicg [S_^W NY@믒_[^X"))
