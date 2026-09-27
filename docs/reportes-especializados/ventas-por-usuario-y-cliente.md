---
search:
  exclude: true
---

<a id="consultar-ventas-por-usuario-y-cliente"></a>

# 2.11 Consultar ventas por usuario y cliente

<a id="217-consultar-ventas-por-usuario-y-cliente"></a>
<a id="objetivo"></a>
<a id="punto-de-partida"></a>
<a id="resultado-esperado"></a>

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>
<a id="acceso-condicional"></a><a id="requisitos-y-datos"></a><a id="campos-y-validaciones-observados"></a><a id="advertencias-y-casos-limite"></a><a id="problemas-frecuentes-y-condiciones-de-detencion"></a><a id="enlaces-relacionados"></a>

Consulte ventas por usuario y cliente en un periodo determinado y contraste los filtros antes de interpretar la tabla.

## Antes de empezar

Los reportes, usuarios, filtros y exportaciones dependen del módulo, sesión, rol y
configuración. Esta ficha no sustituye los reportes generales de Ventas.

### Datos necesarios

- Fecha desde y hasta.
- Usuario o vendedor visible, cuando el selector aparezca.
- Criterio para revisar producto, unidad, cantidad o total de clientes.

## Cómo acceder

Abra el reporte especializado disponible para productos vendidos por usuario o cliente.

## Pasos

1. Ingrese una fecha de inicio y una fecha de fin.
2. Seleccione usuario o vendedor si el control está disponible; use la opción general solo si aparece.
3. Seleccione **Buscar** y confirme las fechas y el filtro antes de interpretar la tabla.
4. Revise los campos de producto, código, unidad, vendedor y total de clientes cuando se muestren.
5. Use la exportación visible solo después de revisar el periodo y los filtros.

### Datos que debe revisar

Los formularios observados requieren fecha desde y hasta; el navegador rechaza fechas
vacías y una fecha final anterior a la inicial. También muestra un selector de usuario
o vendedor y una opción general, según el reporte disponible.

<a id="resultado-revisado-en-fuente"></a>

## Compruebe el resultado

La interfaz vuelve a cargar la tabla con las fechas y el selector elegidos. No confirma
cobertura de datos, significado de los totales, acceso a usuarios ni exactitud del archivo exportado.

## Situaciones frecuentes

No use este resultado como sustituto de [reportes generales de ventas](../ventas/revisar-reportes-de-ventas.md).
Una tabla vacía no prueba que no existan ventas, clientes o usuarios fuera del alcance consultado.

### Si necesita detenerse

- Fechas vacías o invertidas: corríjalas antes de buscar.
- Usuario o vendedor inesperado: no continúe hasta validar el filtro.
- Resultado o exportación inciertos: conserve el contexto y solicite revisión.

## Continuar con

- [Consultar comisiones de ventas por producto](comisiones-de-ventas.md)
- [Consultar reportes consolidados y ventas por producto](../ventas/revisar-reportes-de-ventas.md)
