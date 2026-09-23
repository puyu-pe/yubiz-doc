# Visualizar, imprimir y comunicar una venta

## Estado
- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo
Revisar el detalle de una venta y usar las opciones disponibles para imprimirla o comunicarla.

## Acceso condicional
Las acciones visibles dependen del tipo y estado del documento, su situación de emisión, la deuda, la sesión y la configuración del entorno.

## Requisitos y datos
- Venta identificada en la lista.
- Documento, serie y correlativo revisados.
- Estado y datos mostrados en el detalle.

## Punto de partida
En el detalle de una venta abierta desde la lista.

## Pasos
1. Revise cliente, datos generales, ítems, pagos, estado y emisión mostrados.
2. Abra el menú de acciones y confirme que la opción está habilitada.
3. Para imprimir, seleccione el formato disponible y revise el documento generado.
4. Para comunicar, confirme que la venta es la correcta antes de elegir la acción.
5. Vuelva al detalle y revise el resultado mostrado antes de continuar con otra operación.

## Campos y validaciones observados
El detalle muestra estado, emisión, documento, serie, correlativo, cliente, ítems y pagos. La fuente habilita o deshabilita acciones según tipo de documento, estado, deuda y situación de emisión.

## Resultado revisado en fuente
El navegador solicita la impresión en el formato elegido. La comunicación intenta informar el documento y luego solicitar su impresión. La entrega, aceptación y resultado definitivo requieren verificación en runtime.

## Advertencias y casos límite
No interprete una opción visible, una ventana de impresión o un mensaje del navegador como constancia fiscal, de entrega o de comunicación aceptada. Si el estado no es claro, detenga el flujo y escale la revisión a la persona responsable de la operación.

## Problemas frecuentes y condiciones de detención
- Acción deshabilitada: revise tipo, estado y emisión sin intentar sustituirla.
- Detalle no coincide con la operación: deténgase y confirme documento, serie y correlativo.
- Resultado de impresión o comunicación incierto: no ejecute operaciones posteriores basándose solo en la pantalla.

## Verificaciones pendientes en runtime
- Acciones, formatos y permisos disponibles.
- Comunicación, impresión y resultado desplegado.
- Estados y efectos posteriores de la operación.

## Enlaces relacionados
- [Buscar, filtrar y revisar el detalle de ventas](consultar-ventas.md)
- [Anular una venta con cautela](anular-venta.md)
- [Emitir una nota de crédito o canjear un documento](notas-de-credito-y-canje.md)
