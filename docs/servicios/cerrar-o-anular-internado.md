# Convertir, anular o imprimir un internado

## Estado

- Revisión de fuente: revisada en código.
- Verificación en entorno: pendiente.
- Paridad con la versión desplegada: pendiente.

## Objetivo

Revisar las acciones disponibles para convertir, imprimir o anular una orden de
servicio sin asumir resultados operativos no verificados.

## Acceso condicional

Estas acciones aparecen desde el detalle de **Internados**. Su disponibilidad varía
según el estado de la orden y el entorno.

## Requisitos y datos

- Orden correcta abierta en el detalle.
- Confirmación operativa antes de anular o convertir.

## Punto de partida

Abra una orden desde **Internados** y revise su estado antes de usar el menú de
acciones.

## Pasos

1. Confirme el número, cliente, unidad, ítems y estado de la orden.
2. Para convertir, elija la acción disponible y revise el contexto de la venta.
3. Para imprimir, seleccione orden o nota y compruebe el documento generado.
4. Para anular, confirme que es la orden correcta y acepte la confirmación mostrada.
5. Regrese a la lista y compruebe el estado que presenta la interfaz.

## Campos y validaciones observados

El detalle deshabilita convertir y anular cuando la orden está anulada o ya fue
convertida. La anulación solicita confirmación antes de enviar la acción; las
salidas impresas usan el identificador de la orden.

## Resultado revisado en fuente

La anulación actualiza el estado dentro de una transacción y la lista se recarga.
La conversión abre el flujo de venta y la impresión solicita el documento; sus
resultados operativos deben verificarse en el entorno.

## Advertencias y casos límite

Anular o convertir cambia el contexto del registro. Deténgase si no puede confirmar
la orden o si la interfaz marca la acción como no disponible.

## Problemas frecuentes y condiciones de detención

- Acción deshabilitada: respete el estado mostrado y no fuerce una alternativa.
- Impresión sin resultado visible: no asuma que se generó el documento.
- Duda sobre la orden: deténgase antes de confirmar la anulación.

## Verificaciones pendientes en runtime

- Estados visibles, confirmaciones, archivos de impresión y actualización de lista.
- Resultado de conversión y efecto real de la anulación.

## Enlaces relacionados

- [Consultar un internado y agregar procedimientos](gestionar-internado.md)
- [Servicios](index.md)
