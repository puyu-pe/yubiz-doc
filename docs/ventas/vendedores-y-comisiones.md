# Gestionar vendedores y consultar comisiones

## Estado
- Revisión de fuente: revisada en código
- Verificación en entorno: pendiente
- Paridad con la versión desplegada: pendiente

## Objetivo
Revisar el vínculo observado entre una persona usuaria, establecimientos y el contexto de vendedor, además de los controles de consulta de comisiones disponibles.

## Acceso condicional
La gestión de vendedores, establecimientos y comisiones es condicional: depende de módulos, sesión, rol y configuración del entorno.

## Requisitos y datos
- Persona usuaria o vendedor identificado.
- Establecimientos visibles en el formulario, cuando esté disponible.
- Periodo o filtros de consulta, si aparecen en el reporte.

## Punto de partida
En la opción disponible para establecimientos de vendedor o en un reporte de comisiones.

## Pasos
1. Confirme que está revisando la persona usuaria correcta antes de modificar una selección.
2. Revise los establecimientos y sus datos mostrados en la tabla.
3. Seleccione o quite una relación solo si esa acción está habilitada y corresponde a la decisión autorizada en su organización.
4. Guarde y revise el resultado mostrado por el entorno.
5. Para comisiones, aplique los filtros disponibles y revise el periodo, vendedor y datos mostrados antes de interpretar un resultado.

## Campos y validaciones observados
El formulario observado presenta una lista seleccionable de establecimientos con dirección y ubicación, más una acción de guardar. Los reportes de ventas incluyen filtros de vendedor; la disponibilidad de una consulta de comisiones es condicional.

## Resultado revisado en fuente
La interfaz envía las selecciones de establecimientos para la persona usuaria. La fuente también incluye una salida de comisiones. La asignación efectiva, permisos, cálculo y pago de comisiones requieren verificación en runtime.

## Advertencias y casos límite
No interprete una casilla seleccionada ni un reporte como autorización de acceso o confirmación de pago. Si no conoce las consecuencias de una asignación o de un cálculo, detenga el flujo y escale la consulta.

## Problemas frecuentes y condiciones de detención
- Persona usuaria incorrecta: no guarde cambios.
- Establecimiento o reporte no disponible: no infiera permisos ni habilitación universal.
- Resultado de comisión incierto: no tome decisiones de pago; solicite revisión responsable.

## Verificaciones pendientes en runtime
- Roles, establecimientos y acciones disponibles.
- Resultado de guardado y alcance de la asignación.
- Cálculo, visibilidad y efectos de comisiones.

## Enlaces relacionados
- [Consultar reportes consolidados y ventas por producto](revisar-reportes-de-ventas.md)
- [Elegir documento, serie, fecha y almacén de una venta](configurar-datos-del-documento.md)
