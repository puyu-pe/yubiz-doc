<a id="gestionar-proveedores-y-sus-cuentas-bancarias"></a>

# 3.2 Gestionar proveedores y sus cuentas bancarias

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Registrar o actualizar proveedores y consultar o administrar las cuentas
bancarias asociadas cuando esas opciones estén habilitadas.

## Acceso condicional

La lista de proveedores y las acciones de cuentas dependen de la sesión y del
módulo disponible. Las cuentas se gestionan desde un proveedor existente; no se
asume que todas las sesiones puedan verlas o modificarlas.

## Requisitos y datos

- Tipo y número de documento, y nombre o razón social del proveedor.
- Dirección, correo, teléfono, representante u observación, si aplican.
- Para una cuenta: entidad financiera, tipo de cuenta, moneda, número de cuenta
  y estado; use únicamente información autorizada para la organización.

## Punto de partida

En **Contactos**, abra **Proveedores** y localice el registro a revisar o crear.

## Pasos

1. Busque el proveedor por documento o nombre y abra el registro si ya existe.
2. Para agregarlo, complete el documento y el nombre o razón social; agregue los
   demás datos necesarios y guarde.
3. Para editarlo, revise primero los datos generales y actualice solo los campos
   que correspondan.
4. Con un proveedor existente, abra la acción disponible para **Cuentas
   bancarias** o su consulta equivalente.
5. Al registrar o editar una cuenta, seleccione la entidad financiera y complete
   tipo, moneda, número y estado; revise los datos antes de guardar.
6. Si solo necesita verificar información, use la vista de cuentas y cierre sin
   modificar datos.

## Campos y validaciones observados

El formulario del proveedor contempla documento, nombre o razón social,
dirección, correo, teléfono, representante y observación. Documento y nombre o
razón social son obligatorios; el documento se valida entre ocho y once dígitos,
con comprobaciones de ocho dígitos para DNI y once para RUC. Correo, teléfono y
dirección tienen validaciones de formato, número y longitud. La ficha de cuenta
requiere entidad financiera, tipo de cuenta, moneda, número de cuenta y estado;
CCI y titular aparecen como datos adicionales.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El flujo guarda un proveedor nuevo o actualiza uno existente. Las cuentas quedan
asociadas al proveedor seleccionado y se pueden consultar con su entidad, tipo,
moneda, número, titular y estado. La desactivación de una cuenta se observa como
cambio de estado, no como una garantía de borrado definitivo.

## Advertencias y casos límite

No documente ni comparta números de cuenta, CCI ni nombres de titulares en notas
o capturas. Si el proveedor ya existe, revise su ficha en lugar de duplicarlo.
Una cuenta inactiva puede seguir visible para consulta; confirme el uso operativo
antes de modificar su estado.

## Problemas frecuentes y condiciones de detención

- Documento duplicado o inválido: deténgase y revise el proveedor existente.
- Correo, teléfono o dirección rechazados: corrija el campo indicado.
- No aparece la acción de cuentas: no intente sustituirla por otro flujo; confirme
  la disponibilidad del módulo.
- Faltan datos obligatorios de la cuenta: no guarde hasta completarlos y revisar
  que correspondan al proveedor correcto.

## Enlaces relacionados

- [Gestionar entidades financieras](gestionar-entidades-financieras.md)
- [Gestionar clientes](gestionar-clientes.md)
