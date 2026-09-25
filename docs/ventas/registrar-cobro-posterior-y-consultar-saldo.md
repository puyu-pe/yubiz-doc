<a id="registrar-cobro-posterior-y-consultar-saldo"></a>

# 2.6 Registrar cobro posterior y consultar saldo

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Revisar el saldo de una venta y registrar un cobro posterior cuando el formulario
presente esa posibilidad.

## Acceso condicional

El acceso a pagos y la fila de nuevo cobro dependen de la venta, la sesión y el
módulo disponible. La interfaz solo muestra la fila de ingreso cuando la deuda es
mayor que cero.

## Requisitos y datos

- Referencia de la venta.
- Importe, fecha, método y observación del cobro.
- Confirmación del saldo pendiente antes de registrar.

## Punto de partida

En la pantalla de pagos de una venta identificada desde la lista de ventas.

## Pasos

1. Abra la venta y revise su documento, cliente, **TOTAL**, **PAGADO** y **DEUDA**.
2. Revise las filas de pagos ya registrados, si existen.
3. Si aparece la fila de nuevo pago, complete **Fecha**, **Método pago** y
   **Monto**; agregue una observación cuando corresponda.
4. Para billetera móvil o transferencia, complete el detalle y número de operación
   que habilite el método seleccionado.
5. Revise el monto frente a la deuda y use **Registrar** solo si la información es
   correcta.

## Campos y validaciones observados

La pantalla muestra fecha, método, detalle, número de operación, monto y
observación de pagos existentes. El nuevo pago se habilita con deuda positiva; la
fecha no puede ser posterior al día mostrado por el formulario, el monto debe ser
mayor que cero y el total cancelado no puede superar el total de la venta.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

Al confirmar, se registran el nuevo pago y, ante respuesta exitosa, recarga la pantalla.
El controlador revisado devuelve un resultado de guardado; el saldo final y la
constancia pueden variar según la configuración disponible.

## Advertencias y casos límite

Esta es una operación financiera. No registre un importe mayor que el saldo que
está revisando. Una fila de pago existente o una acción de impresión no sustituyen
la verificación del resultado en el entorno.

## Problemas frecuentes y condiciones de detención

- No aparece la fila de nuevo pago: confirme que la venta tenga deuda y que su
  cuenta disponga de acceso.
- Monto cero, negativo o superior al total: corrija el valor antes de registrar.
- Método incompleto: complete los datos habilitados o detenga la operación.

## Enlaces relacionados

- [Registrar venta con saldo pendiente](registrar-venta-con-saldo-pendiente.md)
- [Registrar venta al contado](registrar-venta-al-contado.md)
