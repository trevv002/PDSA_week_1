#creating a triangle class with every possible properties of a general triangle.

class Triangle():
  def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c
  def Is_valid(self):
    if self.a >= self.b + self.c:
       return "Invalid"
    elif self.b >= self.a + self.c:
       return "Invalid"
    elif self.c >= self.b + self.a:
       return "Invalid"
    else:
      return "Valid
  def Side_Classification(self):
      if Is_valid() == "Valid":
          if self.a == self.b == self.c:
             return "Equilateral"
          elif (self.a == self.b) or (self.b == self.c) or (self.c == self.a):
             return "Isosceles" 
          else:
               return "Scalene"
      else:
        return "Invalid"

  def Angle_Classification(self):
    if Is_valid()== "Valid"
      if self.a*self.a = self.b*self.b >= self.c*self.c:
         return "Acute"
      elif self.a*self.a = self.b*self.b == self.c*self.c:
         return "Right"
      elif self.a*self.a = self.b*self.b <= self.c*self.c:
         return "Obtuse"
    else:
      return "Invalid"

  def Area(self):
    if Is_valid() == "Valid":
      s=(self.a+self.b+self.c)/2
      return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
    return 'Invalid'
      

      
