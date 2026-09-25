<a id="gestionar-líneas-y-conversiones-de-productos"></a>

# 3.11 Gestionar líneas y conversiones de productos

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Registrar una conversión entre un producto de origen y uno de destino cuando la
capacidad esté habilitada; reconocer la selección de línea cuando aparezca en otros
formularios del entorno.

## Acceso condicional

Esta capacidad depende de módulos, configuración y sesión. La interfaz puede mostrar una
entrada de líneas en la navegación y una pantalla de conversión, pero no permite
afirmar que ambas opciones estén habilitadas ni que tengan el mismo alcance en todos
los entornos.

## Requisitos y datos

- Almacén, producto y cantidad de origen.
- Almacén, producto y cantidad de destino.
- Unidades mostradas por el formulario y autorización operativa para la conversión.

## Punto de partida

Abra la opción de conversión solo si está disponible. Antes de registrar, confirme
con el responsable operativo los productos, almacenes y cantidades que corresponden.

## Pasos

1. Seleccione el almacén y el producto de origen disponibles en el formulario.
2. Ingrese una cantidad de origen mayor que cero y revise la medida mostrada.
3. Seleccione el almacén y el producto de destino.
4. Ingrese la cantidad de destino y revise su medida antes de registrar.
5. Revise todos los datos y use la acción de registro solo si puede confirmar el
   procedimiento aplicable.
6. Si su flujo presenta una selección de línea, úsela solo cuando esté disponible y
   confirmada para la operación; esta revisión no prueba una administración autónoma
   de líneas.

## Campos y validaciones observados

La pantalla revisada presenta almacén, producto, cantidad y medida para origen y
destino. Ambas cantidades tienen mínimo uno y las medidas se muestran como solo
lectura. La interfaz no aporta evidencia suficiente para documentar validaciones de
compatibilidad, efectos contables o reglas de líneas como políticas universales.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

La interfaz ofrece registrar una conversión con datos de origen y destino. El efecto
sobre inventario, costos, documentos relacionados y disponibilidad posterior debe
verificarse en el entorno de trabajo antes de ser afirmado.

## Advertencias y casos límite

Una conversión puede ser operativamente sensible. No la use para ajustar existencias
ni para reemplazar una transferencia sin el procedimiento autorizado. No suponga que
la línea observada en otro formulario controle o valide esta operación.

## Problemas frecuentes y condiciones de detención

- Producto o almacén no disponible: confirme la configuración y el contexto de sesión.
- Cantidad menor que uno: corrija el dato antes de registrar.
- No puede explicar el efecto de la conversión: deténgase y solicite validación.
- La opción de líneas o conversión no aparece: no use una ruta alternativa no revisada.

## Enlaces relacionados

- [Crear y editar productos del catálogo](gestionar-productos.md)
- [Gestionar lotes de productos](gestionar-lotes.md)
- [Catálogo](index.md)
