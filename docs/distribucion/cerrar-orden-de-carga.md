# 6.5 Cerrar una orden de carga

<a id="95-cerrar-una-orden-de-carga"></a>

Cierre una orden confirmada cuando sus productos, ventas, recargas y compromisos reflejen el punto de corte operativo. El cierre habilita el paso posterior de descarga según el estado de la orden.

## Cómo acceder

1. En la barra lateral, abra **Distribución**.
2. Seleccione **Listar ordenes de carga**.
3. En la lista, abra el detalle con doble clic en la fila y, en el menú de más opciones, seleccione **Cerrar**.

## Antes de empezar

- Verifique que la orden se encuentre en el estado que habilita **Cerrar**.
- Revise los compromisos no atendidos y el déficit de reposición mostrados en el aviso del detalle.

## Pasos

1. Revise **Datos generales**: documento, **Almacén** y **Vehículo**; luego confirme la **Fecha salida** y el estado en **Detalles**.
2. En **Productos**, contraste los ingresos, salidas y saldo de cada producto. Revise **Recargas**, **Ventas** y **Pagos** cuando existan registros asociados.
3. Consulte **Descargas parciales** solo para verificar el historial; esta pestaña no sustituye la generación de una orden de descarga.
4. **Antes de cerrar**, deténgase si el aviso indica compromisos no atendidos, si hay déficit de reposición o si el saldo de productos no representa el corte que desea realizar. El cierre no debe usarse para corregir cantidades pendientes.
5. Seleccione **Cerrar** en el menú de acciones y acepte el cuadro de confirmación.
6. Espere el mensaje de orden cerrada correctamente antes de continuar.

## Compruebe el resultado

Abra nuevamente el detalle y compruebe que la etiqueta de estado muestra **Cerrada**. Debe quedar disponible la acción **Generar orden de descarga** cuando se cumplan las condiciones de la interfaz.
