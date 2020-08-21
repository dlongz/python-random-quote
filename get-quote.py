import random

def quotes():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rdm = random.randint(0,last)
  print(quotes[rdm])

if __name__== "__main__":
  quotes()