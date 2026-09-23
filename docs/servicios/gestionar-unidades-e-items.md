# Gestionar unidades e ítems de servicio

## Estado

- Revisión de fuente: revisada en código.
- Verificación en entorno: pendiente.
- Paridad con la versión desplegada: pendiente.

## Objetivo

Preparar las unidades y los ítems que se seleccionan al registrar un servicio.

## Acceso condicional

El menú declarado muestra **Unidades** y **Servicios** dentro de Internado. La
disponibilidad y los nombres visibles deben confirmarse en el entorno.

## Requisitos y datos

- Identificación y descripción autorizadas para la unidad o el ítem.
- Criterio operativo para no duplicar registros existentes.

## Punto de partida

En **Internado**, abra **Unidades** o **Servicios** según el dato que necesita
mantener.

## Pasos

1. Busque primero el registro por su descripción o identificador disponible.
2. Abra el registro existente para revisar sus datos antes de crear otro.
3. Use la acción de agregar o editar que muestre la pantalla.
4. Complete los campos solicitados y revise la descripción antes de guardar.
5. Vuelva a la lista y confirme que el registro se reconoce sin ambigüedad.

## Campos y validaciones observados

La fuente separa las unidades de los ítems de servicio. El formulario de internado
selecciona una unidad y agrega ítems a su detalle; la obligatoriedad y los límites
de cada mantenimiento requieren verificación en entorno.

## Resultado revisado en fuente

Una unidad o ítem disponible puede incorporarse al formulario de una orden de
servicio. La creación efectiva y los mensajes mostrados no han sido verificados.

## Advertencias y casos límite

No cambie identificadores o descripciones si no puede distinguir el registro que
ya usan órdenes existentes. Deténgase ante nombres duplicados o datos incompletos.

## Problemas frecuentes y condiciones de detención

- No encuentra el registro esperado: revise la lista antes de crear uno nuevo.
- La unidad no aparece al registrar: deténgase y confirme el contexto del entorno.
- No puede identificar el ítem: no lo agregue a una orden.

## Verificaciones pendientes en runtime

- Etiquetas, filtros, campos obligatorios y mensajes de guardado.
- Disponibilidad real de unidades e ítems en una orden.

## Enlaces relacionados

- [Registrar una orden de servicio o internado](registrar-internado.md)
- [Servicios](index.md)
