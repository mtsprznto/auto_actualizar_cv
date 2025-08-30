"use client";

import { Button } from "@/components/ui/button";
import Link from "next/link";
import { ViewCardHome } from "../ViewCardHome";
import { FileText } from "lucide-react";
import { useEffect, useState } from "react";
import { supabase } from "@/lib/supabase";
import { SniperLoading } from "@/app/components/Shared";

export function ViewHome() {
  const [user, setUser] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchUser = async () => {
      const { data, error } = await supabase.auth.getUser();
      if (error) {
        console.error("Error fetching user:", error.message);
      } else {
        setUser(data.user);
      }
      setLoading(false);
    };

    fetchUser();
  }, []);

  if (loading) {
    return <SniperLoading />
  }
  console.log("USER: ",user);
  
  return (
    <div className="relative items-center mx-auto md:px-12 py-5 md:py-20 w-full md:max-w-6xl px-5">
      <div>
        <div className="text-left mt-3">
          <p className="md:text-[24px] md:tracking-tight tracking-wide text-[#f057ff]">
            Transforma tu propuesta laboral en un currículum personalizado con
            IA
          </p>
          <h1 className="text-[30px] md:text-[55px] tracking-tighter font-bold">
            Generador Inteligente de Curriculum
          </h1>
        </div>
        <p className="text-[16px] md:text-[26px] tracking-normal md:tracking-tight mt-3">
          Ingresa una descripción de trabajo y genera un CV que resalte tus
          proyectos relevantes.
        </p>
        <p className="text-[13px] md:text-[20px] tracking-wide font-light mt-3">
          Integrado con Groq y GitHub para analizar y seleccionar tus
          contribuciones más destacadas.
        </p>
        <div className="w-full flex justify-end md:justify-start">
          <Link href={"/generar-cv"} className="">
            <Button
              className="cursor-pointer text-[20px] md:text-[23px] border md:mt-6 mt-3 px-5 py-4 md:px-8 md:py-6 bg-[#9f1096] hover:bg-[#cc07bd] text-[#f8e8ff] transition hover:scale-[1.02] hover:shadow-2xl duration-300"
              variant={"default"}
            >
              ¡Probar!
            </Button>
          </Link>
        </div>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 w-full md:max-w-[1200px] gap-3 md:py-20 py-5">
        <ViewCardHome
          title={"Generador Inteligente de CV"}
          description={
            "Transforma tu propuesta laboral en un currículum personalizado con IA"
          }
          content={
            <div className="text-sm text-muted-foreground space-y-2">
              <p>
                Ingresá una descripción de trabajo y generá un CV que resalte
                tus proyectos relevantes.
              </p>
              <p>
                Integrado con Groq y GitHub para analizar y seleccionar tus
                contribuciones más destacadas.
              </p>
            </div>
          }
          footer={
            <div className="flex justify-end w-full">
              <span className="text-xs text-purple-500 italic">
                🚀 Generación PDF en tiempo real
              </span>
            </div>
          }
          icon={<FileText className="w-5 h-5 text-purple-500" />}
          redirectTo="/generar-cv"
        ></ViewCardHome>
      </div>
    </div>
  );
}
