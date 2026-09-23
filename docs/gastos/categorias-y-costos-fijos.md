# Gestionar categorías de gasto y costos fijos

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Mantener las categorías usadas para clasificar gastos y los registros de costos
fijos disponibles en la sesión.

## Acceso condicional

Estas opciones dependen de la navegación y sesión disponibles. La fuente muestra
formularios de administración de datos; no confirma quién puede crear, editar o
eliminar registros ni cómo se aplican después en cada operación.

## Requisitos y datos

- Una descripción clara para la categoría.
- Para un costo fijo, descripción, costo y, si corresponde, proveedor.
- Criterios de uso acordados por la organización antes de modificar datos existentes.

## Punto de partida

Abra la lista de categorías de gasto o de costos fijos que esté disponible y revise
los registros existentes antes de agregar o editar uno.

## Pasos

1. Elija categorías de gasto para crear o editar una clasificación.
2. Complete la descripción y, si está disponible, la observación; revise que no
   duplique una clasificación que ya use su operación.
3. Guarde y vuelva a la lista para confirmar el registro mostrado.
4. Para costos fijos, abra su lista y complete descripción y costo; seleccione un
   proveedor cuando el formulario lo solicite o permita.
5. Revise el costo y el proveedor mostrados antes de guardar una modificación.
6. Compruebe en un gasto posterior si la categoría o costo queda disponible; no
   suponga que una actualización se propaga automáticamente.

## Campos y validaciones observados

La categoría requiere descripción y permite una observación. El costo fijo requiere
descripción y costo, trata el costo como dato numérico y presenta una relación con
proveedor. La disponibilidad real de operaciones de edición o eliminación depende
del entorno.

## Resultado revisado en fuente

La interfaz administra registros de categorías y de costos fijos. Estos registros
se presentan como datos separados del gasto registrado; la fuente revisada no
permite afirmar una regla universal de recurrencia, cálculo, impuestos o uso futuro.

## Advertencias y casos límite

No renombre ni elimine datos compartidos sin revisar su uso operativo. Un costo fijo
no equivale por sí mismo a un gasto registrado ni garantiza un registro automático.

## Problemas frecuentes y condiciones de detención

- Descripción ambigua o duplicada: detenga el alta y acuerde una denominación clara.
- Costo no numérico o no revisado: corríjalo antes de guardar.
- Proveedor o acciones no disponibles: no fuerce el flujo; confirme la configuración de su entorno.

## Verificaciones pendientes en runtime

- Opciones de alta, edición, eliminación y visibilidad disponibles para cada sesión.
- Reglas de duplicidad, formato de costo y relación con proveedores.
- Efecto de categorías y costos fijos en registros, reportes y políticas operativas.

## Enlaces relacionados

- [Registrar un gasto](registrar-gasto.md)
- [Consultar, aprobar y exportar gastos](gestionar-gastos.md)
- [Gastos](index.md)
