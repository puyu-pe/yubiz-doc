# Seleccionar productos y revisar condiciones

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Incorporar productos a la venta y revisar sus importes antes de confirmar el pago.

## Acceso condicional

Los productos, precios, opciones adicionales y edición de filas pueden variar por
catálogo, establecimiento, configuración y cuenta.

## Requisitos y datos

- Cliente seleccionado.
- Producto, código o código de barras que se desea buscar.
- Cantidades y condiciones comerciales acordadas.

## Punto de partida

En el formulario de venta, con el control **Item** disponible.

## Pasos

1. Escriba al menos dos caracteres en **Item** para iniciar la búsqueda.
2. Seleccione el producto que corresponda; el formulario agrega una fila y vuelve
   a calcular los totales.
3. Revise **Cant.**, **Producto**, **Descripción**, **P. Unit.** e **Importe**.
4. Ajuste solo los datos habilitados y repita la selección para los demás
   productos.
5. Antes de pagar, confirme el subtotal, IGV y total mostrados.

## Campos y validaciones observados

La búsqueda usa código, descripción o código de barras y devuelve hasta veinte
coincidencias. La tabla conserva cantidad, descripción, tipo de IGV, precio e
importe; el formulario impide continuar si identifica productos eliminados en la
tabla.

## Resultado revisado en fuente

Cada selección agrega una fila de producto y dispara el recálculo de los totales
del formulario. Las existencias y condiciones comerciales finales requieren
verificación en runtime.

## Advertencias y casos límite

No confirme el pago si queda una fila marcada como eliminada o si los importes no
coinciden con lo acordado. Las opciones de descuento, recargo, precio alternativo
o cupón no se asumen disponibles.

## Problemas frecuentes y condiciones de detención

- Búsqueda sin resultados: verifique el término o el producto con el responsable.
- Importe inesperado: detenga la venta antes de abrir el detalle de pago.
- Producto no disponible: no sustituya ni cree un producto sin el procedimiento
  aplicable en su entorno.

## Verificaciones pendientes en runtime

- Disponibilidad de catálogo, precios, stock y opciones de fila.
- Ediciones permitidas y efectos de descuentos, recargos o cupones.
- Resultados de la versión desplegada.

## Enlaces relacionados

- [Seleccionar cliente](seleccionar-cliente.md)
- [Registrar venta al contado](registrar-venta-al-contado.md)
- [Registrar venta con saldo pendiente](registrar-venta-con-saldo-pendiente.md)
