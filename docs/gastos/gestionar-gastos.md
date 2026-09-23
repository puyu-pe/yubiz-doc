# Consultar, aprobar y exportar gastos

## Estado

- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo

Localizar un gasto, revisar su detalle y usar las acciones de aprobar, anular,
imprimir o exportar cuando estén disponibles.

## Acceso condicional

Las columnas, filtros y acciones dependen de la sesión y configuración. La acción
de aprobar observada es un cambio de estado de pendiente a aprobado; no constituye
una política de autorización del negocio ni confirma quién puede ejecutarla.

## Requisitos y datos

- Documento, proveedor, categoría, establecimiento, fecha, moneda o estado para filtrar.
- Criterios de búsqueda definidos antes de exportar.
- Datos del gasto revisados antes de aprobar, anular o imprimir.

## Punto de partida

Abra la lista de gastos y espere la carga de la grilla antes de aplicar filtros o
abrir el detalle de una fila.

## Pasos

1. Filtre por documento, proveedor, fecha, categoría, establecimiento, moneda,
   medio de pago o estado según la información disponible.
2. Revise documento, proveedor, categoría, importes y estado de la fila encontrada.
3. Abra el detalle para confirmar los datos antes de usar una acción.
4. Si la opción está disponible, seleccione **Aprobar**, confirme la advertencia y
   vuelva a cargar la lista para revisar el estado mostrado.
5. Use anular o imprimir solo después de revisar el detalle y las consecuencias en
   su operación.
6. Para exportar, ajuste primero los filtros y genere el PDF detallado del conjunto
   que necesita revisar.

## Campos y validaciones observados

La grilla revisada muestra documento, serie, correlativo, documento del proveedor,
proveedor, fecha, categoría, establecimiento, subtotal, IGV, total, usuario, moneda,
medio de pago y estado. El detalle solicita confirmación antes de aprobar; la
interfaz evita esa acción cuando el control está deshabilitado.

## Resultado revisado en fuente

La lista recupera gastos paginados y permite abrir su detalle. La aprobación envía
el identificador del gasto y actualiza la grilla después de una respuesta exitosa.
La exportación prepara una vista imprimible basada en los filtros y columnas
actuales; su archivo, entrega y significado operativo deben comprobarse en runtime.

## Advertencias y casos límite

No trate aprobar como una autorización universal ni anular como una corrección sin
efectos. Reduzca los filtros antes de exportar y confirme el gasto antes de repetir
una acción que no haya mostrado un resultado claro.

## Problemas frecuentes y condiciones de detención

- No se identifica el gasto: refine filtros y confirme documento, proveedor y fecha.
- La acción está deshabilitada o no aparece: detenga el flujo y revise el estado mostrado.
- La exportación contiene más datos de los esperados: cancele la revisión y ajuste filtros.

## Verificaciones pendientes en runtime

- Columnas, filtros, estados y acciones disponibles para cada sesión.
- Resultado de aprobar, anular, imprimir y exportar.
- Permisos, autorización de negocio y efectos posteriores de cada cambio de estado.

## Enlaces relacionados

- [Registrar un gasto](registrar-gasto.md)
- [Gestionar categorías de gasto y costos fijos](categorias-y-costos-fijos.md)
- [Gastos](index.md)
