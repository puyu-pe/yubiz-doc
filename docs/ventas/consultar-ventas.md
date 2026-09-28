<a id="buscar-filtrar-y-revisar-el-detalle-de-ventas"></a>

# 2.6 Consultar una venta, imprimirla o comunicarla

<a id="28-buscar-filtrar-y-revisar-el-detalle-de-ventas"></a>
<a id="objetivo"></a>
<a id="punto-de-partida"></a>
<a id="resultado-esperado"></a>

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>
<a id="acceso-condicional"></a><a id="requisitos-y-datos"></a><a id="campos-y-validaciones-observados"></a><a id="advertencias-y-casos-limite"></a><a id="problemas-frecuentes-y-condiciones-de-detencion"></a><a id="enlaces-relacionados"></a>

Ubique una venta, revise su detalle y use la impresión o comunicación disponibles solo después de confirmar que es el documento correcto.

## Antes de empezar

La lista, sus columnas, filtros, exportaciones y acciones del detalle dependen de
la sesión, módulo y configuración disponible.

### Datos necesarios

- Acceso a la lista de ventas.
- Un dato de búsqueda o filtro, cuando sea necesario.
- Identificación de la venta que se desea revisar.

## Cómo acceder

1. En la barra lateral, abra **Ventas**.
2. Seleccione **Ventas**.
3. Haga doble clic en la fila de la venta para abrir su detalle.

## Pasos

1. Revise las columnas visibles para identificar documento, serie, correlativo,
   fecha, cliente, establecimiento, total, pagado, deuda y estado.
2. Aplique los filtros que estén disponibles para documento, fecha, línea,
   cliente, establecimiento o vendedor.
3. Si necesita reiniciar la búsqueda, use **Limpiar filtros** o
   **Restablecer columnas** cuando esas opciones estén visibles.
4. Abra el detalle con doble clic en la fila de la venta seleccionada para revisar datos del cliente, datos
   generales, ítems y pagos mostrados.
5. Use **Imprimir** o la opción de comunicación que esté disponible solo después de confirmar que la fila corresponde a la operación que busca.
6. Revise el resultado visible de esa acción junto con el documento abierto; no use el intento de imprimir o comunicar como comprobación de que la venta fue registrada.

### Datos que debe revisar

La lista define columnas para documento, serie, correlativo, fechas, línea,
cliente, establecimiento, subtotal, impuesto, total, pagado, deuda, usuario,
personalizables que aparezcan en el entorno no sustituyen la revisión del detalle.

<a id="resultado-revisado-en-fuente"></a>

## Compruebe el resultado

El navegador carga una tabla de ventas, permite abrir el detalle de una fila y puede ofrecer controles para imprimir o comunicar el documento. Compruebe primero que el detalle, el cliente, los ítems y los importes son los que buscaba; el resultado de una salida puede variar según la configuración disponible.

## Situaciones frecuentes

Los montos pagado y deuda son datos financieros. No tome una fila, un estado o una
salida generada como comprobación definitiva sin contrastarla con el detalle y la
operación real. La disponibilidad de exportaciones y acciones del detalle puede
variar.

### Si necesita detenerse

- No encuentra la venta: revise filtros, columnas y datos de documento antes de
  concluir que no existe.
- El detalle no coincide con la fila esperada: detenga cualquier acción y revise
  documento, serie y correlativo.
- Una exportación o control no está disponible: no lo sustituya con una acción no
  observada; confirme la configuración de su entorno.

## Continuar con

- [Registrar cobro posterior y consultar saldo](registrar-cobro-posterior-y-consultar-saldo.md)
- [Crear y consultar cotizaciones](gestionar-cotizaciones.md)
