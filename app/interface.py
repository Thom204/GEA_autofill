import streamlit as st
import json
import get_Student_ID as GID
import Autofill

with open('vars.json', 'r') as file:
    vars = json.load(file)

st.title(f"registro de asistencias GEA {vars['monitor']}")
activity = st.selectbox('Actividad', ('Tutoria con cita', 'Tutoria abierta', 'taller'), index=1)
student_email = st.text_input("Correo del estudiante")

try:
    id = GID.get(student_email)
    if id != False:
        st.text(f'Estudiante {GID.details(student_email)}')
        st.text(f'Número asignado {id}')

        if st.button("Registrar"):
            Autofill.fill(vars, id)
            st.write("Registrado Exitosamente!")
        

except RuntimeError as e:
    pass