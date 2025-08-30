"use client";

import { useEffect, useState } from "react";
import { ViewGenerarCv } from "./components";
import { supabase } from "@/lib/supabase";
import { useRouter } from "next/navigation";
import { SniperLoading } from "@/app/components/Shared";
import { User } from "@supabase/supabase-js";

export default function GenerarCv() {
  const [propuesta, setPropuesta] = useState("");
  const [questions, setQuestions] = useState("");
  const [respuesta, setRespuesta] = useState("");
  const [cvUrl, setCvUrl] = useState("");
  const [loadingGenerar, setLoadingGenerar] = useState(false);
  const [loadingRespuestas, setLoadingRespuestas] = useState(false);
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchSession = async () => {
      const {
        data: { session },
        error,
      } = await supabase.auth.getSession();

      if (error) {
        console.error("Error fetching session:", error.message);
      } else if (session?.user) {
        setUser(session.user);
        console.log(user);
        
      } else {
        router.push("/login"); // 🔐 Redirige si no hay sesión
      }

      setLoading(false);
    };

    fetchSession();
  }, [router]);

  if (loading) return <SniperLoading />;

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
