import webbrowser
import json

f= open("tarea.html", "wb")
la = """<html>
<head>
<meta charset="utf8" />
<title>Registros</title>
<h1></h1>
</head>
<style type="text/css">
body{background-color:darkblue;
text-decoration-color: black;
}
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
<script src="Tarea4/archivo.js"></script>
<p>"archivo.js"</p>
</body>


</html>"""

f.write(bytes(la, "ascii"))
f.close()
webbrowser.open_new_tab("tarea.html")