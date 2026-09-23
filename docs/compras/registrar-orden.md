# Registrar una orden de compra

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Registrar una orden de compra independiente con proveedor, documento, almacén, fechas
y detalle de productos cuando el módulo esté habilitado.

## Acceso condicional

Los almacenes, categorías de egreso, documentos, series y monedas disponibles dependen
del establecimiento, la configuración y la sesión. No se afirma una aprobación,
contabilización o actualización automática de existencias sin evidencia del entorno.

## Requisitos y datos

- Proveedor, documento, serie, moneda, fecha y período tributable disponibles.
- Almacén y categoría de egreso identificados cuando el formulario los solicite.
- Productos, cantidades, tipo de IGV, precios, importes y datos de lote o serie si se
  muestran para el producto.

## Punto de partida

Abra el formulario de orden de compra. Si no parte de un pedido, defina primero el
proveedor y los datos de cabecera antes de completar el detalle.

## Pasos

1. Seleccione proveedor, documento, serie y moneda.
2. Indique fecha y período tributable; elija almacén y categoría de egreso cuando se
   presenten como opciones.
3. Agregue productos y complete cantidad, descripción, valor, tipo de IGV, precio e
   importe de cada línea.
4. Incluya descuento o recargo solo si la interfaz lo habilita para el caso.
5. Revise subtotal, IGV, total, monto pagado y deuda calculada.
6. Agregue observación interna o detalle de impresión si corresponde y confirme el
   registro tras revisar toda la información.

## Campos y validaciones observados

La validación del navegador exige documento, serie, fecha, almacén y proveedor. La
interfaz incluye moneda, fecha tributable, categoría de egreso, productos, cantidades,
precios, impuestos, descuento, recargo, subtotal, IGV, total, pagado y deuda. El saldo
se calcula a partir del total y el monto pagado ingresado.

## Resultado revisado en fuente

La fuente guarda una orden con su estado, detalle y, cuando existe un monto pagado,
un registro de pago inicial. También conserva el origen si lo hubiera. La presencia de
ese flujo en fuente no confirma movimientos de caja, stock, contabilidad ni resultados
en un entorno desplegado.

## Advertencias y casos límite

No use el valor pagado para superar el total esperando una deuda negativa: la interfaz
presenta deuda cero en ese caso. Revise lote o serie cuando el producto lo requiera.
No reutilice una orden como si fuera el pedido original sin verificar su origen.

## Problemas frecuentes y condiciones de detención

- Faltan documento, serie, fecha, almacén o proveedor: complete los obligatorios.
- El producto o su seguimiento no está claro: detenga el registro y revise el detalle.
- Total, pago o deuda inesperados: revise líneas, descuento, recargo e impuesto antes
  de confirmar.

## Verificaciones pendientes en runtime

- Campos visibles y obligatoriedad por configuración y rol.
- Opciones de moneda, almacén, categoría, lote y serie.
- Estado inicial, efectos de pago, stock y registros contables aplicables.

## Enlaces relacionados

- [Crear una orden desde un pedido de compra](crear-orden-desde-pedido.md)
- [Consultar, editar y notificar pedidos de compra](gestionar-pedidos.md)
- [Compras](index.md)
