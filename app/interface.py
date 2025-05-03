import streamlit as st
import json
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
student_email = st.text_input("Correo del estudiante", value=st.session_state.student_email)

try:
    id = GID.get(student_email)
    if id != False:
        st.text(f'Estudiante {GID.details(student_email)}')
        st.text(f'Número asignado {id}')
        st.session_state.id_shown = True

        if st.button("Registrar"):
            try: 
                Autofill.fill(vars, activity, id)
                st.success("🎉 Estudiante registrado exitosamente")
                
                # Reiniciar campos
                st.session_state.student_email = ""
                st.session_state.id_shown = False
                st.rerun()  # Recargar la interfaz limpia

            except Exception as e:
                st.error(f"❌ Error llenando el formulario: {e}")

except RuntimeError:
    pass
