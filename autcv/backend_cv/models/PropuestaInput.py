from pydantic import BaseModel, Field, constr

class PropuestaInput(BaseModel):
    propuesta: str = Field(...)

    def normalizada(self):
        return self.propuesta.strip().replace("\n", " ").replace("\r", "")
