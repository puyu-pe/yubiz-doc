# Registrar venta al contado

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

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
3. Revise el método **Efectivo** y el campo **Monto**; cuando no hay un pago
   predefinido, la fuente carga efectivo por el total de la venta.
4. Ingrese o confirme el importe recibido y revise **Total pagado**, **Deuda** y
   **Vuelto**.
5. Seleccione **Confirmar** solo si los importes y datos de la operación son
   correctos.

## Campos y validaciones observados

El formulario requiere cliente, documento, serie, fecha y almacén. Los montos de
pago deben ser válidos y mayores que cero; para efectivo, el cálculo puede mostrar
vuelto cuando el pago supera el total. Solo se permite agregar un método de pago
en efectivo al detalle.

## Resultado revisado en fuente

Al confirmar, el navegador envía venta, ítems y pagos al flujo de registro. La
fuente muestra un resultado exitoso del flujo y luego intenta comunicar e imprimir;
la confirmación efectiva, el documento y sus efectos requieren runtime.

## Advertencias y casos límite

Esta es una operación financiera. No confirme si el total pagado, la deuda o el
vuelto no representan el cobro recibido. No interprete el intento de impresión o
comunicación como constancia de que el proceso finalizó en su entorno.

## Problemas frecuentes y condiciones de detención

- Campos obligatorios sin completar: complete o corrija el formulario antes de
  abrir el pago.
- Monto inválido: detenga el registro y corrija el importe.
- Productos eliminados en la tabla: retírelos antes de intentar confirmar.

## Verificaciones pendientes en runtime

- Métodos habilitados, documentos, series y permisos disponibles.
- Validaciones de monto, vuelto y deuda en el entorno.
- Confirmación, impresión, comunicación y comportamiento desplegado.

## Enlaces relacionados

- [Seleccionar productos y revisar condiciones](seleccionar-productos-y-revisar-condiciones.md)
- [Registrar venta con saldo pendiente](registrar-venta-con-saldo-pendiente.md)
