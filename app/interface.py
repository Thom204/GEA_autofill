import streamlit as st
import json
import pandas as pd
from time import sleep
import get_Student_ID as GID
import Autofill

with open('vars.json', 'r') as file:
    vars = json.load(file)

st.title(f"Registro de asistencias GEA {vars['monitor']}")

# Inicializar estado si no existe
if "student_email" not in st.session_state:
    st.session_state.student_email = ""

if "id_shown" not in st.session_state:
    st.session_state.id_shown = False

# Interfaz principal
activity = st.selectbox('Actividad', ('Tutoria con cita', 'Tutoria abierta', 'taller'), index=1)

placeholder = st.empty()

st.session_state.student_email = placeholder.text_input("Correo del estudiante", value="", key=1)

if 'students' not in st.session_state:
    st.session_state.students = pd.DataFrame({ 'correo':[],'nombre': [],'ID': []})

try:
    id = GID.get(st.session_state.student_email)
    if id != False and st.session_state.student_email != '':
        new_df = pd.DataFrame({'correo': [st.session_state.student_email],
                               'nombre': [GID.details(st.session_state.student_email)],
                               'ID': [id]})
                               
        st.session_state.students = pd.concat([st.session_state.students, new_df], ignore_index=True) 
        st.dataframe(st.session_state.students)
        #st.rerun()
        #st.session_state.student_email = placeholder.text_input("Correo del estudiante", value="", key=2)

        #if st.button("eliminar entrada"):
            #index = st.number_input("numero a eliminar", value=-1, step=1)
            #st.session_state.students = st.session_state.students.drop(len(st.session_state.students['ID'])).reset_index(drop = True)

        if st.button("Registrar todos"):
            try:
                for id in st.session_state.students['ID']:
                    Autofill.fill(vars, activity, id)
                    st.success("🎉 Estudiante registrado exitosamente")
                    sleep(3)

            except Exception as e:
                st.error(f"❌ Error llenando el formulario: {e}")

except RuntimeError:
    pass
