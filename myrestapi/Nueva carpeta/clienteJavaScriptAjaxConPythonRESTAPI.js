var xmlHttpRequest;
var lblMensajeAsincrono;

window.addEventListener("load", function(){
	xmlHttpRequest = new XMLHttpRequest();
	lblMensajeAsincrono = document.getElementById("lblMensajeAsincrono");
	console.log("hola");
})

function clickObtenerAlumnos(){
	console.log("click");
	var uri = "http://localhost:8000/alumnos/";
	xmlHttpRequest.open("GET",uri,true);
	xmlHttpRequest.withCredentials = true;
	xmlHttpRequest.onreadystatechange = alumnosCallback;
	xmlHttpRequest.setRequestHeader('Content-Type','Access-Control-Allow-Origin','application/json');
	xmlHttpRequest.send(null);
}

function alumnosCallback(){
	if (xmlHttpRequest.readyState==4){
		if (xmlHttpRequest.status==200){
			var jsonMsg = JSON.parse(xmlHttpRequest.responseText);
			lblMensajeAsincrono.innerHTML = jsonMsg.results[0]['url'];
		}
		else
			lblMensajeAsincrono.innerHTML = "Página no encontrada";
	}
}


 

