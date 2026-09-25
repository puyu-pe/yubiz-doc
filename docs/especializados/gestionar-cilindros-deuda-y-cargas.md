<a id="consultar-cilindros-deuda-y-cargas"></a>

# 5.14 Consultar cilindros, deuda y cargas

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Consultar los reportes especializados de cilindros y deuda, y reconocer el acceso existente a cargas sin duplicar su procedimiento.

## Acceso condicional

El menú declarado incluye reportes de cilindros en cliente y almacén, deuda de cliente y acciones de carga. Los nombres, datos y resultados deben verificarse.

## Requisitos y datos

- Filtros o registro seleccionado en el reporte disponible.
- Confirmación del alcance antes de abrir detalle o impresión.

## Punto de partida

Abra el reporte de cilindros o deuda disponible desde el módulo especializado.

## Pasos

1. Seleccione el reporte de cilindros o deuda que necesita consultar.
2. Revise la lista o resumen mostrado antes de abrir un detalle.
3. Use el detalle o impresión disponible solo después de confirmar el registro.
4. Para una carga, continúe con la guía existente de Inventario.
5. Deténgase si los datos no permiten identificar el contexto de consulta.

## Campos y validaciones observados

La pantalla puede mostrar listas y resúmenes para cilindros y deuda, además de detalles imprimibles. Los filtros, columnas, totales y formatos disponibles deben revisarse antes de continuar.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

La consulta puede presentar un resumen o detalle de cilindros y deuda. La interfaz también declara accesos a crear y listar cargas, cuyo procedimiento ya se documenta en la guía de Inventario.

## Advertencias y casos límite

No use un resumen como confirmación de deuda o entrega. Evite exponer datos de personas y deténgase si el detalle no corresponde al registro seleccionado.

## Problemas frecuentes y condiciones de detención

- No puede identificar el registro: no abra ni imprima el detalle.
- Resultado sin contexto: revise filtros antes de comunicarlo.
- Necesita registrar una carga: siga la guía de Inventario, no duplique el flujo.

## Enlaces relacionados

- [Registrar y consultar cargas de contenedores](../inventario/gestionar-cargas-de-contenedores.md)
- [Módulos especializados](index.md)
