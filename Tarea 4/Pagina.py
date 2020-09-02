import webbrowser
import json

funcion= open("tarea.html", "wb")
abrir = """<html>
<head>
<meta charset="utf8" />
<title>Registros</title>
<h1></h1>
</head>
<style type="text/css">
body{background-color: chartreuse;}
h1{text-align: center;}
.opciones {
    width: 100%;
    background-color: red;
    display:flex;
    justify-content:center;
    width: 1000px;
    height: 700px;
}
.nav{align-content: center;}
</style>
<body>
<h1>Datos Tabulados</h1>
<table id = "tabla">
<p>
{
        "Nombre":"Andres",
        "Edad":28,
        "Activo":False,
        "Saldo": 220
    },
    {
        "Nombre":"Alejandro",
        "Edad":28,
        "Activo":True,
        "Saldo": 300

    },
    {
        "Nombre":"Michelle",
        "Edad":29,
        "Activo":False,
        "Saldo": 63

    },
    {
        "Nombre":"Daniel",
        "Edad":27,
        "Activo":True,
        "Saldo": 87

    },
    {
        "Nombre":"Sofia",
        "Edad":30,
        "Activo":False,
        "Saldo": 654
    },
    {
        "Nombre":"Jonathan",
        "Edad":29,
        "Activo":True,
        "Saldo": 3578

    },
    {
        "Nombre":"Julian",
        "Edad":30,
        "Activo":False,
        "Saldo": 678
    },
    {
        "Nombre":"Jonathan",
        "Edad":29,
        "Activo":True,
        "Saldo": 90

    },
    {
        "Nombre":"Jonathan",
        "Edad":29,
        "Activo":True,
        "Saldo": 10

    },
    {
        "Nombre":"Jonathan",
        "Edad":29,
        "Activo":False,
        "Saldo": 68

    }






</p>
</table>
</body>


</html>"""

funcion.write(bytes(abrir, "ascii"))
funcion.close()
webbrowser.open_new_tab("tarea.html")