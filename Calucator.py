import streamlit as st

st.title("Mini calculator")

def Calcuator():
 if "monitor" not in st.session_state:
     st.session_state.monitor = ""


 def add_to_monitor(value):
    if value !="=":
     st.session_state.monitor=str(st.session_state.monitor) 
     st.session_state.monitor+= value
    else:
        st.session_state.monitor= eval(st.session_state.monitor)
        
        Operation(st.session_state.monitor)
    st.rerun() 
 st.markdown("### Écran :")
 st.code(st.session_state.monitor)
 def create_row(row):
     cols = st.columns(len(row))
     for i, col in enumerate(cols):
         with col: 
             if st.button(row[i],key=row[i])  :
                
                 
                 add_to_monitor(row[i])
                
                     
              

 first = ["x²", "1/x", "|x|", "exp", "del"]
 second = ["(", ")", "n!", "mod", "/"]
 third = ["xy", "7", "8", "9", "*"]
 fourth = ["10x", "4", "5", "6",'-' ]
 fifth = ["log", "1", "2", "3", "+"]
 sixth = ["ln", "*/-", "0", ".", "="]
 
 def Operation(ope):

    return st.title(ope)

    
 
 create_row(first)
 create_row(second)
 create_row(third)
 create_row(fourth)
 create_row(fifth)
 create_row(sixth)

def main():
    Calcuator()

main()

