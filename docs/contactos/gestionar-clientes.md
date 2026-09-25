<a id="gestionar-clientes"></a>

# 3.1 Gestionar clientes

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Crear, revisar, editar o retirar de uso un cliente desde el área de contactos.

## Acceso condicional

La entrada de clientes depende de que el módulo esté visible para la sesión. La
posibilidad de crear, editar o retirar registros debe confirmarse en el entorno.

## Requisitos y datos

- Tipo y número de documento del cliente.
- Nombre o razón social.
- Datos de contacto y dirección, si corresponden a la operación.

## Punto de partida

En **Contactos**, abra **Clientes** cuando la opción esté disponible.

## Pasos

1. Abra la lista y ubique el cliente por documento, nombre o código interno.
2. Para crear un registro, elija la acción disponible para agregar e ingrese el
   documento y el nombre o razón social.
3. Complete código interno, dirección, correo, teléfono o referencia solo si son
   necesarios para el registro.
4. Revise los datos antes de guardar. Para modificar, abra el registro existente
   y repita esta revisión.
5. Si el listado ofrece retirar un registro, deténgase y confirme que no será
   necesario en operaciones posteriores antes de continuar.

## Campos y validaciones observados

La ficha revisada incluye documento, código interno, nombre o razón social,
dirección, correo, teléfono y referencia. El documento, el nombre o razón social
y el tipo de documento son obligatorios en el flujo general. El número se trata
como numérico y se valida entre ocho y once dígitos; para DNI y RUC se observan
longitudes de ocho y once dígitos, respectivamente. El correo se valida como
correo y la dirección y el código interno tienen límites de longitud.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

Al guardar un registro válido, el flujo crea o actualiza el cliente. El listado
no muestra registros retirados de uso; la operación de retiro revisada conserva
el registro para esa finalidad en vez de describirse como eliminación definitiva.

## Advertencias y casos límite

No use datos de otra persona u organización como ejemplo. Un documento ya
registrado requiere revisar el registro existente; no cree un duplicado. Esta
ficha es distinta de [seleccionar cliente](../ventas/seleccionar-cliente.md):
aquella guía asocia un cliente a una venta y no administra su ficha maestra.

## Problemas frecuentes y condiciones de detención

- Documento con longitud no válida: corrija el tipo o el número antes de guardar.
- Nombre insuficiente para el tipo de documento: complete el dato solicitado por
  el formulario.
- Correo, dirección o código rechazados: corrija el campo señalado y vuelva a
  revisar el registro.
- Registro existente o retirada de uso: deténgase y revise su estado antes de
  crear o retirar otro registro.

## Enlaces relacionados

- [Seleccionar cliente](../ventas/seleccionar-cliente.md)
- [Gestionar proveedores y sus cuentas bancarias](gestionar-proveedores.md)
