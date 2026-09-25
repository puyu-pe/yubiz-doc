<a id="consultar-ventas-por-usuario-y-cliente"></a>

# 2.17 Consultar ventas por usuario y cliente

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Consultar reportes especializados de productos vendidos por usuario o cliente en un
periodo, sin garantizar que cubran todas las operaciones o personas.

## Acceso condicional

Los reportes, usuarios, filtros y exportaciones dependen del módulo, sesión, rol y
configuración. Esta ficha no sustituye los reportes generales de Ventas.

## Requisitos y datos

- Fecha desde y hasta.
- Usuario o vendedor visible, cuando el selector aparezca.
- Criterio para revisar producto, unidad, cantidad o total de clientes.

## Punto de partida

Abra el reporte especializado disponible para productos vendidos por usuario o cliente.

## Pasos

1. Ingrese una fecha de inicio y una fecha de fin.
2. Seleccione usuario o vendedor si el control está disponible; use la opción general solo si aparece.
3. Seleccione **Buscar** y confirme las fechas y el filtro antes de interpretar la tabla.
4. Revise los campos de producto, código, unidad, vendedor y total de clientes cuando se muestren.
5. Use la exportación visible solo después de revisar el periodo y los filtros.

## Campos y validaciones observados

Los formularios observados requieren fecha desde y hasta; el navegador rechaza fechas
vacías y una fecha final anterior a la inicial. También muestra un selector de usuario
o vendedor y una opción general, según el reporte disponible.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

La interfaz vuelve a cargar la tabla con las fechas y el selector elegidos. No confirma
cobertura de datos, significado de los totales, acceso a usuarios ni exactitud del archivo exportado.

## Advertencias y casos límite

No use este resultado como sustituto de [reportes generales de ventas](../ventas/revisar-reportes-de-ventas.md).
Una tabla vacía no prueba que no existan ventas, clientes o usuarios fuera del alcance consultado.

## Problemas frecuentes y condiciones de detención

- Fechas vacías o invertidas: corríjalas antes de buscar.
- Usuario o vendedor inesperado: no continúe hasta validar el filtro.
- Resultado o exportación inciertos: conserve el contexto y solicite revisión.

## Enlaces relacionados

- [Consultar comisiones de ventas por producto](comisiones-de-ventas.md)
- [Consultar reportes consolidados y ventas por producto](../ventas/revisar-reportes-de-ventas.md)
