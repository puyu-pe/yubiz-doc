# Crear y gestionar cotizaciones

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Preparar una cotización, revisarla en su detalle y, cuando corresponda, continuar
el flujo hacia una venta.

## Acceso condicional

Las opciones de cotizaciones, documentos, series, líneas, vendedores, edición,
conversión e impresión pueden variar según la sesión y la configuración disponible.

## Requisitos y datos

- Cliente seleccionado y al menos un ítem para cotizar.
- Documento, serie, fecha de emisión y fecha de vencimiento disponibles.
- Cantidad, descripción, precio unitario e importe para cada ítem.

## Punto de partida

En la lista de cotizaciones o en el formulario de una nueva cotización.

## Pasos

1. Seleccione el cliente y complete documento, serie, fecha de emisión y fecha de
   vencimiento.
2. Si están disponibles, revise la línea y el vendedor antes de agregar ítems.
3. Agregue los productos y revise cantidades, precios, impuestos, subtotales y
   total mostrado.
4. Use los campos de detalle para impresión u observación interna solo si su
   operación los requiere.
5. Seleccione **Registrar** y revise el resultado mostrado por el formulario.
6. Desde el detalle, revise los datos antes de usar las opciones de editar,
   replicar, convertir en venta o imprimir que estén disponibles.

## Campos y validaciones observados

El formulario valida cliente, documento, serie, fecha de emisión y fecha de
vencimiento. La serie admite hasta cuatro caracteres en la validación del
navegador. Cada detalle requiere un ítem, cantidad, descripción, precio unitario

## Resultado revisado en fuente

El flujo envía la cotización y sus ítems para guardarlos y, tras una respuesta
exitosa, intenta abrir una impresión. El detalle muestra controles para revisar,
replicar o convertir una cotización cuando esos controles están habilitados. La
persistencia, la impresión y la conversión efectiva deben verificarse en runtime.

## Advertencias y casos límite

Una cotización no debe interpretarse como una venta confirmada. Antes de convertir
una cotización, confirme los ítems, montos y vigencia con la información vigente de
su operación. No suponga que las opciones visibles o el resultado de impresión
están habilitados para todas las personas usuarias.

## Problemas frecuentes y condiciones de detención

- Cliente, documento, serie o fecha faltantes: complete los datos antes de
  registrar.
- Ítems incompletos o con valores no numéricos: corrija el detalle y los totales.
- Opción de editar o convertir no disponible: detenga el flujo y confirme el
  estado de la cotización en su entorno.

## Verificaciones pendientes en runtime

- Documentos, series, líneas, vendedores y controles disponibles.
- Resultado de registro, edición, réplica, conversión e impresión.
- Reglas de vigencia, permisos y comportamiento desplegado.

## Enlaces relacionados

- [Seleccionar productos y revisar condiciones](seleccionar-productos-y-revisar-condiciones.md)
- [Registrar venta al contado](registrar-venta-al-contado.md)
- [Buscar, filtrar y revisar el detalle de ventas](consultar-ventas.md)
