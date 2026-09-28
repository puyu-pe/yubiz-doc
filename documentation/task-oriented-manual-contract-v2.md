# Contrato V2: alcance reconciliado por menú

Este documento define el catálogo autorizado para la implementación V2 del manual orientado a tareas. Reconcilia las 78 entradas históricas de V1 con la interfaz observada en el entorno de demostración el 26 de septiembre de 2026. La integración V2 sigue en curso y no avanza los estados globales de fuente, ejecución o despliegue.

## Estado y lectura correcta

| Aspecto | Estado en este contrato |
| --- | --- |
| V1 | Instantánea histórica de 78 entradas, rutas y compatibilidad de fragmentos. |
| V2 | Implementación autorizada y en curso para 83 tareas en 12 grupos de menú. |
| Interfaz observada | Se observaron 12 grupos de primer nivel del menú y se abrieron las páginas de destino de sus 58 entradas hoja. Los grupos desplegables no se cuentan como páginas adicionales. |
| Acciones de negocio | No se ejecutaron acciones de alta, edición, anulación ni confirmación de registros. |
| Alcance de la observación | Corresponde a este entorno de demostración; no declara disponibilidad universal por tenant, permisos ni paridad desplegada. |
| Fuente y auditoría vigente | Conservan sus estados globales; el alcance de fuente y la evidencia de pantalla son independientes. |

### Niveles de evidencia

| Código | Significado |
| --- | --- |
| `pantalla` | Se observó la pantalla, sus controles o campos; no se ejecutó una escritura. |
| `control` | Se observó un control de acción habilitado, sin ejecutarlo. |
| `deshabilitada` | Se observó la acción, pero estaba deshabilitada para el estado del registro abierto. |
| `403` | La consulta de detalle devolvió acceso denegado; no se intentó eludirlo ni repetirla. |
| `solo menú` | Se confirmó la entrada lateral y su destino, sin confirmar el flujo completo. |
| `solo fuente` | La propuesta conserva una base anterior, pero no obtuvo confirmación de interfaz en esta observación. |

Las rutas de este documento identifican los accesos laterales observados. Cuando una acción posterior solo tiene evidencia de fuente o quedó bloqueada, su recorrido completo sigue pendiente: abrir una lista no demuestra que todas sus acciones estén disponibles. Los nombres de módulos organizan el menú editorial V2; no sustituyen las etiquetas literales de la interfaz.

## Catálogo V2 autorizado

El catálogo contiene **83 tareas autorizadas** en los 12 módulos observados. El cálculo es: 78 entradas V1 menos 10 en espera, más 10 tareas nuevas, más 5 tareas netas por tres divisiones. La numeración, los archivos y la navegación se actualizarán en conjunto al activar V2; los identificadores de capacidad existentes conservan su significado técnico.

### Cobertura del menú observado (58 entradas hoja)

| Módulo lateral | Entradas hoja observadas | Cobertura en V2 |
| --- | --- | --- |
| Panel principal | **Dashboard** (`/panel/index`) | Inicio rápido. |
| Ventas | **Crear cotización** (`/cotizacion/agregar`); **Cotizaciones** (`/cotizacion/index`); **Crear venta** (`/venta/agregar`); **Ventas** (`/venta/index`); **Notas de Crédito** (`/nota_credito/index`); **Pagos** (`/venta/reporte/pagos`); **Tabla pagos** (`/venta/reporte/jqxgrid-pagos`); **Comisiones de ventas** (`/venta/reporte/jqxgrid-comisiones`); **Ingreso egreso dinero** (`/venta/reporte/dinero-ingreso-egreso`) | Registro, consulta, reportes y tres tareas de caja. |
| Internado | **Agregar internado** (`/internado/agregar`); **Internados** (`/internado/index`); **Unidades** (`/unidad/index`); **Servicios** (`/servicio/index`); **Configuraciones** (`/internado/configuracion`) | Siete tareas de internado. |
| Campañas de descuento | **Crear campaña** (`/campania/agregar`); **Campañas** (`/campania/index`) | Campañas. |
| Inventario | **Catálogo** (`/producto/index`); **Gestión detalles producto** (`/aside/product_details`); **Utilidad de productos** (`/aside/productUtility`); **Lotes** (`/aside/lote`); **Series** (`/aside/serie`); **Inventario** (`/almacen_producto/index`); **Conversión** (`/conversion/index`); **Crear traslado interno** (`/aside/internalTransfer`); **Traslados internos** (`/aside/internalTransferList`); **Crear ingreso a almacen** (`/aside/externalTransferInput`); **Crear salida de almacen** (`/aside/externalTransferOutput`); **Ingresos y salidas** (`/aside/transfer_list`); **Crear Guía Remisión** (`/traslado/agregar`); **Guías de Remisión** (`/traslado/index`) | Quince tareas de productos e inventario. |
| Distribución | **Crear orden de carga** (`/orden-carga/agregar`); **Listar ordenes de carga** (`/orden-carga/lista`); **Listar ordenes de descarga** (`/orden-descarga/lista`) | Ocho tareas; cinco acciones dependen del detalle de carga bloqueado. La lista de cargas y el detalle de descarga sí pudieron consultarse. |
| Compras | **Crear pedido** (`/pedido_compra/agregar`); **Pedidos** (`/pedido_compra/index`); **Crear orden** (`/compra/agregar`); **Ordenes** (`/compra/index`); **Crear gasto** (`/gasto/agregar`); **Gastos** (`/gasto/index`) | Catorce tareas de compras y gastos. |
| Contactos | **Clientes** (`/cliente/index`); **Proveedores** (`/proveedor/index`); **Transportistas** (`/transportista/index`); **Entidades Financieras** (`/entidad_financiera/index`) | Cuatro tareas de mantenimiento. |
| Socios | **Gestion de Socios** (`/socio/index`); **Informe** (`/panel/socio`) | Dos tareas nuevas. |
| Presupuesto | **Periodos** (`/presupuesto/periodo`); **Asignaciones** (`/presupuesto/asignacion`); **Consumos de asignaciones** (`/presupuesto/consumo`) | Tres tareas por división de 6.11. |
| Estancia | **Registrar estancia** (`/estancia/insertar`); **Estancias del dia** (`/estancia/del-dia`); **Lista de estancias** (`/estancia/lista`); **Tarifas de estadía** (`/estancia/tarifa`); **Relacion** (`/estancia/relacion`); **Reporte de estancias** (`/estancia/reporte`); **Lista de sujetos** (`/estancia/sujeto`); **Descuentos** (`/estancia/descuento`) | Nueve tareas, incluido el reporte nuevo. |
| Preventa | **Listar preventas** (`/preventa/lista`) | Cuatro tareas; tres dependen de un estado habilitado. |

### Evidencia de pantalla para redactar después

| Área | Campos, controles o resultados observados | Límite de uso |
| --- | --- | --- |
| Cotizaciones y ventas | Cotización: **Registrar**, **Regresar**, DNI/RUC, Documento, serie y fechas, Línea. Venta: **Almacén**, **Canjear cupón de descuento** y **Aplicar precio alternativo**. | No se envió ningún formulario. |
| Listas y reportes de ventas | Ventas mostró CLIENTE, USUARIO y VENDEDOR; exportaciones PDF, EXCEL, PDF por series, pagos y deudas. Pagos mostró Establecimiento, Usuario, Desde y Hasta. Tabla pagos mostró cliente, documento, fecha, método, importe y usuario. Comisiones mostró PRODUCTO, MARCA y USUARIO. | Las columnas no prueban los informes V1 2.10, 2.11 ni 2.12. |
| Caja | Se observaron **Ingresos**, **Egresos**, Detalle comercial, Saldo inicial, Operaciones manuales, Resumen por entregar y los controles **Registrar saldo inicial**, **Registrar inyección** y **Registrar ajuste**. | Los controles no se ejecutaron. |
| Inventario | Conversión mostró Almacén origen, Producto origen, Cantidad, Medida, Almacén destino, Producto destino y **Registrar**. Las entradas, salidas y traslados mostraron formularios; catálogo, utilidad, lotes, series, stock y listas quedaron accesibles. | No se abrieron ajuste, kardex ni acciones de detalle. |
| Compras y gastos | Crear gasto mostró RUC, Documento, Serie, Moneda, Pagado por, Categoría, Fecha, agregar línea y **Guardar**. Gastos mostró exportación Excel y PDF detallado. | La selección de categoría no prueba su mantenimiento. |
| Internado | Agregar internado mostró Unidad, Categoría, Responsable, Prioridad, F. Emisión, F. Estimada salida y Almacén. Configuraciones mostró tablas de parámetros y usuario, un control **Agregar** y un selector de usuario. | No se guardaron parámetros ni se modificaron asignaciones. |
| Socios y entidades | Entidades mostró Tipo entidad, Nombre, Estado y alta, edición, eliminación. Socios mostró Nombre, Aporte, Porcentaje, Color, alta y exportación. Informe mostró selectores de año y mes, ventas, pagos, gastos, impuesto, utilidad e impresión. | No se modificaron registros ni se valida cálculo financiero o tributario. |
| Presupuesto y estancia | Períodos mostró **Nuevo periodo**; asignaciones, **Nueva asignación** y EXCEL; consumos, filtros y EXCEL. Estancia mostró tarifas, relaciones y descuentos independientes, reporte con filtros y tabla Estado/Cantidad, y personas autorizadas en el registro. | No se creó consumo manual ni se guardaron cambios. |
| Distribución y preventa | Carga mostró Serie, Almacén origen, Vehículo, Distribuidor, Fecha salida, **Cargar ventas** y **Cambiar modo**. Descarga confirmó una vista con Datos generales, Detalles y **Imprimir**. Preventa mostró un registro procesado con confirmar, convertir, editar y anular deshabilitados. | El detalle de carga quedó bloqueado por `403`; no se documenta resultado de entrega ni creación de preventa. |

### Panel principal (1)

| Tarea propuesta | Acceso observado | Evidencia | Base V1 |
| --- | --- | --- | --- |
| Empezar a trabajar en Yubiz | **Panel principal > Dashboard** (`/panel/index`) | `pantalla` | 1.1 mejorar: conserva inicio de sesión, menú y cierre de sesión; perfil queda en espera. |

### Ventas (15)

| Tarea propuesta | Acceso observado | Evidencia | Base V1 |
| --- | --- | --- | --- |
| Registrar una venta al contado | **Ventas > Crear venta** (`/venta/agregar`) | `pantalla` | 2.1 mejorar |
| Registrar una venta con saldo pendiente | **Ventas > Crear venta** (`/venta/agregar`) | `pantalla` | 2.2 mejorar |
| Registrar un cobro posterior | **Ventas > Ventas** (`/venta/index`) | `solo menú` | 2.3 retener |
| Crear y consultar cotizaciones | **Ventas > Crear cotización** (`/cotizacion/agregar`) y **Cotizaciones** (`/cotizacion/index`) | `pantalla` | 2.4 mejorar |
| Convertir una cotización en venta | **Ventas > Cotizaciones** (`/cotizacion/index`) | `solo menú` | 2.5 retener |
| Consultar una venta, imprimirla o comunicarla | **Ventas > Ventas** (`/venta/index`) | `pantalla` | 2.6 mejorar |
| Anular una venta | **Ventas > Ventas** (`/venta/index`) | `solo menú` | 2.7 retener |
| Emitir una nota de crédito | **Ventas > Notas de Crédito** (`/nota_credito/index`) | `solo menú` | 2.8 retener |
| Canjear un documento de venta | **Ventas > Ventas** (`/venta/index`), con recorrido de detalle pendiente de comprobar en este entorno | `solo fuente` | 2.9 retener; el control de canjear un cupón de descuento no demuestra un canje de documento. |
| Consultar pagos y deudas de ventas | **Ventas > Reportes > Pagos** (`/venta/reporte/pagos`) | `pantalla` | 2.14 mejorar |
| Consultar la tabla de pagos | **Ventas > Reportes > Tabla pagos** (`/venta/reporte/jqxgrid-pagos`) | `pantalla` | Nueva N1 |
| Consultar comisiones por producto | **Ventas > Reportes > Comisiones de ventas** (`/venta/reporte/jqxgrid-comisiones`) | `pantalla` | 2.13 mejorar |
| Consultar movimientos de caja | **Ventas > Reportes > Ingreso egreso dinero** (`/venta/reporte/dinero-ingreso-egreso`) | `pantalla` | Nueva N2 |
| Registrar saldo inicial de caja | **Ventas > Reportes > Ingreso egreso dinero** (`/venta/reporte/dinero-ingreso-egreso`) | `control` | Nueva N3 |
| Registrar una operación manual de caja | **Ventas > Reportes > Ingreso egreso dinero** (`/venta/reporte/dinero-ingreso-egreso`) | `control` | Nueva N4 |

La tarea N4 cubre las variantes visibles **Registrar inyección** y **Registrar ajuste**; no autoriza una guía general de caja ni readmite automáticamente otras capacidades financieras.

### Internado (7)

| Tarea propuesta | Acceso observado | Evidencia | Base V1 |
| --- | --- | --- | --- |
| Registrar y actualizar unidades de servicio | **Internado > Unidades** (`/unidad/index`) | `control` | 10.1 dividir; se observó Agregar unidad, sin guardar cambios. |
| Registrar y actualizar ítems de servicio | **Internado > Servicios** (`/servicio/index`) | `control` | 10.1 dividir; se observó Agregar servicio, sin guardar cambios. |
| Registrar una orden de servicio o internado | **Internado > Agregar internado** (`/internado/agregar`) | `pantalla` | 10.2 mejorar |
| Consultar un internado y registrar procedimientos | **Internado > Internados** (`/internado/index`) | `pantalla` | 10.3 retener; procedimiento no abierto. |
| Convertir un internado en venta | **Internado > Internados** (`/internado/index`) | `solo fuente` | 10.4 retener |
| Anular un internado | **Internado > Internados** (`/internado/index`) | `solo fuente` | 10.5 retener |
| Configurar parámetros del módulo internado | **Internado > Configuraciones** (`/internado/configuracion`) | `pantalla` | Nueva N5 |

N5 se limita a parámetros del módulo internado y a los controles observados; no representa una configuración global ni cambios de permisos.

### Campañas de descuento (1)

| Tarea propuesta | Acceso observado | Evidencia | Base V1 |
| --- | --- | --- | --- |
| Crear campañas de descuento y asignar productos | **Campañas de descuento > Crear campaña** (`/campania/agregar`) y **Campañas** (`/campania/index`) | `pantalla` | 12.1 mejorar; formulario y lista abiertos, sin ejecutar registro ni asignación. |

### Inventario (15)

| Tarea propuesta | Acceso observado | Evidencia | Base V1 |
| --- | --- | --- | --- |
| Registrar y actualizar productos | **Inventario > Catálogo** (`/producto/index`) | `control` | 4.1 mejorar |
| Eliminar productos | **Inventario > Catálogo** (`/producto/index`) | `solo menú` | 4.2 retener |
| Registrar marcas, categorías, medidas y modelos | **Inventario > Gestión detalles producto** (`/aside/product_details`) | `pantalla` | 4.3 mejorar |
| Configurar precios de venta | **Inventario > Catálogo** (`/producto/index`) | `solo fuente` | 4.4 retener |
| Registrar y actualizar lotes | **Inventario > Lotes** (`/aside/lote`) | `control` | 4.5 mejorar |
| Registrar y consultar series de productos | **Inventario > Series** (`/aside/serie`) | `pantalla` | 4.6 mejorar |
| Registrar una conversión entre productos | **Inventario > Conversión** (`/conversion/index`) | `pantalla` | 4.7 reemplazar |
| Consultar productos y su utilidad | **Inventario > Utilidad de productos** (`/aside/productUtility`) | `pantalla` | 4.8 mejorar |
| Consultar stock por almacén | **Inventario > Inventario** (`/almacen_producto/index`) | `pantalla` | 5.1 mejorar |
| Revisar movimientos y kardex | **Inventario > Ingresos y salidas** (`/aside/transfer_list`) | `solo menú` | 5.2 retener |
| Registrar un ingreso de almacén | **Inventario > Crear ingreso a almacen** (`/aside/externalTransferInput`) | `pantalla` | 5.3 mejorar |
| Registrar una salida de almacén | **Inventario > Crear salida de almacen** (`/aside/externalTransferOutput`) | `pantalla` | 5.4 mejorar |
| Transferir productos entre almacenes | **Inventario > Crear traslado interno** (`/aside/internalTransfer`) y **Traslados internos** (`/aside/internalTransferList`) | `pantalla` | 5.5 mejorar |
| Registrar un ajuste de inventario | **Inventario > Inventario** (`/almacen_producto/index`) | `solo fuente` | 5.6 retener |
| Crear y consultar guías de remisión | **Inventario > Crear Guía Remisión** (`/traslado/agregar`) y **Guías de Remisión** (`/traslado/index`) | `pantalla` | 5.7 mejorar |

La parte de líneas de la entrada 4.7 queda en espera: que el campo Línea aparezca en otros formularios no prueba un mantenimiento independiente. No se ejecutaron acciones de ajuste, kardex ni detalle de producto.

### Distribución (8)

| Tarea propuesta | Acceso observado | Evidencia | Base V1 |
| --- | --- | --- | --- |
| Crear una orden de carga | **Distribución > Crear orden de carga** (`/orden-carga/agregar`) | `pantalla` | 9.1 mejorar |
| Consultar una orden de carga | **Distribución > Listar ordenes de carga** (`/orden-carga/lista`) | `pantalla` y `403` | 9.2 mejorar; lista observada, apertura del detalle bloqueada. |
| Confirmar una orden de carga | **Distribución > Listar ordenes de carga** (`/orden-carga/lista`) | `403` | 9.3 retener condicionalmente |
| Registrar recargas, compromisos y residuales | **Distribución > Listar ordenes de carga** (`/orden-carga/lista`) | `403` | 9.4 retener condicionalmente |
| Cerrar una orden de carga | **Distribución > Listar ordenes de carga** (`/orden-carga/lista`) | `403` | 9.5 retener condicionalmente |
| Generar una orden de descarga | **Distribución > Listar ordenes de carga** (`/orden-carga/lista`) y detalle de carga; la acción Generar orden de descarga conserva evidencia de fuente | `403` | 9.6 retener condicionalmente; la lista de descargas no demuestra un acceso de creación. |
| Consultar e imprimir una orden de descarga | **Distribución > Listar ordenes de descarga** (`/orden-descarga/lista`) | `pantalla` | Nueva N6 |
| Liquidar una orden de carga | **Distribución > Listar ordenes de carga** (`/orden-carga/lista`) | `403` | 9.8 retener condicionalmente |

El detalle de una orden de carga cerrada devolvió `403`. Las solicitudes de vista previa sin datos seleccionados devolvieron `404`; no se atribuye una causa ni se repitieron. N6 se limita a la consulta e impresión observada de una orden de descarga confirmada; no incluye registrar el resultado de entrega.

### Compras (14)

| Tarea propuesta | Acceso observado | Evidencia | Base V1 |
| --- | --- | --- | --- |
| Crear un pedido de compra | **Compras > Crear pedido** (`/pedido_compra/agregar`) | `pantalla` | 6.1 mejorar; formulario y campos observados, sin registrar. |
| Consultar, actualizar y notificar un pedido de compra | **Compras > Pedidos** (`/pedido_compra/index`) | `solo menú` | 6.2 retener |
| Anular un pedido de compra | **Compras > Pedidos** (`/pedido_compra/index`) | `solo fuente` | 6.3 retener |
| Registrar una orden de compra | **Compras > Crear orden** (`/compra/agregar`) | `pantalla` | 6.4 mejorar; formulario y campos observados, sin registrar. |
| Crear una orden de compra desde un pedido | **Compras > Pedidos** (`/pedido_compra/index`) | `solo fuente` | 6.5 retener |
| Consultar y notificar órdenes de compra | **Compras > Ordenes** (`/compra/index`) | `solo menú` | 6.6 mejorar |
| Cambiar el estado de una compra | **Compras > Ordenes** (`/compra/index`) | `solo fuente` | 6.7 retener |
| Anular una compra | **Compras > Ordenes** (`/compra/index`) | `solo fuente` | 6.8 retener |
| Registrar pagos de compra y revisar saldos | **Compras > Ordenes** (`/compra/index`) | `solo fuente` | 6.9 retener |
| Registrar y relacionar documentos de compra | **Compras > Ordenes** (`/compra/index`) | `solo fuente` | 6.10 retener |
| Registrar un gasto | **Compras > Crear gasto** (`/gasto/agregar`) | `pantalla` | 7.1 mejorar |
| Consultar y exportar gastos | **Compras > Gastos** (`/gasto/index`) | `pantalla` | 7.2 mejorar |
| Aprobar un gasto | **Compras > Gastos** (`/gasto/index`) | `solo menú` | 7.3 retener |
| Anular un gasto | **Compras > Gastos** (`/gasto/index`) | `solo menú` | 7.4 retener |

La interfaz usa **Crear orden** y **Ordenes**, no los rótulos editoriales anteriores. En el gasto se observó el botón **Guardar**; una categoría seleccionable no prueba un mantenimiento de categorías o costos fijos.

### Contactos (4)

| Tarea propuesta | Acceso observado | Evidencia | Base V1 |
| --- | --- | --- | --- |
| Registrar y actualizar clientes | **Contactos > Clientes** (`/cliente/index`) | `control` | 3.1 mejorar |
| Registrar y actualizar proveedores y sus cuentas bancarias | **Contactos > Proveedores** (`/proveedor/index`) | `control` | 3.2 mejorar |
| Registrar y actualizar transportistas | **Contactos > Transportistas** (`/transportista/index`) | `control` | 3.3 mejorar |
| Registrar y actualizar entidades financieras | **Contactos > Entidades Financieras** (`/entidad_financiera/index`) | `control` | Nueva N7 |

N7 cubre la tabla observada y sus controles de alta, edición y eliminación; no se modificó ninguna entidad durante la observación.

### Socios (2)

| Tarea propuesta | Acceso observado | Evidencia | Base V1 |
| --- | --- | --- | --- |
| Registrar y actualizar socios y aportes | **Socios > Gestion de Socios** (`/socio/index`) | `control` | Nueva N8 |
| Consultar el informe de socios | **Socios > Informe** (`/panel/socio`) | `pantalla` | Nueva N9 |

N9 permite describir selectores y secciones visibles, no afirmar distribución de utilidades ni exactitud tributaria auditada.

### Presupuesto (3)

| Tarea propuesta | Acceso observado | Evidencia | Base V1 |
| --- | --- | --- | --- |
| Crear y consultar períodos presupuestarios | **Presupuesto > Periodos** (`/presupuesto/periodo`) | `control` | 6.11 dividir |
| Asignar presupuesto | **Presupuesto > Asignaciones** (`/presupuesto/asignacion`) | `control` | 6.11 dividir |
| Consultar consumo de asignaciones | **Presupuesto > Consumos de asignaciones** (`/presupuesto/consumo`) | `pantalla` | 6.11 dividir |

La tercera tarea es de consulta y exportación: no se observó un control para crear consumo manualmente.

### Estancia (9)

| Tarea propuesta | Acceso observado | Evidencia | Base V1 |
| --- | --- | --- | --- |
| Registrar una estancia | **Estancia > Registrar estancia** (`/estancia/insertar`) | `pantalla` | 11.1 mejorar |
| Consultar estancias del día y su detalle | **Estancia > Estancias del dia** (`/estancia/del-dia`) y **Lista de estancias** (`/estancia/lista`) | `pantalla` | 11.2 mejorar |
| Registrar sujetos y personas relacionadas | **Estancia > Lista de sujetos** (`/estancia/sujeto`) y **Registrar estancia** (`/estancia/insertar`) | `pantalla` | 11.3 mejorar |
| Registrar y actualizar tarifas de estadía | **Estancia > Tarifas de estadía** (`/estancia/tarifa`) | `control` | 11.4 dividir |
| Registrar y actualizar relaciones de estancia | **Estancia > Relacion** (`/estancia/relacion`) | `control` | 11.4 dividir |
| Crear y consultar descuentos de estancia | **Estancia > Descuentos** (`/estancia/descuento`) | `control` | 11.4 dividir |
| Consultar el reporte de estancias | **Estancia > Reporte de estancias** (`/estancia/reporte`) | `pantalla` | Nueva N10 |
| Convertir una estancia en venta | **Estancia > Lista de estancias** (`/estancia/lista`) | `solo fuente` | 11.5 retener |
| Anular una estancia | **Estancia > Lista de estancias** (`/estancia/lista`) | `solo fuente` | 11.6 retener |

La asociación de personas se explica dentro del registro de estancia, donde se observaron los campos correspondientes; no se propone una entrada lateral independiente para personas autorizadas.

### Preventa (4)

| Tarea propuesta | Acceso observado | Evidencia | Base V1 |
| --- | --- | --- | --- |
| Consultar y actualizar una preventa | **Preventa > Listar preventas** (`/preventa/lista`) | `pantalla` | 8.2 mejorar |
| Confirmar una preventa | **Preventa > Listar preventas** (`/preventa/lista`) | `deshabilitada` | 8.3 retener condicionalmente |
| Anular una preventa | **Preventa > Listar preventas** (`/preventa/lista`) | `deshabilitada` | 8.4 retener condicionalmente |
| Convertir una preventa en venta | **Preventa > Listar preventas** (`/preventa/lista`) | `deshabilitada` | 8.5 retener condicionalmente |

La lista no mostró una acción para crear preventas. En el registro abierto, procesado, las acciones de confirmar, convertir, editar y anular estaban deshabilitadas. Esto no prueba su inexistencia en otros estados.

## Nuevas candidatas y aperturas acotadas

Las diez candidatas nuevas son N1 tabla de pagos, N2 movimientos de caja, N3 saldo inicial, N4 operación manual, N5 parámetros de internado, N6 consulta e impresión de descarga, N7 entidades financieras, N8 socios y aportes, N9 informe de socios y N10 reporte de estancias. Provienen de ocho entradas laterales nuevas respecto del alcance V1: **Tabla pagos**, **Ingreso egreso dinero**, **Configuraciones** de internado, **Listar ordenes de descarga**, **Entidades Financieras**, **Gestion de Socios**, **Informe** de socios y **Reporte de estancias**. Una sola entrada de caja sustenta tres tareas distintas por sus tres objetivos visibles.

N1 a N10 son referencias editoriales de esta propuesta, no identificadores de capacidad ni sustitutos de los registros técnicos existentes.

Estas aperturas no reactivan de forma general los grupos de Configuración, Operaciones especializadas, PLE, cilindros o funciones externas. Solo incorporan el alcance delimitado por las pantallas enumeradas aquí.

## Mapa completo V1 a V2

Cada fila representa exactamente una de las 78 entradas V1. La disposición expresa la decisión editorial futura; la evidencia se declara por separado en el menú V2.

| V1 | Entrada V1 | Disposición V2 | Resultado o límite |
| --- | --- | --- | --- |
| 1.1 | Empezar a trabajar en Yubiz | mejorar | Conserva inicio, menú, contexto y cierre; perfil queda en espera. |
| 2.1 | Registrar una venta al contado | mejorar | Mantener con el formulario observado. |
| 2.2 | Registrar una venta con saldo pendiente | mejorar | Mantener con el formulario observado. |
| 2.3 | Registrar un cobro posterior | retener | Mantener como flujo aún no ejecutado. |
| 2.4 | Crear y consultar cotizaciones | mejorar | Usar crear y listar como accesos observados. |
| 2.5 | Convertir una cotización en venta | retener | Requiere recorrido de registro origen. |
| 2.6 | Consultar una venta, imprimirla o comunicarla | mejorar | Separar claramente controles de lista observados. |
| 2.7 | Anular una venta | retener | No se ejecutó una anulación. |
| 2.8 | Emitir una nota de crédito | retener | La lista se abrió; no se emitió documento. |
| 2.9 | Canjear un documento de venta | retener | Comprobar el recorrido desde el detalle de venta; no confundir canje de documento con canje de cupón de descuento. |
| 2.10 | Consultar ventas y productos vendidos | hold | No se confirmó informe dedicado; evaluar solapamiento con utilidad sin fusionar por defecto. |
| 2.11 | Consultar ventas por usuario y cliente | hold | Las columnas visibles no prueban el informe combinado. |
| 2.12 | Consultar comisiones de vendedores | hold | El reporte observado no prueba este objetivo específico. |
| 2.13 | Consultar comisiones por producto | mejorar | Usar el reporte de comisiones observado. |
| 2.14 | Consultar pagos y deudas de ventas | mejorar | Usar tablero de pagos observado. |
| 3.1 | Registrar y actualizar clientes | mejorar | Mantener controles observados. |
| 3.2 | Registrar y actualizar proveedores y sus cuentas bancarias | mejorar | Mantener; la cuenta bancaria no se modificó. |
| 3.3 | Registrar y actualizar transportistas | mejorar | Mantener controles observados. |
| 4.1 | Registrar y actualizar productos | mejorar | Usar catálogo observado. |
| 4.2 | Eliminar productos | retener | No se ejecutó eliminación. |
| 4.3 | Registrar marcas, categorías, medidas y modelos | mejorar | Usar tablas de detalle observadas. |
| 4.4 | Configurar precios de venta | retener | Sin recorrido de interfaz en esta sesión. |
| 4.5 | Registrar y actualizar lotes | mejorar | Usar control observado. |
| 4.6 | Registrar y consultar series de productos | mejorar | Limitar a consulta y flujo posterior verificable. |
| 4.7 | Registrar y actualizar líneas y conversiones | reemplazar | Proponer conversión entre productos; líneas quedan en espera. |
| 4.8 | Consultar productos y su utilidad | mejorar | Usar utilidad de productos observada. |
| 5.1 | Consultar stock por almacén | mejorar | Usar inventario observado. |
| 5.2 | Revisar movimientos y kardex | retener | Lista accesible; kardex no abierto. |
| 5.3 | Registrar un ingreso de almacén | mejorar | Usar formulario observado. |
| 5.4 | Registrar una salida de almacén | mejorar | Usar formulario observado. |
| 5.5 | Transferir productos entre almacenes | mejorar | Separar crear y consultar traslado. |
| 5.6 | Registrar un ajuste de inventario | retener | Sin acción abierta. |
| 5.7 | Crear y consultar guías de remisión | mejorar | Usar crear y listar observados. |
| 5.8 | Registrar y consultar cargas de contenedores | hold | No se confirmó entrada ni alcance actuales. |
| 6.1 | Crear un pedido de compra | mejorar | Formulario, RUC, Documento, Serie, Fecha y Registrar observados; no se registró un pedido. |
| 6.2 | Consultar, actualizar y notificar un pedido de compra | retener | Menú confirmado; acciones no ejecutadas. |
| 6.3 | Anular un pedido de compra | retener | Mantener como evidencia previa de fuente. |
| 6.4 | Registrar una orden de compra | mejorar | Ajustar a etiqueta observada Crear orden. |
| 6.5 | Crear una orden de compra desde un pedido | retener | Requiere flujo de origen. |
| 6.6 | Consultar y notificar órdenes de compra | mejorar | Ajustar a etiqueta observada Ordenes. |
| 6.7 | Cambiar el estado de una compra | retener | Sin cambio de estado ejecutado. |
| 6.8 | Anular una compra | retener | Sin anulación ejecutada. |
| 6.9 | Registrar pagos de compra y revisar saldos | retener | Sin flujo ejecutado. |
| 6.10 | Registrar y relacionar documentos de compra | retener | Sin flujo ejecutado. |
| 6.11 | Preparar y consultar el presupuesto de compras | split | Períodos, asignaciones y consumo de asignaciones. |
| 7.1 | Registrar un gasto | mejorar | El cierre de formulario usa Guardar. |
| 7.2 | Consultar y exportar gastos | mejorar | Exportaciones observadas. |
| 7.3 | Aprobar un gasto | retener | Acción no ejecutada. |
| 7.4 | Anular un gasto | retener | Acción no ejecutada. |
| 7.5 | Registrar categorías de gasto y costos fijos | hold | Un selector de categoría no prueba mantenimiento. |
| 8.1 | Crear un pedido de preventa | hold | No se observó acción Crear o Nuevo. |
| 8.2 | Consultar y actualizar una preventa | mejorar | Lista y detalle observado; edición depende del estado. |
| 8.3 | Confirmar una preventa | retener | Control deshabilitado en el estado observado. |
| 8.4 | Anular una preventa | retener | Control deshabilitado en el estado observado. |
| 8.5 | Convertir una preventa en venta | retener | Control deshabilitado en el estado observado. |
| 9.1 | Crear una orden de carga | mejorar | Usar campos observados; no registrar. |
| 9.2 | Consultar una orden de carga | mejorar | Lista y estados observados; detalle bloqueado por `403`. |
| 9.3 | Confirmar una orden de carga | retener | Bloqueada por detalle `403`. |
| 9.4 | Registrar recargas, compromisos y residuales | retener | Bloqueada por detalle `403`. |
| 9.5 | Cerrar una orden de carga | retener | Bloqueada por detalle `403`. |
| 9.6 | Generar una orden de descarga | retener | El recorrido de creación parte del detalle de carga, bloqueado por `403`; no se sustituye por la lista de descargas. |
| 9.7 | Registrar el resultado de una entrega | hold | No se observó acción de resultado; una API no prueba interfaz. |
| 9.8 | Liquidar una orden de carga | retener | Bloqueada por detalle `403`. |
| 10.1 | Registrar unidades e ítems de servicio | split | Unidades y servicios son pantallas distintas. |
| 10.2 | Registrar una orden de servicio o internado | mejorar | Usar Agregar internado y sus campos observados. |
| 10.3 | Consultar un internado y registrar procedimientos | retener | Lista confirmada; procedimiento no abierto. |
| 10.4 | Convertir un internado en venta | retener | Solo evidencia anterior de fuente. |
| 10.5 | Anular un internado | retener | Solo evidencia anterior de fuente. |
| 11.1 | Registrar una estancia | mejorar | Usar registro y campos observados. |
| 11.2 | Consultar estancias del día y su detalle | mejorar | Mantener entradas alternativas distintas. |
| 11.3 | Registrar sujetos y personas relacionadas | mejorar | Mantener personas autorizadas dentro del registro. |
| 11.4 | Definir tarifas, relaciones y descuentos | split | Tarifas, relaciones y descuentos son tareas distintas. |
| 11.5 | Convertir una estancia en venta | retener | Solo evidencia anterior de fuente. |
| 11.6 | Anular una estancia | retener | Solo evidencia anterior de fuente. |
| 12.1 | Crear campañas de descuento y asignar productos | mejorar | Formulario y lista observados; registro y asignación no ejecutados. |
| 13.1 | Registrar y actualizar usuarios | hold | No se observó raíz Usuarios ni Mi Perfil. |
| 13.2 | Registrar y actualizar vendedores | hold | No se observó entrada actual. |
| 13.3 | Asignar establecimientos a vendedores | hold | No se observó entrada actual. |

## Diferencias y límites de implementación posterior

La futura implementación deberá conservar V1 hasta que se aprueben explícitamente la migración de entradas, los identificadores y la navegación. Una fusión entre 2.10 y utilidad de productos solo procede si se demuestra equivalencia de objetivo y recorrido; este contrato no la presume.

Las diez tareas en espera que no entran al objetivo activo V2 son 2.10, 2.11, 2.12, 5.8, 7.5, 8.1, 9.7, 13.1, 13.2 y 13.3. El segmento de líneas separado de 4.7 también queda en espera, sin contar como una entrada V1 adicional. Las tareas con evidencia `403` o `deshabilitada` permanecen en el objetivo únicamente como procedimientos condicionales: requieren revisar el estado correcto del registro y los derechos disponibles antes de escribir instrucciones completas.

No se infiere inexistencia de una función porque no se observó. Tampoco se eleva la observación del entorno de demostración a validación integral de ejecución, de permisos, de tenant o de despliegue.

## Criterios de aceptación de la implementación

- Cada guía V2 debe iniciar desde el módulo lateral y la pantalla exactos indicados en este contrato.
- Cada transición significativa debe indicar la pantalla actual, el contenedor del control, su etiqueta o descripción visible, el gesto requerido, la revelación previa cuando exista y el estado esperado al terminar. Un icono sin etiqueta se describe junto con su contenedor; no se infiere que todos los menús de tres puntos tengan las mismas acciones.
- Cada guía de formulario debe usar los nombres de campos y botones observados, sin completar huecos con campos o resultados inventados.
- Las operaciones sensibles deben advertir antes de guardar, confirmar, anular o eliminar; la advertencia no sustituye evidencia de ejecución.
- Las acciones deshabilitadas deben documentar las condiciones de estado respaldadas por evidencia. Ante un `403`, se requiere resolver el acceso autorizado antes de completar la verificación del recorrido; no se inferirá su causa ni se propondrá eludirlo.
- La comprobación final debe ser de extremo a extremo cuando esa operación se pueda ejecutar de forma autorizada. Las verificaciones pendientes se registrarán en metadatos de mantenimiento, no como avisos de revisión en las fichas públicas; no se presentará un procedimiento incompleto como terminado.
- Se revisará el recorrido en pantalla pequeña cuando el módulo tenga controles laterales, tablas o formularios que puedan cambiar de disposición.
- La implementación debe actualizar en conjunto el contrato activo, el registro de migración, la navegación, inventario, auditoría de acceso, disposiciones, pruebas y validador. Los estados globales siguen siendo independientes de esta integración.

La evidencia de controles estáticos y una caminata de interfaz de solo lectura son pruebas distintas. La primera aporta cobertura de precisión respaldada por fuente y permite comprobar que una guía no omite una revelación o confunde contenedores; no prueba que el control esté disponible para todos los usuarios ni que una escritura se haya ejecutado. La segunda requiere una revisión independiente autorizada; una cobertura de 83 guías no equivale a 83 recorridos verificados en ejecución.

## Relación con V1

V1 conserva la instantánea histórica de 78 entradas, incluidos sus enlaces y fragmentos de contenido. Su auditoría anterior de 76 rutas registradas y 2 brechas técnicas no se presenta como evidencia actual de V2. Las observaciones V2 no alteran los dos estados globales pendientes ni los puntos de control vigentes.
