# Confirmar, anular o convertir una preventa en venta

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Usar las acciones disponibles sobre una preventa moderna después de revisar su
detalle y estado.

## Acceso condicional

Las acciones dependen del estado y de la sesión. Este recorrido corresponde a la
lista moderna: no sustituya las acciones del pedido heredado ni infiera aprobación,
cobro, documentos emitidos o efectos financieros.

## Requisitos y datos

- Una preventa identificada en su detalle.
- Revisión de estado, cliente, almacén e ítems.
- Documento y serie disponibles para la conversión.
- Documento del cliente compatible con la selección disponible.

## Punto de partida

Abra el detalle de una preventa desde la lista moderna.

## Pasos

1. Revise el estado antes de elegir una acción.
2. Para confirmar, use **Confirmar preventa** solo si la acción está habilitada y revise la actualización del estado.
3. Para anular, confirme la advertencia solo si la acción está habilitada; vuelva a la lista y revise el resultado.
4. Para convertir, seleccione documento y serie en el cuadro disponible.
5. Revise el documento del cliente y la serie antes de confirmar la conversión.
6. Actualice la lista y revise que el estado resultante corresponda a la acción realizada.

## Campos y validaciones observados

El detalle presenta estados borrador, confirmada, procesada y cancelada. Confirmar,
editar y anular se muestran para borrador; convertir se muestra para borrador o
confirmada. El cuadro de conversión solicita documento y serie, y valida un documento
de cliente de 8 u 11 dígitos; para factura exige 11 dígitos.

## Resultado revisado en fuente

Confirmar cambia el estado desde borrador. Anular deja la preventa cancelada y la
interfaz impide convertirla. Convertir puede procesar una preventa en borrador o
confirmada después de seleccionar una serie. La fuente trata reservas y movimientos,
pero no permite afirmar su disponibilidad o efecto en un tenant.

## Advertencias y casos límite

Confirmar, anular y convertir no son intercambiables. Una preventa cancelada no se
convierte desde este recorrido. No continúe con la conversión si el documento del
cliente o la serie no cumplen las validaciones visibles.

## Problemas frecuentes y condiciones de detención

- Acción deshabilitada: revise el estado y no intente forzarla.
- Documento del cliente inválido: corríjalo antes de convertir.
- Serie no seleccionada: selecciónela o cancele la conversión.
- Resultado inesperado: detenga acciones posteriores y revise detalle, estado e ítems.

## Verificaciones pendientes en runtime

- Transiciones permitidas, reservas, liberaciones y conversión para la sesión.
- Documentos, series y validaciones disponibles.
- Efectos de inventario, comerciales, financieros y autorizaciones.

## Enlaces relacionados

- [Consultar y editar preventas](consultar-y-editar.md)
- [Crear un pedido de preventa](crear-pedido.md)
- [Registrar una venta al contado](../ventas/registrar-venta-al-contado.md)
