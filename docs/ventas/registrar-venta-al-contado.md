<a id="registrar-venta-al-contado"></a>

# 2.1 Registrar una venta al contado

<a id="24-registrar-venta-al-contado"></a>
<a id="objetivo"></a>
<a id="punto-de-partida"></a>
<a id="resultado-esperado"></a>

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>
<a id="acceso-condicional"></a><a id="requisitos-y-datos"></a><a id="campos-y-validaciones-observados"></a><a id="advertencias-y-casos-limite"></a><a id="problemas-frecuentes-y-condiciones-de-detencion"></a><a id="enlaces-relacionados"></a>

Registre una venta pagada al contado y compruebe el documento, los productos y el cobro antes de continuar.

## Antes de empezar

Las opciones disponibles pueden variar según la sesión y la configuración del
negocio.

### Datos necesarios

- Tener identificado al cliente, el producto y el efectivo recibido.
- Contar con los datos de documento que correspondan a la operación.

## Cómo acceder

1. En la barra lateral, abra **Ventas**.
2. Seleccione **Crear venta**.

## Pasos

1. En **DNI / RUC**, seleccione el cliente.
2. En **Item**, seleccione el producto. Verifique que aparezca una fila en la
   tabla y agregue los demás productos necesarios.
3. Revise cada fila: **Cant.**, **P. Unit.** e **Importe**. Ajuste la cantidad o
   el precio solo si corresponde al cobro acordado.
4. Revise el **Total**. Confirme el documento y complete o cambie la serie, la
   fecha o el almacén solo cuando la operación lo requiera.
5. Seleccione **Registrar**, en la parte superior derecha. Se abre el detalle de
   pago.
6. Confirme o agregue **Efectivo**. En **Monto**, ingrese el efectivo realmente
   recibido; puede ser mayor que el total si debe entregar vuelto.
7. Revise **Total Pagado**, **Deuda**, **Vuelto** y **Total Venta**. Para una
   venta al contado, no continúe si queda deuda o si el vuelto no coincide con el
   efectivo recibido.
8. Seleccione **Confirmar** para guardar. Espere el resultado visible y verifique
   el documento registrado, el cliente, los productos y los importes antes de
   comunicar, imprimir o iniciar otra operación.

### Datos que debe revisar

| Campo o dato | Guía de revisión |
| --- | --- |
| **DNI / RUC** e **Item** | Selección manual obligatoria para identificar al cliente y agregar al menos un producto. |
| **Cant.** | Al agregar un producto parte de `1.00`; confirme o ajuste la cantidad vendida. |
| Documento, serie, fecha y almacén | El documento puede mostrar una opción predeterminada y la fecha parte del día actual. Revise y complete o cambie los demás datos cuando sea necesario. |
| **Monto** en **Efectivo** | Debe ser un importe válido y mayor que cero. Puede superar el total para calcular el vuelto. |

Solo se permite agregar un método de pago en efectivo al detalle.

<a id="resultado-revisado-en-fuente"></a>

## Compruebe el resultado

Después de **Confirmar**, revise el resultado mostrado en pantalla. Continúe
solo si puede reconocer el documento registrado y sus datos coinciden con el
cobro realizado.

## Situaciones frecuentes

Esta es una operación financiera. No confirme si el total pagado, la deuda o el
vuelto no representan el cobro recibido. La impresión o comunicación, si se
realizan después, requieren su propia comprobación. No interprete un intento de
impresión o comunicación como constancia de que la venta se registró.

### Si necesita detenerse

- Campos obligatorios sin completar: complete o corrija el formulario antes de
  abrir el pago.
- Cliente o producto sin seleccionar: detenga el proceso, complete ambos datos y
  compruebe que el producto figure en la tabla.
- Cantidad, precio o importe incorrectos: corrija la fila y vuelva a revisar el
  total antes de abrir el pago.
- Monto inválido o distinto del efectivo recibido: no confirme; corrija el
  monto y revise total pagado, deuda y vuelto.
- Deuda pendiente en una venta al contado: no confirme hasta que el pago cubra
  el total o use el procedimiento de saldo pendiente.
- Productos eliminados en la tabla: retírelos antes de intentar confirmar.

## Continuar con

- [Registrar una venta con saldo pendiente](registrar-venta-con-saldo-pendiente.md)
