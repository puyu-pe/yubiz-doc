# Registrar venta con saldo pendiente

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Preparar una venta con un importe pendiente y una fecha de vencimiento revisable.

## Acceso condicional

La posibilidad de registrar saldo pendiente y los métodos disponibles dependen de
la configuración, documento, sesión y reglas del entorno.

## Requisitos y datos

- Cliente, productos e importes revisados.
- Importe recibido y fecha de vencimiento acordados.
- Documento, serie, fecha y almacén completos.

## Punto de partida

En el detalle de pago de una venta, tras revisar el total.

## Pasos

1. Abra el detalle de pago desde el formulario de venta.
2. Registre el importe recibido y revise cómo cambian **Total pagado** y
   **Deuda**.
3. Cuando exista deuda, complete y revise **Fecha vencimiento crédito**.
4. Verifique que la deuda sea el importe pendiente acordado antes de confirmar.
5. Seleccione **Confirmar** únicamente cuando los importes y la fecha sean
   correctos.

## Campos y validaciones observados

El detalle calcula deuda como la diferencia entre total y pagos ingresados. Si la
deuda es mayor que cero, muestra la fecha de vencimiento y exige que sea posterior
a la fecha de emisión. Cada monto debe ser válido y mayor que cero; en pagos no
efectivo únicos, el monto no puede superar el total.

## Resultado revisado en fuente

El flujo incorpora la deuda y la fecha de vencimiento a los datos enviados para
registrar la venta. La aceptación de cada combinación de pago y deuda debe
verificarse en runtime.

## Advertencias y casos límite

No use una fecha igual o anterior a la emisión cuando el formulario muestre deuda.
No confirme un saldo pendiente sin contrastarlo con el acuerdo comercial; la
fuente no prueba una política de crédito ni su aprobación en el entorno.

## Problemas frecuentes y condiciones de detención

- Deuda diferente de la acordada: corrija montos antes de confirmar.
- Fecha de vencimiento rechazada: use una fecha posterior a la emisión.
- Método o documento no disponible: detenga la operación y valide la configuración.

## Verificaciones pendientes en runtime

- Admisión de pagos parciales y ventas con deuda.
- Reglas de vencimiento, documentos y permisos por cuenta.
- Confirmación final y comportamiento desplegado.

## Enlaces relacionados

- [Registrar venta al contado](registrar-venta-al-contado.md)
- [Registrar cobro posterior y consultar saldo](registrar-cobro-posterior-y-consultar-saldo.md)
