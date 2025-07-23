from pydantic import BaseModel, Field, constr

class PreguntaInput(BaseModel):
    pregunta: str = Field(...)

    def normalizada(self):
        return self.pregunta.strip().replace("\n", " ").replace("\r", "")
