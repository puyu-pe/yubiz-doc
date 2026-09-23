# Registrar una orden de descarga y el resultado de entrega

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Registrar una orden de descarga desde una orden de carga que la habilite,
declarando cantidades y seguimiento cuando corresponda.

## Acceso condicional

El recorrido depende del módulo, estado y sesión. No confirma una entrega real,
un retorno, una pérdida, una salida de stock ni una aprobación de cierre.

## Requisitos y datos

- Una orden de carga cerrada sin descarga asociada, según la interfaz revisada.
- Serie documental, almacén destino y detalle de productos.
- Cantidades retornadas o en vehículo; lotes o series si el producto los exige.

## Punto de partida

Desde el detalle de la orden de carga, seleccione **Generar orden de descarga**
solo cuando esté habilitado.

## Pasos

1. Revise los datos de la orden de carga y el vehículo mostrados.
2. Seleccione serie y almacén destino; agregue una observación si corresponde.
3. Revise por producto las cantidades esperada, entregada, retornada y en vehículo.
4. Para lotes o series, asigne el seguimiento a retornado o vehículo antes de guardar.
5. Si se muestran compromisos protegidos, seleccione solo las ventas que mantendrá cubiertas.
6. Revise el resumen local y confirme el registro una vez; abra luego el detalle.

## Campos y validaciones observados

El formulario pide serie, almacén destino y observación de hasta 500 caracteres.
El detalle requiere producto único y cantidades enteras no negativas. Para
seguimiento se asigna lote o serie a retornado, vehículo o faltante. La pantalla
muestra cantidades de venta, externa, entregada, rechazada, esperada, protegida,
libre, perdida, en vehículo y retornada.

## Resultado revisado en fuente

El navegador solicita confirmación antes de registrar la descarga y el servidor
rechaza datos inválidos. El resumen de seguimiento es local y no persiste por sí
solo. La fuente relaciona resultados de entrega, ajustes, movimientos y cobertura
de compromisos; describir su efecto de stock, caja o ventas como resultado
productivo requiere evidencia runtime.

## Advertencias y casos límite

El stock protegido no debe declararse retornado o perdido sin resolver su
cobertura. No cierre ni liquide la orden basándose solo en el resumen local. Si
falta el historial de seguimiento, no continúe con una asignación incompleta.

## Problemas frecuentes y condiciones de detención

- No se habilita la descarga: revise estado y descarga existente.
- Falta serie, almacén o detalle: complete el dato visible.
- Lote o serie sin asignación completa: deténgase antes de guardar.
- Cobertura de compromiso incierta o respuesta inesperada: cancele y revise el detalle.

## Verificaciones pendientes en runtime

- Disponibilidad de series, almacenes, estados y controles de cobertura.
- Reglas para cantidades entregadas, retornadas, en vehículo y faltantes.
- Efectos reales sobre existencias, compromisos, resultados de entrega y caja.

## Enlaces relacionados

- [Gestionar el ciclo de una orden de carga](gestionar-orden-de-carga.md)
- [Registrar recargas, compromisos y residuales](recargas-y-compromisos.md)
- [Revisar movimientos y kardex](../inventario/revisar-movimientos-y-kardex.md)
