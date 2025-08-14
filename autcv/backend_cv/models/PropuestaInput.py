from pydantic import BaseModel, Field, constr

class PropuestaInput(BaseModel):
    """
    Modelo de entrada para la propuesta de trabajo.
    """
    propuesta: str = Field(...)

    def normalizada(self):
        return self.propuesta.strip().replace("\n", " ").replace("\r", "")
