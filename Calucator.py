import streamlit as st
st.title('Mini calculator')
monitor=""
st.title(monitor)



first=["x²","1/x","|x|","exp","del"]
seconde=["(",")","n!","mod","/"]
thirty=["xy","7","8","9","X"]
fourty=["10x","4","5","6","--"]
fifty = ["log", "1", "2", "3", "++"]
sixty = ["ln", "*/-", "0","," , "="]

rows=st.columns(len(first))      
row2=st.columns(len(seconde))
row3=st.columns(len(thirty))
row4=st.columns(len(fourty))
row5=st.columns(len(fifty))
row6=st.columns(len(sixty))
class Calculator :
 
 def __init__(self,value=""):
  self.output=value

 def Screen(self,M):
  self.output=self.output+ M
  st.title(self.output)

 def button(self):
  for i,col in enumerate(rows):   
   with col: 
    if st.button(first[i]):
     
     self.Screen(first[i])
     

  for i, col in enumerate(row2):
    with col:
     st.button(seconde[i])
      
  for i, col in enumerate(row3):
    with col:
     st.button(thirty[i])
  for i, col in enumerate(row4):
    with col:
     st.button(fourty[i])
  for i, col in enumerate(row5):
    with col:
     st.button(fifty[i])
  for i, col in enumerate(row6):
    with col:
     st.button(sixty[i])


def main():

  Cal=Calculator("")
  st.write()
  Cal.Screen(Cal.output)
  Cal.button()

main()



