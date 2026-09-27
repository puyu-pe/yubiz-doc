<a id="consultar-comisiones-de-ventas-por-producto"></a>

# 2.12 Consultar comisiones por producto

<a id="213-consultar-comisiones-por-producto"></a>

<a id="216-consultar-comisiones-de-ventas-por-producto"></a>
<a id="objetivo"></a>
<a id="punto-de-partida"></a>
<a id="resultado-esperado"></a>

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>
<a id="acceso-condicional"></a><a id="requisitos-y-datos"></a><a id="campos-y-validaciones-observados"></a><a id="advertencias-y-casos-limite"></a><a id="problemas-frecuentes-y-condiciones-de-detencion"></a><a id="enlaces-relacionados"></a>

Consulte las comisiones por producto con el periodo y los filtros disponibles, sin confundir el reporte con una liquidación.

## Antes de empezar

Este reporte especializado depende del módulo, sesión, rol y configuración. Puede no
estar disponible aunque exista la configuración de vendedores de Ventas.

### Datos necesarios

- Periodo, producto, usuario o valor de comisión cuando aparezcan como filtros.
- Criterio para revisar fecha de registro, cantidad y montos mostrados.

## Cómo acceder

1. En la barra lateral, abra **Ventas**.
2. Seleccione **Reportes**.
3. Seleccione **Comisiones de ventas**.
4. La grilla muestra ventas por comisión; use sus filtros antes de revisar los productos, marcas, usuarios y comisiones.

## Pasos

1. Revise los filtros, columnas y periodo que aparezcan antes de interpretar la tabla.
2. Aplique filtros disponibles y confirme el contexto de los resultados.
3. Revise fecha de registro, producto, cantidad, total de venta, valor de venta, usuario y total de comisión cuando se muestren.
4. Use exportación a hoja de cálculo o PDF solo si la acción está visible.
5. Conserve el periodo y filtros usados para una revisión posterior.

### Datos que debe revisar

La tabla observada ofrece filtros por rango de fecha, usuario y valor de comisión.

<a id="resultado-revisado-en-fuente"></a>

## Compruebe el resultado

El navegador presenta una consulta de comisiones con opciones de exportación. No
confirma fórmula, base de cálculo, liquidación, pago ni validez contable.

## Situaciones frecuentes

No confunda este reporte con la asignación de vendedores y establecimientos de
[Ventas](../ventas/consultar-ventas.md). No tome decisiones de pago con un resultado no validado.

### Si necesita detenerse

- Periodo o filtro incorrecto: corríjalo antes de exportar o comunicar un total.
- Sin resultados: no concluya ausencia de comisiones sin validar el contexto.
- Total inesperado: detenga la interpretación y solicite revisión responsable.

## Continuar con

- [Consultar una venta](../ventas/consultar-ventas.md)
