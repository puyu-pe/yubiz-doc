<a id="gestionar-transportistas"></a>

# 3.3 Gestionar transportistas

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Crear, consultar, editar o retirar de uso transportistas para utilizarlos cuando
un flujo operativo los solicite.

## Acceso condicional

La opción de transportistas depende del módulo disponible para la sesión. Algunos
flujos pueden mostrar un selector o una creación rápida; confirme su disponibilidad
en el entorno antes de contar con ella.

## Requisitos y datos

- Número de documento y descripción del transportista.
- RUC, nombre, apellido, licencia de conducir y marca o placa cuando el formulario
  completo los solicite.
- Certificado de inscripción o dueño, si el flujo los muestra y son pertinentes.

## Punto de partida

En **Contactos**, abra **Transportistas** cuando esté disponible; desde otro
formulario, use el selector de transportista solo si se ofrece.

## Pasos

1. Consulte la lista o el selector por número de documento para evitar duplicados.
2. Para crear un transportista, abra la acción disponible y complete los datos
   requeridos por el formulario.
3. Revise documento, RUC, identidad y datos del vehículo antes de guardar.
4. Para editar, abra el registro existente, actualice los campos necesarios y
   confirme el resultado mostrado por el formulario.
5. Si el listado permite retirar un registro, deténgase y valide su uso en
   operaciones pendientes antes de confirmar la acción.

## Campos y validaciones observados

El formulario revisado incluye número de documento, descripción, licencia de
conducir, RUC, nombre, apellido, marca o placa, certificado de inscripción y
dueño. RUC, nombre, apellido, marca o placa, licencia y documento se declaran
obligatorios. RUC se trata con once dígitos y el documento con entre ocho y once;
la comprobación observada relaciona la longitud con DNI o RUC. En un selector de
transporte, la creación rápida solo trata una búsqueda de once caracteres.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El flujo guarda el transportista o devuelve el registro para su uso en un
selector. La lista prioriza datos de identificación y vehículo. La acción de
retiro revisada marca el registro para dejar de usarlo.

## Advertencias y casos límite

No use una placa, licencia, documento o nombre reales como ejemplo. Si el
documento ya existe, revise el registro antes de crear otro. La creación rápida
no sustituye la revisión del formulario completo cuando falten datos requeridos.

## Problemas frecuentes y condiciones de detención

- RUC o documento con longitud incompatible: corrija el dato antes de guardar.
- Registro duplicado: deténgase y revise el transportista encontrado.
- Selector sin resultado: confirme el documento y la disponibilidad del módulo.
- Datos del vehículo o licencia incompletos: no continúe hasta completar lo que
  el formulario solicite.

## Enlaces relacionados

- [Gestionar proveedores y sus cuentas bancarias](gestionar-proveedores.md)
- [Gestionar clientes](gestionar-clientes.md)
