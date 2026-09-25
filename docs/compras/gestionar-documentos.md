<a id="registrar-y-relacionar-documentos-de-compra"></a>

# 6.8 Registrar y relacionar documentos de compra

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Registrar un documento del proveedor para una orden de compra y relacionar los pagos
disponibles con ese documento cuando las acciones estén habilitadas.

## Acceso condicional

La acción depende del estado de la orden; la interfaz la deshabilita cuando la orden
aparece anulada. Los tipos de documento y pagos disponibles dependen de la configuración
y sesión. No se infiere validez fiscal, aprobación ni conciliación externa.

## Requisitos y datos

- Orden de compra identificable y no anulada según el estado mostrado.
- Fecha, tipo de documento, serie y correlativo del documento del proveedor.
- Pagos de la misma orden para relacionar, cuando correspondan.

## Punto de partida

Abra el detalle de la orden y ubique la sección Documentos del proveedor. Revise los
pagos existentes antes de crear o modificar una relación.

## Pasos

1. Seleccione Registrar documento del proveedor desde el detalle de la orden.
2. Complete fecha, tipo de documento, serie y correlativo.
3. Seleccione los pagos de la orden que correspondan al documento y guarde.
4. Revise la tabla de documentos para confirmar fecha, documento, serie y correlativo.
5. Para cambiar relaciones, use la acción de relacionar pagos y revise la selección
   antes de guardar.
6. Elimine un documento solo después de comprobar que no se requiere conservar su
   relación; vuelva a revisar el detalle al finalizar.

## Campos y validaciones observados

El alta solicita compra, fecha, documento, serie y correlativo; la validación del
navegador exige esos cinco datos. La lista de pagos admite selección múltiple. La interfaz
rechaza repetir para el mismo proveedor la combinación de comprobante, serie y
correlativo; al modificar, exige documento y al menos un pago seleccionado.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

Al actualizar relaciones, revise que los pagos retirados y seleccionados correspondan
al documento. El documento del proveedor no es la orden de compra ni el pago: es un
registro relacionado. Verifique su validez, recepción y tratamiento fiscal según el
procedimiento aplicable.

## Advertencias y casos límite

No duplique una combinación de documento, serie y correlativo para el proveedor. No
elimine un documento sin revisar pagos asociados; la interfaz pide confirmación. Una
relación de pago no sustituye la verificación del monto, saldo o documento recibido.

## Problemas frecuentes y condiciones de detención

- Falta fecha, documento, serie o correlativo: complete los campos antes de guardar.
- La combinación ya existe para el proveedor: revise el detalle en lugar de duplicarla.
- No hay pago válido para relacionar: no fuerce una relación vacía.
- La orden está anulada o la acción está deshabilitada: detenga el cambio.

## Enlaces relacionados

- [Registrar pagos de compras y consultar saldos](registrar-pagos-y-saldos.md)
- [Cambiar o anular el estado de una compra](cambiar-estado-de-compra.md)
- [Compras](index.md)
