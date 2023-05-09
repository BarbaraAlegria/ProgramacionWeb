function validarLargoNombre(nombre){

    if(nombre.length >=2 && nombre.length <=30)
    {
        return true;
    }
    return false;
}

function validarEdad(edad){

    if(edad >= 18 && edad <= 35)
    {
        return true;
    }
    return false;
}