import streamlit as st
import math

st.set_page_config(page_title="Calculatrice Avancée")
st.title("Calculatrice Scientifique")

# Initialiser l'état
if "monitor" not in st.session_state:
    st.session_state.monitor = ""

# Affichage de l'écran
st.markdown("### Écran :")
st.code(st.session_state.monitor, language="python")

# Fonction principale
def add_to_monitor(value):
    try:
        if value == "=":
            result = eval_expr(st.session_state.monitor)
            st.session_state.monitor = str(result)
        elif value == "del":
            st.session_state.monitor = st.session_state.monitor[:-1]
        elif value == "Sup":
            st.session_state.monitor = ""
        elif value == "x²":
            st.session_state.monitor = str(eval_expr(st.session_state.monitor) ** 2)
        elif value == "1/x":
            st.session_state.monitor = str(1 / eval_expr(st.session_state.monitor))
        elif value == "|x|":
            st.session_state.monitor = str(abs(eval_expr(st.session_state.monitor)))
        elif value == "n!":
            st.session_state.monitor = str(math.factorial(int(eval_expr(st.session_state.monitor))))
        elif value == "mod":
            st.session_state.monitor += "%"
        elif value == "10x":
            st.session_state.monitor += "*10"
        elif value == "log":
            st.session_state.monitor = str(math.log10(eval_expr(st.session_state.monitor)))
        elif value == "ln":
            st.session_state.monitor = str(math.log(eval_expr(st.session_state.monitor)))
        elif value == "xy":
            st.session_state.monitor += "**"
        else:
            st.session_state.monitor += value
    except Exception as e:
        st.session_state.monitor = "Erreur"

    st.rerun()

# Évaluer l'expression de manière sécurisée
def eval_expr(expr):
    try:
        return eval(expr)
    except:
        return "Erreur"

# Interface
def create_row(buttons):
    cols = st.columns(len(buttons))
    for i, col in enumerate(cols):
        with col:
            if st.button( f"{buttons[i]}," , key=f"btn{buttons[i]}-{i}"):
                add_to_monitor(buttons[i])

rows = [
    ["x²", "1/x", "|x|", "Sup", "del"],
    ["(", ")", "n!", "mod", "/"],
    ["xy", "7", "8", "9", "*"],
    ["10x", "4", "5", "6", "-"],
    ["log", "1", "2", "3", "+"],
    ["ln", "*/-", "0", ".", "="]
]

for row in rows:
    create_row(row)
