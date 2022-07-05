import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback


mayor_nivel_educativo = html.Div(
    [
        dbc.Label("Cuál es el nivel educativo más alto alcanzado por usted y el último año o grado aprobado en este nivel", 
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

sexo = dbc.Row(
    [
        dbc.Label("Sexo",
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
    ],
    className="mb-3",
)

sabe_leer_escribir = dbc.Row(
    [
        dbc.Label("¿Sabe leer y escribir?",
        html_for="sabe_leer_escribir",
        class_name="text-white"),
        dbc.Col(
            dbc.RadioItems(
                id="sabe_leer_escribir",
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

la_vivienda_es = html.Div(
    [
        dbc.Label("La vivienda ocupada por este hogar es:", 
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
            id="radios",
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
    nevera,
    aspiradora
],
# style={"border": "1px solid white", "padding":"20px 20px 20px 20px"}
)

telefono = dbc.Row(
    [
        dbc.Label("¿En este hogar algún o algunos de sus miembros tiene teléfono celular propio?",
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

anos = html.Div(
    [
        dbc.Label("¿Cuántos años cumplidos tiene?", html_for="anos", class_name="text-white"),
        dbc.Input(type="text", id="anos", placeholder="Por favor digite su edad"),
        dbc.FormText(
            "¿cuántos años cumplidos tiene...? (si es menor de 1 año, escriba 00)",
            color="secondary",
        ),
    ],
    className="mb-3",
)

personas = html.Div(
    [
        dbc.Label("Total de personas en el hogar", html_for="personas", class_name="text-white"),
        dbc.Input(type="text", id="personas", placeholder="Por favor digite su edad"),
        dbc.FormText(
            "Total de personas en el hogar",
            color="secondary",
        ),
    ],
    className="mb-3",
)

estrato  = html.Div(
    [
        dbc.Label("Estrato", 
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

submit = html.Div(
    dbc.Button("Predict ->",type="submit", color="primary", size="lg"),
    className="d-grid gap-2 d-md-flex justify-content-md-end",
)
form_variables = dbc.FormFloating([
html.H1("Analisis de informalidad", className="text-white"),
html.P("Por favor diligencie el formulario para conocer la probabilidad de que usted se encuentre en el rango de informalidad analizado con base en el modelo diseñado",  className="text-white"),
anos,
sexo, 
estado_civil,
estrato,
sabe_leer_escribir,
personas,
estudia_escuela_universidad,
mayor_nivel_educativo,
la_vivienda_es,
material_piso,
telefono,
servicio_bienes_uso,
servicios_vivienda,
submit,
], 
style={"max-width": "40vw", "margin": "auto"})


@callback(Output("output", "children"), [Input("radios", "value")])
def display_value(value):
    return f"Selected value: {value}"