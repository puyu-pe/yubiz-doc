# Contrato de alcance histórico: manual orientado a tareas (V1)

Este contrato conserva el catálogo histórico de 78 entradas V1: una entrada de inicio rápido y 77 guías de tarea. No es el catálogo activo ni la autoridad de navegación actual. La implementación autorizada y activa es el [Contrato V2: alcance reconciliado por menú](task-oriented-manual-contract-v2.md), con 83 entradas integradas en la navegación, el inventario y la validación.

## Estado histórico

Las tablas y listas de este documento registran el alcance V1 aprobado en su momento. Se conservan para interpretar URL e identificadores heredados; no sustituyen la numeración, las rutas ni el canon V2 actual. Esta conservación no autoriza publicación ni cambia los estados de fuente, ejecución o despliegue.

## Estado y límite de aprobación

| Aspecto | Estado |
| --- | --- |
| Catálogo de 78 entradas | Histórico; preservado para compatibilidad |
| Estructura de la ficha | Aprobada explícitamente por el solicitante e incorporada en este contrato |
| Implementación y refactor de páginas | Implementación V1 concluida; V2 es el alcance activo |
| Estados de fuente, ejecución o validación | Sin avance automático por este contrato |

Este registro histórico no modifica el alcance activo. Los estados de fuente, ejecución y despliegue permanecen independientes.

## Alcance base

### 1. Inicio rápido (1)

- Empezar a trabajar en Yubiz.

### 2. Ventas (14)

Familias editoriales: Registrar y cobrar (3), Cotizaciones (2), Consultar y corregir documentos (4) y Reportes (5).

- Registrar una venta al contado.
- Registrar una venta con saldo pendiente.
- Registrar un cobro posterior.
- Crear y consultar cotizaciones.
- Convertir una cotización en venta.
- Consultar una venta, imprimirla o comunicarla.
- Anular una venta.
- Emitir una nota de crédito.
- Canjear un documento de venta.
- Consultar ventas y productos vendidos.
- Consultar ventas por usuario y cliente.
- Consultar comisiones de vendedores.
- Consultar comisiones por producto.
- Consultar pagos y deudas de ventas.

La guía de cotizaciones incluye, cuando corresponda, edición, réplica e impresión. La consulta de venta incluye su variante de réplica y la conversión cubre la finalización de la venta.

### 3. Contactos (3)

- Registrar y actualizar clientes.
- Registrar y actualizar proveedores y sus cuentas bancarias.
- Registrar y actualizar transportistas.

### 4. Productos (8)

- Registrar y actualizar productos.
- Eliminar productos.
- Registrar marcas, categorías, medidas y modelos.
- Configurar precios de venta.
- Registrar y actualizar lotes.
- Registrar y consultar series de productos.
- Registrar y actualizar líneas y conversiones.
- Consultar productos y su utilidad.

La información de compra, los proveedores y las imágenes de un producto se integran en su mantenimiento. Las secciones de seguimiento y exportación se incluyen donde corresponda.

### 5. Inventario (8)

- Consultar stock por almacén.
- Revisar movimientos y kardex.
- Registrar un ingreso de almacén.
- Registrar una salida de almacén.
- Transferir productos entre almacenes.
- Registrar un ajuste de inventario.
- Crear y consultar guías de remisión.
- Registrar y consultar cargas de contenedores.

La asignación de series se explica dentro de cada movimiento. El ingreso a guía desde venta u orden de carga se cubre en su entrada correspondiente, sin duplicarlo.

### 6. Compras (11)

- Crear un pedido de compra.
- Consultar, actualizar y notificar un pedido de compra.
- Anular un pedido de compra.
- Registrar una orden de compra.
- Crear una orden de compra desde un pedido.
- Consultar y notificar órdenes de compra.
- Cambiar el estado de una compra.
- Anular una compra.
- Registrar pagos de compra y revisar saldos.
- Registrar y relacionar documentos de compra.
- Preparar y consultar el presupuesto de compras.

Las variantes de réplica, impresión y exportación se incorporan en las consultas correspondientes.

### 7. Gastos (5)

- Registrar un gasto.
- Consultar y exportar gastos.
- Aprobar un gasto.
- Anular un gasto.
- Registrar categorías de gasto y costos fijos.

### 8. Preventa (5)

- Crear un pedido de preventa.
- Consultar y actualizar una preventa.
- Confirmar una preventa.
- Anular una preventa.
- Convertir una preventa en venta.

### 9. Distribución (8)

- Crear una orden de carga.
- Consultar una orden de carga.
- Confirmar una orden de carga.
- Registrar recargas, compromisos y residuales.
- Cerrar una orden de carga.
- Generar una orden de descarga.
- Registrar el resultado de una entrega.
- Liquidar una orden de carga.

`Cerrar una orden de carga` se implementa tras una alineación deliberada y acotada de su interfaz y handler con la revisión de contenido activa. Esta alineación admite únicamente la ficha 9.5; no modifica el checkpoint global, la auditoría pendiente de 332 rutas ni los estados de fuente, ejecución o despliegue.

### 10. Servicios e internados (5)

- Registrar unidades e ítems de servicio.
- Registrar una orden de servicio o internado.
- Consultar un internado y registrar procedimientos.
- Convertir un internado en venta.
- Anular un internado.

### 11. Estancias (6)

- Registrar una estancia.
- Consultar estancias del día y su detalle.
- Registrar sujetos y personas relacionadas.
- Definir tarifas, relaciones y descuentos.
- Convertir una estancia en venta.
- Anular una estancia.

### 12. Fidelización (1)

- Crear campañas de descuento y asignar productos.

Incluye agregar o retirar asociaciones de productos. No presupone la edición de campos generales de una campaña existente sin evidencia de interfaz verificada.

### 13. Usuarios y vendedores (3)

- Registrar y actualizar usuarios.
- Registrar y actualizar vendedores.
- Asignar establecimientos a vendedores.

Los nombres de estos grupos son agrupaciones editoriales; no declaran etiquetas universales ni literales de la barra lateral.

## Integración y exclusiones

No se crearán guías independientes para seleccionar un establecimiento, cliente o producto, completar la serie documental o la fecha, ni elegir medios de pago. Estas instrucciones se integrarán en inicio rápido, precondiciones y procedimientos de venta o cotización, según corresponda. Las imágenes y los datos de compra del producto se explicarán dentro de su mantenimiento; la asignación de series, dentro del movimiento de inventario; y las exportaciones, en las consultas correspondientes.

Esta regla no elimina las tareas de registro y mantenimiento de clientes o productos, ni las consultas con exportación incluidas expresamente en el catálogo.

Quedan fuera de esta propuesta, sin calificarlas como defectos ni como inexistencia de funcionalidad: las cuatro páginas anteriores del grupo Configuración y las cuatro del grupo Operaciones especializadas. También permanecen fuera, pendientes de confirmar entrada y alcance: Caja, Entidades financieras, Consultar roles, Configurar internados y la generación de documentos desde transferencias con enlaces deshabilitados.

Esta exclusión no alcanza mantenimiento de precios de producto, campañas ni mantenimiento de registros solo porque sus títulos contengan verbos de configuración. Se conservan las exclusiones de capacidades ya definidas en los puntos de control de fuente; los metadatos vigentes son la autoridad. No se utilizarán identificadores temporales de la propuesta como identificadores de capacidad.

No se eliminarán automáticamente páginas anteriores ni se reclasificarán capacidades excluidas.

## Requisitos de implementación y aceptación

Cada una de las 78 entradas deberá describir, como mínimo, la entrada al flujo, los datos necesarios cuando correspondan, la acción y una comprobación observable del resultado. La redacción evitará afirmar permisos, rótulos universales, políticas, capturas o comportamiento desplegado sin evidencia de ejecución.

La implementación deberá conservar los identificadores de capacidad existentes. Cuando se reubique contenido con enlaces heredados, deberá existir un mapeo y, cuando aplique, una redirección; la transición no podrá romper enlaces sin una decisión explícita.

La estructura aprobada se define a continuación y sustituirá la plantilla anterior durante la implementación autorizada. Las páginas públicas no expondrán trazas privadas de fuentes, rutas internas ni avisos de estado de ejecución. La ausencia de esas trazas no equivale a una auditoría completa de ejecución.

## Estructura aprobada de cada ficha

La ficha deberá permitir completar una tarea desde su punto de acceso hasta una comprobación observable, sin reconstruir el procedimiento entre varias páginas.

| Elemento | Uso | Contenido |
| --- | --- | --- |
| Título | Obligatorio | Número y acción concreta que realizará la persona. |
| Introducción | Obligatoria | Una o dos frases sobre el resultado de la tarea, sin encabezado «Objetivo». |
| Cómo acceder | Obligatorio | Ruta real de entrada y, cuando corresponda, cómo localizar y abrir el registro de origen. |
| Antes de empezar | Condicional | Solo datos o condiciones necesarios para iniciar. |
| Pasos | Obligatorio | Recorrido completo con controles identificados, datos mínimos y reacciones de la interfaz útiles para orientarse. |
| Compruebe el resultado | Obligatorio | Qué registro, estado o información debe observar y con qué datos contrastarlo. |
| Situaciones frecuentes | Opcional | Alternativas, errores y condiciones de detención reales. |
| Continuar con | Opcional | Enlaces a tareas posteriores; nunca instrucciones imprescindibles omitidas del procedimiento. |

### Plantilla base

Las secciones condicionales y opcionales se omitirán cuando no aporten contenido. Los marcadores de esta plantilla no aparecerán en una ficha terminada.

```markdown
# <Número> <Acción concreta>

<Qué conseguirá al terminar esta tarea.>

## Cómo acceder

<Ruta real hasta la pantalla o el registro donde comienza la tarea.>

## Antes de empezar

- <Dato o condición necesaria para iniciar.>

## Pasos

1. <Acción concreta sobre un control identificado.>
2. <Siguiente acción y reacción de la interfaz, cuando ayude a orientarse.>
3. <Datos mínimos que debe completar o revisar.>
4. <Acción final que completa la operación.>

## Compruebe el resultado

<Qué registro, estado o información debe comprobar y con qué datos contrastarlo.>

## Situaciones frecuentes

- **<Situación>:** <cómo resolverla o cuándo detenerse>.

## Continuar con

- [<Siguiente tarea relacionada>](<ruta>)
```

### Reglas de redacción

- Explicar cada campo en el paso donde se utiliza. Distinguir datos que debe ingresar la persona, valores iniciales que debe revisar y datos opcionales. Usar una tabla breve solo cuando facilite esa distinción.
- Identificar los botones por su etiqueta. Añadir su ubicación cuando esté respaldada y ayude a encontrarlos, sin asumir una posición universal en todas las pantallas.
- Incluir la reacción de la interfaz cuando ayude a reconocer el siguiente paso; no convertir cada clic en una ficha ni inventar reacciones para completar la plantilla.
- Colocar las advertencias de operaciones financieras, anulaciones o eliminaciones inmediatamente antes de la acción sensible. Indicar qué revisar y cuándo detenerse; una advertencia al final no sustituye esta prevención.
- Completar la tarea: no terminar en un botón intermedio si después hay que completar otro formulario, revisar un pago o confirmar el guardado.
- Explicar variantes como pagos combinados, réplica, impresión o entradas alternativas mediante subsecciones cuando formen parte de la misma tarea.
- Usar capturas solo si orientan mejor que el texto. Deben carecer de datos sensibles, tener texto alternativo y mantenerse cuando cambie la interfaz.
- No crear requisitos, tablas, advertencias, errores ni enlaces de relleno para satisfacer una sección opcional.

### Adaptación al tipo de tarea

| Tipo | Recorrido que debe completar |
| --- | --- |
| Registro | Completar los datos mínimos, guardar y comprobar el registro visible. |
| Consulta | Definir los filtros necesarios y comprobar el conjunto o registro obtenido. |
| Exportación | Solicitar y comprobar el archivo correspondiente a la consulta. |
| Conversión | Partir del registro de origen, completar el documento de destino y comprobar el resultado. |
| Anulación o cambio de estado | Verificar condiciones, advertir el impacto antes de confirmar y comprobar el estado resultante. |
| Mantenimiento de registros | Localizar el registro, crear o actualizar según corresponda y comprobar lo guardado; distinguir eliminación de otras formas de retiro. |

La ficha de venta al contado conservará la distinción entre **Registrar**, que abre el detalle de pago, y **Confirmar**, que ejecuta el guardado. La comprobación de la venta no se sustituirá por un intento de impresión o comunicación.

### Aceptación de la estructura implementada

- Una persona podrá acceder desde el punto de entrada indicado y completar la tarea básica sin consultar otras fichas obligatoriamente.
- Los campos y botones relevantes serán inequívocos, y los datos mínimos se explicarán en contexto.
- La comprobación final será observable; no se afirmarán efectos de caja, stock, impresión o comunicación sin evidencia que los respalde.
- Las detenciones de seguridad aparecerán antes de confirmar una operación sensible.
- El validador, sus pruebas y los ejemplos de prueba se actualizarán junto con las fichas para exigir el núcleo aprobado, no los diez encabezados anteriores.
- Se conservarán los anclajes y enlaces heredados o se incluirán en el mapeo de migración aprobado. El cambio de encabezados no autoriza su eliminación indiscriminada.
- Las pruebas estructurales no se presentarán como demostración de usabilidad; se revisará también que el recorrido sea completo y comprensible.

## Criterio de cierre de la propuesta

La estructura de ficha y el catálogo de 78 entradas quedan aprobados e incorporados. La implementación debe conservar los estados de fuente o ejecución sin avances automáticos.
