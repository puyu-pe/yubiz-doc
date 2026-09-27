# 6.1 Crear una orden de carga

<a id="91-crear-una-orden-de-carga"></a>

Registre una orden de carga con su serie, almacén de origen, vehículo, distribuidor y detalle de productos. Al terminar, el sistema muestra la orden registrada para continuar con su revisión.

## Cómo acceder

1. En la barra lateral, abra **Distribución**.
2. Seleccione **Crear orden de carga**.

## Antes de empezar

- Tenga identificados la **Serie**, el **Almacén origen**, el **Vehículo**, el **Distribuidor**, la **Fecha salida** y los productos que cargará.
- Si incorporará ventas, tenga a la mano los documentos que desea seleccionar.

## Pasos

1. En el formulario, seleccione **Serie**, **Almacén origen**, **Vehículo** y **Distribuidor**.
2. Revise **Fecha salida**. La pantalla propone la fecha actual y no permite elegir una anterior a la fecha mostrada.
3. Si corresponde, escriba una **Observación**; este campo se presenta como detalle para imprimir.
4. En **Producto**, busque y seleccione cada producto. Puede usar **Cambiar modo de ingreso** cuando necesite buscar por serie.
5. Registre para cada fila la **Cantidad** y revise el producto, precio e importe. Agregue los productos necesarios sin repetirlos.
6. Si parte de ventas, seleccione **Cargar ventas**, marque las ventas que se incluirán y envíe la selección para que sus productos aparezcan en el detalle.
7. Revise que cada producto tenga una cantidad mayor que cero y, cuando aplique, sus lotes y series; confirme que el almacén de origen y el vehículo son los previstos.
8. Seleccione **Registrar**. La pantalla envía el formulario y comunica que la orden fue registrada correctamente.

## Compruebe el resultado

Abra la orden creada y contraste su documento, **Almacén**, **Vehículo**, **Fecha salida**, productos y cantidades. Debe figurar con estado **Programada**.

## Situaciones frecuentes

- **Residuales:** los residuales físicos se calculan en el servidor; no se agregan manualmente como productos de la orden.
- **Cantidad o seguimiento incompletos:** corrija la fila antes de registrar; cada producto requiere cantidad positiva y los datos de lote o serie que correspondan.
