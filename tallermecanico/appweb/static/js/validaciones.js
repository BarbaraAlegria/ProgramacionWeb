function validarLargoNombre(nombre){

    if(nombre.length >=2 && nombre.length <=30)
    {
        return true;
    }
    return false;
}

function validarLargoRut(rut){

    if(rut.length >= 9 && rut.length <= 10)
    {
        return true;
    }
    return false;
}
function validarLargoApellido(apellido){

    if(apellido.length >=2 && apellido.length <=30)
    {
        return true;
    }
    return false;
}
function validarLargoPatente(patente){

    if(patente.length ===6)
    {
        return true;
    }
    return false;
}
function validarLargoTelefono(telefono){

    if(telefono.length >= 8 && telefono.length <= 9)
    {
        return true;
    }
    return false;
}