<a id="gestionar-sujetos-y-personas-relacionadas"></a>

# 5.8 Gestionar sujetos y personas relacionadas

<a id="estado"></a>
<a id="verificaciones-pendientes-en-runtime"></a>

## Objetivo

Registrar o actualizar el sujeto de una estancia y asociar personas relacionadas
para preparar una operación, sin interpretar esas relaciones como permisos del
sistema.

## Acceso condicional

En **Estancias**, abra la opción declarada para sujetos. Use únicamente datos
ficticios en pruebas y evite ingresar datos personales reales.

## Punto de partida

Prepare un caso ficticio y busque antes de crear un registro.

## Requisitos y datos

- El sujeto puede registrarse como persona, mascota u objeto.
- La interfaz solicita nombre, tipo y número de documento de identidad para el
  alta de un sujeto.
- Puede sincronizar personas relacionadas, incluidas referencias principal y de
  recojo, con una observación cuando esté disponible.

## Pasos

1. Busque primero por nombre o documento para evitar duplicar un sujeto.
2. Si no existe, elija el tipo de sujeto y complete los datos solicitados con un
   ejemplo ficticio.
3. Agregue la persona relacionada solo si el caso operativo lo requiere.
4. Revise las relaciones mostradas y guarde los cambios.
5. Vuelva a buscar el sujeto y confirme que el registro corresponde al ejemplo
   que acaba de usar antes de seleccionarlo en una estancia.

## Campos y validaciones observados

- El nombre, el tipo de documento y el número de documento son requeridos por
  la interfaz al guardar un sujeto.
- No se admite otro sujeto activo con el mismo número de documento.
- El guardado de sujeto y relaciones se realiza como una sola transacción.
- La relación de recojo modela datos de negocio; no otorga, comprueba ni
  reemplaza autorización de software.

<a id="resultado-revisado-en-fuente"></a>

## Resultado esperado

El flujo registra el sujeto y sincroniza sus relaciones. Los campos visibles,
mensajes y disponibilidad real de estas opciones deben confirmarse en el
entorno.

## Advertencias y casos límite

Las relaciones registradas describen el caso; no son prueba de permisos del sistema.

## Problemas frecuentes y condiciones de detención

- El documento ya existe: deténgase y busque el registro existente antes de
  crear otro.
- Faltan datos obligatorios: complete el caso o cancele el alta.
- No está claro quién debe figurar en la relación: no deduzca reglas de negocio
  ni aprobación real a partir de esta pantalla; escale el caso a quien
  corresponda.

## Enlaces relacionados

- [Registrar una estancia](registrar-estancia.md)
- [Gestionar tarifas, relaciones y descuentos](gestionar-tarifas-y-descuentos.md)
