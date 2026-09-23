# Crear una orden desde un pedido de compra

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Crear una orden de compra a partir de un pedido existente cuando la acción esté
disponible y el pedido continúe en un estado que permita la conversión.

## Acceso condicional

Esta es una capacidad condicional: la acción depende del estado del pedido y de la
sesión. La fuente muestra que no está disponible en los estados `COMPRADO` y
`ANULADO`; las reglas definitivas deben verificarse en runtime.

## Requisitos y datos

- Pedido de compra existente, identificable y revisado.
- Proveedor, documento, serie, moneda, fechas, almacén y categoría de egreso para la
  orden resultante cuando el formulario los solicite.
- Detalle de productos, cantidades, impuestos y precios revisado antes de confirmar.

## Punto de partida

Abra el detalle del pedido de compra desde la lista y confirme que muestra la acción
para generar una orden.

## Pasos

1. Revise en el detalle del pedido el proveedor, las líneas, las cantidades, el IGV y
   los totales.
2. Confirme que el estado no haya deshabilitado la acción Generar orden.
3. Seleccione Generar orden y revise los datos trasladados al formulario de orden.
4. Complete documento, serie, moneda, fecha, período tributable, almacén y categoría
   de egreso según las opciones disponibles.
5. Revise el detalle trasladado; en este origen la interfaz restringe la modificación
   de cantidades y eliminación de líneas.
6. Confirme la orden solo después de validar productos, impuestos, importes, total,
   pago y deuda.

## Campos y validaciones observados

El formulario de orden conserva el origen y carga los datos y productos del pedido.
La validación exige documento, serie, fecha, almacén y proveedor. El detalle conserva
cantidad, descripción, valor, afectación de IGV, precio e importe; las opciones de
seguimiento dependen del producto y de la configuración.

## Resultado revisado en fuente

La fuente guarda el vínculo entre la orden y el pedido y actualiza el estado del
pedido a `COMPRADO` cuando la orden se registra desde ese origen. Este significado es
documental y de estado observado en fuente; no confirma recepción física, aprobación,
stock, pago, caja ni asiento contable en el entorno desplegado.

## Advertencias y casos límite

No convierta un pedido sin revisar su estado y detalle. La conversión no debe tratarse
como duplicación: crea una orden relacionada. Si los datos trasladados no corresponden
al caso, detenga el registro y revise el pedido antes de crear una nueva orden.

## Problemas frecuentes y condiciones de detención

- La acción Generar orden no está disponible: revise el estado y no intente forzarla.
- Faltan almacén, serie o proveedor en la orden: complete los obligatorios antes de
  confirmar.
- Las cantidades o líneas requieren cambios: vuelva a revisar el pedido antes de
  continuar con la conversión.

## Verificaciones pendientes en runtime

- Estados reales que permiten convertir y su presentación para cada rol.
- Datos trasladados, restricciones de edición y mensajes finales.
- Consecuencias operativas, de stock, pago, caja y contabilidad tras el registro.

## Enlaces relacionados

- [Consultar, editar y notificar pedidos de compra](gestionar-pedidos.md)
- [Registrar una orden de compra](registrar-orden.md)
- [Compras](index.md)
