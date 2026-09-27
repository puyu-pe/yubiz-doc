<a id="crear-y-gestionar-cotizaciones"></a>

# 2.4 Crear y consultar cotizaciones

<a id="27-crear-y-gestionar-cotizaciones"></a>
<a id="objetivo"></a>
<a id="punto-de-partida"></a>
<a id="resultado-esperado"></a>

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>
<a id="acceso-condicional"></a><a id="requisitos-y-datos"></a><a id="campos-y-validaciones-observados"></a><a id="advertencias-y-casos-limite"></a><a id="problemas-frecuentes-y-condiciones-de-detencion"></a><a id="enlaces-relacionados"></a>

Prepare una cotización, revísela en su detalle y consérvela lista para su seguimiento o conversión posterior.

## Antes de empezar

Las opciones de cotizaciones, documentos, series, líneas, vendedores, edición,
conversión e impresión pueden variar según la sesión y la configuración disponible.

### Datos necesarios

- Cliente seleccionado y al menos un ítem para cotizar.
- Documento, serie, fecha de emisión y fecha de vencimiento disponibles.
- Cantidad, descripción, precio unitario e importe para cada ítem.

## Cómo acceder

1. En la barra lateral, abra **Ventas**.
2. Seleccione **Crear cotización** para iniciar una cotización nueva.
3. Para consultar una cotización existente, abra **Ventas**, seleccione **Cotizaciones** y seleccione el registro.

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

### Datos que debe revisar

El formulario valida cliente, documento, serie, fecha de emisión y fecha de
vencimiento. La serie admite hasta cuatro caracteres en la validación del
navegador. Cada detalle requiere un ítem, cantidad, descripción, precio unitario e importe.

<a id="resultado-revisado-en-fuente"></a>

## Compruebe el resultado

El flujo envía la cotización y sus ítems para guardarlos y, tras una respuesta
exitosa, intenta abrir una impresión. El detalle muestra controles para revisar,
replicar o convertir una cotización cuando esos controles están habilitados. La
persistencia, la impresión y la conversión efectiva deben verificarse en el entorno de trabajo.

## Situaciones frecuentes

Una cotización no debe interpretarse como una venta confirmada. Antes de convertir
una cotización, confirme los ítems, montos y vigencia con la información vigente de
su operación. No suponga que las opciones visibles o el resultado de impresión
están habilitados para todas las personas usuarias.

### Si necesita detenerse

- Cliente, documento, serie o fecha faltantes: complete los datos antes de
  registrar.
- Ítems incompletos o con valores no numéricos: corrija el detalle y los totales.
- Opción de editar o convertir no disponible: detenga el flujo y confirme el
  estado de la cotización en su entorno.

## Continuar con

- [Convertir una cotización en venta](convertir-cotizacion-en-venta.md)
- [Consultar una venta, imprimirla o comunicarla](consultar-ventas.md)
