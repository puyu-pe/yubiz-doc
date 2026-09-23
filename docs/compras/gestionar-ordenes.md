# Consultar, exportar y notificar órdenes de compra

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Localizar una orden de compra, revisar su información, exportar el conjunto filtrado o
notificarla al proveedor cuando esas acciones estén disponibles.

## Acceso condicional

Las columnas, filtros, exportación y correo dependen de la sesión y configuración. La
fuente muestra acciones deshabilitadas para un estado anulado; no confirma permisos,
entrega de correo ni validez del archivo en un entorno desplegado.

## Requisitos y datos

- Referencia de documento, serie, correlativo, proveedor, almacén, fecha o estado.
- Correo del proveedor revisado antes de solicitar una notificación.
- Criterios de filtro definidos para no exportar más registros de los necesarios.

## Punto de partida

Abra la lista de órdenes de compra. Ajuste las columnas o limpie filtros antes de
abrir el detalle de la orden que necesita revisar.

## Pasos

1. Filtre por documento, serie, correlativo, fecha, proveedor, almacén, categoría de
   egreso, origen, moneda o estado según el dato disponible.
2. Revise en la lista subtotal, IGV, total, pagado, deuda y los documentos del
   proveedor asociados cuando se presenten.
3. Abra el detalle para confirmar proveedor, fechas, almacén, origen, líneas e
   importes antes de actuar.
4. Exporte el conjunto filtrado solo después de comprobar los criterios aplicados.
5. Para notificar, seleccione el proveedor, confirme el correo y envíe la orden.
6. Consulte de nuevo la lista o el detalle antes de repetir una exportación o envío.

## Campos y validaciones observados

La lista revisada incluye documento, serie, correlativo, fecha, proveedor, almacén,
categoría de egreso, período tributable, importes, deuda, pagado, origen, moneda,
usuario y estado. El formulario de correo exige orden identificable, proveedor y
correo. La exportación de fuente rechaza conjuntos de más de 10 000 registros.

## Resultado revisado en fuente

La exportación prepara un enlace para las columnas y filtros recibidos. La
notificación genera un documento y solicita envío al correo indicado. Una orden es
distinta del pedido que pudo originarla y de los documentos del proveedor asociados;
el resultado no confirma recepción, pago ni efecto contable en runtime.

## Advertencias y casos límite

No use la exportación como sustituto de revisar el detalle de una orden. Para una
orden anulada, la interfaz deshabilita registrar documento, notificar, imprimir y
anular. Verifique el destinatario y no reenvíe si el resultado no es claro.

## Problemas frecuentes y condiciones de detención

- El listado es demasiado amplio: reduzca filtros antes de exportar.
- El correo o proveedor no está confirmado: detenga el envío hasta revisarlo.
- La acción aparece deshabilitada: revise el estado mostrado y no intente forzarla.

## Verificaciones pendientes en runtime

- Filtros, columnas, límite de exportación y acciones disponibles para cada rol.
- Archivo descargado, correo entregado y mensajes de error finales.
- Significado operativo del estado y efectos posteriores de notificar o imprimir.

## Enlaces relacionados

- [Cambiar o anular el estado de una compra](cambiar-estado-de-compra.md)
- [Registrar pagos de compras y consultar saldos](registrar-pagos-y-saldos.md)
- [Compras](index.md)
