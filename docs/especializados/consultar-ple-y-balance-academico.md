<a id="consultar-ple-y-balance-académico"></a>

# 5.12 Consultar PLE y balance académico

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Consultar los recorridos de PLE y balance disponibles en el módulo académico.

## Acceso condicional

El menú declarado incluye **Reporte PLE** y **Balance de ingresos y egresos**. Los filtros, nombres y resultados efectivos dependen del entorno.

## Requisitos y datos

- Período y filtros disponibles para la consulta.
- Criterio para revisar los resultados antes de exportar o imprimir.

## Punto de partida

Abra el reporte requerido desde el módulo especializado y confirme el período mostrado antes de solicitar datos.

## Pasos

1. Seleccione el reporte PLE o el balance disponible.
2. Complete los filtros de fecha, documento u otros controles visibles.
3. Ejecute la consulta y revise filas, totales y filtros aplicados.
4. Si la interfaz ofrece exportación o impresión, confirme el período antes de usarla.
5. Deténgase si el resultado no puede asociarse al período elegido.

## Campos y validaciones observados

La interfaz devuelve filas, total y filtros para el balance. El exportador PLE limita la salida cuando la consulta alcanza 5 000 filas; los campos y formatos visibles deben confirmarse en el entorno.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

La consulta puede devolver una tabla con total y filtros, y el PLE puede generar una salida de reporte. La exactitud contable y el archivo resultante no se verificaron.

## Advertencias y casos límite

No interprete un total como cierre o aprobación. Si la consulta supera el límite o no corresponde al período, ajuste filtros antes de continuar.

## Problemas frecuentes y condiciones de detención

- No hay datos: revise el período y no infiera que no existen registros.
- Límite de filas: reduzca el alcance de la consulta.
- Exportación no verificable: no asuma que el archivo fue generado.

## Enlaces relacionados

- [Módulos especializados](index.md)
