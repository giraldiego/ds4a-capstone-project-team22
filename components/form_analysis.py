import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback,State
import re
import pandas as pd
import pickle
import xgboost

edad = html.Div(
    [
        dbc.Label("¿Cuántos años cumplidos tiene?", html_for="edad", class_name="text-white"),
        dbc.Input(type="text", id="edad", placeholder="Por favor digite su edad"),
        dbc.FormText(
            "¿cuántos años cumplidos tiene...? (si es menor de 1 año, escriba 00)",
            color="secondary",
        ),
        html.Div(id="output-edad", className="text-danger")
    ],
    className="mb-3",
)

sexo = dbc.Row(
    [
        dbc.Label("¿A cuál sexo tiene usted más afinidad?",
        html_for="sexo",
        class_name="text-white"),
        dbc.Col(
            dbc.RadioItems(
                id="sexo",
                options=[
                    {"label": "Hombre", "value": 1},
                    {"label": "Mujer", "value": 2},
                ],
            ),
            class_name="text-white"
        ),
    ],
    className="mb-3",
) 

estado_civil = html.Div(
    [
        dbc.Label("Estado civil", 
        html_for="estado_civil",
        class_name="text-white"),
        dcc.Dropdown(
            id="estado_civil",
            options=[
                {"label": "No esta casado(a) y vive en pareja hace menos de dos años", "value": 1},
                {"label": "No esta casado (a) y vive en pareja hace dos años o más ", "value": 2},
                {"label": "Esta casado (a)", "value": 3},
                {"label": "Esta separado (a) o divorciado (a)", "value": 4},
                {"label": "Esta viudo(a)", "value": 5},
                {"label": "Esta soltero (a)", "value": 6},
            ],
        ),
        html.Div(id="output-estado_civil", className="text-danger")
    ],
    className="mb-3",
)

estrato  = html.Div(
    [
        dbc.Label("Estrato socioeconomico", 
        html_for="estrato",
        class_name="text-white"),
        dcc.Dropdown(
            id="estrato",
            options=[
                {"label": "1", "value": 1},
                {"label": "2", "value": 2},
                {"label": "3", "value": 3},
                {"label": "4", "value": 4},
                {"label": "5", "value": 5},
                {"label": "6", "value": 6},
                {"label": "No sabe o cuenta con planta eléctrica", "value": 7},
                {"label": "Conexión Pirata", "value": 8},
            ],
        ),
    ],
    className="mb-3",
)

personas = html.Div(
    [
        dbc.Label("Total de personas en el hogar", html_for="personas", class_name="text-white"),
        dbc.Input(type="text", id="personas", placeholder="Por favor digite la cantidad de personas en su hogar"),
        dbc.FormText(
            "Total de personas en el hogar",
            color="secondary",
        ),
        html.Div(id="output-personas", className="text-danger")
    ],
    className="mb-3",
)

estudia_escuela_universidad = dbc.Row(
    [
        dbc.Label("¿actualmente Asiste a la escuela, colegio o universidad?",
        html_for="estudia_escuela_universidad",
        class_name="text-white"),
        dbc.Col(
            dbc.RadioItems(
                id="estudia_escuela_universidad",
                options=[
                    {"label": "Sí", "value": 1},
                    {"label": "No", "value": 2},
                ],
            ),
            width=10,
            class_name="text-white"
        ),
    ],
    className="mb-3",
) 

mayor_nivel_educativo = html.Div(
    [
        dbc.Label("Cuál es el nivel educativo más alto alcanzado por usted", 
        html_for="mayor_nivel_educativo",
        class_name="text-white"),
        dcc.Dropdown(
            id="mayor_nivel_educativo",
            options=[
                {"label": "Ninguno", "value": 1},
                {"label": "Básica primaria (1º - 5º)", "value": 2},
                {"label": "Básica secundaria (6º - 9º)", "value": 3},
                {"label": "Media (10º - 13º)", "value": 4},
                {"label": "Superior o universitaria", "value": 5},
                {"label": "No sabe, no informa", "value": 6},
            ],
        ),
    ],
    className="mb-3",
)

la_vivienda_es = html.Div(
    [
        dbc.Label("La vivienda ocupada por usted es de tipo", 
        html_for="la_vivienda_es",
        class_name="text-white"),
        dcc.Dropdown(
            id="la_vivienda_es",
            options=[
                {"label": "Propia,totalmente pagada", "value": 1},
                {"label": "Propia, la están pagando", "value": 2},
                {"label": "En arriendo o subarriendo", "value": 3},
                {"label": "En usufructo", "value": 4},
                {"label": "Posesión sin titulo (Ocupante de hecho) ó propiedad colectiva", "value": 5},
                {"label": "Otra", "value": 6},
            ],
        ),
    ],
    className="mb-3",
)

material_piso = html.Div(
    [
        dbc.Label("¿Cuál es el material predominante de los pisos de la vivienda?", 
        html_for="dropdown",
        class_name="text-white"),
        dcc.Dropdown(
            id="material_piso",
            options=[
                {"label": "Tierra, arena", "value": 1},
                {"label": "Cemento,gravilla", "value": 2},
                {"label": "Madera burda, tabla, tablón, otro vegetal", "value": 3},
                {"label": "Baldosín, ladrillo, vinisol, otros materiales sintéticos", "value": 4},
                {"label": "Mármol", "value": 5},
                {"label": "Madera pulida", "value": 6},
                {"label": "Alfombra o tapete de pared a pared", "value": 7},
            ],
        ),
    ],
    className="mb-3",
)

telefono = dbc.Row(
    [
        dbc.Label("¿En su hogar algun miembro tiene teléfono celular propio?",
        html_for="example-radios-row",
        class_name="text-white"),
        dbc.Col(
            dbc.RadioItems(
                id="telefono",
                options=[
                    {"label": "Sí", "value": 1},
                    {"label": "No", "value": 2},
                ],
            ),
            class_name="text-white"
        ),
    ],
    className="mb-3",
) 

# services or goods
tel_fijo = html.Div(
    [
        dbc.Label("Servicio de teléfono fijo", className="text-white col-7"),
        dbc.RadioItems(
            id="tel_fijo",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

tv_cable = html.Div(
    [
        dbc.Label("Servicio de televisión por suscripción cable o antena parabólica", className="text-white col-7"),
        dbc.RadioItems(
            id="tv_cable",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

internet = html.Div(
    [
        dbc.Label("Servicio de Internet", className="text-white col-7"),
        dbc.RadioItems(
            id="internet",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

lavadora = html.Div(
    [
        dbc.Label("Máquina lavadora de ropa",  className="text-white col-7"),
        dbc.RadioItems(
            id="lavadora",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

nevera = html.Div(
    [
        dbc.Label("Nevera o refrigerador",  className="text-white col-7"),
        dbc.RadioItems(
            id="nevera",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

licuadora = html.Div(
    [
        dbc.Label("Licuadora",  className="text-white col-7"),
        dbc.RadioItems(
            id="licuadora",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

estufa = html.Div(
    [
        dbc.Label("Estufa eléctrica o de gas",  className="text-white col-7"),
        dbc.RadioItems(
            id="estufa",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

microondas = html.Div(
    [
        dbc.Label("Horno Microondas",  className="text-white col-7"),
        dbc.RadioItems(
            id="microondas",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

calentador = html.Div(
    [
        dbc.Label("Calentador de agua eléctrico, de gas o ducha eléctrica",  className="text-white col-7"),
        dbc.RadioItems(
            id="calentador",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

televisor = html.Div(
    [
        dbc.Label("Televisor a color",  className="text-white col-7"),
        dbc.RadioItems(
            id="televisor",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

dvd = html.Div(
    [
        dbc.Label("dvd",  className="text-white col-7"),
        dbc.RadioItems(
            id="dvd",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
    ],
    className="radio-group",
)

sonido = html.Div(
    [
        dbc.Label("Equipo de sonido",  className="text-white col-7"),
        dbc.RadioItems(
            id="sonido",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

computador = html.Div(
    [
        dbc.Label("Computador (para uso del hogar)",  className="text-white col-7"),
        dbc.RadioItems(
            id="computador",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

acondicionado = html.Div(
    [
        dbc.Label("Aire acondicionado",  className="text-white col-7"),
        dbc.RadioItems(
            id="acondicionado",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

ventilador = html.Div(
    [
        dbc.Label("Ventilador o abanico",  className="text-white col-7"),
        dbc.RadioItems(
            id="ventilador",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

bicicleta = html.Div(
    [
        dbc.Label("Bicicleta",  className="text-white col-7"),
        dbc.RadioItems(
            id="bicicleta",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

motocicleta = html.Div(
    [
        dbc.Label("Motocicleta",  className="text-white col-7"),
        dbc.RadioItems(
            id="motocicleta",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

carro = html.Div(
    [
        dbc.Label("Carro particular",  className="text-white col-7"),
        dbc.RadioItems(
            id="carro",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

aspiradora = html.Div(
    [
        dbc.Label("Aspiradora / brilladora",  className="text-white col-7"),
        dbc.RadioItems(
            id="aspiradora",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

servicio_bienes_uso = html.Div([
    dbc.Label("¿Cuáles de los siguientes servicios o bienes en uso, posee su hogar?", class_name="text-white"),
    tel_fijo,
    tv_cable,
    internet,
    lavadora,
    nevera,
    licuadora,
    estufa,
    microondas,
    calentador,
    televisor,
    dvd,
    sonido,
    computador,
    acondicionado,
    ventilador,
    bicicleta,
    motocicleta,
    carro,
    aspiradora
],
)


# services
electricidad = html.Div(
    [
        dbc.Label("Energía eléctrica",  className="text-white col-7"),
        dbc.RadioItems(
            id="electricidad",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

gas = html.Div(
    [
        dbc.Label("Gas natural conectado a red pública",  className="text-white col-7"),
        dbc.RadioItems(
            id="gas",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

alcantarillado = html.Div(
    [
        dbc.Label("Alcantarillado",  className="text-white col-7"),
        dbc.RadioItems(
            id="alcantarillado",
            className="btn-group text-white",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Sí", "value": 1},
                {"label": "No", "value": 2},
            ],
            value=1,
        ),
        html.Div(id="output"),
    ],
    className="radio-group",
)

servicios_vivienda = html.Div([
    dbc.Label("¿Con cuáles de los siguientes servicios cuenta la vivienda?", class_name="text-white"),
    electricidad,
    gas,
    alcantarillado,
])

#submit button
submit = html.Div(
    dbc.Button("Predecir ->",type="submit", color="success", size="lg",id="open", n_clicks=0),
    className="d-grid gap-2 d-md-flex justify-content-md-end",
)

modal = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Header"), id="modal-header"),
                dbc.ModalBody("This is the content of the modal" , id="modal-body"),
                dbc.ModalFooter(["Si deseas ver mas información de la informalidad en colombia, por favor revisa el siguiente link: ", html.A("dashboard",href="/descriptive")]),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close", className="ms-auto", n_clicks=0
                    )
                ),
            ],
            id="modal",
            is_open=False,
        ),
    ]
)

form_variables = dbc.FormFloating([
html.H1("Informal app", className="text-white"),
html.P("Mediante las respuestas de las siguientes preguntas, la persona que este diligenciando la encuesta podra conocer en cual segmento (informal o formal) se encuentra",  className="text-white"),
edad,
sexo, 
estado_civil,
estrato,
personas,
estudia_escuela_universidad,
mayor_nivel_educativo,
la_vivienda_es,
material_piso,
telefono,
servicio_bienes_uso,
servicios_vivienda,
 dbc.Alert(
            "Por favor complete el formulario",
            id="alert-fade",
            dismissable=True,
            is_open=False,
            color="danger",
            duration="5000",
        ),
submit,
modal
], 
style={"max-width": "40vw", "margin": "auto"})

# Functions

def check_number(data, ide):
    if data == "":
        return ""

    result = re.match(r'^([\s\d]+)$', str(data))
    if not result and data != None:
        return "Por favor digite solo numeros"
    

def loadmodel():
# load the model from disk
    filename = './assets/script/modelXGBoost_Informal.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model

def Datos(Sexo, Edad, Estado_civil, Asiste_Escuela_Universidad, Mayor_nivel_educativo, Tipo_Vivienda , Vivienda_Propiedad,
         No_Personas_Hogar, Tel_fijo, TV_cable, Internet, Lavadora, Nevera, Microondas, Calentador_agua, Equipo_sonido, Computador,
         Aspiradora, Aire_Acondicionado, Ventilador, Motocicleta, Carro, Celular, Estrato, Gas_natural, Materiales_Pisos):

        names=['Sexo', 'Edad', 'Estado_civil', 'Asiste_Escuela_Universidad','Mayor_nivel_educativo', 'Tipo_Vivienda', 'Vivienda_Propiedad',
        'No_Personas_Hogar', 'Tel_fijo', 'TV_cable', 'Internet', 'Lavadora', 'Nevera', 'Microondas', 'Calentador_agua', 'Equipo_sonido',
        'Computador', 'Aspiradora', 'Aire_Acondicionado', 'Ventilador','Motocicleta', 'Carro', 'Celular', 'Estrato', 'Gas_natural',
        'Materiales_Pisos']

        respuestas=[Sexo, Edad, Estado_civil, Asiste_Escuela_Universidad, Mayor_nivel_educativo, Tipo_Vivienda , Vivienda_Propiedad,
        No_Personas_Hogar, Tel_fijo, TV_cable, Internet, Lavadora, Nevera, Microondas, Calentador_agua, Equipo_sonido, Computador,
        Aspiradora, Aire_Acondicionado, Ventilador, Motocicleta, Carro, Celular, Estrato, Gas_natural, Materiales_Pisos]
                     
        dict1=dict(zip(names,respuestas))
        df_respuestas=pd.DataFrame(data=dict1,index=[0])

        return df_respuestas

def ejecutamodelo(Datos):
    #Ejecuta modelo y devuelve 1==Informal, 0==Formal
    respuesta=loadmodel().predict(Datos)
    return respuesta

@callback(
Output("output-edad","children"),
[Input("edad","value"), Input("edad","id")]
)
def number_1_callback(*args, **kwargs):
    return check_number(*args, **kwargs)

@callback(
Output("output-personas","children"),
[Input("personas","value"), Input("personas","id")]
)
def number_2_callback(*args, **kwargs):
    return check_number(*args, **kwargs)

@callback(
    Output("modal", "is_open"), Output("modal-header","children"), Output("modal-body","children"), Output("alert-fade", "is_open"),
    [Input("open", "n_clicks"), 
    Input("close", "n_clicks")],
    [State("modal", "is_open"),
    State("alert-fade", "is_open"),
    State("mayor_nivel_educativo","value"),
    State("sexo","value"),
    State("estado_civil","value"),
    State("estudia_escuela_universidad","value"),
    State("la_vivienda_es","value"),
    State("tel_fijo","value"),
    State("tv_cable","value"),
    State("internet","value"),
    State("lavadora","value"),
    State("nevera","value"),
    State("licuadora","value"),
    State("estufa","value"),
    State("microondas","value"),
    State("calentador","value"),
    State("televisor","value"),
    State("dvd","value"),
    State("sonido","value"),
    State("computador","value"),
    State("acondicionado","value"),
    State("ventilador","value"),
    State("bicicleta","value"),
    State("motocicleta","value"),
    State("carro","value"),
    State("aspiradora","value"),
    State("telefono","value"),
    State("material_piso","value"),
    State("electricidad","value"),
    State("gas","value"),
    State("alcantarillado","value"),
    State("edad","value"),
    State("personas","value"),
    State("estrato","value"),
    ],
)
def toggle_modal(n1, n2, is_open_modal, is_open_alert,
    mayor_nivel_educativo,
    sexo,
    estado_civil,
    estudia_escuela_universidad,
    la_vivienda_es,
    tel_fijo,
    tv_cable,
    internet,
    lavadora,
    nevera,
    licuadora,
    estufa,
    microondas,
    calentador,
    televisor,
    dvd,
    sonido,
    computador,
    acondicionado,
    ventilador,
    bicicleta,
    motocicleta,
    carro,
    aspiradora,
    telefono,
    material_piso,
    electricidad,
    gas,
    alcantarillado,
    edad,
    personas,
    estrato,
    ):
    if n1 or n2:
        #check if any variable is none or empty
        if not [x for x in ( 
            mayor_nivel_educativo,
            sexo,
            estado_civil,
            estudia_escuela_universidad,
            la_vivienda_es,
            tel_fijo,
            tv_cable,
            internet,
            lavadora,
            nevera,
            licuadora,
            estufa,
            microondas,
            calentador,
            televisor,
            dvd,
            sonido,
            computador,
            acondicionado,
            ventilador,
            bicicleta,
            motocicleta,
            carro,
            aspiradora,
            telefono,
            material_piso,
            electricidad,
            gas,
            alcantarillado,
            edad,
            personas,
            estrato) if x is None]:
            
            df = Datos(sexo,
            int(edad),
            estado_civil,
            estudia_escuela_universidad,
            mayor_nivel_educativo,
            la_vivienda_es,
            la_vivienda_es,
            int(personas),
            tel_fijo,
            tv_cable,
            internet,
            lavadora,
            nevera,
            microondas,
            calentador,
            sonido,
            computador,
            aspiradora,
            acondicionado,
            ventilador,
            motocicleta,
            carro,
            telefono,
            estrato,
            gas,
            material_piso,
            )
            respuesta = ejecutamodelo(df)
            if respuesta == 1:
                modal_header = "informal"
            else:
                modal_header = "formal"

            modal_body = "Con base en nuestro modelo, analizando tus respuestas eres de la población " + modal_header
            return not is_open_modal, modal_header,modal_body, is_open_alert
        else:
            return is_open_modal,"","", not is_open_alert
         
    return is_open_modal, "", "", is_open_alert