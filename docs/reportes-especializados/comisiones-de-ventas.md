<a id="consultar-comisiones-de-ventas-por-producto"></a>

# 2.16 Consultar comisiones de ventas por producto

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Consultar la tabla de comisiones por producto y usar los filtros o exportaciones que
estén visibles, sin interpretar sus valores como una liquidación o pago confirmado.

## Acceso condicional

Este reporte especializado depende del módulo, sesión, rol y configuración. Puede no
estar disponible aunque exista la configuración de vendedores de Ventas.

## Requisitos y datos

- Periodo, producto, usuario o valor de comisión cuando aparezcan como filtros.
- Criterio para revisar fecha de registro, cantidad y montos mostrados.

## Punto de partida

Abra el reporte de comisiones disponible en el entorno.

## Pasos

1. Revise los filtros, columnas y periodo que aparezcan antes de interpretar la tabla.
2. Aplique filtros disponibles y confirme el contexto de los resultados.
3. Revise fecha de registro, producto, cantidad, total de venta, valor de venta, usuario y total de comisión cuando se muestren.
4. Use exportación a hoja de cálculo o PDF solo si la acción está visible.
5. Conserve el periodo y filtros usados para una revisión posterior.

## Campos y validaciones observados

La tabla observada ofrece filtros por rango de fecha, usuario y valor de comisión.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El navegador presenta una consulta de comisiones con opciones de exportación. No
confirma fórmula, base de cálculo, liquidación, pago ni validez contable.

## Advertencias y casos límite

No confunda este reporte con la asignación de vendedores y establecimientos de
[Ventas](../ventas/vendedores-y-comisiones.md). No tome decisiones de pago con un resultado no validado.

## Problemas frecuentes y condiciones de detención

- Periodo o filtro incorrecto: corríjalo antes de exportar o comunicar un total.
- Sin resultados: no concluya ausencia de comisiones sin validar el contexto.
- Total inesperado: detenga la interpretación y solicite revisión responsable.

## Enlaces relacionados

- [Gestionar vendedores y consultar comisiones](../ventas/vendedores-y-comisiones.md)
- [Consultar ventas por usuario y cliente](ventas-por-usuario-y-cliente.md)
