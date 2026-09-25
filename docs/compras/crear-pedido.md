<a id="crear-un-pedido-de-compra"></a>

# 6.1 Crear un pedido de compra

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Registrar un pedido de compra con su proveedor, documento, fecha y detalle de
productos cuando esta opción esté disponible para la sesión.

## Acceso condicional

La disponibilidad del módulo, los documentos, las series y los productos depende de
la configuración, el establecimiento y la sesión. Esta guía no confirma permisos ni
reglas de aprobación en el entorno desplegado.

## Requisitos y datos

- Proveedor identificable y documento y serie disponibles.
- Fecha del pedido y, por cada línea, producto, cantidad, descripción, importe y
  tipo de IGV aplicable.
- Observaciones para impresión o uso interno solo si son necesarias.

## Punto de partida

Abra el formulario para crear un pedido de compra. Tenga los datos comerciales antes
de agregar productos para poder revisar el total completo.

## Pasos

1. Seleccione el proveedor y revise el documento y la serie mostrados.
2. Indique la fecha del pedido.
3. Agregue cada producto y complete cantidad, descripción, valor unitario, tipo de
   IGV, precio unitario e importe.
4. Revise subtotal, IGV y total calculados por la tabla.
5. Agregue detalle de impresión u observación interna solo cuando corresponda.
6. Registre el pedido y conserve la referencia generada para consultarla después.

## Campos y validaciones observados

La interfaz solicita documento, serie, fecha y proveedor. La validación revisada
exige esos datos; para cada detalle exige producto, cantidad, descripción, valor
unitario e importe. La serie tiene un límite de longitud en la validación del
formulario. Los mensajes exactos pueden variar según la configuración disponible.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El flujo registra la cabecera y sus detalles dentro de una transacción y asigna un
correlativo de la serie. El pedido es un documento de solicitud: no equivale por sí
mismo a una orden de compra ni confirma recepción, stock, pago o efecto contable.

## Advertencias y casos límite

No registre productos eliminados que continúen en la tabla. Revise importes e IGV
antes de guardar; los campos de resumen son calculados y no sustituyen la revisión
del detalle. Una observación interna no debe reemplazar los datos del producto.

## Problemas frecuentes y condiciones de detención

- Falta proveedor, documento, serie o fecha: complete los campos antes de registrar.
- Una línea no tiene producto, cantidad, descripción, valor o importe: corríjala o
  retírela antes de continuar.
- El resultado no es claro: consulte la lista antes de repetir el registro.

## Enlaces relacionados

- [Consultar, editar y notificar pedidos de compra](gestionar-pedidos.md)
- [Registrar una orden de compra](registrar-orden.md)
- [Compras](index.md)
