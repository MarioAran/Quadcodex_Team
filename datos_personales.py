import streamlit as st
st.set_page_config(page_title="Datos Personales", layout="centered")

# Las classes para manejar los datos del usuario

class Usuario_datos:
    def __init__(self, nombre, apellido, edad, genero, altura, peso, objetivo, nivel):
        self.Nombre = nombre
        self.Apellido = apellido
        self.Edad = edad
        self.Genero = genero
        self.Altura = altura
        self.Peso = peso
        self.Objetivo = objetivo
        self.Nivel = nivel


class Gestor_Usuario:

    def get_usuario(self, nombre_completo, edad, genero, altura, peso, objetivo, nivel):
        nombre, apellido = self.verif_nombre(nombre_completo)
        edad = self.verif_edad(edad)
        genero = self.verif_genero(genero)
        altura = self.verif_altura(altura)
        peso = self.verif_peso(peso)
        objetivo = self.verif_objetivo(objetivo)
        nivel = self.verif_nivel(nivel)

        return Usuario_datos(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            genero=genero,
            altura=altura,
            peso=peso,
            objetivo=objetivo,
            nivel=nivel
        )

# La parte de verificaciñon para todos los datos.

    def verif_nombre(self, nombre_completo):
        partes = nombre_completo.strip().split()
        if len(partes) == 0:
            return ("", "")
        nombre = partes[0]
        apellido = " ".join(partes[1:]) if len(partes) > 1 else ""
        return (nombre, apellido)

    def verif_edad(self, edad):
        return max(12, min(edad, 80))

    def verif_genero(self, genero):
        genero = genero.lower()
        if genero in ["male", "masculino"]:
            return "Male"
        if genero in ["female", "femenino"]:
            return "Female"
        return "Other"

    def verif_altura(self, altura):
        return max(100, min(altura, 270))

    def verif_peso(self, peso):
        return max(30, min(peso, 300))

    def verif_objetivo(self, objetivo):
        objetivo = objetivo.lower()
        if "gain" in objetivo:
            return "Gain muscle"
        if "lose" in objetivo:
            return "Lose weight"
        return "Unknown"

    def verif_nivel(self, nivel):
        return nivel.split("(")[0].strip()

st.markdown("""
<style>
    .card {
        background: linear-gradient(180deg, #a1d6e2, #a1d6e2);
        border-radius: 12px;
        padding: 18px;
        color: #e6f6ff;
        box-shadow: 0 6px 18px rgba(0,0,0,0.5);
    }
    .label {
        color: #afd7ff;
        font-weight: 600;
    }
    .metric {
        font-size: 20px;
        font-weight: 700;
        color: #d8f3ff;
    }
    .small {
        color: #bcdff7;
        font-size: 13px;
    }
    .two-col { display:flex; gap:12px; }
    .two-col > div { flex: 1; }
</style>
""", unsafe_allow_html=True)

st.title("Sign up and join our community!")
st.markdown("Fill in your personal details to join our community.")

gestor = Gestor_Usuario()

with st.form("perfil_gym_form", clear_on_submit=False):
    st.header("New Registration")
    col1, col2 = st.columns(2)

    with col1:
        nombre_completo = st.text_input("Full name (mandatory)", max_chars=80)
        fecha_nac = st.date_input("Birth date (mandatory)")
        genero = st.selectbox("Gender (mandatory)", ["Male","Female"])

    with col2:
        edad = st.number_input("Age (mandatory)", min_value=12, max_value=80, value=16)
        altura_cm = st.number_input("height (cm)", min_value=100, max_value=270, value=170)
        peso_kg = st.number_input("weight (kg)", min_value=30.0, max_value=300.0, value=70.0, format="%.1f")

    st.header("Physical information and objectives")
    objetivo = st.selectbox("Objetive", [
        "Gain muscle/weight",
        "lose weight"
    ])
    experiencia = st.selectbox("Gym experience", [
        "Beginner (0-6 meses)",
        "Intermediate (6-12 meses)",
        "Expert (>12 meses)"
    ])

    enviar = st.form_submit_button("Enviar")


if enviar:
    usuario = gestor.get_usuario(
        nombre_completo,
        edad,
        genero,
        altura_cm,
        peso_kg,
        objetivo,
        experiencia
    )

    st.success("Data sent successfully!")

    st.json({
        "Nombre": usuario.Nombre,
        "Apellido": usuario.Apellido,
        "Edad": usuario.Edad,
        "Genero": usuario.Genero,
        "Altura": usuario.Altura,
        "Peso": usuario.Peso,
        "Objetivo": usuario.Objetivo,
        "Nivel": usuario.Nivel
    })

st.info("Fill out the form to join our community!!!")






