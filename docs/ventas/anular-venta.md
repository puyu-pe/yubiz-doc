# Anular una venta con cautela

## Estado
- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo
Revisar el mecanismo observado para solicitar la anulación de una venta sin ejecutar una operación real desde esta guía.

## Acceso condicional
La anulación se muestra solo para determinados documentos y puede depender del estado, la emisión, una condición de acceso y la configuración disponible.

## Requisitos y datos
- Venta correcta abierta en detalle.
- Estado, documento y fecha revisados.
- Motivo y decisión sobre devolución de productos, cuando el formulario los solicite.

## Punto de partida
En el menú de acciones del detalle de una venta elegible.

## Pasos
1. Confirme documento, serie, correlativo, cliente, ítems y montos antes de abrir la acción.
2. Revise si **Anular** está habilitado; si no lo está, no intente continuar por otra vía.
3. En el formulario observado, complete el motivo y revise la opción sobre devolución de productos.
4. Deténgase si no puede validar el impacto operativo con la persona responsable.
5. Solo una persona autorizada en su operación debe confirmar la solicitud.

## Campos y validaciones observados
El formulario observado incluye motivo y una opción para devolución de productos. Para documentos distintos de nota de venta, el navegador compara la fecha con un límite suministrado por la configuración; no se documenta aquí una ventana universal.

## Resultado revisado en fuente
La interfaz envía la solicitud de anulación con esos datos y vuelve a cargar el detalle de la venta. La anulación efectiva y sus efectos sobre productos, caja, documentos o comunicaciones requieren verificación en runtime.

## Advertencias y casos límite
Es una operación destructiva. No infiera una política de aprobación, una regla tributaria ni un efecto de stock o caja desde la mecánica observada. Si existe duda sobre el impacto, detenga el proceso y escale la decisión.

## Problemas frecuentes y condiciones de detención
- Acción no disponible o deshabilitada: revise el estado y escale la consulta.
- Motivo o decisión de devolución incompletos: no confirme.
- Fecha fuera del rango mostrado: no suponga una excepción; solicite orientación operativa.

## Verificaciones pendientes en runtime
- Documentos, estados y condiciones de acceso habilitados.
- Reglas de fecha configuradas en el entorno.
- Efectos de anulación, devolución, caja, stock y comunicación.

## Enlaces relacionados
- [Buscar, filtrar y revisar el detalle de ventas](consultar-ventas.md)
- [Visualizar, imprimir y comunicar una venta](imprimir-y-comunicar-venta.md)
