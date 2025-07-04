

from connect import groq_client as client



def modificar_cv():
    """Modifica el CV con la información de GitHub"""


    # Preparar la solicitud
    messages = [
        {
            "role": "system", 
            "content": f"""
                Recibiras una propuesta de trabajo y un listado de proyectos, tu objetivo es actualizar el curriculum perfectamente para el trabajo que se te esta entregando
            """
        },
        {
            "role": "user", 
            "content": ""
        }
    ]

    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    #print(chat_completion.choices[0].message.content)
    respuesta = chat_completion.choices[0].message.content
    return respuesta