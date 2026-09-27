<a id="registrar-venta-con-saldo-pendiente"></a>

# 2.2 Registrar una venta con saldo pendiente

<a id="25-registrar-venta-con-saldo-pendiente"></a>
<a id="objetivo"></a>
<a id="punto-de-partida"></a>
<a id="resultado-esperado"></a>

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>
<a id="acceso-condicional"></a><a id="requisitos-y-datos"></a><a id="campos-y-validaciones-observados"></a><a id="advertencias-y-casos-limite"></a><a id="problemas-frecuentes-y-condiciones-de-detencion"></a><a id="enlaces-relacionados"></a>

Registre una venta con el importe pendiente y la fecha de vencimiento acordados.

## Antes de empezar

La posibilidad de registrar saldo pendiente y los métodos disponibles dependen de
la configuración, documento, sesión y reglas del entorno.

### Datos necesarios

- Cliente, productos e importes revisados.
- Importe recibido y fecha de vencimiento acordados.
- Documento, serie, fecha y almacén completos.

## Cómo acceder

1. En la barra lateral, abra **Ventas**.
2. Seleccione **Crear venta**.

## Pasos

1. Abra el detalle de pago desde el formulario de venta.
2. Registre el importe recibido y revise cómo cambian **Total pagado** y
   **Deuda**.
3. Cuando exista deuda, complete y revise **Fecha vencimiento crédito**.
4. Verifique que la deuda sea el importe pendiente acordado antes de confirmar.
5. Seleccione **Confirmar** únicamente cuando los importes y la fecha sean
   correctos.

### Datos que debe revisar

El detalle calcula deuda como la diferencia entre total y pagos ingresados. Si la
deuda es mayor que cero, muestra la fecha de vencimiento y exige que sea posterior
a la fecha de emisión. Cada monto debe ser válido y mayor que cero; en pagos no
efectivo únicos, el monto no puede superar el total.

<a id="resultado-revisado-en-fuente"></a>

## Compruebe el resultado

El flujo incorpora la deuda y la fecha de vencimiento a los datos enviados para
registrar la venta. La aceptación de cada combinación de pago y deuda debe
verificarse en el entorno de trabajo.

## Situaciones frecuentes

No use una fecha igual o anterior a la emisión cuando el formulario muestre deuda.
No confirme un saldo pendiente sin contrastarlo con el acuerdo comercial; la
la pantalla no prueba una política de crédito ni su aprobación en el entorno.

### Si necesita detenerse

- Deuda diferente de la acordada: corrija montos antes de confirmar.
- Fecha de vencimiento rechazada: use una fecha posterior a la emisión.
- Método o documento no disponible: detenga la operación y valide la configuración.

## Continuar con

- [Registrar venta al contado](registrar-venta-al-contado.md)
- [Registrar cobro posterior y consultar saldo](registrar-cobro-posterior-y-consultar-saldo.md)
