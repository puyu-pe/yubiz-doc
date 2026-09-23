# Cambiar o anular el estado de una compra

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Actualizar el estado disponible de una orden de compra o solicitar su anulación con
cautela cuando el módulo y el estado actual lo permitan.

## Acceso condicional

Esta capacidad es condicional y potencialmente destructiva. Los estados y acciones
dependen de la sesión y configuración. La guía no establece políticas de autorización,
aprobación ni consecuencias financieras u operativas no verificadas en runtime.

## Requisitos y datos

- Orden de compra identificable y detalle revisado antes de cambiar su estado.
- Nuevo estado disponible en la lista de estados mostrada por la interfaz.
- Motivo claro y revisado si se solicita anulación.

## Punto de partida

Abra el detalle de la orden y revise documento, proveedor, importes, origen, pagos y
estado mostrado antes de iniciar un cambio.

## Pasos

1. Seleccione el estado mostrado en el encabezado para abrir la lista de estados,
   solo si la orden no aparece anulada.
2. Elija el estado disponible y guarde después de revisar que corresponde al caso.
3. Actualice el detalle o la lista y confirme el estado resultante.
4. Para anular, abra la acción Anular desde el detalle y escriba el motivo.
5. Revise una última vez documento, importes, pagos y motivo antes de confirmar.
6. Consulte nuevamente la orden después de la respuesta y no repita la solicitud si
   el resultado es incierto.

## Campos y validaciones observados

El cambio de estado solicita la orden y un estado de compra. La anulación solicita la
referencia de compra y un motivo obligatorio. La fuente impide cambiar a un estado con
orden anterior y rechaza anular una orden ya anulada o no identificada.

## Resultado revisado en fuente

El cambio guarda el estado seleccionado dentro de una transacción. La anulación marca
la compra con un estado anulado y conserva el motivo junto con la observación interna.
Estos son comportamientos revisados en fuente; no confirman devoluciones, caja, stock,
presupuesto, contabilidad ni aprobaciones en el entorno desplegado.

## Advertencias y casos límite

No use el cambio de estado para deshacer una decisión sin revisar su orden y pagos. La
interfaz informa que una orden anulada no permite cambiar estado. La anulación es una
acción sensible: documente un motivo útil y deténgase ante cualquier duda.

## Problemas frecuentes y condiciones de detención

- No se identifica la orden: vuelva a la lista y confirme la referencia.
- El estado propuesto es anterior al actual: no continúe; revise la secuencia visible.
- Falta motivo de anulación: complete el motivo antes de enviar.
- La orden ya está anulada: no intente una segunda anulación.

## Verificaciones pendientes en runtime

- Estados disponibles, orden de transición y permisos por rol.
- Mensajes de confirmación, posibilidad de reversión y trazabilidad visible.
- Efectos sobre pagos, inventario, caja, presupuesto y contabilidad.

## Enlaces relacionados

- [Consultar, exportar y notificar órdenes de compra](gestionar-ordenes.md)
- [Registrar pagos de compras y consultar saldos](registrar-pagos-y-saldos.md)
- [Compras](index.md)
