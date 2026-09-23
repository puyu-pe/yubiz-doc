# Consultar, editar y notificar pedidos de compra

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Localizar un pedido de compra, revisar su detalle y usar las acciones disponibles
para editarlo, replicarlo, notificarlo o generar una orden cuando corresponda.

## Acceso condicional

Los filtros, acciones y estados visibles dependen de la sesión y la configuración.
La fuente muestra restricciones de interfaz para algunos estados; no confirma una
política de permisos ni la entrega de una notificación en producción.

## Requisitos y datos

- Referencia, fecha, proveedor o establecimiento para localizar el pedido.
- Datos corregidos del pedido si se necesita editarlo.
- Correo del proveedor revisado antes de solicitar una notificación.

## Punto de partida

Abra la lista de pedidos de compra. Puede ajustar columnas y limpiar o restablecer
filtros antes de abrir el detalle de un registro.

## Pasos

1. Filtre por serie, correlativo, fecha, proveedor, establecimiento o estado según
   el dato que tenga disponible.
2. Abra el detalle del pedido y revise proveedor, fecha, líneas, cantidades, IGV,
   subtotal y total.
3. Si el pedido continúa editable, use Editar y revise los datos antes de guardar.
4. Use Replicar solo para crear una nueva referencia a partir de datos revisados.
5. Para notificar, seleccione el proveedor, confirme el correo y envíe el pedido.
6. Consulte nuevamente el detalle o la lista antes de repetir una acción.

## Campos y validaciones observados

La lista contiene fecha, proveedor, establecimiento, importes, usuario y estado. El
detalle muestra las líneas y sus cantidades, descripción, afectación de IGV, precio
unitario e importe. El formulario de notificación exige un pedido, proveedor y correo.

## Resultado revisado en fuente

El detalle distingue el pedido de las compras generadas desde él. Cuando el estado
mostrado es `COMPRADO` o `ANULADO`, la interfaz deshabilita editar, generar orden y
anular; el envío por correo se deshabilita para `ANULADO`. Estas condiciones describen
la interfaz revisada y requieren validación en runtime.

## Advertencias y casos límite

Un pedido y una compra generada son documentos distintos. No interprete el estado
`COMPRADO` como una aprobación universal, recepción de mercadería o conciliación de
pagos. Verifique el destinatario antes de notificar y no reenvíe ante un resultado
incierto.

## Problemas frecuentes y condiciones de detención

- No encuentra el registro: reduzca el filtro o confirme serie, correlativo y fecha.
- El pedido no permite editar o generar orden: revise el estado mostrado y no fuerce
  una acción alternativa.
- Falta proveedor o correo: complete y confirme esos datos antes de enviar.

## Verificaciones pendientes en runtime

- Filtros, columnas y acciones disponibles para cada rol.
- Entrega real del correo, contenido del documento adjunto y mensajes de error.
- Significado operativo de los estados y reglas para editar, anular o convertir.

## Enlaces relacionados

- [Crear un pedido de compra](crear-pedido.md)
- [Crear una orden desde un pedido de compra](crear-orden-desde-pedido.md)
- [Compras](index.md)
