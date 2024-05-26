## Requisitos

Asegúrate de tener Python 3.11+ instalado.

## Instalación

1. Crea un entorno virtual

    - Documentación entornos virtuales de python: [Ingrese Aquí](https://docs.python.org/es/3.11/tutorial/venv.html#creating-virtual-environments)

        ```bash
        python -m venv api_env
        ```

2. Activa el entorno virtual

    - En Windows:

      ```bash
      api_env/Scripts/activate
      ```

    - En Linux:

      ``` bash
      source api_env/bin/activate
      ```

3. Instalar dependencias

    ```bash
    pip install -r requirements.txt
    ```

## Ejecución

1. Inicia el Servidor de FastAPI

    ```bash
    uvicorn main:app --reload
    ```

## Guardar dependencias

Ejecutamos el siguiente comando para guardar las dependencias que estamos usando
```bash
pip freeze > requirements.txt
```