"use client";

import { useState } from "react";
import { ViewGenerarCv } from "./components";

export default function GenerarCv() {
  const [propuesta, setPropuesta] = useState("");
  const [questions, setQuestions] = useState("");
  const [respuesta, setRespuesta] = useState("");
  const [cvUrl, setCvUrl] = useState("");
  const [loadingGenerar, setLoadingGenerar] = useState(false);
  const [loadingRespuestas, setLoadingRespuestas] = useState(false);

  const generarCV = async () => {
    setLoadingGenerar(true);

    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/propuesta`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ propuesta }),
      });
      const data = await res.json();
      setCvUrl(data.cv_url);
    } catch (err) {
      console.error("❌ Error al generar el CV:", err);
    } finally {
      setLoadingGenerar(false);
    }
  };

  const generarRespuestas = async () => {
    setLoadingRespuestas(true);

    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/responder`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pregunta: questions }),
      });
      const data = await res.json();
      console.log(data);

      setRespuesta(data.respuestas);
    } catch (err) {
      console.error("❌ Error al generar las respuestas:", err);
    } finally {
      setLoadingRespuestas(false);
    }
  };

  return (
    <ViewGenerarCv
      propuesta={propuesta}
      cvUrl={cvUrl}
      loadingGenerar={loadingGenerar}
      loadingRespuestas={loadingRespuestas}
      generarCV={generarCV}
      setPropuesta={setPropuesta}
      questions={questions}
      response={respuesta}
      generarRespuestas={generarRespuestas}
      setQuestions={setQuestions}
    ></ViewGenerarCv>
  );
}
