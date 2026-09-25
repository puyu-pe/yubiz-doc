<a id="gestionar-períodos-asignaciones-y-consumo-de-presupuesto"></a>

# 6.9 Gestionar períodos, asignaciones y consumo de presupuesto

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Crear y revisar períodos presupuestarios, asignar montos y consultar los consumos
cuando el módulo de presupuesto esté disponible.

## Acceso condicional

Este módulo es condicional y sus vistas, acciones y datos dependen de la sesión y
configuración. Los controles observados no definen una política de autorización ni
garantizan disponibilidad para todas las personas usuarias.

## Requisitos y datos

- Para un período: nombre, fecha de inicio, fecha de cierre y establecimiento.
- Para una asignación: documento, serie, fecha, período, usuario, monto, moneda y
  política de uso.
- Para revisar consumos: una asignación o filtros de período, fecha, usuario, origen,
  moneda o tipo.

## Punto de partida

Abra la lista de períodos, asignaciones o consumos según la tarea y espere la carga
de la grilla antes de usar filtros o abrir un detalle.

## Pasos

1. Para crear un período, complete nombre, fechas y establecimiento; confirme que
   la fecha de cierre sea posterior a la de inicio antes de registrar.
2. Revise el período creado y su estado antes de continuar con una asignación.
3. Para crear una asignación, complete documento, serie, fecha, período, usuario,
   monto, moneda y política de uso; revise que el monto sea mayor que cero.
4. Abra el detalle de la asignación para revisar monto asignado, disponible, período,
   usuario, política y los registros de consumos o ajustes mostrados.
5. Use cambio de estado, ajuste, modificación o generación de rendición solo cuando
   la acción esté disponible y después de revisar el detalle.
6. En consumos, filtre por período, fecha, usuario, origen, moneda o tipo; exporte
   el conjunto filtrado solo después de confirmar su alcance.

## Campos y validaciones observados

El período exige todos sus campos y una fecha final mayor que la inicial. La
asignación exige documento, serie, fecha, período, usuario, monto, moneda y política;
el monto debe ser numérico y mayor que cero. Las listas muestran estados, importes,
usuario y referencias de origen según el recorrido revisado.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El flujo guarda períodos inicialmente planificados y asignaciones inicialmente
activas. El detalle reúne datos de la asignación, el período, consumos y ajustes. Un
gasto puede seleccionar una asignación compatible y quedar registrado como consumo;
esto no confirma presupuesto aprobado, autorización de negocio, moneda aplicable ni
efectos financieros, fiscales, contables o de stock en el entorno de trabajo.

## Advertencias y casos límite

Un período archivado no se reactiva en la interfaz. Al cerrar o archivar un
período, la interfaz revisa asignaciones activas; una asignación con política estricta
puede impedir el cierre o archivo si conserva monto disponible. Confirme los estados
reales antes de cambiar cualquiera de ellos.

## Problemas frecuentes y condiciones de detención

- Fechas inválidas o sin orden: corrija el período antes de registrarlo.
- Monto, moneda o política incompletos: detenga la asignación y complete los datos.
- Estado o acción no disponible: no fuerce el cambio; revise período, asignación y detalle.
- Consumo o exportación inesperados: ajuste filtros y confirme el origen antes de continuar.

## Enlaces relacionados

- [Registrar un gasto](../gastos/registrar-gasto.md)
- [Consultar, aprobar y exportar gastos](../gastos/gestionar-gastos.md)
- [Compras](index.md)
