//alert ('Hola Javascript')

var num_id = 1020304050;
var nombre = "Pepito"
var apellido = "Perez"
var direccion = "calle 80 # 80 - 20"
var telefono = 3103103103
var edad = 34
var estado_civil = "soltero"
var num_hijos = 4
var estatura_cm = 176
var fecha_cont = "17/02/2022"
var sueldo_bas = 3400000
var dias_labr = 260

var concatenar = num_id + " " + nombre + " " + apellido + " " + direccion + " " + telefono + " " + edad + " " + estado_civil + " " + num_hijos + " " + estatura_cm + " " + fecha_cont + " " + sueldo_bas + " " + dias_labr + " ";

//document.write(concatenar);
/*
document.write(num_id);
document.write(nombre);
document.write(apellido);
document.write(direccion);
document.write(telefono);
document.write(edad);
document.write(estado_civil);
document.write(num_hijos);
document.write(estatura_cm);
document.write(fecha_cont);
document.write(sueldo_bas);
document.write(dias_labr);
*/

var datos = document.getElementById("datos");
//datos.innerHTML = concatenar;

datos.innerHTML = `
    <h1>Estos son los Datos</h1>
    <h3>Identificación: ${num_id}</h3>
    <h3>Nombre: ${nombre}</h3>
    <h3>Apellido: ${apellido}</h3>
    <h3>Dirección: ${direccion}</h3>
    <h3>Teléfono: ${telefono}</h3>
    <h3>Edad: ${edad}</h3>
    <h3>Estado Civil: ${estado_civil}</h3>
    <h3>Numero de Hijos: ${num_hijos}</h3>
    <h3>Estatura: ${estatura_cm}cm</h3>
    <h3>Fecha de Contratación: ${fecha_cont}</h3>
    <h3>Sueldo Base: $ ${sueldo_bas}</h3>
    <h3>Dias Laborados: ${dias_labr}</h3>
    `;