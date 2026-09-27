<a id="consultar-pagos-y-deudas-de-ventas"></a>

# 2.10 Consultar pagos y deudas de ventas

<a id="214-consultar-pagos-y-deudas-de-ventas"></a>

<a id="616-consultar-pagos-y-deudas-de-ventas"></a>
<a id="objetivo"></a>
<a id="punto-de-partida"></a>
<a id="resultado-esperado"></a>

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>
<a id="acceso-condicional"></a><a id="requisitos-y-datos"></a><a id="campos-y-validaciones-observados"></a><a id="advertencias-y-casos-limite"></a><a id="problemas-frecuentes-y-condiciones-de-detencion"></a><a id="enlaces-relacionados"></a>

Revise pagos y deudas de ventas para un establecimiento, una persona usuaria y un periodo determinado.

## Antes de empezar

La disponibilidad del reporte y de los establecimientos o personas usuarias depende
de la sesión. Las categorías de pago, los montos y la diferencia mostrada son datos
del reporte filtrado; no prueban conciliación, cobro efectivo, exactitud ni una
política de medios de pago.

### Datos necesarios

- Un establecimiento o la opción amplia disponible para la sesión.
- Una persona usuaria cuando el selector la requiera.
- Fechas **Desde** y **Hasta** con inicio no posterior al final.

## Cómo acceder

1. En la barra lateral, abra **Ventas**.
2. Seleccione **Reportes**.
3. Seleccione **Pagos**.
4. Use los filtros disponibles para consultar pagos y deudas.

## Pasos

1. Seleccione el establecimiento o mantenga la vista amplia si está disponible.
2. Elija una persona usuaria cuando el formulario la solicite.
3. Indique **Desde** y **Hasta**; corrija el período si la fecha inicial supera la final.
4. Seleccione **Buscar** y confirme que los filtros siguen visibles antes de interpretar el tablero.
5. Revise el total de pagos y los grupos que la interfaz presente para el período.
6. Contraste el importe de ventas mostrado con el total de pagos solo como señal de revisión; investigue la diferencia en los registros de origen.

### Datos que debe revisar

El formulario revisado contiene establecimiento, usuario y dos fechas. El navegador
exige esos datos y rechaza un rango con fecha inicial posterior a la final. El tablero
presenta un total de pagos, desglose por los métodos disponibles y un importe total
de ventas para el mismo contexto de consulta.

<a id="resultado-revisado-en-fuente"></a>

## Compruebe el resultado

Al buscar, el navegador solicita los datos del período, establecimiento y usuario
seleccionados y actualiza el tablero con agrupaciones y totales. La interfaz compara el
total de pagos con el total de ventas mostrado, pero esa diferencia no establece por
sí sola una deuda conciliada ni la calidad de los datos.

## Situaciones frecuentes

La fecha del pago y la fecha de la venta pueden corresponder a momentos distintos;
no mezcle ambos criterios al comparar períodos. Un tablero sin datos puede reflejar
los filtros elegidos. No use una diferencia como autorización para ajustar saldos.

### Si necesita detenerse

- Fechas faltantes o invertidas: corríjalas y vuelva a buscar.
- Usuario o establecimiento inesperado: detenga la interpretación y revise el contexto de consulta.
- Diferencia no explicada: revise ventas y pagos de origen antes de escalarla.
- Sin resultados: reduzca o corrija filtros; no concluya que no existen operaciones.

## Continuar con

- [Registrar un cobro posterior y consultar el saldo](../ventas/registrar-cobro-posterior-y-consultar-saldo.md)
- [Consultar una venta](../ventas/consultar-ventas.md)
