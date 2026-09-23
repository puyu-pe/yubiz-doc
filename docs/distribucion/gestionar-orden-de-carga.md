# Consultar y gestionar el ciclo de una orden de carga

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Consultar una orden de carga y usar solo las acciones habilitadas por su estado.

## Acceso condicional

El ciclo depende del módulo y de la sesión. Las etiquetas y transiciones se
revisaron en fuente, pero su disponibilidad en un tenant requiere verificación.

## Requisitos y datos

- Una orden de carga localizada en la lista.
- Revisión de almacén, vehículo, fecha, productos y estado antes de actuar.

## Punto de partida

Abra la lista de órdenes de carga y seleccione el detalle del registro.

## Pasos

1. Revise documento, estado y detalle de productos.
2. Si está disponible, confirme la orden y vuelva a abrir el detalle.
3. Use recarga solo cuando la acción esté habilitada.
4. Genere una orden de descarga únicamente desde el estado que la habilita.
5. Después de una descarga, liquide solo si la acción aparece disponible.
6. Si necesita anular, hágalo solo antes de avanzar el ciclo y compruebe el estado.

## Campos y validaciones observados

El detalle muestra almacén, vehículo, fecha, usuario, observación, resumen de
productos y, cuando existen, compromisos y recargas. La interfaz distingue los
estados programada, confirmada, cerrada, descargada, liquidada y cancelada. Las
acciones visibles se restringen por estado y por la existencia de una descarga.

## Resultado revisado en fuente

La confirmación cambia la orden de programada a confirmada. La descarga se
habilita desde una orden cerrada sin descarga, y la liquidación desde una orden
descargada con descarga asociada. Estos son mecanismos de fuente; no son una
aprobación operativa, financiera ni de inventario en producción.

## Advertencias y casos límite

No fuerce enlaces o acciones deshabilitadas. La anulación se ofrece para una
orden programada; confirmar, descargar y liquidar no son acciones equivalentes.
Una orden de carga de Distribución no reemplaza una carga de contenedores.

## Problemas frecuentes y condiciones de detención

- Acción deshabilitada: revise el estado y la descarga asociada.
- Estado inesperado tras una acción: detenga pasos posteriores y vuelva al detalle.
- Compromisos o cantidades no entendidos: no liquide; revise el detalle y el contexto.
- Error al confirmar, anular o liquidar: no repita sin comprobar la lista.

## Verificaciones pendientes en runtime

- Estados, permisos y acciones permitidas para la sesión.
- Significado operativo de cerrar, descargar y liquidar.
- Efectos sobre stock, ventas, caja, compromisos y documentos.

## Enlaces relacionados

- [Crear una orden de carga](crear-orden-de-carga.md)
- [Registrar una orden de descarga y el resultado de entrega](registrar-descarga-y-entrega.md)
- [Distribución](index.md)
