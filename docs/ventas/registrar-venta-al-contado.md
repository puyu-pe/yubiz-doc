<a id="registrar-venta-al-contado"></a>

# 2.4 Registrar venta al contado

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Registrar una venta cuyo pago recibido cubre el total mostrado por el formulario.

## Acceso condicional

El registro de ventas, documentos, series, almacenes y métodos de pago depende de
la sesión, módulo y configuración disponible.

## Requisitos y datos

- Cliente y al menos un producto revisados.
- Documento, serie, fecha y almacén disponibles en el formulario.
- Importe recibido para la operación.

## Punto de partida

En el formulario **Venta / Agregar**, después de revisar el total de los ítems.

## Pasos

1. Revise cliente, documento, serie, fecha, almacén y total antes de usar
   **Registrar**.
2. Confirme el detalle de pago que se abre desde el formulario.
3. Revise el método **Efectivo** y el campo **Monto**; cuando no haya un pago
   predefinido, confirme que el importe coincida con el total de la venta.
4. Ingrese o confirme el importe recibido y revise **Total pagado**, **Deuda** y
   **Vuelto**.
5. Seleccione **Confirmar** solo si los importes y datos de la operación son
   correctos.

## Campos y validaciones observados

El formulario requiere cliente, documento, serie, fecha y almacén. Los montos de
pago deben ser válidos y mayores que cero; para efectivo, el cálculo puede mostrar
vuelto cuando el pago supera el total. Solo se permite agregar un método de pago
en efectivo al detalle.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

Al confirmar, revise el resultado mostrado antes de comunicar o imprimir. Confirme
el documento y sus efectos en la pantalla antes de continuar.

## Advertencias y casos límite

Esta es una operación financiera. No confirme si el total pagado, la deuda o el
vuelto no representan el cobro recibido. No interprete el intento de impresión o
comunicación como constancia de que el proceso finalizó en su entorno.

## Problemas frecuentes y condiciones de detención

- Campos obligatorios sin completar: complete o corrija el formulario antes de
  abrir el pago.
- Monto inválido: detenga el registro y corrija el importe.
- Productos eliminados en la tabla: retírelos antes de intentar confirmar.

## Enlaces relacionados

- [Seleccionar productos y revisar condiciones](seleccionar-productos-y-revisar-condiciones.md)
- [Registrar venta con saldo pendiente](registrar-venta-con-saldo-pendiente.md)
