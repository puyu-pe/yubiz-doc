---
search:
  exclude: true
---

<a id="gestionar-vendedores-y-consultar-comisiones"></a>

# 2.12 Consultar comisiones de vendedores

<a id="215-gestionar-vendedores-y-consultar-comisiones"></a>
<a id="objetivo"></a>
<a id="punto-de-partida"></a>
<a id="resultado-esperado"></a>

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>
<a id="acceso-condicional"></a><a id="requisitos-y-datos"></a><a id="campos-y-validaciones-observados"></a><a id="advertencias-y-casos-limite"></a><a id="problemas-frecuentes-y-condiciones-de-detencion"></a><a id="enlaces-relacionados"></a>

Consulte las comisiones disponibles por vendedor para un periodo y conserve el contexto de filtros para su revisión.

## Antes de empezar
La gestión de vendedores, establecimientos y comisiones es condicional: depende de módulos, sesión, rol y configuración del entorno.

### Datos necesarios
- Periodo de consulta y vendedor, cuando el filtro esté disponible.
- Criterio para contrastar los importes y productos mostrados.

## Cómo acceder
En el reporte de comisiones disponible en el área de ventas.

## Cómo acceder

1. En la barra lateral, abra **Ventas**.
2. Seleccione **Gestión de vendedores**.

## Pasos
1. Seleccione el periodo y el vendedor cuando esos filtros estén disponibles.
2. Seleccione **Buscar** y confirme que el periodo y el vendedor visibles corresponden a la consulta.
3. Revise los datos de comisión mostrados junto con el vendedor y el periodo.
4. Antes de exportar o comunicar un importe, deténgase si no puede confirmar el contexto de filtros o el registro que lo origina.

### Datos que debe revisar
Los reportes de ventas incluyen filtros de vendedor; la disponibilidad de una consulta de comisiones depende de la configuración disponible.

<a id="resultado-revisado-en-fuente"></a>

## Compruebe el resultado
La interfaz presenta la salida de comisiones para el periodo y los filtros elegidos. El cálculo y el pago de comisiones requieren contrastarse con los registros aplicables.

## Situaciones frecuentes
No interprete un reporte como confirmación de pago. Si no conoce el origen de un importe o las consecuencias de usarlo, detenga la revisión y escale la consulta.

### Si necesita detenerse
- Vendedor o periodo incorrectos: corrija los filtros antes de interpretar el resultado.
- Reporte no disponible: no infiera su disponibilidad en otra sesión.
- Resultado de comisión incierto: no tome decisiones de pago; solicite revisión responsable.

## Continuar con
- [Consultar ventas y productos vendidos](revisar-reportes-de-ventas.md)
- [Consultar comisiones por producto](../reportes-especializados/comisiones-de-ventas.md)
