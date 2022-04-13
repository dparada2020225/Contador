var inicio = 0;
var h1 = document.getElementById('cantidad');
h1.style.color = "#265EFF"

function CambiarColor(){
    if (inicio > 0)
        h1.style.color = "#69D112"

    else if (inicio < 0)
        h1.style.color = "#FF2626"
    else 

        h1.style.color = "#265EFF"
}

function aumentar(){ 
    h1.innerHTML = ++inicio; 
        CambiarColor()
}

function disminuir(){ 
    h1.innerHTML = --inicio;
        CambiarColor()
}

function reset(){ 
    inicio = 0
    h1.innerHTML = inicio;
        CambiarColor()
}

    