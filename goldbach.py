def prime(n):
  if n < 2:
    return False
  for i in range(n//2+1):
    if n % i == 0:
      return False
  return True

def Goldbach(n):
  res=[]
  for i in range((n//2)+1):
    if prime(i) == True:
      if prime(n-i) == True:
        res.append((i,n-i))
  return(res)
        